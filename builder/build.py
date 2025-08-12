from dataclasses import dataclass
from hashlib import sha1
from json import dumps, loads
from pathlib import Path
from typing import Sequence

import openapi_python_client.parser.openapi
from httpx import get

import openapi_python_client.utils
from openapi_python_client import Project
from openapi_python_client.config import Config, MetaType, ConfigFile
from openapi_python_client.parser.bodies import Body
from openapi_python_client.parser.openapi import GeneratorData, Endpoint
from openapi_python_client.parser.errors import (
    GeneratorError,
)
from openapi_python_client.parser.properties import (
    UnionProperty,
    ListProperty,
)

from builder.config import APIS, BASE_URL

BASE_DIR = (Path(__file__).parent / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"
TEMPLATE_DIR = Path(__file__).parent / "templates"
SRC_DIR = BASE_DIR / "src"


def _load_openapi(api_id: str, use_cached: bool) -> tuple[dict, Path]:
    """
    Load the OpenAPI specification for the given API ID, either from cache or by fetching it.

    :param api_id: The identifier for the API to load.
    :param use_cached: If True, use cached OpenAPI spec if available; otherwise, fetch it.
    :return: A tuple containing the OpenAPI specification as a dictionary and the path to the cache file.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    openapi_url = f"{BASE_URL.rstrip('/')}/{APIS[api_id]}/openapi.json"
    cache_file = (
        CACHE_DIR
        / f"{api_id}-{sha1(openapi_url.encode(), usedforsecurity=False).hexdigest()}.json"
    )

    if not use_cached:
        response = get(openapi_url)
        response.raise_for_status()
        openapi = response.json()
        cache_file.write_text(dumps(openapi))

    return loads(cache_file.read_text()), cache_file


@dataclass
class SatVuEndpoint(Endpoint):
    body_docstrings: list[str] | None = None


# Override
class SatVuProject(Project):
    def _build_api(self, api_id: str, config: Config) -> None:
        """
        Build the API module for the given API ID.

        :param api_id: The identifier for the API to build.
        :param config: The configuration for openapi-python-client.
        """
        # Generate endpoints
        api_dir = self.package_dir
        api_init_path = api_dir / "__init__.py"
        api_init_template = self.env.get_template("api_init.py.jinja")
        api_init_path.write_text(
            api_init_template.render(), encoding=self.config.file_encoding
        )

        endpoint_collections_by_tag = self.openapi.endpoint_collections_by_tag
        endpoint_template = self.env.get_template(
            "endpoint_module.py.jinja",
            globals={"isbool": lambda obj: obj.get_base_type_string() == "bool"},
        )
        endpoints: list[Endpoint] = []

        for endpoint_collection in endpoint_collections_by_tag.values():
            for endpoint in endpoint_collection.endpoints:
                body_docstrings = []
                if endpoint.bodies:
                    body_docstrings = self.body_docstrings(endpoint.bodies[0])
                endpoint = SatVuEndpoint(
                    body_docstrings=body_docstrings,
                    **vars(endpoint),
                )
                endpoints.append(endpoint)

        api_class_path = api_dir / "api.py"
        endpoint_template.environment.filters["split"] = lambda s, sep: s.split(sep)
        api_class_path.write_text(
            endpoint_template.render(
                endpoints=endpoints, api_id=api_id, base_path=APIS[api_id]
            ),
            encoding=self.config.file_encoding,
        )

    def build(self, api_id: str, config: Config) -> Sequence[GeneratorError]:
        """Create the project from templates"""

        print(f"Generating {self.project_dir}")
        try:
            self.project_dir.mkdir()
        except FileExistsError:
            if not self.config.overwrite:
                return [
                    GeneratorError(
                        detail="Directory already exists. Delete it or use the --overwrite option."
                    )
                ]

        self._build_models()
        self._build_api(api_id, config)
        types_template = self.env.get_template("types.py.jinja")
        types_path = self.package_dir / "types.py"
        types_path.write_text(
            types_template.render(), encoding=self.config.file_encoding
        )
        self._run_post_hooks()
        return self._get_errors()

    def body_docstrings(self, body: Body) -> list[str]:
        """
        Generate docstrings for the request body.
        """
        docstrings = []
        if isinstance(body.prop, UnionProperty):
            # TODO: Agree a way to document unions
            models = body.prop.inner_properties
            docstring = f"body ({body.prop.get_type_string()}):\n"
            docstring += "One of:\n"

            for model in models:
                model_docstring = f"- {model.get_type_string()}: {model.description}\n"
                docstring += model_docstring

            docstrings.append(docstring)
        else:
            body_prop = (
                body.prop.inner_property
                if isinstance(body.prop, ListProperty)
                else body.prop
            )
            docstring = f"body ({body_prop.get_type_string()}): {body_prop.description}"
            docstrings.append(docstring)

        return docstrings


def build(api_id: str, use_cached: False):
    """
    Build the SatVu API client for the given API ID.

    :param api_id: The identifier for the API to build.
    :param use_cached: If True, use cached OpenAPI spec if available; otherwise, fetch it.
    """
    openapi_python_client.parser.openapi.models_relative_prefix = f"{api_id}."
    openapi_dict, openapi_src = _load_openapi(api_id, use_cached)
    config = Config.from_sources(
        config_file=ConfigFile(),
        meta_type=MetaType.NONE,
        document_source=openapi_src,
        file_encoding="utf-8",
        overwrite=True,
        output_path=SRC_DIR / api_id,
    )

    openapi = GeneratorData.from_dict(openapi_dict, config=config)
    if isinstance(openapi, GeneratorError):
        print(GeneratorError)
        exit(1)

    project = SatVuProject(
        openapi=openapi,
        custom_template_path=TEMPLATE_DIR,
        config=config,
    )

    errors = project.build(api_id, config)
    if len(errors) > 0:
        for error in errors:
            print("=" * 20)
            print(error)
        exit(1)
