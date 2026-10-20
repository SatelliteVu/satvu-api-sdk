"""Tests for the Pydantic model field Jinja filter."""

from enum import StrEnum
from types import SimpleNamespace
from typing import cast

import pydantic
import pytest
from openapi_python_client.parser.properties.protocol import PropertyProtocol

from builder.jinja_filters.to_pydantic_model_field import to_pydantic_model_field


class Field(StrEnum):
    NAME = "name"


def _prop(*, required: bool) -> PropertyProtocol:
    stub = SimpleNamespace(
        python_name="field",
        name="field",
        description=None,
        default=None,
        required=required,
        get_type_string=lambda: "Field",
    )
    return cast(PropertyProtocol, stub)


@pytest.mark.parametrize("required", [True, False])
def test_spec_schema_named_field_does_not_shadow_pydantic(required):
    """A generated model may import a spec enum called `Field` into module scope."""
    line = to_pydantic_model_field(_prop(required=required))
    namespace = {"pydantic": pydantic, "Field": Field}

    exec(f"class Model(pydantic.BaseModel):\n    {line}\n", namespace)  # noqa: S102  # nosec B102

    assert namespace["Model"](field="name").field is Field.NAME
