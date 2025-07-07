import builtins
import re
from dataclasses import dataclass
from hashlib import sha1
from json import dumps, loads
from pathlib import Path
from typing import Sequence, Union

import openapi_python_client.parser.openapi
from attr._make import evolve
from httpx import get

import openapi_python_client.utils
from openapi_python_client import Project, schema, utils
from openapi_python_client.config import Config, MetaType, ConfigFile
from openapi_python_client.parser.bodies import Body, body_from_data
from openapi_python_client.parser.openapi import GeneratorData, Endpoint
from openapi_python_client.parser.errors import (
    GeneratorError,
    ParseError,
    PropertyError,
)
from openapi_python_client.parser.properties import (
    UnionProperty,
    Schemas,
    Parameters,
    ModelProperty,
    ListProperty,
    Property,
    Class,
    ReferencePath,
)
from openapi_python_client.parser.properties.model_property import _process_property_data
from openapi_python_client.schema import Schema

from builder.config import APIS, BASE_URL

BASE_DIR = (Path(__file__).parent / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"
TEMPLATE_DIR = Path(__file__).parent / "templates"
SRC_DIR = BASE_DIR / "src"

# Override reserved words - we want to still use "type"
RESERVED_WORDS = (set(dir(builtins)) | {"self", "true", "false"}) - {
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

def get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> str:
    if json:
        type_string = self.get_base_json_type_string()
    else:
        type_string = self.get_base_type_string()

    if no_optional or self.required:
        return type_string
    return f"Union[None, {type_string}]"

openapi_python_client.parser.properties.list_property.ListProperty.get_type_string = get_type_string

def to_string(self) -> str:
    default: str | None
    if self.default is not None:
        default = self.default.python_code
        return f"{self.python_name}: {self.get_type_string(quoted=True)} = {default}"
    elif not self.required:
        default = None
        return f"{self.python_name}: {self.get_type_string(quoted=True)} = {default}"
    else:
        return f"{self.python_name}: {self.get_type_string(quoted=True)}"

def get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> str:
    if json:
        type_string = self.get_base_json_type_string(quoted=quoted)
    else:
        type_string = self.get_base_type_string(quoted=quoted)

    if no_optional or self.required:
        return type_string
    return f"Union[None, {type_string}]"

openapi_python_client.parser.properties.protocol.PropertyProtocol.to_string = to_string
openapi_python_client.parser.properties.protocol.PropertyProtocol.get_type_string = get_type_string


def get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> str:
    lit = f"Literal[{self.value.python_code}]"
    if not no_optional and not self.required:
        return f"Union[{lit}, None]"
    return lit

openapi_python_client.parser.properties.const.get_type_string = get_type_string

def get_type_strings_in_union(
    self, *, no_optional: bool = False, json: bool
) -> set[str]:
    type_strings = self._get_inner_type_strings(json=json)
    if no_optional:
        return type_strings
    return type_strings

def _get_inner_type_strings(self, json: bool) -> set[str]:
    return {
        p.get_type_string(no_optional=True, json=json, quoted=True) if "geometries_item_type" in p.name else p.get_type_string(no_optional=True, json=json, quoted=False) for p in self.inner_properties
    }

openapi_python_client.parser.properties.union.UnionProperty.get_type_strings_in_union = get_type_strings_in_union
openapi_python_client.parser.properties.union.UnionProperty._get_inner_type_strings = _get_inner_type_strings

def get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> str:
    if json:
        type_string = self.get_base_json_type_string()
    else:
        type_string = self.get_base_type_string()

    if quoted:
        if type_string == self.class_info.name:
            type_string = f"'{type_string}'"

    if no_optional or self.required:
        return type_string
    return f"Union[None, {type_string}]"

def build(
    data: Schema,
    name: str,
    schemas: Schemas,
    required: bool,
    parent_name: str | None,
    config: Config,
    process_properties: bool,
    roots: set[ReferencePath | utils.ClassName],
) -> tuple[ModelProperty | PropertyError, Schemas]:
    """
    A single ModelProperty from its OAI data

    Args:
        data: Data of a single Schema
        name: Name by which the schema is referenced, such as a model name.
            Used to infer the type name if a `title` property is not available.
        schemas: Existing Schemas which have already been processed (to check name conflicts)
        required: Whether or not this property is required by the parent (affects typing)
        parent_name: The name of the property that this property is inside of (affects class naming)
        config: Config data for this run of the generator, used to modifying names
        roots: Set of strings that identify schema objects on which the new ModelProperty will depend
        process_properties: Determines whether the new ModelProperty will be initialized with property data
    """
    if not config.use_path_prefixes_for_title_model_names and data.title:
        class_string = data.title
    else:
        title = data.title or name
        if parent_name:
            class_string = f"{utils.pascal_case(parent_name)}{utils.pascal_case(title)}"
        else:
            class_string = title
    class_info = Class.from_string(string=class_string, config=config)
    # see https://github.com/openapi-generators/openapi-python-client/issues/652
    suffix = 1
    while class_info.name in schemas.classes_by_name:
        class_info = Class.from_string(string=class_string + str(suffix), config=config)
        suffix += 1
    model_roots = {*roots, class_info.name}
    required_properties: list[Property] | None = None
    optional_properties: list[Property] | None = None
    relative_imports: set[str] | None = None
    lazy_imports: set[str] | None = None
    additional_properties: Property | None = None
    if process_properties:
        data_or_err, schemas = _process_property_data(
            data=data, schemas=schemas, class_info=class_info, config=config, roots=model_roots
        )
        if isinstance(data_or_err, PropertyError):
            return data_or_err, schemas
        property_data, additional_properties = data_or_err
        required_properties = property_data.required_props
        optional_properties = property_data.optional_props
        relative_imports = property_data.relative_imports
        lazy_imports = property_data.lazy_imports
        for root in roots:
            if isinstance(root, utils.ClassName):
                continue
            schemas.add_dependencies(root, {class_info.name})

    prop = ModelProperty(
        class_info=class_info,
        data=data,
        roots=model_roots,
        required_properties=required_properties,
        optional_properties=optional_properties,
        relative_imports=relative_imports,
        lazy_imports=lazy_imports,
        additional_properties=additional_properties,
        description=data.description or "",
        default=None,
        required=required,
        name=name,
        python_name=utils.PythonIdentifier(value=name, prefix=config.field_prefix),
        example=data.example,
    )
    if class_info.name in schemas.classes_by_name:
        error = PropertyError(
            data=data, detail=f'Attempted to generate duplicate models with name "{class_info.name}"'
        )
        return error, schemas

    schemas = evolve(
        schemas,
        classes_by_name={**schemas.classes_by_name, class_info.name: prop},
        models_to_process=[*schemas.models_to_process, prop],
    )
    return prop, schemas

openapi_python_client.parser.properties.model_property.ModelProperty.get_type_string = get_type_string
openapi_python_client.parser.properties.model_property.ModelProperty.build = build

def get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> str:
    lit = f"Literal[{self.value.python_code}]"
    if not no_optional and not self.required:
        return f"Union[{lit}, None]"
    return lit

openapi_python_client.parser.properties.const.ConstProperty.get_type_string = get_type_string

def sanitize(value: str) -> str:
    """Removes every character that isn't 0-9, A-Z, a-z, or a known delimiter"""
    value = value.replace(":", "_")  # Replace colons with underscores
    return re.sub(rf"[^\w{utils.DELIMITERS}]+", "", value)

openapi_python_client.utils.sanitize = sanitize

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
    response_disambiguation: dict | None = None


def build_response_disambiguation(endpoint, models_by_name):
    """
    For each response, if a Union type, build a dict describing how to disambiguate.
    Returns a dict for use in the template, or None if not needed.
    """
    # Find the first successful response (e.g. 200, 201, etc)
    for resp in endpoint.responses:
        # Only look at successful responses for now
        if not resp.status_code.is_success:
            continue
        resp_type = resp.prop.get_type_string(quoted=False)
        if resp_type.startswith("Union["):
            # Parse the union types
            inner = resp_type[len("Union["):-1]
            model_names = [name.strip().replace("'", "") for name in inner.split(",")]
            fallback_models = model_names
            # Try to find discriminator info
            # This requires looking up the OpenAPI schema for this response
            discriminator_property = None
            model_map = {}
            uses_discriminator = False

            # Try to find which model, if any, has a discriminator
            for name in model_names:
                model_cls = models_by_name.get(name)
                if not model_cls:
                    continue
                # If your model dataclass has _discriminator info, use it (pseudo-code)
                # This is OpenAPI specific: you might need to load this from schemas/components
                # For now, let's assume you have model_cls._discriminator_property and model_cls._discriminator_mapping
                discriminator = getattr(model_cls, "_discriminator_property", None)
                mapping = getattr(model_cls, "_discriminator_mapping", None)
                if discriminator and mapping:
                    discriminator_property = discriminator
                    model_map = mapping
                    uses_discriminator = True
                    break  # Use the first found

            if uses_discriminator:
                return {
                    "uses_discriminator": True,
                    "discriminator_property": discriminator_property,
                    "model_map": model_map,
                    "fallback_models": fallback_models,
                }
            else:
                return {
                    "uses_discriminator": False,
                    "fallback_models": fallback_models,
                }
    return None


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
                response_disambiguation = build_response_disambiguation(
                    endpoint, {}
                )
                endpoint = SatVuEndpoint(body_docstrings=body_docstrings, response_disambiguation=response_disambiguation, **vars(endpoint))
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
            body_prop = body.prop.inner_property if isinstance(body.prop, ListProperty) else body.prop
            props = body_prop.required_properties + body_prop.optional_properties
            for prop in props:
                docstring = f"{prop.python_name} ({prop.get_type_string()}): {prop.description or ''}"
                docstrings.append(docstring)

        return docstrings


def build(api_id: str, use_cached: False):
    openapi_python_client.parser.openapi.models_relative_prefix = f"{api_id}."
    openapi_dict, openapi_src = _load_openapi(api_id, use_cached)
    config = Config.from_sources(
        config_file=ConfigFile(
            # class_overrides={"Price": {"class_name": "OrderPrice2", "module_name": "order_price_2"}},
        ),
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
