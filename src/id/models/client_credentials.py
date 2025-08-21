from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ClientCredentials(BaseModel):
    """
    Attributes:
        client_id (str):
        client_secret (str):
    """

    client_id: str = Field(..., description=None, alias="client_id")
    client_secret: str = Field(..., description=None, alias="client_secret")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
