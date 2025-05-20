import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING

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
        eocloud_cover (float): Estimate of cloud cover
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str): Platform name. E.g. Hotsat-1
        processingsoftware (StacPropertiesV5ProcessingSoftwareNameVersion):
        projbbox (list[float]):
        projepsg (int): EPSG code. Defines the geographic coordinate system
        projgeometry (Polygon):
        projshape (list[int]): Number of pixels in Y and X directions for the default grid
        projtransform (list[float]): The affine transformation coefficients for the default grid
        viewazimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees.
        viewoff_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees.
        viewsun_azimuth (float): Sun azimuth angle. The angle between truth north and the sun at the scene centre.
            Measured clockwise in degrees.
        viewsun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun
    """

    datetime_: datetime.datetime
    created: datetime.datetime
    created_at: datetime.datetime
    eocloud_cover: float
    gsd: float
    platform: str
    processingsoftware: "StacPropertiesV5ProcessingSoftwareNameVersion"
    projbbox: list[float]
    projepsg: int
    projgeometry: "Polygon"
    projshape: list[int]
    projtransform: list[float]
    viewazimuth: float
    viewoff_nadir: float
    viewsun_azimuth: float
    viewsun_elevation: float

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "datetime",
            "created",
            "created_at",
            "eo:cloud_cover",
            "gsd",
            "platform",
            "processing:software",
            "proj:bbox",
            "proj:epsg",
            "proj:geometry",
            "proj:shape",
            "proj:transform",
            "view:azimuth",
            "view:off_nadir",
            "view:sun_azimuth",
            "view:sun_elevation",
        }
