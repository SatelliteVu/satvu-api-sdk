# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any, Union

import pydantic


class ContractsGeometry(pydantic.BaseModel):
    """Allowed geographical area of the contract

    Attributes:
        coordinates (Union[None, Any]): Value of any type, including null
        type_ (Union[None, str]):
    """

    coordinates: Union[None, Any] = pydantic.Field(
        default=None,
        description="""Value of any type, including null""",
        alias="coordinates",
    )
    type_: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
