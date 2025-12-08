"""
JSON Schema utilities for hypothesis-jsonschema compatibility.

Problem: hypothesis-jsonschema cannot generate data for recursive schemas
(e.g., CQL2's booleanExpression which references itself via andOrExpression).
It will hang or raise Unsatisfiable.

Solution:
1. Detect which schemas are recursive (find_recursive_refs)
2. Remove recursive variants from oneOf/anyOf, leaving non-recursive options
   (e.g., booleanExpression oneOf [andOrExpression, boolean] → [boolean])

This allows hypothesis to generate valid data by choosing non-recursive paths.

Additionally, this module handles JSON Schema dialect conversion:
- OpenAPI 3.1 uses JSON Schema 2020-12
- hypothesis-jsonschema only supports draft-07
- clean_schema() converts 2020-12 → draft-07 (e.g., prefixItems → items)
"""

from typing import Any

# Standard UUID regex pattern (lowercase hex with hyphens)
# hypothesis-jsonschema treats "format": "uuid" as a hint, not a constraint,
# so we add an explicit pattern to ensure valid UUIDs are generated
UUID_PATTERN = "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"

# Schema names to exclude from oneOf/anyOf variants.
# These are rarely-used types that cause hypothesis to hang or timeout.
EXCLUDED_SCHEMA_REFS = {
    "GeometryCollection",
}


def clean_schema(obj: Any) -> Any:
    """
    Clean JSON schema for hypothesis-jsonschema compatibility.

    Performs:
    - JSON Schema 2020-12 → draft-07 conversion (prefixItems → items)
    - OpenAPI ref style → JSON Schema ref style (#/components/schemas/ → #/definitions/)
    - UUID pattern constraint addition
    - Removal of incompatible keywords (exclusiveMinimum/Maximum as numbers)
    - Removal of empty arrays that would be invalid

    Args:
        obj: JSON schema (dict, list, or primitive)

    Returns:
        Cleaned schema compatible with hypothesis-jsonschema
    """
    if isinstance(obj, dict):
        result = {}

        for key, value in obj.items():
            # Skip empty composition arrays (invalid in JSON Schema)
            # Note: prefixItems included here - skip BEFORE converting to items
            if (
                key in ("allOf", "anyOf", "oneOf", "items", "prefixItems")
                and value == []
            ):
                continue

            # Skip nullable: false (default, not needed)
            if key == "nullable" and value is False:
                continue

            # Skip exclusiveMinimum/Maximum - incompatible representations
            # OpenAPI 3.0: exclusiveMinimum is a number
            # JSON Schema draft-07: exclusiveMinimum is boolean + requires minimum
            if key in ("exclusiveMinimum", "exclusiveMaximum"):
                continue

            # Convert prefixItems → items (JSON Schema 2020-12 → draft-07)
            # 2020-12 uses prefixItems for tuple validation
            # draft-07 uses items (array form) for the same purpose
            if key == "prefixItems":
                result["items"] = clean_schema(value)
                continue

            # Rewrite OpenAPI-style refs to JSON Schema style
            if key == "$ref" and isinstance(value, str):
                result[key] = value.replace("#/components/schemas/", "#/definitions/")
            else:
                result[key] = clean_schema(value)

        # Add UUID pattern constraint
        # hypothesis-jsonschema treats format as a hint, so we need explicit pattern
        if (
            result.get("type") == "string"
            and result.get("format") == "uuid"
            and "pattern" not in result
        ):
            result["pattern"] = UUID_PATTERN

        return result

    elif isinstance(obj, list):
        return [clean_schema(item) for item in obj]

    else:
        return obj


