from pydantic import BaseModel


class ErrorResponse(BaseModel):
    """
    Attributes:
        detail (str):
    """

    detail: str
