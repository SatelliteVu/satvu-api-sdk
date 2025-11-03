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
    # Work on paths
    if "paths" in spec:
        for path, path_item in spec["paths"].items():
            # Each path can have multiple HTTP methods
            for method in [
                "get",
                "post",
                "put",
                "patch",
                "delete",
                "options",
                "head",
                "trace",
            ]:
                if method in path_item:
                    operation = path_item[method]

                    # Fix operationId if present
                    if "operationId" in operation:
                        original_id = operation["operationId"]
                        sanitized_id = sanitize_operation_id(original_id)

                        if original_id != sanitized_id:
                            operation["operationId"] = sanitized_id

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
    spec = preprocess_openapi_spec(spec)
    return spec
