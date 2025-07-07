from pydantic import BaseModel


class ClientCredentials(BaseModel):
    """
    Attributes:
        client_id (str):
        client_secret (str):
    """

    client_id: str
    client_secret: str
