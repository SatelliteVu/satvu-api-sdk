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
from openapi_python_client import utils
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

# ============================================================================
# PATCH 1: Allow "id" as field name
# ============================================================================
# By default, "id" is reserved because it's a Python builtin.
# But it's a very common field name in APIs (user id, product id, etc.)
# So we remove it from the reserved words list.

RESERVED_WORDS = (set(dir(builtins)) | {"self", "true", "false", "datetime"}) - {"id"}
openapi_python_client.utils.RESERVED_WORDS = RESERVED_WORDS


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
) -> str:
    """Get type string for ListProperty without Unset."""
    if json:
        type_string = self.get_base_json_type_string()
    else:
        type_string = self.get_base_type_string()

    if no_optional or self.required:
        return type_string
    # Use None instead of Unset for optional lists
    return f"Union[None, {type_string}]"


def list_get_base_type_string(self, *, quoted: bool = False) -> str:
    """Use lowercase list[T] syntax."""
    return f"list[{self.inner_property.get_type_string()}]"


def list_get_base_json_type_string(self, *, quoted: bool = False) -> str:
    """Use lowercase list[T] syntax for JSON types."""
    return f"list[{self.inner_property.get_type_string(json=True)}]"


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
) -> str:
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
    return f"Union[None, {type_string}]"


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
) -> str:
    """Generate Literal type for const properties."""
    lit = f"Literal[{self.value.python_code}]"
    if not no_optional and not self.required:
        return f"Union[{lit}, None]"
    return lit


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
) -> set[str]:
    """Get all type strings in the union."""
    type_strings = self._get_inner_type_strings(json=json, quoted=quoted)
    if no_optional:
        return type_strings
    return type_strings


def union_get_inner_type_strings(self, json: bool, quoted: bool = True) -> set[str]:
    """Extract type strings from inner properties with quoted support."""
    result = set()
    for p in self.inner_properties:
        # Only ModelProperty supports quoted parameter
        if isinstance(p, ModelProperty):
            result.add(p.get_type_string(no_optional=True, json=json, quoted=quoted))
        else:
            result.add(p.get_type_string(no_optional=True, json=json))
    return result


def union_get_type_string_from_inner_type_strings(self, inner_types: set[str]) -> str:
    """
    Build union type string - CRITICAL for forward references.

    Uses Union[...] syntax when types are quoted (forward references).
    This is necessary because 'Type1' | 'Type2' is invalid Python syntax.
    """
    if len(inner_types) == 1:
        return inner_types.pop()

    # Check if any type is quoted (forward reference)
    has_quoted = any(t.startswith("'") and t.endswith("'") for t in inner_types)

    if has_quoted:
        # MUST use Union[...] syntax for quoted types
        return f"Union[{', '.join(sorted(inner_types, key=lambda x: x.lower()))}]"
    else:
        # Can use | syntax for non-quoted types (cleaner)
        return " | ".join(sorted(inner_types, key=lambda x: x.lower()))


def union_get_base_type_string(self, *, quoted: bool = True) -> str:
    """Get base type string with control over forward reference quoting."""
    return self._get_type_string_from_inner_type_strings(
        self._get_inner_type_strings(json=False, quoted=quoted)
    )


def union_get_base_json_type_string(self, *, quoted: bool = True) -> str:
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
) -> str:
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
    if "'" in type_string or '"' in type_string:
        return f"Union[None, {type_string}]"
    else:
        return f"None | {type_string}"


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
) -> str:
    """Get type string for model property with optional quoting."""
    if json:
        type_string = self.get_base_json_type_string()
    else:
        type_string = self.get_base_type_string()

    # Quote the type if requested (for forward references)
    if quoted and type_string == self.class_info.name:
        type_string = f"'{type_string}'"

    if no_optional or self.required:
        return type_string
    return f"Union[None, {type_string}]"


openapi_python_client.parser.properties.model_property.ModelProperty.get_type_string = (
    model_get_type_string
)


# ============================================================================
# PATCH 15: utils.sanitize - Replace colons in field names
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
    return re.sub(rf"[^\w{utils.DELIMITERS}]+", "", value)


openapi_python_client.utils.sanitize = sanitize


# ============================================================================
# PATCH 16: EnumProperty.get_base_type_string - Always quote enums
# ============================================================================
# Enum types should always be quoted as forward references


def enum_get_base_type_string(self, *, quoted: bool = False) -> str:
    """Always return quoted enum name (forward reference)."""
    return f"'{self.class_info.name}'"


