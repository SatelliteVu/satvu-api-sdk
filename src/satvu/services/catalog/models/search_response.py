# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.feature import Feature
    from ..models.link import Link


class SearchResponse(pydantic.BaseModel):
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

    features: list[Feature] = pydantic.Field(
        ..., description="""A list of Feature objects.""", alias="features"
    )
    links: list[Link] = pydantic.Field(
        ..., description="""A list of references to other documents.""", alias="links"
    )
    number_matched: int = pydantic.Field(
        ...,
        description="""Number of features matching the request filter.""",
        alias="numberMatched",
    )
    number_returned: int = pydantic.Field(
        ...,
        description="""Number of features in current page.""",
        alias="numberReturned",
    )
    type_: str = pydantic.Field(..., description="""FeatureCollection.""", alias="type")
    next_token: Union[None, str] = pydantic.Field(
        default=None,
        description="""A token that can be used to retrieve the next page of results.""",
        alias="next_token",
    )
    prev_token: Union[None, str] = pydantic.Field(
        default=None,
        description="""A token that can be used to retrieve the previous page of results.""",
        alias="prev_token",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
