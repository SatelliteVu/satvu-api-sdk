from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.batch_balance_response_balances import BatchBalanceResponseBalances


class BatchBalanceResponse(BaseModel):
    """
    Attributes:
        balances (BatchBalanceResponseBalances): Mapping of contract IDs to their credit balance responses
    """

    balances: "BatchBalanceResponseBalances" = Field(
        ...,
        description="Mapping of contract IDs to their credit balance responses",
        alias="balances",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
