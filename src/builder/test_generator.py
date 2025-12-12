"""
Test generator for SDK service classes.

Generates property-based tests using hypothesis-jsonschema from OpenAPI specs.
Tests validate both SDK methods and Pydantic model parsing.
"""

import subprocess
from pathlib import Path
from typing import Any

from openapi_python_client import Project
from openapi_python_client.parser.openapi import Endpoint
from openapi_python_client.parser.responses import Response
from openapi_python_client.schema.openapi_schema_pydantic import Reference

from builder.schema_utils import (
    clean_schema,
    find_recursive_refs,
    remove_excluded_refs,
    remove_recursive_refs,
)


def extract_response_schema(response: Response) -> dict[str, Any] | None:
    """
    Extract raw JSON schema from an openapi-python-client Response object.

    Args:
        response: Parsed Response from openapi-python-client

    Returns:
        Raw JSON Schema dict for hypothesis, or None if not extractable
    """
    # If response has a Property, extract schema from Property.data
    # This contains the resolved oai.Schema that was used to generate the Property
    schema_obj = getattr(response.prop, "data", None)
    if schema_obj:
        # Convert oai.Schema Pydantic model to dict with proper aliasing ($ref instead of ref)
        return schema_obj.model_dump(mode="json", by_alias=True, exclude_none=True)

    # Fallback: try to extract from response.data.content (for inline schemas)
    if isinstance(response.data, Reference):
        return None

    if not response.data.content:
        return None

    media_type = response.data.content.get("application/json")
    if not media_type or not media_type.media_type_schema:
        return None

    if isinstance(media_type.media_type_schema, Reference):
        return None

    # Convert oai.Schema Pydantic model to dict with proper aliasing
    return media_type.media_type_schema.model_dump(
        mode="json", by_alias=True, exclude_none=True
    )


def extract_request_body_schema(endpoint) -> dict[str, Any] | None:
    """
    Extract request body schema from endpoint.

    Args:
        endpoint: Parsed Endpoint from openapi-python-client

    Returns:
        Raw JSON Schema dict for hypothesis, or None if no body
    """
    if not endpoint.bodies:
        return None

    body = endpoint.bodies[0]  # Take first body (usually only one)

    # Handle UnionProperty (Union of multiple body models)
    if type(body.prop).__name__ == "UnionProperty":
        # Extract schemas from each inner property
        inner_schemas = []
        for inner_prop in body.prop.inner_properties:
            if hasattr(inner_prop, "data"):
                schema = inner_prop.data.model_dump(
                    mode="json", by_alias=True, exclude_none=True
                )
                inner_schemas.append(schema)

        if inner_schemas:
            # Return oneOf schema for Union types
            return {"oneOf": inner_schemas}
        return None

    # Handle ListProperty (array of items)
    if type(body.prop).__name__ == "ListProperty":
        # ListProperty has an inner_property with the item schema
        if hasattr(body.prop, "inner_property") and hasattr(
            body.prop.inner_property, "data"
        ):
            item_schema = body.prop.inner_property.data.model_dump(
                mode="json", by_alias=True, exclude_none=True
            )
            # Return array schema with items
            return {"type": "array", "items": item_schema}
        return None

    # Handle regular ModelProperty
    if hasattr(body.prop, "data"):
        schema_obj = body.prop.data
        return schema_obj.model_dump(mode="json", by_alias=True, exclude_none=True)

    print(
        f"  [TESTS] Warning: No data attribute on {endpoint.name} body prop "
        f"(type: {type(body.prop).__name__})"
    )
    return None


def extract_query_param_schema(param) -> dict[str, Any] | None:
    """
    Extract schema for a query parameter.

    Args:
        param: QueryParameter from openapi-python-client

    Returns:
        Raw JSON Schema dict for hypothesis, or None if not extractable
    """
    # Try to extract schema from parameter's data attribute
    if hasattr(param, "data") and param.data:
        return param.data.model_dump(mode="json", by_alias=True, exclude_none=True)

    # Fallback: construct simple schema from python_type
    # This is a basic fallback for primitives
    type_mapping = {
        "str": "string",
        "int": "integer",
        "float": "number",
        "bool": "boolean",
    }

    python_type = param.python_type
    if python_type in type_mapping:
        return {"type": type_mapping[python_type]}

    return None


