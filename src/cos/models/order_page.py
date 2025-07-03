from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.feature_collection_order import FeatureCollectionOrder
    from ..models.link import Link
    from ..models.reseller_feature_collection_order import (
        ResellerFeatureCollectionOrder,
    )


@dataclass
class OrderPage:
    """
    Attributes:
        orders (list[Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']]): A list of existing orders
            owned by the user.
        links (list['Link']): A list of links to next and/or previous pages of the query.
    """

    orders: list[Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]]
    links: list["Link"]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "orders",
            "links",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "orders": object,
            "links": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
