from pydantic import BaseModel, Field


class HttpExceptionResponse(BaseModel):
    """
    Attributes:
        detail (str):
    """

    detail: str = Field(..., description=None)
