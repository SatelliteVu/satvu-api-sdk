from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.contracts_contract_with_products import ContractsContractWithProducts


class RouterActiveContractsResponse(BaseModel):
    """
    Attributes:
        result (list[ContractsContractWithProducts]): Result of the active contracts query
        terms_accepted (bool): User has accepted terms of service
    """

    result: list[ContractsContractWithProducts] = Field(
        ..., description="Result of the active contracts query", alias="result"
    )
    terms_accepted: bool = Field(
        ..., description="User has accepted terms of service", alias="terms_accepted"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
