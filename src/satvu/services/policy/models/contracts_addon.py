# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.contracts_addon_option import ContractsAddonOption


class ContractsAddon(pydantic.BaseModel):
    """
    Attributes:
        name (str): Name of the addon option. Example: Withhold.
        options (list[ContractsAddonOption]): List of options available with this addon.
    """

    name: str = pydantic.Field(
        ..., description="""Name of the addon option.""", alias="name"
    )
    options: list[ContractsAddonOption] = pydantic.Field(
        ...,
        description="""List of options available with this addon.""",
        alias="options",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
