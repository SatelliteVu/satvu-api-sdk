from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.contracts_addon_option import ContractsAddonOption


@dataclass
class ContractsAddon:
    """
    Attributes:
        name (str): Name of the addon option Example: Withhold.
        options (list['ContractsAddonOption']): List of options available with this addon
    """

    name: str
    options: list["ContractsAddonOption"]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "name",
            "options",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "name": str,
            "options": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
