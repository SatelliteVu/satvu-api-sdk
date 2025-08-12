from typing import Union

from pydantic import BaseModel, Field

from ..models.feature_collection_order import FeatureCollectionOrder
from ..models.link import Link
from ..models.reseller_feature_collection_order import ResellerFeatureCollectionOrder


class OrderPage(BaseModel):
    """Response payload for querying orders

    Attributes:
        orders (list[Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]]): A list of existing orders owned by
            the user.
        links (list['Link']): A list of links to next and/or previous pages of the query.
    """

    orders: list[Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]] = Field(
        ..., description="A list of existing orders owned by the user."
    )
    links: list["Link"] = Field(
        ..., description="A list of links to next and/or previous pages of the query."
    )
