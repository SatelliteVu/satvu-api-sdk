from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.feature import Feature
    from ..models.link import Link


class SearchResponse(BaseModel):
    """
    Attributes:
        features (list[Feature]): A list of Feature objects.
        links (list[Link]): A list of references to other documents.
        number_matched (int): Number of features matching the request filter.
        number_returned (int): Number of features in current page.
        type_ (str): FeatureCollection. Example: FeatureCollection.
        next_token (Union[None, str]): A token that can be used to retrieve the next page of results.
        prev_token (Union[None, str]): A token that can be used to retrieve the previous page of results.
    """

    features: list[Feature] = Field(
        ..., description="A list of Feature objects.", alias="features"
    )
    links: list[Link] = Field(
        ..., description="A list of references to other documents.", alias="links"
    )
    number_matched: int = Field(
        ...,
        description="Number of features matching the request filter.",
        alias="numberMatched",
    )
    number_returned: int = Field(
        ..., description="Number of features in current page.", alias="numberReturned"
    )
    type_: str = Field(..., description="FeatureCollection.", alias="type")
    next_token: Union[None, str] = Field(
        None,
        description="A token that can be used to retrieve the next page of results.",
        alias="next_token",
    )
    prev_token: Union[None, str] = Field(
        None,
        description="A token that can be used to retrieve the previous page of results.",
        alias="prev_token",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
