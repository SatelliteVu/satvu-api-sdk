import datetime

from pydantic import BaseModel

from ..models.geojson_polygon import GeojsonPolygon


class StacPropertiesV4(BaseModel):
    """
    Attributes:
        datetime (datetime.datetime): Acquisition datetime
        eo_cloud_cover (float): Estimate of cloud cover
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str): Platform name. E.g. Hotsat-1
        proj_epsg (int): EPSG code. Defines the geographic coordinate system
        proj_geometry (GeojsonPolygon):
        proj_shape (list[int]): Number of pixels in Y and X directions for the default grid
        proj_transform (list[float]): The affine transformation coefficients for the default grid
        view_azimuth (float): Viewing azimuth angle. The angle between the scene centre and true north. Measured
            clockwise from north in degrees.
        view_off_nadir (float): The angle between satellite nadir and the scene center. Measured in degrees.
        view_sun_azimuth (float): Sun azimuth angle. The angle between truth north and the sun at the scene centre.
            Measured clockwise in degrees.
        view_sun_elevation (float): Sun elevation angle. The angle from the tangent of the scene center to the sun
    """

    datetime: datetime.datetime
    eo_cloud_cover: float
    gsd: float
    platform: str
    proj_epsg: int
    proj_geometry: "GeojsonPolygon"
    proj_shape: list[int]
    proj_transform: list[float]
    view_azimuth: float
    view_off_nadir: float
    view_sun_azimuth: float
    view_sun_elevation: float

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "datetime",
            "eo:cloud_cover",
            "gsd",
            "platform",
            "proj:epsg",
            "proj:geometry",
            "proj:shape",
            "proj:transform",
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
            "eo:cloud_cover": float,
            "gsd": float,
            "platform": str,
            "proj:epsg": int,
            "proj:geometry": object,
            "proj:shape": object,
            "proj:transform": object,
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
        return {}
