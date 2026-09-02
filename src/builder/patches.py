"""
Monkey-patches for openapi-python-client.
"""

import builtins
import re
from typing import Any, ClassVar

import openapi_python_client
import openapi_python_client.parser.properties as props
import openapi_python_client.parser.properties.union as union_module
from attr import define, evolve
from openapi_python_client import strings
from openapi_python_client.config import Config
from openapi_python_client.parser.errors import PropertyError
from openapi_python_client.parser.properties import (
    Class,
    ModelProperty,
    Property,
    ReferencePath,
    Schemas,
)
from openapi_python_client.parser.properties.enum_property import EnumProperty
from openapi_python_client.parser.properties.model_property import (
    _process_property_data,
)
from openapi_python_client.parser.properties.none import NoneProperty
from openapi_python_client.parser.properties.protocol import PropertyProtocol, Value
from openapi_python_client.parser.properties.union import UnionProperty
from openapi_python_client.schema import DataType as OAIDataType
from openapi_python_client.schema import Schema as OAISchema
from openapi_python_client.schema import UntrustedString

from builder.code_strings import unwrap_code

# ============================================================================
# PATCH 1: Allow "id" as field name
# ============================================================================
# By default, "id" is reserved because it's a Python builtin.
# But it's a very common field name in APIs (user id, product id, etc.)
# So we remove it from the reserved words list.

RESERVED_WORDS = (set(dir(builtins)) | {"self", "true", "false", "datetime"}) - {"id"}
strings.RESERVED_WORDS = RESERVED_WORDS


# ============================================================================
# PATCH 2-4: ListProperty type string methods
# ============================================================================
# These patches customize how list types are rendered:
# - Remove "Unset" from optional lists (use None instead)
# - Use lowercase list[T] instead of List[T]
# - Add quoted parameter support for forward references


def list_get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> strings.PythonCode:
    """Get type string for ListProperty without Unset."""
    if json:
        type_string = self.get_base_json_type_string()
    else:
        type_string = self.get_base_type_string()

    if no_optional or self.required:
        return type_string
    # Use None instead of Unset for optional lists
    return strings.PythonCode(f"Union[None, {unwrap_code(type_string)}]")


def list_get_base_type_string(self, *, quoted: bool = False) -> strings.PythonCode:
    """Use lowercase list[T] syntax."""
    inner = unwrap_code(self.inner_property.get_type_string())
    return strings.PythonCode(f"list[{inner}]")


def list_get_base_json_type_string(self, *, quoted: bool = False) -> strings.PythonCode:
    """Use lowercase list[T] syntax for JSON types."""
    inner = unwrap_code(self.inner_property.get_type_string(json=True))
    return strings.PythonCode(f"list[{inner}]")


openapi_python_client.parser.properties.list_property.ListProperty.get_type_string = (
    list_get_type_string
)
openapi_python_client.parser.properties.list_property.ListProperty.get_base_type_string = list_get_base_type_string
openapi_python_client.parser.properties.list_property.ListProperty.get_base_json_type_string = list_get_base_json_type_string


# ============================================================================
# PATCH 5: PropertyProtocol.get_type_string with quoted parameter
# ============================================================================
# Base protocol needs to accept quoted parameter so subclasses can use it


def property_protocol_get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> strings.PythonCode:
    """
    Get type string for any property with optional quoted parameter support.

    This is the base implementation for PropertyProtocol that accepts the quoted
    parameter. Specific property types (ModelProperty, UnionProperty, etc.) will
    override this with their own implementations that actually use the parameter.
    """
    if json:
        # Try to call get_base_json_type_string with quoted parameter
        try:
            type_string = self.get_base_json_type_string(quoted=quoted)
        except TypeError:
            # Fallback if the property doesn't support quoted parameter
            type_string = self.get_base_json_type_string()
    else:
        type_string = self.get_base_type_string()

    if no_optional or self.required:
        return type_string
    return strings.PythonCode(f"Union[None, {unwrap_code(type_string)}]")


