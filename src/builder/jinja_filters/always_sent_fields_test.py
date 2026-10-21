"""Tests for the always-sent request fields Jinja filter."""

from types import SimpleNamespace
from typing import cast

import pytest
from openapi_python_client.parser.properties.const import ConstProperty
from openapi_python_client.parser.properties.protocol import PropertyProtocol

from builder.jinja_filters.always_sent_fields import always_sent_fields


def _prop(name: str, *, default: object = None) -> PropertyProtocol:
    stub = SimpleNamespace(python_name=name, required=True, default=default)
    return cast(PropertyProtocol, stub)


def _const(name: str) -> PropertyProtocol:
    const = object.__new__(ConstProperty)
    for attr, value in {"python_name": name, "required": True}.items():
        object.__setattr__(const, attr, value)
    return cast(PropertyProtocol, const)


@pytest.mark.parametrize(
    ("prop", "expected"),
    [
        (_const("type_"), ["type_"]),
        (_prop("limit", default=10), ["limit"]),
        (_prop("name"), []),
        (_prop("schema", default="x"), ["schema_"]),
    ],
)
def test_always_sent_fields(prop, expected):
    assert always_sent_fields([prop]) == expected
