from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class Error(BaseModel):
    """
    Attributes:
        id (str): A unique identifier for the type of error.
        message (str): An error message describing what went wrong.
        field (Union[None, str]): The field that failed validation, for 'ValidationError' errors only.
    """

    id: str = Field(
        ..., description="A unique identifier for the type of error.", alias="id"
    )
    message: str = Field(
        ..., description="An error message describing what went wrong.", alias="message"
    )
    field: Union[None, str] = Field(
        None,
        description="The field that failed validation, for 'ValidationError' errors only.",
        alias="field",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
