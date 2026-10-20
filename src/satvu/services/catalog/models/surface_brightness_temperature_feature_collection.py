# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.surface_brightness_temperature_feature_collection_type import (
    SurfaceBrightnessTemperatureFeatureCollectionType,
)

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.surface_brightness_temperature_item import (
        SurfaceBrightnessTemperatureItem,
    )


class SurfaceBrightnessTemperatureFeatureCollection(pydantic.BaseModel):
    """
    Attributes:
        features (Union[None, list[SurfaceBrightnessTemperatureItem]]):
        links (Union[None, list[Link]]):
        number_matched (Union[None, int]):
        number_returned (Union[None, int]):
        type_ (Union[None, 'SurfaceBrightnessTemperatureFeatureCollectionType']):
    """

    features: Union[None, list[SurfaceBrightnessTemperatureItem]] = pydantic.Field(
        default=None, description=None, alias="features"
    )
    links: Union[None, list[Link]] = pydantic.Field(
        default=None, description=None, alias="links"
    )
    number_matched: Union[None, int] = pydantic.Field(
        default=None, description=None, alias="numberMatched"
    )
    number_returned: Union[None, int] = pydantic.Field(
        default=None, description=None, alias="numberReturned"
    )
    type_: Union[None, SurfaceBrightnessTemperatureFeatureCollectionType] = (
        pydantic.Field(default=None, description=None, alias="type")
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
