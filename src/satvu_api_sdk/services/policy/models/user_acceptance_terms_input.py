from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class UserAcceptanceTermsInput(BaseModel):
    """
    Attributes:
        accepted (bool): Terms and Conditions have been accepted
        token (str): User access token
    """

    accepted: bool = Field(
        ..., description="Terms and Conditions have been accepted", alias="accepted"
    )
    token: str = Field(..., description="User access token", alias="token")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
