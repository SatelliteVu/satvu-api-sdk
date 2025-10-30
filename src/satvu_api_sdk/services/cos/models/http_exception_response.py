from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class HttpExceptionResponse(BaseModel):
    """
    Attributes:
        detail (str):
    """

    detail: str = Field(..., description=None, alias="detail")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
