from pydantic import BaseModel, Field

from ..models.contracts_contract_with_products import ContractsContractWithProducts


class RouterActiveContractsResponse(BaseModel):
    """
    Attributes:
        result (list['ContractsContractWithProducts']): Result of the active contracts query
        terms_accepted (bool): User has accepted terms of service
    """

    result: list["ContractsContractWithProducts"] = Field(
        ..., description="Result of the active contracts query"
    )
    terms_accepted: bool = Field(..., description="User has accepted terms of service")
