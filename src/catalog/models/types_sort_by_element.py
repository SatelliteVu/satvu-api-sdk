from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class TypesSortByElement(BaseModel):
    """
    Attributes:
        direction (str): The direction to sort by, either 'asc' or 'desc'. Example: desc.
        field (str): The name of the field to sort by. Example: datetime.
    """

    direction: str = Field(
        ...,
        description="The direction to sort by, either 'asc' or 'desc'.",
        alias="direction",
    )
    field: str = Field(
        ..., description="The name of the field to sort by.", alias="field"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
