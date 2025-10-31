from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class OrderName(BaseModel):
    """
    Attributes:
        name (None | str): The name of the order.
    """

    name: None | str = Field(None, description="The name of the order.", alias="name")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
