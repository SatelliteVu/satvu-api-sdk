from pydantic import BaseModel, ConfigDict, Field


class PostActiveContractsInput(BaseModel):
    """
    Attributes:
        token (str): User access token
    """

    token: str = Field(..., description="User access token", alias="token")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
