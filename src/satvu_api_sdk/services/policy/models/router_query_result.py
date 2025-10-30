from __future__ import annotations

from typing import Any, Union

from pydantic import BaseModel, ConfigDict, Field


class RouterQueryResult(BaseModel):
    """
    Attributes:
        message (Union[None, str]):
        result (Union[None, Any]): Value of any type, including null
    """

    message: Union[None, str] = Field(None, description=None, alias="message")
    result: Union[None, Any] = Field(
        None, description="Value of any type, including null", alias="result"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
