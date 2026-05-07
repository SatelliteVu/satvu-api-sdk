# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.primary_feature_collection_type import PrimaryFeatureCollectionType

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.primary_item import PrimaryItem


class PrimaryFeatureCollection(BaseModel):
    """
    Attributes:
        features (Union[None, list[PrimaryItem]]):
        links (Union[None, list[Link]]):
        number_matched (Union[None, int]):
        number_returned (Union[None, int]):
        type_ (Union[None, 'PrimaryFeatureCollectionType']):
    """

    features: Union[None, list[PrimaryItem]] = Field(
        default=None, description=None, alias="features"
    )
    links: Union[None, list[Link]] = Field(
        default=None, description=None, alias="links"
    )
    number_matched: Union[None, int] = Field(
        default=None, description=None, alias="numberMatched"
    )
    number_returned: Union[None, int] = Field(
        default=None, description=None, alias="numberReturned"
    )
    type_: Union[None, PrimaryFeatureCollectionType] = Field(
        default=None, description=None, alias="type"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
