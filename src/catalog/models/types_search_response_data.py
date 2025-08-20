from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.feature import Feature
from ..models.link import Link


class TypesSearchResponseData(BaseModel):
    """
    Attributes:
        features (list[Feature]):
        links (list[Link]): A list of references to other documents.
        number_matched (int): Number of features matching the request filter.
        number_returned (int): Number of features in current page.
        type_ (str): FeatureCollection. Example: FeatureCollection.
        next_token (Union[None, str]):
        prev_token (Union[None, str]):
    """

    features: list[Feature] = Field(..., description=None, alias="features")
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
    next_token: Union[None, str] = Field(None, description=None, alias="NextToken")
    prev_token: Union[None, str] = Field(None, description=None, alias="PrevToken")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
