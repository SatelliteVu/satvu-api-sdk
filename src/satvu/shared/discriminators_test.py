"""Tests for callable union discriminators."""

from typing import Literal

import pydantic
import pytest

from satvu.shared.discriminators import const_tag


class Assured(pydantic.BaseModel):
    product_: Literal["assured"] = pydantic.Field(default="assured", alias="product")


def test_const_tag_reads_python_name():
    tag = const_tag("type", default=None, python_name="type_")

    assert tag({"type_": "Point"}) == "Point"
    assert tag({"type": "Point", "type_": "Polygon"}) == "Point"


@pytest.mark.parametrize(
    ("value", "default", "expected"),
    [
        ({"product": "assured"}, "standard", "assured"),
        ({}, "standard", "standard"),
        ({}, None, None),
        (Assured(), "standard", "assured"),
        ("not-a-mapping", "standard", "standard"),
    ],
    ids=[
        "dict-tag",
        "dict-missing",
        "dict-missing-no-default",
        "instance-by-alias",
        "other",
    ],
)
def test_const_tag(value, default, expected):
    assert const_tag("product", default=default)(value) == expected
