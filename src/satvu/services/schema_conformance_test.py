"""Tests for the minimal-dump request body conformance check."""

from typing import Any, Literal

import pydantic
import pytest

from satvu.services.schema_conformance import (
    assert_minimal_dump_conforms,
    minimal_request_body,
)

_FEATURE = {
    "type": "object",
    "required": ["type", "name"],
    "properties": {"type": {"const": "Feature"}, "name": {"type": "string"}},
}


@pytest.mark.parametrize(
    ("schema", "body", "expected"),
    [
        pytest.param(
            {
                "type": "object",
                "required": ["name"],
                "properties": {"name": {"type": "string"}, "note": {"type": "string"}},
            },
            {"name": "a", "note": "b"},
            {"name": "a"},
            id="optional dropped",
        ),
        pytest.param(
            _FEATURE,
            {"type": "Feature", "name": "a"},
            {"name": "a"},
            id="required const dropped",
        ),
        pytest.param(
            {
                "type": "object",
                "required": ["limit", "name"],
                "properties": {
                    "limit": {"type": "integer", "default": 10},
                    "name": {"type": "string"},
                },
            },
            {"limit": 10, "name": "a"},
            {"name": "a"},
            id="required default dropped",
        ),
        pytest.param(
            {
                "type": "object",
                "required": ["kind", "name"],
                "properties": {
                    "kind": {"allOf": [{"$ref": "#/definitions/Kind"}], "default": "x"},
                    "name": {"type": "string"},
                },
                "definitions": {"Kind": {"type": "string"}},
            },
            {"kind": "x", "name": "a"},
            {"name": "a"},
            id="default beside a ref wrapper dropped",
        ),
        pytest.param(
            {
                "type": "object",
                "required": ["kind", "tag"],
                "properties": {
                    "kind": {"$ref": "#/definitions/Kind"},
                    "tag": {"$ref": "#/definitions/Tag"},
                },
                "definitions": {
                    "Kind": {"type": "string", "enum": ["a", "b"], "default": "a"},
                    "Tag": {"const": "Feature"},
                },
            },
            {"kind": "a", "tag": "Feature"},
            {"kind": "a"},
            id="default on a referenced schema kept, const behind a ref dropped",
        ),
        pytest.param(
            {
                "type": "object",
                "required": ["geometry"],
                "properties": {
                    "geometry": {
                        "anyOf": [{"$ref": "#/definitions/Point"}, {"type": "string"}]
                    }
                },
                "definitions": {
                    "Point": {
                        "type": "object",
                        "required": ["type", "x"],
                        "properties": {
                            "type": {"const": "Point"},
                            "x": {"type": "number"},
                        },
                    }
                },
            },
            {"geometry": {"type": "Point", "x": 1}},
            {"geometry": {"x": 1}},
            id="single object branch drops its constant",
        ),
        pytest.param(
            {
                "allOf": [
                    {"$ref": "#/definitions/Base"},
                    {
                        "type": "object",
                        "required": ["name"],
                        "properties": {"name": {"type": "string"}},
                    },
                ],
                "definitions": {
                    "Base": {
                        "type": "object",
                        "required": ["type"],
                        "properties": {"type": {"const": "Feature"}},
                    }
                },
            },
            {"type": "Feature", "name": "a", "extra": 1},
            {"name": "a"},
            id="multi-member allOf merged",
        ),
        pytest.param(
            {
                "oneOf": [
                    {
                        "type": "object",
                        "required": ["product", "name"],
                        "properties": {
                            "product": {"const": "standard"},
                            "name": {"type": "string"},
                        },
                    },
                    {
                        "type": "object",
                        "required": ["product"],
                        "properties": {"product": {"const": "assured"}},
                    },
                ]
            },
            {"product": "standard", "name": "a"},
            {"product": "standard", "name": "a"},
            id="union variant keeps its tag",
        ),
    ],
)
def test_minimal_request_body(schema, body, expected):
    assert minimal_request_body(body, schema) == expected


class _Stripped(pydantic.BaseModel):
    type_: Literal["Feature"] = pydantic.Field(default="Feature", alias="type")
    name: str

    model_config = pydantic.ConfigDict(validate_by_name=True, validate_by_alias=True)


class _Kept(_Stripped):
    def model_post_init(self, context: Any, /) -> None:
        self.__pydantic_fields_set__ = self.model_fields_set.union(["type_"])


def test_minimal_dump_conforms_when_constants_are_kept():
    assert_minimal_dump_conforms(_Kept, {"type": "Feature", "name": "a"}, _FEATURE)


def test_minimal_dump_fails_when_exclude_unset_strips_a_constant():
    with pytest.raises(AssertionError, match="'type' is a required property"):
        assert_minimal_dump_conforms(
            _Stripped, {"type": "Feature", "name": "a"}, _FEATURE
        )


def test_minimal_dump_stands_down_for_a_non_conforming_body():
    assert_minimal_dump_conforms(_Stripped, {"name": 1}, _FEATURE)


def test_minimal_dump_skips_a_schema_it_cannot_reduce():
    with pytest.raises(pytest.skip.Exception):
        assert_minimal_dump_conforms(_Stripped, {"name": "a"}, {"type": "object"})
