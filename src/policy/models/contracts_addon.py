from pydantic import BaseModel, Field

from ..models.contracts_addon_option import ContractsAddonOption


class ContractsAddon(BaseModel):
    """
    Attributes:
        name (str): Name of the addon option. Example: Withhold.
        options (list['ContractsAddonOption']): List of options available with this addon.
    """

    name: str = Field(..., description="Name of the addon option.")
    options: list["ContractsAddonOption"] = Field(
        ..., description="List of options available with this addon."
    )
