from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    pass


class BatchBalanceResponseBalances(BaseModel):
    """Mapping of contract IDs to their credit balance responses"""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
