import json
from typing import Any

# Keys whose values are arbitrary user data rather than sub-schemas, so must not be
# rewritten by the schema walkers below.
_DATA_KEYS = frozenset({"const", "default", "enum", "example", "examples"})

# Ignored when deduplicating tuple positions: Pydantic labels each one (Longitude,
# Latitude, ...), which would otherwise make identical schemas look distinct.
_MERGE_IGNORED_KEYS = frozenset({"title", "description"})


def sanitize_operation_id(operation_id: str) -> str:
    """
    Sanitize an operationId to be a valid Python identifier.

    Replaces dashes with underscores (e.g., "get-credit" → "get_credit")

    Args:
        operation_id: The operationId from OpenAPI spec

    Returns:
        Sanitized operationId safe for Python function names
    """
    return operation_id.replace("-", "_")


def _process_operation(operation: dict[str, Any]) -> None:
    """
    Process a single operation to sanitize its operationId.

    Args:
        operation: Operation object from OpenAPI spec
    """
    operation_id = operation.get("operationId")
    if not operation_id:
        return

    sanitized_id = sanitize_operation_id(operation_id)
    if sanitized_id != operation_id:
        operation["operationId"] = sanitized_id


def _process_path_item(path_item: dict[str, Any]) -> None:
    """
    Process all operations in a path item.

    Args:
        path_item: Path item object from OpenAPI spec
    """
    http_methods = ["get", "post", "put", "patch", "delete", "options", "head", "trace"]

    for method in http_methods:
        operation = path_item.get(method)
        if operation:
            _process_operation(operation)


def _merge_tuple_item_schemas(
    prefix_items: list[Any], rest_items: Any
) -> dict[str, Any] | None:
    """
    Union the per-position schemas of a tuple into a single ``items`` schema.

    Args:
        prefix_items: The ``prefixItems`` list (one schema per tuple position)
        rest_items: The sibling ``items`` value, if it is a schema

    Returns:
        A single schema covering every position, or None if there is nothing to merge
    """
    candidates = [*prefix_items]
    if isinstance(rest_items, dict) and rest_items:
        candidates.append(rest_items)

    merged: list[dict[str, Any]] = []
    seen: set[str] = set()
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        stripped = {
            key: value
            for key, value in candidate.items()
            if key not in _MERGE_IGNORED_KEYS
        }
        fingerprint = json.dumps(stripped, sort_keys=True)
        if fingerprint not in seen:
            seen.add(fingerprint)
            merged.append(stripped)

    if not merged:
        return None
    if len(merged) == 1:
        return merged[0]
    return {"anyOf": merged}


def collapse_tuple_arrays(node: Any) -> Any:
    """
    Rewrite JSON Schema 2020-12 tuple validation into a plain array schema.

    Pydantic emits fixed-length tuples as ``prefixItems`` plus ``items: false``.
    openapi-python-client models ``items`` as a single optional schema, so a boolean
    there fails spec validation outright and ``prefixItems`` is ignored entirely
    (yielding ``list[Any]``). Collapsing the positions into one ``items`` schema keeps
    the spec parseable and the generated element type precise.

    Args:
        node: Any node of the OpenAPI specification

    Returns:
        The node with tuple arrays rewritten
    """
    if isinstance(node, list):
        return [collapse_tuple_arrays(item) for item in node]
    if not isinstance(node, dict):
        return node

    result = {
        key: value if key in _DATA_KEYS else collapse_tuple_arrays(value)
        for key, value in node.items()
    }

    prefix_items = result.pop("prefixItems", None)
    if prefix_items is not None:
        items = _merge_tuple_item_schemas(prefix_items, result.get("items"))
        if items is None:
            result.pop("items", None)
        else:
            result["items"] = items
    elif isinstance(result.get("items"), bool):
        result.pop("items")

    return result


def preprocess_openapi_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """
    Preprocess OpenAPI specification to fix issues.

    Transformations applied:
    1. Fix operationIds: Replace dashes with underscores
    2. Collapse JSON Schema 2020-12 tuple arrays into plain array schemas

    Args:
        spec: OpenAPI specification dictionary

    Returns:
        Preprocessed OpenAPI specification
    """
    spec = collapse_tuple_arrays(spec)

    paths = spec.get("paths")
    if not paths:
        return spec

    for path_item in paths.values():
        _process_path_item(path_item)

    return spec


def preprocess_for_sdk_generation(spec: dict[str, Any]) -> dict[str, Any]:
    """
    Main entry point for preprocessing OpenAPI specs for SDK generation.

    This function applies all necessary transformations to make the spec
    work with our SDK generation without requiring library patches.

    Args:
        spec: Raw OpenAPI specification dictionary

    Returns:
        Preprocessed specification ready for openapi-python-client
    """
    return preprocess_openapi_spec(spec)
