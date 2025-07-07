from typing import Literal

from pydantic import BaseModel


class AssuredFeasibilityFields(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the request.
    """

    product: Literal["assured"]
    datetime: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "product",
            "datetime",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "product": object,
            "datetime": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
