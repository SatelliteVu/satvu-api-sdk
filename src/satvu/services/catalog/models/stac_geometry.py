# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class StacGeometry(BaseModel):
    """Searches items by performing intersection between their geometry and provided GeoJSON geometry.

    Attributes:
        bbox (Union[None, list[int]]): Bounding box.
        coordinates (Union[None, list[int]]): The coordinates of the Geometry object.
        geometries (Union[None, list[int]]): A list of geometries. For 'GeometryCollection' geometries only.
        type_ (None | str): The type of geometry represented.
    """

    bbox: Union[None, list[int]] = Field(
        default=None, description="""Bounding box.""", alias="bbox"
    )
    coordinates: Union[None, list[int]] = Field(
        default=None,
        description="""The coordinates of the Geometry object.""",
        alias="coordinates",
    )
    geometries: Union[None, list[int]] = Field(
        default=None,
        description="""A list of geometries. For 'GeometryCollection' geometries only.""",
        alias="geometries",
    )
    type_: None | str = Field(
        default=None, description="""The type of geometry represented.""", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
