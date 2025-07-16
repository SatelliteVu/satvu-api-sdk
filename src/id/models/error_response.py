from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    """
    Attributes:
        detail (str):
    """

    detail: str = Field(..., description=None)
