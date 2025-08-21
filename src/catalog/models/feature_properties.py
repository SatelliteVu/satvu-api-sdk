from __future__ import annotations

import datetime
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_polygon import GeoJSONPolygon


class FeatureProperties(BaseModel):
    """
    Attributes:
        datetime_ (datetime.datetime): Acquisition datetime. Example: 2023-10-10T01:22:55Z.
        eo_cloud_cover (float): Estimate of cloud cover. Example: 25.
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground. Example: 3.21.
        platform (str): Platform name e.g. Hotsat-1. Example: Hotsat-1.
        price_currency (str): Price currency e.g. GBP. Example: GBP.
        price_value (int): Price of the image in minor units of the currency e.g. pence, cents. Example: 100000.
        proj_epsg (int): EPSG code. Defines the geographic coordinate system. Example: 32723.
        proj_geometry (GeoJSONPolygon):
        proj_shape (list[int]): Number of pixels in Y and X directions for the default grid. Example: [1100, 1200].
        proj_transform (list[float]): The affine transformation coefficients for the default grid.
        satvu_image_withheld (bool): Whether the image has ever been withheld for the contract. Example: True.
        satvu_publicly_available (datetime.datetime): Datetime at which the image was (or will be) made available for
            public consumption. Example: 2024-05-03T10:21:07.92846Z.
        view_azimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees. Example: 175.9374.
        view_off_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees. Example:
            1.452.
        view_sun_azimuth (float): Sun azimuth angle. The angle between truth north and the sun at the scene centre.
            Measured clockwise in degrees. Example: 150.846372.
        view_sun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun.
            Example: -50.829374.
    """

    datetime_: datetime.datetime = Field(
        ..., description="Acquisition datetime.", alias="datetime"
    )
    eo_cloud_cover: float = Field(
        ..., description="Estimate of cloud cover.", alias="eo:cloud_cover"
    )
    gsd: float = Field(
        ...,
        description="Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the ground.",
        alias="gsd",
    )
    platform: str = Field(
        ..., description="Platform name e.g. Hotsat-1.", alias="platform"
    )
    price_currency: str = Field(
        ..., description="Price currency e.g. GBP.", alias="price:currency"
    )
    price_value: int = Field(
        ...,
        description="Price of the image in minor units of the currency e.g. pence, cents.",
        alias="price:value",
    )
    proj_epsg: int = Field(
        ...,
        description="EPSG code. Defines the geographic coordinate system.",
        alias="proj:epsg",
    )
    proj_geometry: "GeoJSONPolygon" = Field(
        ..., description=None, alias="proj:geometry"
    )
    proj_shape: list[int] = Field(
        ...,
        description="Number of pixels in Y and X directions for the default grid.",
        alias="proj:shape",
    )
    proj_transform: list[float] = Field(
        ...,
        description="The affine transformation coefficients for the default grid.",
        alias="proj:transform",
    )
    satvu_image_withheld: bool = Field(
        ...,
        description="Whether the image has ever been withheld for the contract.",
        alias="satvu:image_withheld",
    )
    satvu_publicly_available: datetime.datetime = Field(
        ...,
        description="Datetime at which the image was (or will be) made available for public consumption.",
        alias="satvu:publicly_available",
    )
    view_azimuth: float = Field(
        ...,
        description="Viewing azimuth angle. The angle between the scene centre and true north. Measured clockwise from north in degrees.",
        alias="view:azimuth",
    )
    view_off_nadir: float = Field(
        ...,
        description="The angle between satellite nadir and the scene center. Measured in degrees.",
        alias="view:off_nadir",
    )
    view_sun_azimuth: float = Field(
        ...,
        description="Sun azimuth angle. The angle between truth north and the sun at the scene centre. Measured clockwise in degrees.",
        alias="view:sun_azimuth",
    )
    view_sun_elevation: float = Field(
        ...,
        description="Sun elevation angle. The angle from the tangent of the scene center to the sun.",
        alias="view:sun_elevation",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
