from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.response_context import ResponseContext
    from ..models.stored_feasibility_request import StoredFeasibilityRequest


class StoredFeasibilityFeatureCollection(BaseModel):
    """Payload for list stored feasibility requests response.

    Attributes:
        type_ (Literal['FeatureCollection']):
        features (list[StoredFeasibilityRequest]): List of stored feasibility requests.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Context about the response.
        bbox (list[float] | None):
    """

    type_: Literal["FeatureCollection"] = Field(
        "FeatureCollection", description=None, alias="type"
    )
    features: list[StoredFeasibilityRequest] = Field(
        ..., description="List of stored feasibility requests.", alias="features"
    )
    links: list[Link] = Field(
        ..., description="Links to previous and/or next page.", alias="links"
    )
    context: "ResponseContext" = Field(
        ..., description="Context about the response.", alias="context"
    )
    bbox: list[float] | None = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
