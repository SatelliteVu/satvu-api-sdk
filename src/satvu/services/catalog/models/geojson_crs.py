# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class GeojsonCRS(pydantic.BaseModel):
    """
    Attributes:
        properties (Union[None, dict]):
        type_ (Union[None, str]):
    """

    properties: Union[None, dict] = pydantic.Field(
        default=None, description=None, alias="properties"
    )
    type_: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
