from typing import TypedDict


class ClientCredentials(TypedDict):
    """
    Attributes:
        client_id (str):
        client_secret (str):
    """

    client_id: str
    client_secret: str
