from pydantic import BaseModel, ConfigDict, Field


class RouterHttpError(BaseModel):
    """
    Attributes:
        id (str): A unique identifier for the type of error
        message (str): An error message describing what went wrong
    """

    id: str = Field(
        ..., description="A unique identifier for the type of error", alias="id"
    )
    message: str = Field(
        ..., description="An error message describing what went wrong", alias="message"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