def generate_tests(
    api_name: str,
    project: Project,
    openapi_dict: dict,
    base_path: str,
    output_dir: Path,
) -> None:
    """
    Generate test file for a service API.

    Args:
        api_name: API identifier (e.g., 'catalog', 'wallet')
        project: Existing Project object with loaded templates
        openapi_dict: Raw OpenAPI dict with components/schemas
        base_path: Base path for the API (e.g., '/catalog/v1')
        output_dir: Directory to write test files to

    Generated files:
        - api_test.py: Test class with test methods
        - test_schemas.py: Operations dict with helper functions
    """
    # Extract and clean components/schemas for $ref resolution
    components = _prepare_components(openapi_dict)

    # Find recursive schemas once for all endpoints
    recursive_refs = find_recursive_refs(components)
    if recursive_refs:
        print(f"  [TESTS] Detected recursive schemas: {recursive_refs}")
        # Clean recursive refs from the definitions themselves
        # This is necessary because hypothesis-jsonschema will resolve $refs
        # to definitions, and those definitions must also be cycle-free
        components = {
            name: remove_recursive_refs(schema, recursive_refs)
            for name, schema in components.items()
        }

    # Build operations dict and endpoint data for templates
    operations, endpoints_data = _extract_operations(
        project, components, recursive_refs
    )

    # Skip if no testable endpoints
    if not endpoints_data:
        return

    # Render and write test files
    _render_test_files(
        api_name=api_name,
        project=project,
        components=components,
        operations=operations,
        endpoints_data=endpoints_data,
        base_path=base_path,
        output_dir=output_dir,
    )

    print(f"  [TESTS] Generated {len(endpoints_data)} test cases")


def _prepare_components(openapi_dict: dict) -> dict[str, Any]:
    """
    Extract and clean component schemas from OpenAPI dict.

    Args:
        openapi_dict: Raw OpenAPI dict

    Returns:
        Dict of schema name → cleaned schema
    """
    if "components" not in openapi_dict or "schemas" not in openapi_dict["components"]:
        return {}

    raw_schemas = openapi_dict["components"]["schemas"]
    return {
        name: remove_excluded_refs(clean_schema(schema))
        for name, schema in raw_schemas.items()
    }


def _prepare_schema_for_hypothesis(
    schema: dict[str, Any],
    components: dict[str, Any],
    recursive_refs: set[str],
) -> dict[str, Any]:
    """
    Prepare a schema for hypothesis-jsonschema.

    Applies all necessary transformations:
    1. Clean schema (2020-12 → draft-07, etc.)
    2. Remove excluded refs
    3. Remove recursive refs
    4. Attach definitions for $ref resolution

    Args:
        schema: Raw schema to prepare
        components: All component schemas (for definitions)
        recursive_refs: Set of recursive schema names to remove

    Returns:
        Schema ready for hypothesis-jsonschema
    """
    cleaned = remove_excluded_refs(clean_schema(schema))
    cleaned = remove_recursive_refs(cleaned, recursive_refs)
    return {**cleaned, "definitions": components}


def _extract_operations(
    project: Project,
    components: dict[str, Any],
    recursive_refs: set[str],
) -> tuple[dict, list]:
    """
    Extract operations dict and endpoint data from project.

    Args:
        project: openapi-python-client Project
        components: Cleaned component schemas
        recursive_refs: Set of recursive schema names

    Returns:
        Tuple of (operations dict, endpoints_data list)
    """
    operations = {}
    endpoints_data = []

    for collection in project.openapi.endpoint_collections_by_tag.values():
        for endpoint in collection.endpoints:
            operation_data, endpoint_info = _process_endpoint(
                endpoint, components, recursive_refs
            )

            if endpoint_info:
                key = (endpoint.path, endpoint.method.lower())
                operations[key] = operation_data
                endpoints_data.append(endpoint_info)

    return operations, endpoints_data


