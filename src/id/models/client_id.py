from pydantic import BaseModel, Field


class ClientID(BaseModel):
    """
    Attributes:
        client_id (str):
    """

    client_id: str = Field(..., description=None)
