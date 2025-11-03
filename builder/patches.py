"""
Monkey-patches for openapi-python-client.
"""

import builtins
import re

import openapi_python_client
from attr import evolve
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
from openapi_python_client.parser.properties.model_property import (
    _process_property_data,
)
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
# PATCH 5-6: ConstProperty type strings
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
# PATCH 7-12: UnionProperty type handling
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

    # Avoid duplicate None in union (e.g., from anyOf: [string, null])
    if "None" in type_string or "null" in type_string.lower():
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
# PATCH 13: ModelProperty.get_type_string with quoted support
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
    if quoted:
        if type_string == self.class_info.name:
            type_string = f"'{type_string}'"

    if no_optional or self.required:
        return type_string
    return f"Union[None, {type_string}]"


openapi_python_client.parser.properties.model_property.ModelProperty.get_type_string = (
    model_get_type_string
)


# ============================================================================
# PATCH 14: utils.sanitize - Replace colons in field names
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
# PATCH 15: EnumProperty.get_base_type_string - Always quote enums
# ============================================================================
# Enum types should always be quoted as forward references


def enum_get_base_type_string(self, *, quoted: bool = False) -> str:
    """Always return quoted enum name (forward reference)."""
    return f"'{self.class_info.name}'"


openapi_python_client.parser.properties.enum_property.EnumProperty.get_base_type_string = enum_get_base_type_string


# ============================================================================
# PATCH 16: ModelProperty.build - Handle duplicate model names
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
# PATCHES SUMMARY
# ============================================================================
print("✅ Applied 16 minimal patches to openapi-python-client")
print("   📦 Type System (13 patches):")
print(
    "      • ListProperty: 3 patches (get_type_string, get_base_type_string, get_base_json_type_string)"
)
print("      • ConstProperty: 2 patches (Literal type handling)")
print("      • UnionProperty: 6 patches (quoted forward references, Union[...] syntax)")
print("      • ModelProperty: 1 patch (get_type_string with quoted parameter)")
print("      • EnumProperty: 1 patch (always quote enum names)")
print("   🏗️  Model Building (1 patch):")
print("      • ModelProperty.build: Handle duplicate model names with numeric suffixes")
print("   🔧 Utilities (2 patches):")
print("      • RESERVED_WORDS: Allow 'id' as field name")
print("      • utils.sanitize: Replace colons in field names (geo:lat → geo_lat)")
