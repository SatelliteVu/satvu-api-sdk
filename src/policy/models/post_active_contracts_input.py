from pydantic import BaseModel


class PostActiveContractsInput(BaseModel):
    """
    Attributes:
        token (str): User access token
    """

    token: str
