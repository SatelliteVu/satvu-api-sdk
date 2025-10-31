from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ResellerSubmissionOrderPayload(BaseModel):
    """Order payload for resellers

    Attributes:
        reseller_end_user_id (UUID): The ID of the end user for whom the order is placed for.
        item_id (list[str] | str): The item ID.
        name (None | str): The optional name of the order
        licence_level (None | str): The optional licence level for the order. Licence levels are specific to the
            contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant
            contract.
    """

    reseller_end_user_id: UUID = Field(
        ...,
        description="The ID of the end user for whom the order is placed for.",
        alias="reseller_end_user_id",
    )
    item_id: list[str] | str = Field(..., description="The item ID.", alias="item_id")
    name: None | str = Field(
        None, description="The optional name of the order", alias="name"
    )
    licence_level: None | str = Field(
        None,
        description="The optional licence level for the order. Licence levels are specific to the contract. If not specified, the option will be set to the licence with the smallest uplift in the relevant contract.",
        alias="licence_level",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
