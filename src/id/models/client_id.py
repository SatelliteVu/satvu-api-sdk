from pydantic import BaseModel


class ClientID(BaseModel):
    """
    Attributes:
        client_id (str):
    """

    client_id: str
