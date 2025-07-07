from typing import Literal, Union

from pydantic import BaseModel


class AssuredOrderRequestProperties(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        signature (str): Signature token.
        addon_withhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
    """

    product: Literal["assured"]
    signature: str
    addon_withhold: Union[None, str] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "product",
            "signature",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "product": object,
            "signature": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "addon:withhold": object,
        }
