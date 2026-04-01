# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class QueryableProperty(BaseModel):
    """
    Attributes:
        enum (Union[None, list[str]]): Allowed values.
        format_ (Union[None, str]): The format of the property.
        title (Union[None, str]): The title of the property.
        type_ (Union[None, str]): The type of the property.
    """

    enum: Union[None, list[str]] = Field(
        default=None, description="""Allowed values.""", alias="enum"
    )
    format_: Union[None, str] = Field(
        default=None, description="""The format of the property.""", alias="format"
    )
    title: Union[None, str] = Field(
        default=None, description="""The title of the property.""", alias="title"
    )
    type_: Union[None, str] = Field(
        default=None, description="""The type of the property.""", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
