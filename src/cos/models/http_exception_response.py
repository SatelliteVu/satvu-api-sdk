from pydantic import BaseModel


class HttpExceptionResponse(BaseModel):
    """
    Attributes:
        detail (str):
    """

    detail: str
