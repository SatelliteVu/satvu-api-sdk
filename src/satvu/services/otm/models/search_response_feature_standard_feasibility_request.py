# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

import pydantic

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.point import Point
    from ..models.standard_stored_feasibility_request_properties import (
        StandardStoredFeasibilityRequestProperties,
    )


class SearchResponseFeatureStandardFeasibilityRequest(pydantic.BaseModel):
    """
    Attributes:
        type_ (Literal['Feature']):
        geometry (Union['Point', None]):
        properties (Union['StandardStoredFeasibilityRequestProperties', None]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        links (Union[None, list[Link]]): A list of links to the STAC item that fulfilled the order, if applicable.
        feature_type (Literal['feasibility-request-standard']):  Default: 'feasibility-request-standard'.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Union[Point, None] = pydantic.Field(
        ..., description=None, alias="geometry"
    )
    properties: Union[StandardStoredFeasibilityRequestProperties, None] = (
        pydantic.Field(..., description=None, alias="properties")
    )
    id: UUID = pydantic.Field(
        ...,
        description="""ID of an item associated with the search parameters.""",
        alias="id",
    )
    contract_id: UUID = pydantic.Field(
        ...,
        description="""Contract ID associated with the search.""",
        alias="contract_id",
    )
    collection: str = pydantic.Field(
        ...,
        description="""Name of collection associated with the search result item.""",
        alias="collection",
    )
    links: Union[None, list[Link]] = pydantic.Field(
        default=None,
        description="""A list of links to the STAC item that fulfilled the order, if applicable.""",
        alias="links",
    )
    feature_type: Literal["feasibility-request-standard"] = pydantic.Field(
        default="feasibility-request-standard", description=None, alias="feature_type"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