openapi_python_client.parser.properties.protocol.PropertyProtocol.get_type_string = (
    property_protocol_get_type_string
)


# ============================================================================
# PATCH 6-7: ConstProperty type strings
# ============================================================================
# Handle Literal types for const properties


def const_get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> strings.PythonCode:
    """Generate Literal type for const properties."""
    lit = f"Literal[{unwrap_code(self.value.python_code)}]"
    # A const with a default always round-trips as Literal — wrapping in
    # Union[..., None] is semantically useless (default guarantees non-None)
    # and breaks Pydantic's field-based discriminator which requires a plain
    # Literal on every variant.
    if self.default is not None:
        return strings.PythonCode(lit)
    if not no_optional and not self.required:
        return strings.PythonCode(f"Union[{lit}, None]")
    return strings.PythonCode(lit)


openapi_python_client.parser.properties.const.get_type_string = const_get_type_string
openapi_python_client.parser.properties.const.ConstProperty.get_type_string = (
    const_get_type_string
)


# ============================================================================
# PATCH 8-13: UnionProperty type handling
# ============================================================================
# These are CRITICAL patches for handling Union types correctly.
# The main issue: quoted forward references need Union[...] syntax.
# Cannot use: 'Type1' | 'Type2'  (invalid Python!)
# Must use: Union['Type1', 'Type2']  (valid)


def union_get_type_strings_in_union(
    self, *, no_optional: bool = False, json: bool, quoted: bool = True
) -> set[strings.PythonCode]:
    """Get all type strings in the union."""
    type_strings = self._get_inner_type_strings(json=json, quoted=quoted)
    if no_optional:
        return type_strings
    return type_strings


def union_get_inner_type_strings(
    self, json: bool, quoted: bool = True
) -> set[strings.PythonCode]:
    """Extract type strings from inner properties with quoted support."""
    result = set()
    for p in self.inner_properties:
        # Only ModelProperty supports quoted parameter
        if isinstance(p, ModelProperty):
            result.add(p.get_type_string(no_optional=True, json=json, quoted=quoted))
        else:
            result.add(p.get_type_string(no_optional=True, json=json))
    return result


def union_get_type_string_from_inner_type_strings(
    self, inner_types: set[strings.PythonCode]
) -> strings.PythonCode:
    """
    Build union type string - CRITICAL for forward references.

    Uses Union[...] syntax when types are quoted (forward references).
    This is necessary because 'Type1' | 'Type2' is invalid Python syntax.
    """
    if len(inner_types) == 1:
        return inner_types.pop()

    unwrapped = sorted(
        (unwrap_code(t) for t in inner_types),
        key=lambda type_string: type_string.lower(),
    )

    # Check if any type is quoted (forward reference)
    has_quoted = any(t.startswith("'") for t in unwrapped)

    if has_quoted:
        # MUST use Union[...] syntax for quoted types
        return strings.PythonCode(f"Union[{', '.join(unwrapped)}]")

    # Can use | syntax for non-quoted types (cleaner)
    return strings.PythonCode(" | ".join(unwrapped))


def union_get_base_type_string(self, *, quoted: bool = True) -> strings.PythonCode:
    """Get base type string with control over forward reference quoting."""
    return self._get_type_string_from_inner_type_strings(
        self._get_inner_type_strings(json=False, quoted=quoted)
    )


def union_get_base_json_type_string(self, *, quoted: bool = True) -> strings.PythonCode:
    """Get JSON type string with control over forward reference quoting."""
    return self._get_type_string_from_inner_type_strings(
        self._get_inner_type_strings(json=True, quoted=quoted)
    )


def union_get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = True,
) -> strings.PythonCode:
    """Get full type string for union with optional support."""
    if json:
        type_string = self.get_base_json_type_string(quoted=quoted)
    else:
        type_string = self.get_base_type_string(quoted=quoted)

    if no_optional or self.required:
        return type_string

    # Check if None is already in the union (e.g., from anyOf: [string, null])
    # This prevents duplicate None in types like "None | None | str"
    has_none = any(
        isinstance(p, openapi_python_client.parser.properties.none.NoneProperty)
        for p in self.inner_properties
    )
    if has_none:
        return type_string

    # Use Union[None, ...] for quoted types, None | ... for others
    code = unwrap_code(type_string)
    if "'" in code or '"' in code:
        return strings.PythonCode(f"Union[None, {code}]")
    else:
        return strings.PythonCode(f"None | {code}")


