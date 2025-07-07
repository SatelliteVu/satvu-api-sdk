from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..models.link import Link
    from ..models.point import Point
    from ..models.price_1 import Price1
    from ..models.stored_assured_order_request_properties import (
        StoredAssuredOrderRequestProperties,
    )
    from ..models.stored_standard_order_request_properties import (
        StoredStandardOrderRequestProperties,
    )


@dataclass
class ResellerStoredOrderRequest:
    """
    Attributes:
        type (Literal['Feature']):
        geometry (Point): Point Model
        properties (Union['StoredAssuredOrderRequestProperties', 'StoredStandardOrderRequestProperties']): A dictionary
            of additional metadata about the requested image.
        id (UUID): Order ID
        links (list['Link']): A list of related links for the order.
        contract_id (UUID): Contract ID.
        price (Price1):
        reseller_end_user_id (UUID):
    """

    type: Literal["Feature"]
    geometry: "Point"
    properties: Union[
        "StoredAssuredOrderRequestProperties", "StoredStandardOrderRequestProperties"
    ]
    id: UUID
    links: list["Link"]
    contract_id: UUID
    price: "Price1"
    reseller_end_user_id: UUID

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
            "links",
            "contract_id",
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
            "links": object,
            "contract_id": UUID,
            "price": object,
            "reseller_end_user_id": UUID,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
