from pydantic import BaseModel, ConfigDict, Field


class DateInstant(BaseModel):
    """
    Attributes:
        date (str):
    """

    date: str = Field(..., description=None, alias="date")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
