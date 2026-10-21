"""
Extract raw JSON schemas from parsed openapi-python-client objects.

Feeds hypothesis-jsonschema in the generated service tests.
"""

from typing import Any

from openapi_python_client.parser.responses import Response
from openapi_python_client.schema import UntrustedString
from openapi_python_client.schema.openapi_schema_pydantic import Reference


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

    media_type = response.data.content.get(UntrustedString("application/json"))
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
