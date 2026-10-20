# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon


class PrimaryItemProperties(pydantic.BaseModel):
    """
    Attributes:
        created (datetime.datetime):
        updated (datetime.datetime):
        datetime_ (Union[None, datetime.datetime]):
        eo_cloud_cover (float | None):
        gsd (Union[None, float]):
        platform (Union[None, str]):
        processing_software (dict | None):
        proj_bbox (list[float] | None):
        proj_epsg (float | None):
        proj_geometry (Union['GeoJSONGeometryCollection', 'GeoJSONLineString', 'GeoJSONMultiLineString',
            'GeoJSONMultiPoint', 'GeoJSONMultiPolygon', 'GeoJSONPoint', 'GeoJSONPolygon', None]):
        proj_shape (list[float] | None):
        proj_transform (list[float] | None):
        satvu_atmospheric_model (Union[None, bool]):
        satvu_atmospheric_model_downwelling (float | None):
        satvu_atmospheric_model_transmission (float | None):
        satvu_atmospheric_model_upwelling (float | None):
        satvu_filter (Union[None, str]):
        satvu_geometric_calibration (Union[None, bool]):
        satvu_radiometric_calibration (Union[None, bool]):
        view_azimuth (Union[None, float]):
        view_off_nadir (Union[None, float]):
        view_sun_azimuth (Union[None, float]):
        view_sun_elevation (Union[None, float]):
    """

    created: datetime.datetime = pydantic.Field(..., description=None, alias="created")
    updated: datetime.datetime = pydantic.Field(..., description=None, alias="updated")
    datetime_: Union[None, datetime.datetime] = pydantic.Field(
        default=None, description=None, alias="datetime"
    )
    eo_cloud_cover: float | None = pydantic.Field(
        default=None, description=None, alias="eo:cloud_cover"
    )
    gsd: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="gsd"
    )
    platform: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="platform"
    )
    processing_software: dict | None = pydantic.Field(
        default=None, description=None, alias="processing:software"
    )
    proj_bbox: list[float] | None = pydantic.Field(
        default=None, description=None, alias="proj:bbox"
    )
    proj_epsg: float | None = pydantic.Field(
        default=None, description=None, alias="proj:epsg"
    )
    proj_geometry: Union[
        GeoJSONGeometryCollection,
        GeoJSONLineString,
        GeoJSONMultiLineString,
        GeoJSONMultiPoint,
        GeoJSONMultiPolygon,
        GeoJSONPoint,
        GeoJSONPolygon,
        None,
    ] = pydantic.Field(default=None, description=None, alias="proj:geometry")
    proj_shape: list[float] | None = pydantic.Field(
        default=None, description=None, alias="proj:shape"
    )
    proj_transform: list[float] | None = pydantic.Field(
        default=None, description=None, alias="proj:transform"
    )
    satvu_atmospheric_model: Union[None, bool] = pydantic.Field(
        default=None, description=None, alias="satvu:atmospheric_model"
    )
    satvu_atmospheric_model_downwelling: float | None = pydantic.Field(
        default=None, description=None, alias="satvu:atmospheric_model_downwelling"
    )
    satvu_atmospheric_model_transmission: float | None = pydantic.Field(
        default=None, description=None, alias="satvu:atmospheric_model_transmission"
    )
    satvu_atmospheric_model_upwelling: float | None = pydantic.Field(
        default=None, description=None, alias="satvu:atmospheric_model_upwelling"
    )
    satvu_filter: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="satvu:filter"
    )
    satvu_geometric_calibration: Union[None, bool] = pydantic.Field(
        default=None, description=None, alias="satvu:geometric_calibration"
    )
    satvu_radiometric_calibration: Union[None, bool] = pydantic.Field(
        default=None, description=None, alias="satvu:radiometric_calibration"
    )
    view_azimuth: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:azimuth"
    )
    view_off_nadir: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:off_nadir"
    )
    view_sun_azimuth: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:sun_azimuth"
    )
    view_sun_elevation: Union[None, float] = pydantic.Field(
        default=None, description=None, alias="view:sun_elevation"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
