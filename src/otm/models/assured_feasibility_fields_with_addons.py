from dataclasses import dataclass
from typing import Literal, Union


@dataclass
class AssuredFeasibilityFieldsWithAddons:
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
        addonwithhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be withheld
            from the public catalog. Withhold options are specific to the contract. If not specified, the option will be set
            to the default specified in the relevant contract.
    """

    product: Literal["assured"]
    datetime_: str
    addonwithhold: Union[None, str] = None

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
        return {
            "addon:withhold": object,
        }
