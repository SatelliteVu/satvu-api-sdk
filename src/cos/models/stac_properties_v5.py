import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..models.satvu_filter import SatvuFilter

if TYPE_CHECKING:
    from ..models.polygon import Polygon
    from ..models.stac_properties_v5_processing_software_name_version import (
        StacPropertiesV5ProcessingSoftwareNameVersion,
    )


@dataclass
class StacPropertiesV5:
    """
    Attributes:
        datetime_ (datetime.datetime): Acquisition datetime
        created (datetime.datetime): Time at which this STAC item was created
        created_at (datetime.datetime): Time at which this STAC item was created (deprecated - use 'created')
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str): Platform name. E.g. Hotsat-1
        processingsoftware (StacPropertiesV5ProcessingSoftwareNameVersion):
        projepsg (int): EPSG code. Defines the geographic coordinate system
        projshape (list[int]): Number of pixels in Y and X directions for the default grid
        viewazimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees.
        viewoff_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees.
        viewsun_azimuth (float): Sun azimuth angle. The angle between truth north and the sun at the scene centre.
            Measured clockwise in degrees.
        viewsun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun
        eocloud_cover (Union[None, float]): Estimate of cloud cover
        projbbox (Union[None, list[float]]):
        projgeometry (Union['Polygon', None]): Defines the projected footprint.
        projtransform (Union[None, list[float]]): The affine transformation coefficients for the default grid
        satvufilter (Union[None, SatvuFilter]): Filter used for earth view acquisition
        satvugeometric_calibration (Union[None, bool]): Flag indiciating if refined geometric processing was applied
        satvuradiometric_calibration (Union[None, bool]): Flag indicating if radiometric calibration parameters are
            available
        satvuatmospheric_model (Union[None, bool]): Flag indicating if atmospheric model parameters are available
        satvuatmospheric_model_transmission (Union[None, float]): Atmospheric model transmission
        satvuatmospheric_model_upwelling (Union[None, float]): Model upwelling radiance term
        satvuatmospheric_model_downwelling (Union[None, float]): Model downwelling radiance term
        satvusensitivity (Union[None, float]): Modelled one-sigma brightness temperature temporal noise at 300 K in
            kelvin
    """

    datetime_: datetime.datetime
    created: datetime.datetime
    created_at: datetime.datetime
    gsd: float
    platform: str
    processingsoftware: "StacPropertiesV5ProcessingSoftwareNameVersion"
    projepsg: int
    projshape: list[int]
    viewazimuth: float
    viewoff_nadir: float
    viewsun_azimuth: float
    viewsun_elevation: float
    eocloud_cover: Union[None, float] = None
    projbbox: Union[None, list[float]] = None
    projgeometry: Union["Polygon", None] = None
    projtransform: Union[None, list[float]] = None
    satvufilter: Union[None, SatvuFilter] = None
    satvugeometric_calibration: Union[None, bool] = None
    satvuradiometric_calibration: Union[None, bool] = None
    satvuatmospheric_model: Union[None, bool] = None
    satvuatmospheric_model_transmission: Union[None, float] = None
    satvuatmospheric_model_upwelling: Union[None, float] = None
    satvuatmospheric_model_downwelling: Union[None, float] = None
    satvusensitivity: Union[None, float] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "datetime",
            "created",
            "created_at",
            "gsd",
            "platform",
            "processing:software",
            "proj:epsg",
            "proj:shape",
            "view:azimuth",
            "view:off_nadir",
            "view:sun_azimuth",
            "view:sun_elevation",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "datetime": object,
            "created": object,
            "created_at": object,
            "gsd": float,
            "platform": str,
            "processing:software": object,
            "proj:epsg": int,
            "proj:shape": object,
            "view:azimuth": float,
            "view:off_nadir": float,
            "view:sun_azimuth": float,
            "view:sun_elevation": float,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "eo:cloud_cover": object,
            "proj:bbox": object,
            "proj:geometry": object,
            "proj:transform": object,
            "satvu:filter": object,
            "satvu:geometric_calibration": object,
            "satvu:radiometric_calibration": object,
            "satvu:atmospheric_model": object,
            "satvu:atmospheric_model_transmission": object,
            "satvu:atmospheric_model_upwelling": object,
            "satvu:atmospheric_model_downwelling": object,
            "satvu:sensitivity": object,
        }
