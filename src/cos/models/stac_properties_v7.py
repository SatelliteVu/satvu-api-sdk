import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.polygon_1 import Polygon1
from ..models.satvu_filter import SatvuFilter
from ..models.stac_properties_v7_processing_software_name_version import (
    StacPropertiesV7ProcessingSoftwareNameVersion,
)


class StacPropertiesV7(BaseModel):
    """
    Attributes:
        datetime_ (datetime.datetime): Acquisition datetime
        created (datetime.datetime): Time at which this STAC item was created
        created_at (datetime.datetime): Time at which this STAC item was created (deprecated - use 'created')
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str): Platform name. E.g. Hotsat-1
        processing_software (StacPropertiesV7ProcessingSoftwareNameVersion):
        proj_epsg (int): EPSG code. Defines the geographic coordinate system
        proj_shape (list[int]): Number of pixels in Y and X directions for the default grid
        view_azimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees.
        view_off_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees.
        view_sun_azimuth (float): Sun azimuth angle. The angle between truth north and the sun at the scene centre.
            Measured clockwise in degrees.
        view_sun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun
        eo_cloud_cover (Union[None, float]): Estimate of cloud cover
        proj_bbox (Union[None, list[float]]):
        proj_geometry (Union[None, Polygon1]): Defines the projected footprint.
        proj_transform (Union[None, list[float]]): The affine transformation coefficients for the default grid
        satvu_filter (Union[None, SatvuFilter]): Filter used for earth view acquisition
        satvu_geometric_calibration (Union[None, bool]): Flag indiciating if refined geometric processing was applied
        satvu_radiometric_calibration (Union[None, bool]): Flag indicating if radiometric calibration parameters are
            available
        satvu_atmospheric_model (Union[None, bool]): Flag indicating if atmospheric model parameters are available
        satvu_atmospheric_model_transmission (Union[None, float]): Atmospheric model transmission
        satvu_atmospheric_model_upwelling (Union[None, float]): Model upwelling radiance term
        satvu_atmospheric_model_downwelling (Union[None, float]): Model downwelling radiance term
        satvu_sensitivity (Union[None, float]): Modelled one-sigma brightness temperature temporal noise at 300 K in
            kelvin
    """

    datetime_: datetime.datetime = Field(
        ..., description="Acquisition datetime", alias="datetime"
    )
    created: datetime.datetime = Field(
        ..., description="Time at which this STAC item was created", alias="created"
    )
    created_at: datetime.datetime = Field(
        ...,
        description="Time at which this STAC item was created (deprecated - use 'created')",
        alias="created_at",
    )
    gsd: float = Field(
        ...,
        description="Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the ground",
        alias="gsd",
    )
    platform: str = Field(
        ..., description="Platform name. E.g. Hotsat-1", alias="platform"
    )
    processing_software: "StacPropertiesV7ProcessingSoftwareNameVersion" = Field(
        ..., description=None, alias="processing:software"
    )
    proj_epsg: int = Field(
        ...,
        description="EPSG code. Defines the geographic coordinate system",
        alias="proj:epsg",
    )
    proj_shape: list[int] = Field(
        ...,
        description="Number of pixels in Y and X directions for the default grid",
        alias="proj:shape",
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
        description="Sun elevation angle. The angle from the tangent of the scene center to the sun",
        alias="view:sun_elevation",
    )
    eo_cloud_cover: Union[None, float] = Field(
        None, description="Estimate of cloud cover", alias="eo:cloud_cover"
    )
    proj_bbox: Union[None, list[float]] = Field(
        None, description=None, alias="proj:bbox"
    )
    proj_geometry: Union[None, Polygon1] = Field(
        None, description="Defines the projected footprint.", alias="proj:geometry"
    )
    proj_transform: Union[None, list[float]] = Field(
        None,
        description="The affine transformation coefficients for the default grid",
        alias="proj:transform",
    )
    satvu_filter: Union[None, SatvuFilter] = Field(
        None, description="Filter used for earth view acquisition", alias="satvu:filter"
    )
    satvu_geometric_calibration: Union[None, bool] = Field(
        None,
        description="Flag indiciating if refined geometric processing was applied",
        alias="satvu:geometric_calibration",
    )
    satvu_radiometric_calibration: Union[None, bool] = Field(
        None,
        description="Flag indicating if radiometric calibration parameters are available",
        alias="satvu:radiometric_calibration",
    )
    satvu_atmospheric_model: Union[None, bool] = Field(
        None,
        description="Flag indicating if atmospheric model parameters are available",
        alias="satvu:atmospheric_model",
    )
    satvu_atmospheric_model_transmission: Union[None, float] = Field(
        None,
        description="Atmospheric model transmission",
        alias="satvu:atmospheric_model_transmission",
    )
    satvu_atmospheric_model_upwelling: Union[None, float] = Field(
        None,
        description="Model upwelling radiance term",
        alias="satvu:atmospheric_model_upwelling",
    )
    satvu_atmospheric_model_downwelling: Union[None, float] = Field(
        None,
        description="Model downwelling radiance term",
        alias="satvu:atmospheric_model_downwelling",
    )
    satvu_sensitivity: Union[None, float] = Field(
        None,
        description="Modelled one-sigma brightness temperature temporal noise at 300 K in kelvin",
        alias="satvu:sensitivity",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
