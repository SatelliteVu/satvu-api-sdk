from pydantic import BaseModel

from ..models.order_name import OrderName


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Attributes:
        properties (OrderName):
    """

    properties: "OrderName"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "properties",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "properties": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
