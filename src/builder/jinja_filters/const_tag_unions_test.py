"""Tests for constant-field union discriminator detection and rendering."""

import ast
from collections.abc import Mapping
from typing import Annotated, Literal, Union
from unittest.mock import Mock

import pydantic
import pytest
from openapi_python_client.parser.properties.model_property import ModelProperty
from openapi_python_client.parser.properties.none import NoneProperty
from openapi_python_client.parser.properties.union import UnionProperty
from openapi_python_client.schema import Schema

from builder.jinja_filters.const_tag_unions import const_tag_for
from builder.jinja_filters.to_pydantic_model_field import to_pydantic_model_field
from satvu.shared.discriminators import const_tag

STANDARD = ("Standard", {"product": "standard"}, [])
ASSURED = ("Assured", {"product": "assured"}, ["product"])


def _model(name: str, consts: Mapping[str, object], required: list[str]) -> Mock:
    model = Mock(spec=ModelProperty)
    model.data = Schema.model_validate(
        {
            "type": "object",
            "properties": {
                "datetime": {"type": "string"},
                **{key: {"const": value} for key, value in consts.items()},
            },
            "required": ["datetime", *required],
        }
    )
    model.get_type_string.return_value = f"'{name}'"
    return model


def _union(*members: Mock, required: bool = True) -> Mock:
    union = Mock(spec=UnionProperty)
    union.inner_properties = list(members)
    union.required = required
    union.python_name = "properties"
    union.name = "properties"
    union.description = None
    union.default = None
    union.get_type_string.return_value = "Union['Assured', 'Standard']"
    return union


def test_one_optional_variant_becomes_the_default():
    const_tag_info = const_tag_for(_union(_model(*STANDARD), _model(*ASSURED)))

    assert const_tag_info is not None
    assert const_tag_info.alias == "product"
    assert const_tag_info.default == "standard"
    assert const_tag_info.variants == (
        ("'Assured'", "assured"),
        ("'Standard'", "standard"),
    )
    assert not const_tag_info.nullable


def test_all_required_has_no_default():
    union = _union(
        _model("Point", {"type": "Point"}, ["type"]),
        _model("Polygon", {"type": "Polygon"}, ["type"]),
    )

    const_tag_info = const_tag_for(union)

    assert const_tag_info is not None
    assert const_tag_info.default is None
    assert 'python_name="type_"' in const_tag_info.type_string()


@pytest.mark.parametrize(
    "members",
    [
        pytest.param(
            [_model("A", {"type": "a"}, []), _model("B", {"type": "b"}, [])],
            id="two-optional-tags-are-ambiguous",
        ),
        pytest.param(
            [
                _model("A", {"type": "x"}, ["type"]),
                _model("B", {"type": "x"}, ["type"]),
            ],
            id="duplicate-tag-values",
        ),
        pytest.param(
            [_model("A", {"type": "a"}, ["type"]), _model("B", {}, [])],
            id="constant-not-shared",
        ),
        pytest.param(
            [_model("A", {"type": 1}, ["type"]), _model("B", {"type": 2}, ["type"])],
            id="non-string-constant",
        ),
        pytest.param(
            [_model("A", {"type": "a"}, ["type"]), Mock()],
            id="non-model-member",
        ),
        pytest.param([_model(*STANDARD)], id="single-model"),
    ],
)
def test_not_detected(members):
    assert const_tag_for(_union(*members)) is None


@pytest.mark.parametrize(
    ("extra", "required"),
    [([Mock(spec=NoneProperty)], True), ([], False)],
    ids=["null-member", "optional-field"],
)
def test_nullable_union_keeps_none(extra, required):
    union = _union(_model(*STANDARD), _model(*ASSURED), *extra, required=required)

    const_tag_info = const_tag_for(union)

    assert const_tag_info is not None
    assert const_tag_info.type_string().startswith("Union[None, Annotated[")


def test_tag_values_are_escaped():
    hostile = 'a"); import os; ("'
    union = _union(
        _model("A", {"type": hostile}, ["type"]),
        _model("B", {"type": "b"}, ["type"]),
    )

    const_tag_info = const_tag_for(union)

    assert const_tag_info is not None
    tree = ast.parse(const_tag_info.type_string(), mode="eval")
    tags = [
        node.args[0].value
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and getattr(node.func, "attr", None) == "Tag"
        and isinstance(node.args[0], ast.Constant)
    ]
    assert tags == [hostile, "b"]


class Standard(pydantic.BaseModel):
    product: Literal["standard"] = pydantic.Field(default="standard", alias="product")
    datetime: str


class Assured(pydantic.BaseModel):
    product: Literal["assured"] = pydantic.Field(default="assured", alias="product")
    datetime: str


@pytest.mark.parametrize(
    ("properties", "expected"),
    [
        ({"datetime": "x"}, Standard),
        ({"datetime": "x", "product": "standard"}, Standard),
        ({"datetime": "x", "product": "assured"}, Assured),
    ],
)
def test_rendered_field_parses_the_spec_variant(properties, expected):
    """Without the discriminator, smart mode parses a tagless body as Assured."""
    line = to_pydantic_model_field(_union(_model(*STANDARD), _model(*ASSURED)))
    namespace = {
        "pydantic": pydantic,
        "Annotated": Annotated,
        "Union": Union,
        "Standard": Standard,
        "Assured": Assured,
        "const_tag": const_tag,
    }

    exec(f"class Model(pydantic.BaseModel):\n    {line}\n", namespace)  # noqa: S102  # nosec B102

    model_cls = namespace["Model"]
    model_cls.model_rebuild(_types_namespace=namespace)
    model = model_cls.model_validate({"properties": properties})
    assert type(model.properties) is expected
