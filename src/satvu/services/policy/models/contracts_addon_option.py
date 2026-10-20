# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class ContractsAddonOption(pydantic.BaseModel):
    """
    Attributes:
        label (str): Label assigned to addon option. Example: Withhold - 3 days.
        uplift (int): Coefficient that base price is multiplied by in percent. Example: 10.
        value (str): Value of the addon option. Example: 3d.
        default (Union[None, bool]):
        eula_type (Union[None, str]): The EULA type. Only provided for 'Licence' addons. Example: Standard.
    """

    label: str = pydantic.Field(
        ..., description="""Label assigned to addon option.""", alias="label"
    )
    uplift: int = pydantic.Field(
        ...,
        description="""Coefficient that base price is multiplied by in percent.""",
        alias="uplift",
    )
    value: str = pydantic.Field(
        ..., description="""Value of the addon option.""", alias="value"
    )
    default: Union[None, bool] = pydantic.Field(
        default=None, description=None, alias="default"
    )
    eula_type: Union[None, str] = pydantic.Field(
        default=None,
        description="""The EULA type. Only provided for 'Licence' addons.""",
        alias="eula_type",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
