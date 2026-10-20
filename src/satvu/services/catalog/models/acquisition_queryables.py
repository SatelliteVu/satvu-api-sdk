# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class AcquisitionQueryables(pydantic.BaseModel):
    """
    Attributes:
        id (Union[None, str]):
        schema (Union[None, str]):
        properties (Union[None, dict]):
        title (Union[None, str]):
        type_ (Union[None, str]):
    """

    id: Union[None, str] = pydantic.Field(default=None, description=None, alias="$id")
    schema_: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="$schema"
    )
    properties: Union[None, dict] = pydantic.Field(
        default=None, description=None, alias="properties"
    )
    title: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="title"
    )
    type_: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
