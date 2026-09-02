"""Tests for OpenAPI spec preprocessing."""

from builder.openapi_preprocessor import collapse_tuple_arrays


def test_prefix_items_collapse_to_a_single_items_schema():
    """Identical tuple positions must yield one element schema, not a union."""
    schema = {
        "type": "array",
        "prefixItems": [{"type": "number"}, {"type": "number"}],
        "items": False,
        "minItems": 2,
        "maxItems": 2,
    }

    assert collapse_tuple_arrays(schema) == {
        "type": "array",
        "items": {"type": "number"},
        "minItems": 2,
        "maxItems": 2,
    }


def test_prefix_item_labels_do_not_split_the_element_type():
    """Pydantic names each position, which must not make identical schemas distinct."""
    schema = {
        "type": "array",
        "prefixItems": [
            {"title": "Longitude", "type": "number"},
            {"title": "Latitude", "type": "number"},
        ],
        "items": {},
    }

    assert collapse_tuple_arrays(schema) == {
        "type": "array",
        "items": {"type": "number"},
    }


def test_differing_prefix_items_become_a_union():
    schema = {
        "type": "array",
        "prefixItems": [{"type": "string"}, {"type": "integer"}],
        "items": False,
    }

    assert collapse_tuple_arrays(schema) == {
        "type": "array",
        "items": {"anyOf": [{"type": "string"}, {"type": "integer"}]},
    }


def test_boolean_items_are_dropped_without_prefix_items():
    """`items: false` alone fails openapi-python-client's Schema validation."""
    assert collapse_tuple_arrays({"type": "array", "items": False}) == {"type": "array"}


def test_boolean_additional_properties_is_preserved():
    """Only `items` is affected; booleans are legitimate elsewhere."""
    schema = {"type": "object", "additionalProperties": False}

    assert collapse_tuple_arrays(schema) == schema


def test_nested_schemas_are_rewritten():
    spec = {
        "components": {
            "schemas": {
                "Point": {
                    "type": "object",
                    "properties": {
                        "coordinates": {
                            "type": "array",
                            "prefixItems": [{"type": "number"}],
                            "items": False,
                        }
                    },
                }
            }
        }
    }

    coordinates = collapse_tuple_arrays(spec)["components"]["schemas"]["Point"][
        "properties"
    ]["coordinates"]

    assert coordinates == {"type": "array", "items": {"type": "number"}}


def test_example_payloads_are_left_alone():
    """Example data is not a schema, so its keys must survive verbatim."""
    schema = {
        "type": "object",
        "example": {"prefixItems": [1, 2], "items": False},
    }

    assert collapse_tuple_arrays(schema) == schema
