from typing import Literal, Union
from uuid import UUID

from pydantic import BaseModel

from ..models.point import Point
from ..models.price import Price
from ..models.search_standard_order_properties import SearchStandardOrderProperties


class SearchResponseFeatureStandardOrderRequest(BaseModel):
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Union[None, Point]):
        properties (Union[None, SearchStandardOrderProperties]):
        id (UUID): ID of an item associated with the search parameters.
        contract_id (UUID): Contract ID associated with the search.
        collection (str): Name of collection associated with the search result item.
        price (Price):
        bbox (Union[None, list[float]]):
    """

    type: Literal["Feature"]
    geometry: Union[None, Point]
    properties: Union[None, SearchStandardOrderProperties]
    id: UUID
    contract_id: UUID
    collection: str
    price: "Price"
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
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "bbox": object,
        }
