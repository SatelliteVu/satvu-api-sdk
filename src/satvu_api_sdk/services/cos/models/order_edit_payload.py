from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class OrderEditPayload(BaseModel):
    """Request payload for editing an order.

    Attributes:
        name (None | str): The optional name of the order
    """

    name: None | str = Field(
        None, description="The optional name of the order", alias="name"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
