# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Annotated, Literal, Union
from uuid import UUID

import pydantic

from satvu.shared.discriminators import const_tag

if TYPE_CHECKING:
    from ..models.assured_stored_feasibility_request_properties import (
        AssuredStoredFeasibilityRequestProperties,
    )
    from ..models.link import Link
    from ..models.point import Point
    from ..models.standard_stored_feasibility_request_properties import (
        StandardStoredFeasibilityRequestProperties,
    )


class StoredFeasibilityRequest(pydantic.BaseModel):
    """Object representing a stored feasibility request.

    Attributes:
        type_ (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['AssuredStoredFeasibilityRequestProperties', 'StandardStoredFeasibilityRequestProperties']): A
            map of additional metadata about the requested image.
        id (UUID): Feasibility Request ID.
        links (list[Link]): A list of related links for the feasibility request.
        contract_id (UUID): Contract ID.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    geometry: Point = pydantic.Field(
        ..., description="""Point Model""", alias="geometry"
    )
    properties: Annotated[
        Union[
            Annotated[
                AssuredStoredFeasibilityRequestProperties, pydantic.Tag("assured")
            ],
            Annotated[
                StandardStoredFeasibilityRequestProperties, pydantic.Tag("standard")
            ],
        ],
        pydantic.Discriminator(const_tag("product", default="standard")),
    ] = pydantic.Field(
        ...,
        description="""A map of additional metadata about the requested image.""",
        alias="properties",
    )
    id: UUID = pydantic.Field(
        ..., description="""Feasibility Request ID.""", alias="id"
    )
    links: list[Link] = pydantic.Field(
        ...,
        description="""A list of related links for the feasibility request.""",
        alias="links",
    )
    contract_id: UUID = pydantic.Field(
        ..., description="""Contract ID.""", alias="contract_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
