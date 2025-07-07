import datetime
from typing import Union

from pydantic import BaseModel

from ..models.polygon import Polygon
from ..models.satvu_filter import SatvuFilter
from ..models.stac_properties_v5_processing_software_name_version import (
    StacPropertiesV5ProcessingSoftwareNameVersion,
)


class StacPropertiesV5(BaseModel):
    """
    Attributes:
        datetime (datetime.datetime): Acquisition datetime
        created (datetime.datetime): Time at which this STAC item was created
        created_at (datetime.datetime): Time at which this STAC item was created (deprecated - use 'created')
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str): Platform name. E.g. Hotsat-1
        processing_software (StacPropertiesV5ProcessingSoftwareNameVersion):
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
        proj_geometry (Union[None, Polygon]): Defines the projected footprint.
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

    datetime: datetime.datetime
    created: datetime.datetime
    created_at: datetime.datetime
    gsd: float
    platform: str
    processing_software: "StacPropertiesV5ProcessingSoftwareNameVersion"
    proj_epsg: int
    proj_shape: list[int]
    view_azimuth: float
    view_off_nadir: float
    view_sun_azimuth: float
    view_sun_elevation: float
    eo_cloud_cover: Union[None, float] = None
    proj_bbox: Union[None, list[float]] = None
    proj_geometry: Union[None, Polygon] = None
    proj_transform: Union[None, list[float]] = None
    satvu_filter: Union[None, SatvuFilter] = None
    satvu_geometric_calibration: Union[None, bool] = None
    satvu_radiometric_calibration: Union[None, bool] = None
    satvu_atmospheric_model: Union[None, bool] = None
    satvu_atmospheric_model_transmission: Union[None, float] = None
    satvu_atmospheric_model_upwelling: Union[None, float] = None
    satvu_atmospheric_model_downwelling: Union[None, float] = None
    satvu_sensitivity: Union[None, float] = None