openapi_python_client.parser.properties.union.UnionProperty.get_type_strings_in_union = union_get_type_strings_in_union
openapi_python_client.parser.properties.union.UnionProperty._get_inner_type_strings = (
    union_get_inner_type_strings
)
openapi_python_client.parser.properties.union.UnionProperty._get_type_string_from_inner_type_strings = union_get_type_string_from_inner_type_strings
openapi_python_client.parser.properties.union.UnionProperty.get_base_type_string = (
    union_get_base_type_string
)
openapi_python_client.parser.properties.union.UnionProperty.get_base_json_type_string = union_get_base_json_type_string
openapi_python_client.parser.properties.union.UnionProperty.get_type_string = (
    union_get_type_string
)


# ============================================================================
# PATCH 14: ModelProperty.get_type_string with quoted support
# ============================================================================
# Add quoted parameter to control forward reference quoting


def model_get_type_string(
    self,
    no_optional: bool = False,
    json: bool = False,
    *,
    quoted: bool = False,
) -> strings.PythonCode:
    """Get type string for model property with optional quoting."""
    if json:
        type_string = unwrap_code(self.get_base_json_type_string())
    else:
        type_string = unwrap_code(self.get_base_type_string())

    # Quote the type if requested (for forward references)
    if quoted and type_string == self.class_info.name:
        type_string = f"'{type_string}'"

    if no_optional or self.required:
        return strings.PythonCode(type_string)
    return strings.PythonCode(f"Union[None, {type_string}]")


openapi_python_client.parser.properties.model_property.ModelProperty.get_type_string = (
    model_get_type_string
)


# ============================================================================
# PATCH 15: strings.sanitize - Replace colons in field names
# ============================================================================
# Some APIs use colons in field names (e.g., GeoJSON: geo:lat, geo:lon)
# Colons aren't valid in Python identifiers, so replace with underscores


def sanitize(value: str) -> str:
    """
    Sanitize field names by replacing invalid characters.

    Replaces:
    - Colons with underscores (geo:lat → geo_lat)
    - Other invalid characters with nothing
    """
    value = value.replace(":", "_")
    return re.sub(rf"[^\w{strings.DELIMITERS}]+", "", value)


strings.sanitize = sanitize


# ============================================================================
# PATCH 16: EnumProperty.get_base_type_string - Always quote enums
# ============================================================================
# Enum types should always be quoted as forward references


def enum_get_base_type_string(self, *, quoted: bool = False) -> strings.PythonCode:
    """Always return quoted enum name (forward reference)."""
    return strings.PythonCode(f"'{self.class_info.name}'")


openapi_python_client.parser.properties.enum_property.EnumProperty.get_base_type_string = enum_get_base_type_string


# ============================================================================
# PATCH 17: PropertyProtocol.to_string - Use None instead of UNSET for parameters
# ============================================================================
# Override to_string to generate parameter strings with None instead of UNSET


def property_to_string(self) -> strings.PythonCode:
    """
    Generate parameter string with None instead of UNSET.

    For optional parameters, use None as default instead of UNSET.
    """
    type_string = unwrap_code(self.get_type_string())

    if self.required or self.default is not None:
        if self.default is not None:
            default = unwrap_code(self.default.python_code)
            return strings.PythonCode(f"{self.python_name}: {type_string} = {default}")
        return strings.PythonCode(f"{self.python_name}: {type_string}")

    # Optional parameter - use None instead of UNSET
    return strings.PythonCode(f"{self.python_name}: {type_string} = None")


openapi_python_client.parser.properties.protocol.PropertyProtocol.to_string = (
    property_to_string
)


