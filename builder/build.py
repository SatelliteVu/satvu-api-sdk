from dataclasses import dataclass
from hashlib import sha1
from json import dumps, loads
from pathlib import Path
from typing import Sequence

import openapi_python_client.parser.openapi
from httpx import get

from openapi_python_client import Project
from openapi_python_client.config import Config, MetaType, ConfigFile
from openapi_python_client.parser.bodies import Body
from openapi_python_client.parser.openapi import GeneratorData, Endpoint
from openapi_python_client.parser.errors import GeneratorError

from builder.config import APIS, BASE_URL

BASE_DIR = (Path(__file__).parent / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"
TEMPLATE_DIR = Path(__file__).parent / "templates"
SRC_DIR = BASE_DIR / "src"


def _load_openapi(api_id: str, use_cached: bool):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    openapi_url = f"{BASE_URL.rstrip('/')}/{APIS[api_id]}/openapi.json"
    cache_file = CACHE_DIR / f"{api_id}-{sha1(openapi_url.encode()).hexdigest()}.json"

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
        # Generate endpoints
        api_dir = self.package_dir
        api_init_path = api_dir / "__init__.py"
        api_init_template = self.env.get_template("api_init.py.jinja")
        api_init_path.write_text(api_init_template.render(), encoding=self.config.file_encoding)

        endpoint_collections_by_tag = self.openapi.endpoint_collections_by_tag
        endpoint_template = self.env.get_template(
            "endpoint_module.py.jinja", globals={"isbool": lambda obj: obj.get_base_type_string() == "bool"}
        )
        endpoints: list[Endpoint] = []
        for endpoint_collection in endpoint_collections_by_tag.values():
            for endpoint in endpoint_collection.endpoints:
                body_docstrings = []
                if endpoint.bodies:
                    body_docstrings = self.body_docstrings(endpoint.bodies[0])
                endpoint = SatVuEndpoint(body_docstrings=body_docstrings, **vars(endpoint))
                endpoints.append(endpoint)

        api_class_path = api_dir / "api.py"
        api_class_path.write_text(
            endpoint_template.render(
                endpoints=endpoints,
                api_id=api_id,
                base_path=APIS[api_id]
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
                return [GeneratorError(detail="Directory already exists. Delete it or use the --overwrite option.")]

        self._build_models()
        self._build_api(api_id, config)
        types_template = self.env.get_template("types.py.jinja")
        types_path = self.package_dir / "types.py"
        types_path.write_text(types_template.render(), encoding=self.config.file_encoding)
        self._run_post_hooks()
        return self._get_errors()

    def body_docstrings(self, body: Body) -> list[str]:
        docstrings = []
        for prop in body.prop.required_properties + body.prop.optional_properties:
            docstring = f"{prop.python_name} ({prop.get_type_string()}): {prop.description or ''}"
            print(docstring)
            docstrings.append(docstring)

        return docstrings


def build(api_id: str, use_cached: False):
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
