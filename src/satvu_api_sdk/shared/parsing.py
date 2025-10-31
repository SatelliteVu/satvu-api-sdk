"""
Utility functions for parsing API responses using Pydantic's TypeAdapter.

This module provides a clean, performant way to parse JSON responses into
strongly-typed Pydantic models, with proper support for Union types, nested
models, and type coercion.
"""

import logging
from typing import Any
from pydantic import TypeAdapter, ValidationError

logger = logging.getLogger(__name__)

# Cache for TypeAdapters to avoid recreating them
# Key: id of type annotation -> Value: TypeAdapter instance
_type_adapter_cache: dict[int, TypeAdapter] = {}


def parse_response(
    data: Any,
    annotation: Any,
) -> Any:
    """
    Parse API response data into strongly-typed Pydantic models.

    Uses Pydantic's TypeAdapter for robust type conversion with:
    - Union type resolution (smart discriminator detection)
    - Nested model parsing
    - Automatic type coercion (str -> int, str -> datetime, etc.)
    - Comprehensive validation
    - Detailed error messages

    Args:
        data: Raw JSON-like data (dict, list, or primitive)
        annotation: Target type annotation (Union[...], list[...], BaseModel, etc.)

    Returns:
        Parsed object matching the annotation type

    Raises:
        ValueError: When data cannot be parsed into the specified type,
                   includes detailed validation errors from Pydantic

    Examples:
        >>> from typing import Union
        >>> result = parse_response(
        ...     {"id": "123", "name": "Test", "amount": 100},
        ...     Union[SimpleOrder, ResellerOrder]
        ... )
        >>> isinstance(result, SimpleOrder)
        True

        >>> # Type coercion works automatically
        >>> result = parse_response(
        ...     {"id": "456", "name": "Test", "amount": "200"},  # amount is string
        ...     Order
        ... )
        >>> result.amount == 200  # Coerced to int
        True
    """
    # Use annotation's id as cache key (safe because types are immutable)
    cache_key = id(annotation)

    # Get or create TypeAdapter for this annotation
    if cache_key not in _type_adapter_cache:
        logger.debug(f"Creating new TypeAdapter for {annotation}")
        adapter = TypeAdapter(annotation)
        _type_adapter_cache[cache_key] = adapter
    else:
        logger.debug(f"TypeAdapter cache hit for {annotation}")

    adapter = _type_adapter_cache[cache_key]

    try:
        # Let Pydantic handle everything: validation, coercion, Union resolution
        result = adapter.validate_python(data)
        logger.debug(f"Successfully parsed data as {type(result).__name__}")
        return result

    except ValidationError as e:
        # Convert Pydantic's ValidationError to ValueError with enhanced details
        logger.debug(f"Validation failed for {annotation}: {e}")

        # Extract useful info from Pydantic error
        error_count = len(e.errors())
        first_errors = e.errors()[:3]  # Show first 3 errors

        # Build helpful error message
        error_lines = [f"Failed to parse data as {annotation}"]

        if isinstance(data, dict):
            error_lines.append(f"Data keys: {list(data.keys())}")
        else:
            error_lines.append(f"Data type: {type(data).__name__}")

        error_lines.append(f"\nValidation errors ({error_count} total):")

        for err in first_errors:
            loc = " -> ".join(str(location) for location in err["loc"])
            msg = err["msg"]
            error_lines.append(f"  • {loc}: {msg}")

        if error_count > 3:
            error_lines.append(f"  ... and {error_count - 3} more errors")

        error_lines.append(f"\nFull error details: {str(e)}")

        raise ValueError("\n".join(error_lines)) from e


def normalize_keys(obj: Any) -> Any:
    """
    Recursively replaces colons in dictionary keys with underscores
    for a nested JSON-like object (dicts, lists, primitives).

    This is useful for APIs that return keys with colons, which aren't
    valid Python identifiers.

    Args:
        obj: Any JSON-like object (dict, list, or primitive)

    Returns:
        Same structure with colon keys replaced by underscore keys

    Examples:
        >>> normalize_keys({"geo:lat": 1.0, "geo:lon": 2.0})
        {"geo_lat": 1.0, "geo_lon": 2.0}
    """
    if isinstance(obj, dict):
        return {k.replace(":", "_"): normalize_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [normalize_keys(item) for item in obj]
    else:
        return obj  # Base case: primitive types (str, int, float, etc.)
