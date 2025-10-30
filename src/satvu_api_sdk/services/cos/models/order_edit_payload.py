from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class OrderEditPayload(BaseModel):
    """Request payload for editing an order.

    Attributes:
        name (Union[None, str]): The optional name of the order
    """

    name: Union[None, str] = Field(
        None, description="The optional name of the order", alias="name"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
