from pydantic import BaseModel, Field


class RouterHttpError(BaseModel):
    """
    Attributes:
        id (str): A unique identifier for the type of error
        message (str): An error message describing what went wrong
    """

    id: str = Field(..., description="A unique identifier for the type of error")
    message: str = Field(..., description="An error message describing what went wrong")
