from pydantic import BaseModel


class RouterHttpError(BaseModel):
    """
    Attributes:
        id (str): A unique identifier for the type of error
        message (str): An error message describing what went wrong
    """

    id: str
    message: str