openapi_python_client.parser.properties.enum_property.EnumProperty.get_base_type_string = enum_get_base_type_string


# ============================================================================
# PATCH 17: PropertyProtocol.to_string - Use None instead of UNSET for parameters
# ============================================================================
# Override to_string to generate parameter strings with None instead of UNSET


def property_to_string(self) -> str:
    """
    Generate parameter string with None instead of UNSET.

    For optional parameters, use None as default instead of UNSET.
    """
    type_string = self.get_type_string()

    if self.required or self.default is not None:
        if self.default is not None:
            return f"{self.python_name}: {type_string} = {self.default.python_code}"
        return f"{self.python_name}: {type_string}"

    # Optional parameter - use None instead of UNSET
    return f"{self.python_name}: {type_string} = None"


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

    name: str
    required: bool
    default: Value | None
    python_name: utils.PythonIdentifier
    description: str | None
    example: str | None
    _type_string: ClassVar[str] = "dict"
    _json_type_string: ClassVar[str] = "dict"

    @classmethod
    def build(
        cls,
        name: str,
        required: bool,
        default: Any,
        python_name: utils.PythonIdentifier,
        description: str | None,
        example: str | None,
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
        return Value(python_code=repr(value), raw_value=value)


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
                python_name=utils.PythonIdentifier(
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
    roots: set[ReferencePath | utils.ClassName],
) -> tuple[ModelProperty | PropertyError, Schemas]:
    """
    Build a ModelProperty from OAI schema data, handling duplicate names.

    This is a critical patch that prevents "duplicate model" errors by
    appending numeric suffixes to conflicting model names.
    """
    from openapi_python_client import utils
    from openapi_python_client.parser.properties import ModelProperty

    # Determine class name from title or name
    if not config.use_path_prefixes_for_title_model_names and data.title:
        class_string = data.title
    else:
        title = data.title or name
        if parent_name:
            class_string = f"{utils.pascal_case(parent_name)}{utils.pascal_case(title)}"
        else:
            class_string = title

    class_info = Class.from_string(string=class_string, config=config)

    # Handle duplicate names by adding numeric suffix
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
# PATCH 21: UnionProperty.build - Propagate parent title to array enum items
# ============================================================================
# When a schema like this is encountered:
#   anyOf: [{type: array, items: {enum: [...]}}, {type: null}]
#   title: "Primary Formats"
#
# The title is on the parent (anyOf), not on the array or enum items inside.
# This patch propagates the title from the anyOf schema down to array children
# that contain enum items, so the enum gets a proper name (e.g., "PrimaryFormat"
# instead of "DownloadOrderPrimaryFormatsType0Item").
#
# The title is singularized (e.g., "Primary Formats" → "PrimaryFormat") since
# the enum represents individual items, not the collection.

_original_union_build = union_module.UnionProperty.build


def _singularize_title(title: str) -> str:
    """
    Convert a plural title to singular PascalCase.

    "Primary Formats" → "PrimaryFormat"
    "Collections" → "Collection"
    """
    # Simple singularization: remove trailing 's' if present (but not 'ss')
    if title.endswith("s") and not title.endswith("ss"):
        title = title[:-1]
    # Convert to PascalCase without spaces
    return "".join(word.capitalize() for word in title.split())


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
    Patched UnionProperty.build that propagates title to array enum items.

    If the union schema has a title and contains an array with enum items,
    propagate the title (singularized) to the enum items so they get proper names.
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

    return _original_union_build(
        data=data,
        name=name,
        required=required,
        schemas=schemas,
        parent_name=parent_name,
        config=config,
    )


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
print("      • ConstProperty: 2 patches (Literal type handling)")
print("      • UnionProperty: 6 patches (quoted forward references, Union[...] syntax)")
print("      • ModelProperty: 1 patch (get_type_string with quoted parameter)")
print("      • EnumProperty: 1 patch (always quote enum names)")
print("   🏗️  Model Building (4 patches):")
print("      • property_from_data: Free-form objects → DictProperty (not empty models)")
print("      • ModelProperty.build: Handle duplicate model names with numeric suffixes")
print("      • EnumProperty.build: Use title directly without parent prefix")
print("      • UnionProperty.build: Propagate parent title to array enum items")
print("   🔧 Utilities (2 patches):")
print("      • RESERVED_WORDS: Allow 'id' as field name")
print("      • utils.sanitize: Replace colons in field names (geo:lat → geo_lat)")
