# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class Queryables(BaseModel):
    """
    Attributes:
        id (str): The URL of the endpoint.
        schema (str): The schema of the response. Example: http://json-schema.org/draft-07/schema#.
        type_ (str): The type of the resource. Example: object.
        properties (Union[None, dict]): A map of queryable properties to use as search filters.
        title (Union[None, str]): The title of the queryables schema.
    """

    id: str = Field(..., description="""The URL of the endpoint.""", alias="$id")
    schema_: str = Field(
        ..., description="""The schema of the response.""", alias="$schema"
    )
    type_: str = Field(..., description="""The type of the resource.""", alias="type")
    properties: Union[None, dict] = Field(
        default=None,
        description="""A map of queryable properties to use as search filters.""",
        alias="properties",
    )
    title: Union[None, str] = Field(
        default=None,
        description="""The title of the queryables schema.""",
        alias="title",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
