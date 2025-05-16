import datetime
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from ..models.geojson_polygon import GeojsonPolygon


class StacPropertiesV4(TypedDict):
    """
    Attributes:
        datetime_ (datetime.datetime): Acquisition datetime
        eocloud_cover (float): Estimate of cloud cover
        gsd (float): Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the
            ground
        platform (str): Platform name. E.g. Hotsat-1
        projepsg (int): EPSG code. Defines the geographic coordinate system
        projgeometry (GeojsonPolygon):
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
    eocloud_cover: float
    gsd: float
    platform: str
    projepsg: int
    projgeometry: "GeojsonPolygon"
    projshape: list[int]
    projtransform: list[float]
    viewazimuth: float
    viewoff_nadir: float
    viewsun_azimuth: float
    viewsun_elevation: float
