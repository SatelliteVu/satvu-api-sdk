from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    pass


class BboxLiteral(BaseModel):
    """
    Attributes:
        bbox (Any):
    """

    bbox: Any = Field(..., description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
