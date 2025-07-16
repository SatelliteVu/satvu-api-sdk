import builtins
import re
from typing import Union

import openapi_python_client
from attr._make import evolve
from openapi_python_client import schema, Config, utils
from openapi_python_client.parser.bodies import body_from_data
from openapi_python_client.parser.errors import ParseError, PropertyError
from openapi_python_client.parser.openapi import Endpoint
from openapi_python_client.parser.properties import (
    Schemas,
    Parameters,
    ModelProperty,
    Property,
    Class,
    ReferencePath,
)
from openapi_python_client.parser.properties.model_property import _process_property_data
from openapi_python_client.schema import Schema

"""
Patching the openapi-python-client library
"""

# Override reserved words - we want to still use "type"
RESERVED_WORDS = (set(dir(builtins)) | {"self", "true", "false"}) - {"id", "type"}

openapi_python_client.utils.RESERVED_WORDS = RESERVED_WORDS


# Override Endpoint.from_data to replace dashes in operationId with underscores
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
        name = openapi_python_client.parser.generate_operation_id(
            path=path, method=method
        )
    else:
        # Replace dashes with underscores to avoid issues with Python identifiers
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
            body.prop.get_imports(
                prefix=openapi_python_client.parser.openapi.models_relative_prefix
            )
        )
        result.relative_imports.update(
            body.prop.get_lazy_imports(
                prefix=openapi_python_client.parser.openapi.models_relative_prefix
            )
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


# Override lots of methods to avoid the use of 'Unset'
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


openapi_python_client.parser.properties.list_property.ListProperty.get_type_string = (
    get_type_string
)


def to_string(self) -> str:
    default: str | None

    # For const (literal) properties, default to the value of the constant
    if isinstance(self, openapi_python_client.parser.properties.const.ConstProperty):
        return f"{self.python_name}: {self.get_type_string(quoted=True)} = {self.value.python_code}"

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
openapi_python_client.parser.properties.protocol.PropertyProtocol.get_type_string = (
    get_type_string
)


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


openapi_python_client.parser.properties.const.ConstProperty.get_type_string = (
    get_type_string
)


def get_type_strings_in_union(
    self, *, no_optional: bool = False, json: bool
) -> set[str]:
    type_strings = self._get_inner_type_strings(json=json)
    if no_optional:
        return type_strings
    return type_strings


# Override the inner type strings to handle geometries_item_type
def _get_inner_type_strings(self, json: bool) -> set[str]:
    return {
        p.get_type_string(no_optional=True, json=json, quoted=True)
        if "geometries_item_type" in p.name
        else p.get_type_string(no_optional=True, json=json, quoted=False)
        for p in self.inner_properties
    }


openapi_python_client.parser.properties.union.UnionProperty.get_type_strings_in_union = get_type_strings_in_union
openapi_python_client.parser.properties.union.UnionProperty._get_inner_type_strings = (
    _get_inner_type_strings
)


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
            data=data,
            schemas=schemas,
            class_info=class_info,
            config=config,
            roots=model_roots,
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
            data=data,
            detail=f'Attempted to generate duplicate models with name "{class_info.name}"',
        )
        return error, schemas

    schemas = evolve(
        schemas,
        classes_by_name={**schemas.classes_by_name, class_info.name: prop},
        models_to_process=[*schemas.models_to_process, prop],
    )
    return prop, schemas


openapi_python_client.parser.properties.model_property.ModelProperty.get_type_string = (
    get_type_string
)
openapi_python_client.parser.properties.model_property.ModelProperty.build = build


# Override the sanitize function to replace colons with underscores
def sanitize(value: str) -> str:
    """Removes every character that isn't 0-9, A-Z, a-z, or a known delimiter"""
    value = value.replace(":", "_")  # Replace colons with underscores
    return re.sub(rf"[^\w{utils.DELIMITERS}]+", "", value)


openapi_python_client.utils.sanitize = sanitize
