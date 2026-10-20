# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class TermsUserTermsAccepted(pydantic.BaseModel):
    """
    Attributes:
        accepted (Union[None, bool]):
        user_id (Union[None, str]):
    """

    accepted: Union[None, bool] = pydantic.Field(
        default=None, description=None, alias="accepted"
    )
    user_id: Union[None, str] = pydantic.Field(
        default=None, description=None, alias="user_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
