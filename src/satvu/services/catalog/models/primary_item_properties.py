# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string import GeoJSONLineString
    from ..models.geo_json_multi_line_string import GeoJSONMultiLineString
    from ..models.geo_json_multi_point import GeoJSONMultiPoint
    from ..models.geo_json_multi_polygon import GeoJSONMultiPolygon
    from ..models.geo_json_point import GeoJSONPoint
    from ..models.geo_json_polygon import GeoJSONPolygon


class PrimaryItemProperties(BaseModel):
    """
    Attributes:
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
        satvu_radiometric_calibration (Union[None, bool]):
    """

    processing_software: dict | None = Field(
        default=None, description=None, alias="processing:software"
    )
    proj_bbox: list[float] | None = Field(
        default=None, description=None, alias="proj:bbox"
    )
    proj_epsg: float | None = Field(default=None, description=None, alias="proj:epsg")
    proj_geometry: Union[
        GeoJSONGeometryCollection,
        GeoJSONLineString,
        GeoJSONMultiLineString,
        GeoJSONMultiPoint,
        GeoJSONMultiPolygon,
        GeoJSONPoint,
        GeoJSONPolygon,
        None,
    ] = Field(default=None, description=None, alias="proj:geometry")
    proj_shape: list[float] | None = Field(
        default=None, description=None, alias="proj:shape"
    )
    proj_transform: list[float] | None = Field(
        default=None, description=None, alias="proj:transform"
    )
    satvu_atmospheric_model: Union[None, bool] = Field(
        default=None, description=None, alias="satvu:atmospheric_model"
    )
    satvu_atmospheric_model_downwelling: float | None = Field(
        default=None, description=None, alias="satvu:atmospheric_model_downwelling"
    )
    satvu_atmospheric_model_transmission: float | None = Field(
        default=None, description=None, alias="satvu:atmospheric_model_transmission"
    )
    satvu_atmospheric_model_upwelling: float | None = Field(
        default=None, description=None, alias="satvu:atmospheric_model_upwelling"
    )
    satvu_radiometric_calibration: Union[None, bool] = Field(
        default=None, description=None, alias="satvu:radiometric_calibration"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
