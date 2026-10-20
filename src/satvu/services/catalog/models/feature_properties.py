# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.geo_json_polygon import GeoJSONPolygon


class FeatureProperties(pydantic.BaseModel):
    """Properties of the Item

    Attributes:
        created (datetime.datetime): Creation datetime of the metadata for this Item. Example: 2023-10-10T01:22:55Z.
        datetime_ (datetime.datetime): Acquisition datetime. Example: 2023-10-10T01:22:55Z.
        eo_cloud_cover (float | None): Estimate of cloud cover. Example: 25.
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground. Example: 3.21.
        platform (str): Platform name e.g. Hotsat-1. Example: Hotsat-1.
        price_currency (str): Price currency e.g. GBP. Example: GBP.
        price_value (int): Price of the image in minor units of the currency e.g. pence, cents. Example: 100000.
        satvu_image_withheld (bool): Whether the image has ever been withheld for the contract. Example: True.
        satvu_publicly_available (str): When the image was (or will be) made available for public consumption. Usually
            an ISO-8601 date-time, but may be the literal 'infinity' or '-infinity' when the image has no finite public-
            availability date. Example: 2024-05-03T10:21:07.92846Z.
        updated (datetime.datetime): Datetime the metadata for this Item was last updated. Example:
            2023-10-10T01:22:55Z.
        view_azimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees. Example: 175.9374.
        view_off_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees. Example:
            1.452.
        view_sun_azimuth (float): Sun azimuth angle. The angle between true north and the sun at the scene centre.
            Measured clockwise in degrees. Example: 150.846372.
        view_sun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun.
            Example: -50.829374.
        proj_epsg (int | None): EPSG code. Defines the geographic coordinate system. Example: 32723.
        proj_geometry (Union['GeoJSONPolygon', None]):
        proj_shape (list[int] | None): Number of pixels in Y and X directions for the default grid. Example: [1100,
            1200].
        proj_transform (list[float] | None): The affine transformation coefficients for the default grid.
        satvu_filter (Union[None, str]): Optical filter applied during acquisition. Example: night.
        satvu_geometric_calibration (Union[None, bool]): Whether geometric calibration has been applied to the image.
            Example: True.
    """

    created: datetime.datetime = pydantic.Field(
        ...,
        description="""Creation datetime of the metadata for this Item.""",
        alias="created",
    )
    datetime_: datetime.datetime = pydantic.Field(
        ..., description="""Acquisition datetime.""", alias="datetime"
    )
    eo_cloud_cover: float | None = pydantic.Field(
        ..., description="""Estimate of cloud cover.""", alias="eo:cloud_cover"
    )
    gsd: float = pydantic.Field(
        ...,
        description="""Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the ground.""",
        alias="gsd",
    )
    platform: str = pydantic.Field(
        ..., description="""Platform name e.g. Hotsat-1.""", alias="platform"
    )
    price_currency: str = pydantic.Field(
        ..., description="""Price currency e.g. GBP.""", alias="price:currency"
    )
    price_value: int = pydantic.Field(
        ...,
        description="""Price of the image in minor units of the currency e.g. pence, cents.""",
        alias="price:value",
    )
    satvu_image_withheld: bool = pydantic.Field(
        ...,
        description="""Whether the image has ever been withheld for the contract.""",
        alias="satvu:image_withheld",
    )
    satvu_publicly_available: str = pydantic.Field(
        ...,
        description="""When the image was (or will be) made available for public consumption. Usually an ISO-8601 date-time, but may be the literal 'infinity' or '-infinity' when the image has no finite public-availability date.""",
        alias="satvu:publicly_available",
    )
    updated: datetime.datetime = pydantic.Field(
        ...,
        description="""Datetime the metadata for this Item was last updated.""",
        alias="updated",
    )
    view_azimuth: float = pydantic.Field(
        ...,
        description="""Viewing azimuth angle. The angle between the scene centre and true north. Measured clockwise from north in degrees.""",
        alias="view:azimuth",
    )
    view_off_nadir: float = pydantic.Field(
        ...,
        description="""The angle between satellite nadir and the scene center. Measured in degrees.""",
        alias="view:off_nadir",
    )
    view_sun_azimuth: float = pydantic.Field(
        ...,
        description="""Sun azimuth angle. The angle between true north and the sun at the scene centre. Measured clockwise in degrees.""",
        alias="view:sun_azimuth",
    )
    view_sun_elevation: float = pydantic.Field(
        ...,
        description="""Sun elevation angle. The angle from the tangent of the scene center to the sun.""",
        alias="view:sun_elevation",
    )
    proj_epsg: int | None = pydantic.Field(
        default=None,
        description="""EPSG code. Defines the geographic coordinate system.""",
        alias="proj:epsg",
    )
    proj_geometry: Union[GeoJSONPolygon, None] = pydantic.Field(
        default=None, description=None, alias="proj:geometry"
    )
    proj_shape: list[int] | None = pydantic.Field(
        default=None,
        description="""Number of pixels in Y and X directions for the default grid.""",
        alias="proj:shape",
    )
    proj_transform: list[float] | None = pydantic.Field(
        default=None,
        description="""The affine transformation coefficients for the default grid.""",
        alias="proj:transform",
    )
    satvu_filter: Union[None, str] = pydantic.Field(
        default=None,
        description="""Optical filter applied during acquisition.""",
        alias="satvu:filter",
    )
    satvu_geometric_calibration: Union[None, bool] = pydantic.Field(
        default=None,
        description="""Whether geometric calibration has been applied to the image.""",
        alias="satvu:geometric_calibration",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