# ============================================================================
# PATCH 18: Free-form object schemas → DictProperty instead of ModelProperty
# ============================================================================
# OpenAPI pattern: anyOf: [{type: object, additionalProperties: true}, {type: null}]
# This should generate: dict | None
# But openapi-python-client creates an empty model class (e.g., LinkBodyType0)
#
# This patch intercepts property_from_data() to detect free-form object schemas
# (type: object, additionalProperties: true, no explicit properties) and returns
# a custom DictProperty instead of ModelProperty.


@define
class DictProperty(PropertyProtocol):
    """A property that represents a free-form dictionary (dict)."""

    name: UntrustedString
    required: bool
    default: Value | None
    python_name: strings.PythonIdentifier
    description: UntrustedString | None
    example: UntrustedString | None
    _type_string: ClassVar[str] = "dict"
    _json_type_string: ClassVar[str] = "dict"

    @classmethod
    def build(
        cls,
        name: UntrustedString,
        required: bool,
        default: Any,
        python_name: strings.PythonIdentifier,
        description: UntrustedString | None,
        example: UntrustedString | None,
    ) -> "DictProperty":
        return cls(
            name=name,
            required=required,
            default=cls.convert_value(default),
            python_name=python_name,
            description=description,
            example=example,
        )

    @classmethod
    def convert_value(cls, value: Any) -> Value | None:
        if value is None:
            return None
        return Value(python_code=strings.PythonCode(repr(value)), raw_value=value)


# Store original function
_original_property_from_data = props.property_from_data


def _is_free_form_object(data: OAISchema) -> bool:
    """
    Check if schema is a free-form object (should be dict).

    A free-form object has:
    - type: object
    - additionalProperties: true (or unset, which defaults to true)
    - No explicit properties defined
    """
    if not isinstance(data, OAISchema):
        return False

    # Must be type: object
    if data.type != OAIDataType.OBJECT:
        return False

    # Must have no explicit properties
    if data.properties:
        return False

    # additionalProperties must be True or a schema (not False)
    # When additionalProperties is True or a schema, it's a free-form dict
    # The OAISchema.additionalProperties can be True, False, or a Schema
    return data.additionalProperties is not False


def patched_property_from_data(
    name: str,
    required: bool,
    data,
    schemas: Schemas,
    parent_name: str,
    config: Config,
    process_properties: bool = True,
    roots=None,
):
    """
    Patched property_from_data that handles free-form objects as DictProperty.

    This prevents openapi-python-client from generating empty model classes
    for schemas like {type: object, additionalProperties: true}.
    """
    # Check if this is a free-form object schema
    if isinstance(data, OAISchema) and _is_free_form_object(data):
        return (
            DictProperty.build(
                name=name,
                required=required,
                default=data.default,
                python_name=strings.PythonIdentifier(
                    value=name, prefix=config.field_prefix
                ),
                description=data.description,
                example=data.example,
            ),
            schemas,
        )

    # Otherwise, use the original function
    return _original_property_from_data(
        name=name,
        required=required,
        data=data,
        schemas=schemas,
        parent_name=parent_name,
        config=config,
        process_properties=process_properties,
        roots=roots,
    )


# Apply the patch
props.property_from_data = patched_property_from_data
openapi_python_client.parser.properties.property_from_data = patched_property_from_data


# ============================================================================
# PATCH 19: ModelProperty.build - Handle duplicate model names
# ============================================================================
# When OpenAPI specs have duplicate schema names (common with composed schemas),
# add numeric suffixes to make them unique: Model, Model1, Model2, etc.


