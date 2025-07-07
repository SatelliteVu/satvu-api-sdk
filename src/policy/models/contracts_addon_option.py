from typing import Union

from pydantic import BaseModel


class ContractsAddonOption(BaseModel):
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