def remove_excluded_refs(obj: Any) -> Any:
    """
    Remove excluded schema refs from oneOf/anyOf variants.

    Some schemas (e.g., GeometryCollection) are recursive or complex
    and cause hypothesis to hang. We exclude them from Union types.

    Args:
        obj: JSON schema (dict, list, or primitive)

    Returns:
        Schema with excluded refs removed from oneOf/anyOf
    """
    if isinstance(obj, dict):
        result = {}

        for key, value in obj.items():
            if key in ("oneOf", "anyOf") and isinstance(value, list):
                # Filter out excluded $refs
                filtered = []
                for variant in value:
                    if isinstance(variant, dict) and "$ref" in variant:
                        ref_name = variant["$ref"].split("/")[-1]
                        if ref_name in EXCLUDED_SCHEMA_REFS:
                            continue
                    filtered.append(remove_excluded_refs(variant))

                # Only include if we have variants left
                if filtered:
                    result[key] = filtered
            else:
                result[key] = remove_excluded_refs(value)

        return result

    elif isinstance(obj, list):
        return [remove_excluded_refs(item) for item in obj]

    else:
        return obj


def find_recursive_refs(definitions: dict[str, Any]) -> set[str]:
    """
    Find schema names involved in recursive cycles.

    Uses DFS (Depth-First Search) with path tracking. If we encounter a $ref we've already
    seen in the current path, that schema is part of a cycle.

    Args:
        definitions: Dict of schema name → schema definition

    Returns:
        Set of schema names that are involved in recursive cycles

    Example:
        Given definitions where:
        - booleanExpression refs andOrExpression
        - andOrExpression refs booleanExpression (cycle!)

        Returns: set of recursive schema names
    """
    recursive: set[str] = set()

    def find_in_schema(schema: Any, current_path: frozenset[str]) -> None:
        """DFS through schema, tracking current path for cycle detection."""
        if not isinstance(schema, dict):
            return

        for key, value in schema.items():
            if key == "$ref" and isinstance(value, str):
                ref_name = value.split("/")[-1]
                if ref_name in current_path:
                    # Found a cycle - this ref points back to an ancestor
                    recursive.add(ref_name)
                elif ref_name in definitions:
                    # Follow the ref, adding it to the current path
                    find_in_schema(
                        definitions[ref_name],
                        current_path | {ref_name},
                    )

            elif isinstance(value, dict):
                find_in_schema(value, current_path)

            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        find_in_schema(item, current_path)

    # Check each definition as a potential cycle starting point
    for name, definition in definitions.items():
        find_in_schema(definition, frozenset({name}))

    return recursive


def remove_recursive_refs(obj: Any, recursive_refs: set[str]) -> Any:
    """
    Remove recursive schema refs from oneOf/anyOf variants.

    This allows hypothesis to generate data by choosing non-recursive paths.
    For example: booleanExpression oneOf [andOrExpression, notExpression, boolean]
    becomes [boolean] after removing recursive andOrExpression and notExpression.

    Warning: If ALL variants are recursive, the oneOf/anyOf keeps original value.
    This may still cause hypothesis issues, but is better than an empty array.

    Args:
        obj: JSON schema (dict, list, or primitive)
        recursive_refs: Set of schema names that are recursive

    Returns:
        Schema with recursive refs removed from oneOf/anyOf
    """
    if not recursive_refs:
        return obj

    if isinstance(obj, dict):
        result = {}

        for key, value in obj.items():
            if key in ("oneOf", "anyOf") and isinstance(value, list):
                # Filter out recursive $refs
                filtered = []
                for variant in value:
                    if isinstance(variant, dict) and "$ref" in variant:
                        ref_name = variant["$ref"].split("/")[-1]
                        if ref_name in recursive_refs:
                            continue
                    filtered.append(remove_recursive_refs(variant, recursive_refs))

                # If all variants were recursive, keep original to avoid invalid schema
                result[key] = filtered if filtered else value

            else:
                result[key] = remove_recursive_refs(value, recursive_refs)

        return result

    elif isinstance(obj, list):
        return [remove_recursive_refs(item, recursive_refs) for item in obj]

    else:
        return obj
