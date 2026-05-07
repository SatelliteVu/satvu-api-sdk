# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class AcquisitionQueryables(BaseModel):
    """
    Attributes:
        id (Union[None, str]):
        schema (Union[None, str]):
        properties (Union[None, dict]):
        title (Union[None, str]):
        type_ (Union[None, str]):
    """

    id: Union[None, str] = Field(default=None, description=None, alias="$id")
    schema_: Union[None, str] = Field(default=None, description=None, alias="$schema")
    properties: Union[None, dict] = Field(
        default=None, description=None, alias="properties"
    )
    title: Union[None, str] = Field(default=None, description=None, alias="title")
    type_: Union[None, str] = Field(default=None, description=None, alias="type")

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
