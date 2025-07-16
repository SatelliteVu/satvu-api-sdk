from pydantic import BaseModel, Field


class UserAcceptanceTermsInput(BaseModel):
    """
    Attributes:
        accepted (bool): Terms and Conditions have been accepted
        token (str): User access token
    """

    accepted: bool = Field(..., description="Terms and Conditions have been accepted")
    token: str = Field(..., description="User access token")
