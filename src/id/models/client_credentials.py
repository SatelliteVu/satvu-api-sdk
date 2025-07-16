from pydantic import BaseModel, Field


class ClientCredentials(BaseModel):
    """
    Attributes:
        client_id (str):
        client_secret (str):
    """

    client_id: str = Field(..., description=None)
    client_secret: str = Field(..., description=None)
