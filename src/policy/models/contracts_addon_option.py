from dataclasses import dataclass
from typing import Union


@dataclass
class ContractsAddonOption:
    """
    Attributes:
        label (str): Label assigned to addon option Example: Withhold - 3 days.
        uplift (int): Coefficient that base price is multiplied by in percent Example: 10.
        value (str): Value of the addon option Example: 3d.
        default (Union[None, bool]):
    """

    label: str
    uplift: int
    value: str
    default: Union[None, bool] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "label",
            "uplift",
            "value",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "label": str,
            "uplift": int,
            "value": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "default": bool,
        }
