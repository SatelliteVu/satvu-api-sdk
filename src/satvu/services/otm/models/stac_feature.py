# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.link_1 import Link1
    from ..models.point_geometry import PointGeometry
    from ..models.polygon_geometry import PolygonGeometry


class StacFeature(BaseModel):
    """STAC Feature (Item).

    A STAC Item is a GeoJSON Feature with additional STAC-specific fields.
    It represents a single spatiotemporal asset and includes links to related
    resources and downloadable assets.

        Attributes:
            id (str): The unique identifier for this item.
            collection (str): The ID of the STAC Collection this item belongs to.
            bbox (list[float | int]): The bounding box of the asset represented by this item.
            properties (dict): A map of additional metadata for the item.
            type_ (Literal['Feature']):  Default: 'Feature'.
            stac_version (Union[None, str]): The STAC version the Item implements. Default: '1.0.0'.
            geometry (Union['PointGeometry', 'PolygonGeometry', None]): Defines the full footprint of the asset represented
                by this item.
            links (Union[None, list[Link1]]): A list of link objects to resources and related URLs.
            assets (Union[None, dict]): A map of asset objects that can be downloaded, each with a unique key.
            stac_extensions (Union[None, list[str]]): A list of STAC extensions the Item implements.
    """

    id: str = Field(
        ..., description="""The unique identifier for this item.""", alias="id"
    )
    collection: str = Field(
        ...,
        description="""The ID of the STAC Collection this item belongs to.""",
        alias="collection",
    )
    bbox: list[float | int] = Field(
        ...,
        description="""The bounding box of the asset represented by this item.""",
        alias="bbox",
    )
    properties: dict = Field(
        ...,
        description="""A map of additional metadata for the item.""",
        alias="properties",
    )
    type_: Literal["Feature"] = Field(default="Feature", description=None, alias="type")
    stac_version: Union[None, str] = Field(
        default="1.0.0",
        description="""The STAC version the Item implements.""",
        alias="stac_version",
    )
    geometry: Union[PointGeometry, PolygonGeometry, None] = Field(
        default=None,
        description="""Defines the full footprint of the asset represented by this item.""",
        alias="geometry",
    )
    links: Union[None, list[Link1]] = Field(
        default=None,
        description="""A list of link objects to resources and related URLs.""",
        alias="links",
    )
    assets: Union[None, dict] = Field(
        default=None,
        description="""A map of asset objects that can be downloaded, each with a unique key.""",
        alias="assets",
    )
    stac_extensions: Union[None, list[str]] = Field(
        default=None,
        description="""A list of STAC extensions the Item implements.""",
        alias="stac_extensions",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
