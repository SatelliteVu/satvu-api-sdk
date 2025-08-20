from pydantic import BaseModel, ConfigDict, Field

from ..models.feature import Feature
from ..models.link import Link


class TypesFeatureCollection(BaseModel):
    """
    Attributes:
        features (list[Feature]):
        links (list[Link]): A list of references to other documents.
        number_matched (int): Number of features matching the request filter.
        number_returned (int): Number of features in current page.
        type_ (str): FeatureCollection. Example: FeatureCollection.
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

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