def model_property_build(
    data: OAISchema,
    name: str,
    schemas: Schemas,
    required: bool,
    parent_name: str | None,
    config: Config,
    process_properties: bool,
    roots: set[ReferencePath | strings.ClassName],
) -> tuple[ModelProperty | PropertyError, Schemas]:
    """
    Build a ModelProperty from OAI schema data, handling duplicate names.

    This is a critical patch that prevents "duplicate model" errors by
    appending numeric suffixes to conflicting model names.
    """
    from openapi_python_client import strings
    from openapi_python_client.parser.properties import ModelProperty

    # Determine class name from title or name
    if not config.use_path_prefixes_for_title_model_names and data.title:
        class_string = data.title
    else:
        title = data.title or name
        if parent_name:
            class_string = (
                f"{strings.pascal_case(parent_name)}{strings.pascal_case(title)}"
            )
        else:
            class_string = title

    class_info = Class.from_string(string=class_string, config=config)

    # Handle duplicate names by adding numeric suffix. Suffix the sanitised
    # ClassName rather than `class_string` — the latter may be an UntrustedString
    # straight from the document, which doesn't support concatenation.
    base_class_name = class_info.name
    suffix = 1
    while class_info.name in schemas.classes_by_name:
        class_info = Class.from_string(
            string=f"{base_class_name}{suffix}", config=config
        )
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
            if isinstance(root, strings.ClassName):
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
        python_name=strings.PythonIdentifier(value=name, prefix=config.field_prefix),
        example=data.example,
    )

    # Check for duplicates one more time (shouldn't happen but be safe)
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


openapi_python_client.parser.properties.model_property.ModelProperty.build = (
    model_property_build
)


# ============================================================================
# PATCH 20: EnumProperty.build - Use title directly without parent prefix
# ============================================================================
# When an enum schema has an explicit title, use it as the class name directly
# without prepending the parent context. This allows OpenAPI spec authors to
# control enum naming by adding title fields.
#
# Example: title: "PrimaryFormat" → class PrimaryFormat (not DownloadOrderPrimaryFormat)

_original_enum_build = EnumProperty.build


@classmethod  # type: ignore[misc]
def enum_build_with_title_support(
    cls,
    *,
    data: OAISchema,
    name: str,
    required: bool,
    schemas: Schemas,
    parent_name: str,
    config: Config,
) -> tuple[EnumProperty | NoneProperty | UnionProperty | PropertyError, Schemas]:
    """
    Patched EnumProperty.build that uses title directly without parent prefix.

    If the schema has a title, use it as the enum name without prepending
    the parent context. Otherwise, fall back to original behavior.
    """
    # If there's a title, temporarily clear parent_name so it won't be prefixed
    if data.title:
        return _original_enum_build(
            data=data,
            name=name,
            required=required,
            schemas=schemas,
            parent_name="",  # Empty parent = no prefix
            config=config,
        )

    # Otherwise, use original behavior
    return _original_enum_build(
        data=data,
        name=name,
        required=required,
        schemas=schemas,
        parent_name=parent_name,
        config=config,
    )


EnumProperty.build = enum_build_with_title_support


# ============================================================================
# PATCH 21: UnionProperty.build - Title propagation + discriminator stashing
# ============================================================================
# Two responsibilities, both layered on top of the original UnionProperty.build:
#
# 1. Propagate parent title to array enum items.
#    When a schema looks like:
#      anyOf: [{type: array, items: {enum: [...]}}, {type: null}]
#      title: "Primary Formats"
#    The title is on the parent (anyOf), not on the array or enum items
#    inside. We push the title (singularised) down to array children that
#    contain enum items, so the enum gets a proper name (e.g.,
#    "PrimaryFormat" instead of "DownloadOrderPrimaryFormatsType0Item").
#
# 2. Stash `discriminator` from the spec.
#    OpenAPI `discriminator:` blocks are dropped by the upstream generator
#    before reaching the render path. We capture `data.discriminator
#    .propertyName` after the original build runs and store it keyed by the
#    `UnionProperty` instance so the Jinja filter can emit
#    `Annotated[..., Field(discriminator="<name>")]`.
#    Keyed by id(prop) — UnionProperty instances are not cloned between
#    build and render in current upstream. If that ever changes, switch to
#    a structural key (python_name + inner class names).

_UNION_DISCRIMINATORS: dict[int, str] = {}

_original_union_build = union_module.UnionProperty.build


