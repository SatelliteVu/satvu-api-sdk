from pydantic import BaseModel, Field


class PostActiveContractsInput(BaseModel):
    """
    Attributes:
        token (str): User access token
    """

    token: str = Field(..., description="User access token")
