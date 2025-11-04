from typing import Any


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


def preprocess_openapi_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """
    Preprocess OpenAPI specification to fix issues.

    Transformations applied:
    1. Fix operationIds: Replace dashes with underscores

    Args:
        spec: OpenAPI specification dictionary

    Returns:
        Preprocessed OpenAPI specification
    """
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
