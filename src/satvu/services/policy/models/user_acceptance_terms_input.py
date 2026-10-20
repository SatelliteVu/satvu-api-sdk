# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class UserAcceptanceTermsInput(pydantic.BaseModel):
    """
    Attributes:
        accepted (bool): Terms and Conditions have been accepted
        token (str): User access token
    """

    accepted: bool = pydantic.Field(
        ..., description="""Terms and Conditions have been accepted""", alias="accepted"
    )
    token: str = pydantic.Field(..., description="""User access token""", alias="token")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
