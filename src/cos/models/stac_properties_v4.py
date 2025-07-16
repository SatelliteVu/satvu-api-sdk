import datetime

from pydantic import BaseModel, Field

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

    datetime: datetime.datetime = Field(..., description="Acquisition datetime")
    eo_cloud_cover: float = Field(..., description="Estimate of cloud cover")
    gsd: float = Field(
        ...,
        description="Ground Sampling Distance. Distance in metres between two consecutive pixel centers measured on the ground",
    )
    platform: str = Field(..., description="Platform name. E.g. Hotsat-1")
    proj_epsg: int = Field(
        ..., description="EPSG code. Defines the geographic coordinate system"
    )
    proj_geometry: "GeojsonPolygon" = Field(..., description=None)
    proj_shape: list[int] = Field(
        ..., description="Number of pixels in Y and X directions for the default grid"
    )
    proj_transform: list[float] = Field(
        ..., description="The affine transformation coefficients for the default grid"
    )
    view_azimuth: float = Field(
        ...,
        description="Viewing azimuth angle. The angle between the scene centre and true north. Measured clockwise from north in degrees.",
    )
    view_off_nadir: float = Field(
        ...,
        description="The angle between satellite nadir and the scene center. Measured in degrees.",
    )
    view_sun_azimuth: float = Field(
        ...,
        description="Sun azimuth angle. The angle between truth north and the sun at the scene centre. Measured clockwise in degrees.",
    )
    view_sun_elevation: float = Field(
        ...,
        description="Sun elevation angle. The angle from the tangent of the scene center to the sun",
    )
