# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union

import pydantic

from ..models.satvu_cloud_confidence import SatvuCloudConfidence
from ..models.satvu_filter import SatvuFilter

if TYPE_CHECKING:
    from ..models.eo_band import EoBand


class StacPropertiesAcquisition(pydantic.BaseModel):
    """Metadata properties for satellite imagery with optimized serialization for acquisition items.

    Attributes:
        datetime_ (datetime.datetime): Acquisition datetime
        created (datetime.datetime): Time at which this STAC item was created
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str):
        view_azimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees.
        view_off_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees.
        view_sun_azimuth (float): Sun azimuth angle. The angle between truth north and the sun at the scene centre.
            Measured clockwise in degrees.
        view_sun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun
        satvu_filter ('SatvuFilter'):
        satvu_geometric_calibration (bool): Flag indicating if refined geometric processing was applied
        eo_cloud_cover (float): Estimate of cloud cover
        satvu_cloud_confidence (Union['SatvuCloudConfidence', None]): Confidence level of the cloud cover estimate
        instruments (list[str] | None):
        constellation (None | str):
        eo_bands (list[EoBand] | None):
    """

    datetime_: datetime.datetime = pydantic.Field(
        ..., description="""Acquisition datetime""", alias="datetime"
    )
    created: datetime.datetime = pydantic.Field(
        ..., description="""Time at which this STAC item was created""", alias="created"
    )
    gsd: float = pydantic.Field(
        ...,
        description="""Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the ground""",
        alias="gsd",
    )
    platform: str = pydantic.Field(..., description=None, alias="platform")
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
        description="""Sun azimuth angle. The angle between truth north and the sun at the scene centre. Measured clockwise in degrees.""",
        alias="view:sun_azimuth",
    )
    view_sun_elevation: float = pydantic.Field(
        ...,
        description="""Sun elevation angle. The angle from the tangent of the scene center to the sun""",
        alias="view:sun_elevation",
    )
    satvu_filter: SatvuFilter = pydantic.Field(
        ..., description=None, alias="satvu:filter"
    )
    satvu_geometric_calibration: bool = pydantic.Field(
        ...,
        description="""Flag indicating if refined geometric processing was applied""",
        alias="satvu:geometric_calibration",
    )
    eo_cloud_cover: float = pydantic.Field(
        ..., description="""Estimate of cloud cover""", alias="eo:cloud_cover"
    )
    satvu_cloud_confidence: Union[SatvuCloudConfidence, None] = pydantic.Field(
        default=None,
        description="""Confidence level of the cloud cover estimate""",
        alias="satvu:cloud_confidence",
    )
    instruments: list[str] | None = pydantic.Field(
        default=None, description=None, alias="instruments"
    )
    constellation: None | str = pydantic.Field(
        default=None, description=None, alias="constellation"
    )
    eo_bands: list[EoBand] | None = pydantic.Field(
        default=None, description=None, alias="eo:bands"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
