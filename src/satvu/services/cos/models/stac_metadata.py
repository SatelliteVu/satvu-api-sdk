# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.legacy_link import LegacyLink
    from ..models.stac_link import StacLink
    from ..models.stac_properties_acquisition import StacPropertiesAcquisition
    from ..models.stac_properties_v4 import StacPropertiesV4
    from ..models.stac_properties_v7 import StacPropertiesV7


class StacMetadata(BaseModel):
    """Compact STAC metadata for display in order listings, containing only essential information and thumbnails.

    Attributes:
        id (str): The unique image identifier.
        collection (str): Collection ID.
        assets (dict): A dictionary of asset objects that can be downloaded, each with a unique key.
        bbox (list[float | int]): The bounding box of the asset represented by this item.
        properties (Union['StacPropertiesAcquisition', 'StacPropertiesV4', 'StacPropertiesV7', dict]): A dictionary of
            additional metadata for the item.
        links (Union[None, list[Union['LegacyLink', 'StacLink']]]): Links to related resources such as derived products
            and source imagery.
    """

    id: str = Field(..., description="""The unique image identifier.""", alias="id")
    collection: str = Field(..., description="""Collection ID.""", alias="collection")
    assets: dict = Field(
        ...,
        description="""A dictionary of asset objects that can be downloaded, each with a unique key.""",
        alias="assets",
    )
    bbox: list[float | int] = Field(
        ...,
        description="""The bounding box of the asset represented by this item.""",
        alias="bbox",
    )
    properties: Union[
        StacPropertiesAcquisition, StacPropertiesV4, StacPropertiesV7, dict
    ] = Field(
        ...,
        description="""A dictionary of additional metadata for the item.""",
        alias="properties",
    )
    links: Union[None, list[Union[LegacyLink, StacLink]]] = Field(
        default=None,
        description="""Links to related resources such as derived products and source imagery.""",
        alias="links",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
