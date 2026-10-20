# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class ClientID(pydantic.BaseModel):
    """
    Attributes:
        client_id (str):
    """

    client_id: str = pydantic.Field(..., description=None, alias="client_id")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
