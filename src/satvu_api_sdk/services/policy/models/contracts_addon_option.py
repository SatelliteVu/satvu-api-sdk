from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class ContractsAddonOption(BaseModel):
    """
    Attributes:
        label (str): Label assigned to addon option. Example: Withhold - 3 days.
        uplift (int): Coefficient that base price is multiplied by in percent. Example: 10.
        value (str): Value of the addon option. Example: 3d.
        default (Union[None, bool]):
        eula_type (Union[None, str]): The EULA type. Only provided for 'Licence' addons. Example: Standard.
    """

    label: str = Field(
        ..., description="Label assigned to addon option.", alias="label"
    )
    uplift: int = Field(
        ...,
        description="Coefficient that base price is multiplied by in percent.",
        alias="uplift",
    )
    value: str = Field(..., description="Value of the addon option.", alias="value")
    default: Union[None, bool] = Field(None, description=None, alias="default")
    eula_type: Union[None, str] = Field(
        None,
        description="The EULA type. Only provided for 'Licence' addons.",
        alias="eula_type",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
