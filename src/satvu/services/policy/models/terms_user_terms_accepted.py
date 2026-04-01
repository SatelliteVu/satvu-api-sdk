# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class TermsUserTermsAccepted(BaseModel):
    """
    Attributes:
        accepted (Union[None, bool]):
        user_id (Union[None, str]):
    """

    accepted: Union[None, bool] = Field(
        default=None, description=None, alias="accepted"
    )
    user_id: Union[None, str] = Field(default=None, description=None, alias="user_id")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
