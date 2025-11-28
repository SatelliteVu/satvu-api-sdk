import subprocess
from pathlib import Path
from typing import Any

from openapi_python_client import Project
from openapi_python_client.parser.responses import Response
from openapi_python_client.schema.openapi_schema_pydantic import Reference


UUID_PATTERN_CONSTRAINT = (
    "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
)


def uuid_pattern_constraint(result: dict[str, Any]):
    """
    Add pattern constraint for UUID fields in JSON schema.
    hypothesis-jsonschema treats format as a hint, so it can generate invalid UUIDs.
    Adding pattern ensures hypothesis generates valid UUIDs that pass Pydantic validation.

    Args:
        result: JSON schema dict to modify
    """
    if result.get("type") == "string" and result.get("format") == "uuid":
        if "pattern" not in result:
            # Standard UUID regex pattern (lowercase hex with hyphens)
            result["pattern"] = UUID_PATTERN_CONSTRAINT


def clean_schema(obj: Any) -> Any:
    """
    Clean JSON schema for hypothesis-jsonschema compatibility.

    Args:
        obj: JSON schema object (dict, list, or primitive)

    Returns:
        Cleaned JSON schema object
    """
    if isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            # Skip empty composition arrays and default nullable
            if key in ("allOf", "anyOf", "oneOf", "prefixItems") and value == []:
                continue
            if key == "nullable" and value is False:
                continue

            # Handle OpenAPI 3.0 exclusive min/max (incompatible with JSON Schema draft-07)
            # In OpenAPI 3.0: exclusiveMinimum is a number
            # In JSON Schema draft-07: exclusiveMinimum is boolean, requires minimum
            if key in ("exclusiveMinimum", "exclusiveMaximum"):
                # Skip these for now - hypothesis-jsonschema doesn't handle them well
                continue

            # Rewrite OpenAPI 3.0 style refs to JSON Schema style
            if key == "$ref" and isinstance(value, str):
                result[key] = value.replace("#/components/schemas/", "#/definitions/")
            else:
                result[key] = clean_schema(value)

        # Add UUID pattern constraint after processing all fields
        uuid_pattern_constraint(result)

        return result
    elif isinstance(obj, list):
        return [clean_schema(item) for item in obj]
    else:
        return obj


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
    if hasattr(response.prop, "data"):
        schema_obj = response.prop.data
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
        f"  [TESTS] Warning: No data attribute on {endpoint.name} body prop (type: {type(body.prop).__name__})"
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
    # Extract components/schemas for $ref resolution from raw OpenAPI dict
    components = {}
    if "components" in openapi_dict and "schemas" in openapi_dict["components"]:
        raw_schemas = openapi_dict["components"]["schemas"]
        # Clean and rewrite refs in each schema
        components = {
            name: clean_schema(schema) for name, schema in raw_schemas.items()
        }

    # Build operations dict: (path, method) -> {responses, requestBody, parameters}
    operations = {}
    endpoints_data = []  # Still needed for template

    for collection in project.openapi.endpoint_collections_by_tag.values():
        for endpoint in collection.endpoints:
            key = (endpoint.path, endpoint.method.lower())

            operation_data = {
                "responses": {},
                "parameters": {},
            }

            # Extract response schemas
            response_info = {}
            error_response_info = {}
            has_204 = False
            for response in endpoint.responses:
                status_pattern = response.status_code.pattern

                # Track 204 No Content responses
                if status_pattern == "204":
                    has_204 = True
                    continue

                # Determine if this is a success (2xx) or error (4xx/5xx) response
                is_error_response = not status_pattern.startswith("2")

                # Skip responses without a property (no schema)
                if not response.prop:
                    # For error responses without schema, create a minimal schema
                    if is_error_response:
                        minimal_schema = {"type": "object"}
                        operation_data["responses"][status_pattern] = {
                            "schema": minimal_schema,
                            "is_error": True,
                        }
                        error_response_info[status_pattern] = {
                            "status_code": int(status_pattern),
                            "schema": minimal_schema,
                            "has_schema": False,
                            "description": response.data.description
                            if hasattr(response.data, "description")
                            else "",
                        }
                    continue

                # Extract raw JSON schema for hypothesis
                schema = extract_response_schema(response)

                if schema:
                    # Clean schema and rewrite refs for hypothesis-jsonschema
                    schema = clean_schema(schema)
                    # Attach definitions for $ref resolution
                    schema["definitions"] = components

                    operation_data["responses"][status_pattern] = {
                        "schema": schema,
                        "is_error": is_error_response,
                    }

                    if is_error_response:
                        # Store error response info
                        error_response_info[status_pattern] = {
                            "status_code": int(status_pattern),
                            "schema": schema,
                            "has_schema": True,
                            "description": response.data.description
                            if hasattr(response.data, "description")
                            else "",
                        }
                    else:
                        # Store success response info for template (backwards compat)
                        response_info[status_pattern] = {
                            "status_code": int(status_pattern),
                            "schema": schema,
                            "type_string": response.prop.get_type_string(),
                            "description": response.data.description
                            if hasattr(response.data, "description")
                            else "",
                        }

            # Extract request body schema
            body_schema = extract_request_body_schema(endpoint)
            if body_schema:
                body_schema = clean_schema(body_schema)
                # Attach definitions for $ref resolution
                body_schema["definitions"] = components
                operation_data["requestBody"] = {"schema": body_schema}

            # Extract required query parameter schemas
            for param in endpoint.query_parameters:
                if param.required:
                    param_schema = extract_query_param_schema(param)
                    if param_schema:
                        param_schema = clean_schema(param_schema)
                        operation_data["parameters"][param.python_name] = {
                            "schema": param_schema
                        }

            # Include endpoints with testable responses (success or error)
            if response_info or error_response_info or has_204:
                operations[key] = operation_data

                endpoints_data.append(
                    {
                        "endpoint": endpoint,
                        "responses": response_info,
                        "error_responses": error_response_info,
                        "has_204": has_204,
                    }
                )

    # If no endpoints with schemas, skip generation
    if not endpoints_data:
        return

    # Prepare template context
    spec_version = "unknown"
    if hasattr(project.openapi, "info") and project.openapi.info:
        spec_version = getattr(project.openapi.info, "version", "unknown")

    context = {
        "api_name": api_name,
        "service_class_name": f"{api_name.capitalize()}Service",
        "endpoints": endpoints_data,
        "spec_version": spec_version,
        "components": components,
        "operations": operations,  # NEW: operations dict
        "base_path": base_path,
    }

    # Load templates from custom_template_path (src/builder/templates/)
    test_template = project.env.get_template("test_module.py.jinja")
    schemas_template = project.env.get_template("test_schemas.py.jinja")

    # Render and write
    test_content = test_template.render(**context)
    schemas_content = schemas_template.render(**context)

    test_file = output_dir / "api_test.py"
    schemas_file = output_dir / "test_schemas.py"

    test_file.write_text(test_content, encoding="utf-8")
    schemas_file.write_text(schemas_content, encoding="utf-8")

    print(f"  [TESTS] Generated {len(endpoints_data)} test cases")

    # Clean up generated test files with ruff
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