def _singularize_title(title: UntrustedString | str) -> UntrustedString:
    """
    Convert a plural title to singular PascalCase.

    "Primary Formats" → "PrimaryFormat"
    "Collections" → "Collection"
    """
    pascal = strings.pascal_case(title)
    # Simple singularization: remove trailing 's' if present (but not 'ss')
    if pascal.endswith("s") and not pascal.endswith("ss"):
        pascal = pascal[:-1]
    return UntrustedString(pascal)


@classmethod  # type: ignore[misc]
def union_build_with_title_propagation(
    cls,
    *,
    data: OAISchema,
    name: str,
    required: bool,
    schemas: Schemas,
    parent_name: str,
    config: Config,
) -> tuple:
    """
    Patched UnionProperty.build with two behaviours layered on the original:

    1. If the union schema has a title and contains an array with enum items,
       propagate the title (singularised) to the enum items so they get proper
       names.
    2. If the spec declares a `discriminator`, stash its propertyName (sanitised
       to a Python identifier) against the built `UnionProperty` so the Jinja
       filter can emit `Annotated[..., Field(discriminator=...)]`.
    """
    # Check if we should propagate title
    if data.title and data.anyOf:
        modified_any_of = []
        for sub_schema in data.anyOf:
            if (
                isinstance(sub_schema, OAISchema)
                and sub_schema.type == OAIDataType.ARRAY
                and sub_schema.items is not None
                and isinstance(sub_schema.items, OAISchema)
                and sub_schema.items.enum is not None
                and sub_schema.items.title is None
            ):
                # Propagate singularized title to the enum items
                singular_title = _singularize_title(data.title)
                modified_items = sub_schema.items.model_copy(
                    update={"title": singular_title}
                )
                modified_sub_schema = sub_schema.model_copy(
                    update={"items": modified_items}
                )
                modified_any_of.append(modified_sub_schema)
            else:
                modified_any_of.append(sub_schema)

        # Create modified data with propagated titles
        data = data.model_copy(update={"anyOf": modified_any_of})

    prop, schemas = _original_union_build(
        data=data,
        name=name,
        required=required,
        schemas=schemas,
        parent_name=parent_name,
        config=config,
    )

    # Stash discriminator so the jinja filter can emit
    # Annotated[Union[...], Field(discriminator=...)] at render time.
    # Pydantic's field discriminator looks up by Python attribute name, not
    # alias — so sanitise (e.g. "type" → "type_") to match the generated
    # variant field declarations.
    if (
        isinstance(prop, UnionProperty)
        and data.discriminator
        and data.discriminator.propertyName
    ):
        python_name = str(
            strings.PythonIdentifier(
                value=data.discriminator.propertyName, prefix=config.field_prefix
            )
        )
        _UNION_DISCRIMINATORS[id(prop)] = python_name

    return prop, schemas


union_module.UnionProperty.build = union_build_with_title_propagation


# ============================================================================
# PATCHES SUMMARY
# ============================================================================
print("✅ Applied 21 patches to openapi-python-client")
print("   📦 Type System (15 patches):")
print(
    "      • ListProperty: 3 patches (get_type_string, get_base_type_string, get_base_json_type_string)"
)
print(
    "      • PropertyProtocol: 2 patches (get_type_string with quoted parameter, to_string with None)"
)
print(
    "      • ConstProperty: 2 patches (Literal type handling; no Union[..., None] when default present)"
)
print("      • UnionProperty: 6 patches (quoted forward references, Union[...] syntax)")
print("      • ModelProperty: 1 patch (get_type_string with quoted parameter)")
print("      • EnumProperty: 1 patch (always quote enum names)")
print("   🏗️  Model Building (4 patches):")
print("      • property_from_data: Free-form objects → DictProperty (not empty models)")
print("      • ModelProperty.build: Handle duplicate model names with numeric suffixes")
print("      • EnumProperty.build: Use title directly without parent prefix")
print(
    "      • UnionProperty.build: Propagate parent title to array enum items; stash discriminator for Field(discriminator=...) emission"
)
print("   🔧 Strings (2 patches):")
print("      • RESERVED_WORDS: Allow 'id' as field name")
print("      • strings.sanitize: Replace colons in field names (geo:lat → geo_lat)")
