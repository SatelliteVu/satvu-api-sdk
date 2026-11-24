"""Tests for OpenAPI spec preprocessing."""

import pytest

from builder.openapi_preprocessor import (
    collapse_tuple_arrays,
    prefix_clashing_enum_titles,
)


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


def _op(values: list) -> dict:
    return {"type": "string", "enum": values, "title": "Op"}


def _components(schemas: dict) -> dict:
    return {"components": {"schemas": schemas}}


def _op_titles(spec: dict) -> dict[str, str]:
    return {
        name: schema["properties"]["op"]["title"]
        for name, schema in spec["components"]["schemas"].items()
    }


@pytest.mark.parametrize("order", [["And", "Cmp"], ["Cmp", "And"]])
def test_every_clashing_enum_title_is_prefixed_regardless_of_order(order):
    ops = {"And": _op(["and", "or"]), "Cmp": _op(["=", "<>"])}
    spec = _components({name: {"properties": {"op": ops[name]}} for name in order})

    assert _op_titles(prefix_clashing_enum_titles(spec)) == {
        "And": "AndOp",
        "Cmp": "CmpOp",
    }


def test_enums_with_identical_values_keep_their_shared_title():
    spec = _components(
        {
            "A": {"properties": {"op": _op(["x", "y"])}},
            "B": {"properties": {"op": _op(["y", "x"])}},
        }
    )

    assert prefix_clashing_enum_titles(spec) == spec


def test_enum_nested_in_any_of_does_not_clash():
    """The builder names a nested enum `<Parent><Name>Type0`, not by the outer title."""
    nullable = {
        "anyOf": [{"type": "string", "enum": ["p"]}, {"type": "null"}],
        "title": "Op",
    }
    spec = _components(
        {
            "A": {"properties": {"op": _op(["x"])}},
            "B": {"properties": {"op": nullable}},
        }
    )

    assert prefix_clashing_enum_titles(spec) == spec


def test_prefixed_title_keeps_word_boundaries():
    status = {"type": "string", "enum": ["a"], "title": "status"}
    spec = _components(
        {
            "order": {"properties": {"op": status}},
            "task": {"properties": {"op": {**status, "enum": ["b"]}}},
        }
    )

    assert _op_titles(prefix_clashing_enum_titles(spec)) == {
        "order": "OrderStatus",
        "task": "TaskStatus",
    }


def test_component_level_enums_are_not_renamed():
    """Components are shared via $ref, so only inline enums are candidates."""
    spec = _components(
        {
            "Op": _op(["a"]),
            "A": {"properties": {"op": _op(["x"])}},
        }
    )

    renamed = prefix_clashing_enum_titles(spec)["components"]["schemas"]

    assert renamed["Op"]["title"] == "Op"
    assert renamed["A"]["properties"]["op"]["title"] == "Op"