def _process_endpoint(
    endpoint: Endpoint,
    components: dict[str, Any],
    recursive_refs: set[str],
) -> tuple[dict, dict | None]:
    """
    Process a single endpoint, extracting schemas and metadata.

    Args:
        endpoint: Parsed Endpoint from openapi-python-client
        components: Cleaned component schemas
        recursive_refs: Set of recursive schema names

    Returns:
        Tuple of (operation_data dict, endpoint_info dict or None)
    """
    operation_data: dict[str, Any] = {
        "responses": {},
        "parameters": {},
    }

    response_info = {}
    error_response_info = {}
    has_204 = False

    # Process responses
    for response in endpoint.responses:
        status = response.status_code.pattern

        if status == "204":
            has_204 = True
            continue

        is_error = not status.startswith("2")

        if not response.prop:
            # Error responses without schema get a minimal schema
            if is_error:
                minimal_schema = {"type": "object"}
                operation_data["responses"][status] = {
                    "schema": minimal_schema,
                    "is_error": True,
                }
                error_response_info[status] = {
                    "status_code": int(status),
                    "schema": minimal_schema,
                    "has_schema": False,
                    "description": getattr(response.data, "description", ""),
                }
            continue

        schema = extract_response_schema(response)
        if not schema:
            continue

        prepared = _prepare_schema_for_hypothesis(schema, components, recursive_refs)
        operation_data["responses"][status] = {
            "schema": prepared,
            "is_error": is_error,
        }

        if is_error:
            error_response_info[status] = {
                "status_code": int(status),
                "schema": prepared,
                "has_schema": True,
                "description": getattr(response.data, "description", ""),
            }
        else:
            response_info[status] = {
                "status_code": int(status),
                "schema": prepared,
                "type_string": response.prop.get_type_string(),
                "description": getattr(response.data, "description", ""),
            }

    # Process request body
    body_schema = extract_request_body_schema(endpoint)
    if body_schema:
        prepared = _prepare_schema_for_hypothesis(
            body_schema, components, recursive_refs
        )
        operation_data["requestBody"] = {"schema": prepared}

    # Process required query parameters
    for param in endpoint.query_parameters:
        if param.required:
            param_schema = extract_query_param_schema(param)
            if param_schema:
                operation_data["parameters"][param.python_name] = {
                    "schema": clean_schema(param_schema)
                }

    # Return None for endpoint_info if nothing testable
    if not (response_info or error_response_info or has_204):
        return operation_data, None

    endpoint_info = {
        "endpoint": endpoint,
        "responses": response_info,
        "error_responses": error_response_info,
        "has_204": has_204,
    }

    return operation_data, endpoint_info


def _render_test_files(
    api_name: str,
    project: Project,
    components: dict[str, Any],
    operations: dict,
    endpoints_data: list,
    base_path: str,
    output_dir: Path,
) -> None:
    """
    Render and write test files from templates.

    Args:
        api_name: API identifier
        project: Project with Jinja2 environment
        components: Component schemas
        operations: Operations dict
        endpoints_data: Endpoint metadata list
        base_path: API base path
        output_dir: Output directory
    """
    # Get spec version from GeneratorData
    spec_version = getattr(project.openapi, "version", "unknown")

    context = {
        "api_name": api_name,
        "service_class_name": f"{api_name.capitalize()}Service",
        "endpoints": endpoints_data,
        "spec_version": spec_version,
        "components": components,
        "operations": operations,
        "base_path": base_path,
    }

    # Load and render templates
    test_template = project.env.get_template("test_module.py.jinja")
    schemas_template = project.env.get_template("test_schemas.py.jinja")

    test_content = test_template.render(**context)
    schemas_content = schemas_template.render(**context)

    # Write files
    test_file = output_dir / "api_test.py"
    schemas_file = output_dir / "test_schemas.py"

    test_file.write_text(test_content, encoding="utf-8")
    schemas_file.write_text(schemas_content, encoding="utf-8")

    # Clean up with ruff
    _format_with_ruff(test_file, schemas_file)


def _format_with_ruff(test_file: Path, schemas_file: Path) -> None:
    """
    Format generated files with ruff.

    Args:
        test_file: Path to test file
        schemas_file: Path to schemas file
    """
    # First apply autofixes (remove unused imports, etc.)
    subprocess.run(  # nosec B607
        ["ruff", "check", "--fix", str(test_file), str(schemas_file)],
        check=False,
        capture_output=True,
    )
    # Then format the code
    subprocess.run(  # nosec B607
        ["ruff", "format", str(test_file), str(schemas_file)],
        check=False,
        capture_output=True,
    )
