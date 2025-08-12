from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ResellerSubmissionOrderPayload(BaseModel):
    """Order payload for resellers

    Attributes:
        reseller_end_user_id (UUID): The ID of the end user for whom the order is placed for.
        item_id (Union[list[str], str]): The item ID.
        name (Union[None, str]): The optional name of the order
        licence_level (Union[None, str]):
    """

    reseller_end_user_id: UUID = Field(
        ...,
        description="The ID of the end user for whom the order is placed for.",
        alias="reseller_end_user_id",
    )
    item_id: Union[list[str], str] = Field(
        ..., description="The item ID.", alias="item_id"
    )
    name: Union[None, str] = Field(
        None, description="The optional name of the order", alias="name"
    )
    licence_level: Union[None, str] = Field(
        None, description=None, alias="licence_level"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
