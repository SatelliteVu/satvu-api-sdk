from typing import Union

from pydantic import BaseModel, Field


class ContractsAddonOption(BaseModel):
    """
    Attributes:
        label (str): Label assigned to addon option Example: Withhold - 3 days.
        uplift (int): Coefficient that base price is multiplied by in percent Example: 10.
        value (str): Value of the addon option Example: 3d.
        default (Union[None, bool]):
    """

    label: str = Field(..., description="Label assigned to addon option")
    uplift: int = Field(
        ..., description="Coefficient that base price is multiplied by in percent"
    )
    value: str = Field(..., description="Value of the addon option")
    default: Union[None, bool] = Field(None, description=None)
