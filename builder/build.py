import builtins
from dataclasses import dataclass
from hashlib import sha1
from json import dumps, loads
from pathlib import Path
from typing import Sequence, Union

import openapi_python_client.parser.openapi
from httpx import get

import openapi_python_client.utils
from openapi_python_client import Project, schema, utils
from openapi_python_client.config import Config, MetaType, ConfigFile
from openapi_python_client.parser.bodies import Body, body_from_data
from openapi_python_client.parser.openapi import GeneratorData, Endpoint
from openapi_python_client.parser.errors import GeneratorError, ParseError
from openapi_python_client.parser.properties import UnionProperty, Schemas, Parameters

from builder.config import APIS, BASE_URL

BASE_DIR = (Path(__file__).parent / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"
TEMPLATE_DIR = Path(__file__).parent / "templates"
SRC_DIR = BASE_DIR / "src"

# Override reserved words - we want to still use "type"
RESERVED_WORDS = (set(dir(builtins)) | {"self", "true", "false", "datetime"}) - {
    "id", "type"
}

openapi_python_client.utils.RESERVED_WORDS = RESERVED_WORDS

def from_data(
    *,
    data: schema.Operation,
    path: str,
    method: str,
    tags: list[openapi_python_client.utils.PythonIdentifier],
    schemas: Schemas,
    parameters: Parameters,
    request_bodies: dict[str, Union[schema.RequestBody, schema.Reference]],
    responses: dict[str, Union[schema.Response, schema.Reference]],
    config: Config,
) -> tuple[Union["Endpoint", ParseError], Schemas, Parameters]:
    """Construct an endpoint from the OpenAPI data"""

    if data.operationId is None:
        name = openapi_python_client.parser.generate_operation_id(path=path, method=method)
    else:
        name = data.operationId.replace("-", "_")

    endpoint = Endpoint(
        path=path,
        method=method,
        summary=utils.remove_string_escapes(data.summary) if data.summary else "",
        description=utils.remove_string_escapes(data.description)
        if data.description
        else "",
        name=name,
        requires_security=bool(data.security),
        tags=tags,
    )

    result, schemas, parameters = Endpoint.add_parameters(
        endpoint=endpoint,
        data=data,
        schemas=schemas,
        parameters=parameters,
        config=config,
    )
    if isinstance(result, ParseError):
        return result, schemas, parameters
    result, schemas = Endpoint._add_responses(
        endpoint=result,
        data=data.responses,
        schemas=schemas,
        responses=responses,
        config=config,
    )
    if isinstance(result, ParseError):
        return result, schemas, parameters
    bodies, schemas = body_from_data(
        data=data,
        schemas=schemas,
        config=config,
        endpoint_name=result.name,
        request_bodies=request_bodies,
    )
    body_errors = []
    for body in bodies:
        if isinstance(body, ParseError):
            body_errors.append(body)
            continue
        result.bodies.append(body)
        result.relative_imports.update(
            body.prop.get_imports(prefix=openapi_python_client.parser.openapi.models_relative_prefix)
        )
        result.relative_imports.update(
            body.prop.get_lazy_imports(prefix=openapi_python_client.parser.openapi.models_relative_prefix)
        )
    if len(result.bodies) > 0:
        result.errors.extend(body_errors)
    elif len(body_errors) > 0:
        return (
            ParseError(
                header="Endpoint requires a body, but none were parseable.",
                detail="\n".join(error.detail or "" for error in body_errors),
            ),
            schemas,
            parameters,
        )

    return result, schemas, parameters

openapi_python_client.parser.openapi.Endpoint.from_data = from_data

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
        endpoint_template.environment.filters["split"] = lambda s, sep: s.split(sep)
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
        if isinstance(body.prop, UnionProperty):
            # TODO: Agree a way to document unions
            models = body.prop.inner_properties
            docstring = "Either"
            for model in models:
                docstring += f" ({model.get_type_string()}):"
                for prop in model.required_properties:
                    docstring += f"\n- {prop.python_name} ({prop.get_type_string()}): {prop.description or ''}"
                docstrings.append(docstring)
                docstring = "Or:"
        else:
            props = body.prop.required_properties + body.prop.optional_properties
            for prop in props:
                docstring = f"{prop.python_name} ({prop.get_type_string()}): {prop.description or ''}"
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
