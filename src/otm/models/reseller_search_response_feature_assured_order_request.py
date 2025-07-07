from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..models.point import Point
    from ..models.price import Price
    from ..models.search_assured_order_properties import SearchAssuredOrderProperties


@dataclass
class ResellerSearchResponseFeatureAssuredOrderRequest:
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Union['Point', None]):
        properties (Union['SearchAssuredOrderProperties', None]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        reseller_end_user_id (UUID):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"]
    geometry: Union["Point", None]
    properties: Union["SearchAssuredOrderProperties", None]
    id: UUID
    contract_id: UUID
    collection: str
    price: "Price"
    reseller_end_user_id: UUID
    bbox: Union[None, list[float]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "type",
            "geometry",
            "properties",
            "id",
            "contract_id",
            "collection",
            "price",
            "reseller_end_user_id",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "type": object,
            "geometry": object,
            "properties": object,
            "id": UUID,
            "contract_id": UUID,
            "collection": str,
            "price": object,
            "reseller_end_user_id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
