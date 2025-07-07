from pydantic import BaseModel

from ..models.contracts_contract_with_products import ContractsContractWithProducts


class RouterActiveContractsResponse(BaseModel):
    """
    Attributes:
        result (list['ContractsContractWithProducts']): Result of the active contracts query
        terms_accepted (bool): User has accepted terms of service
    """

    result: list["ContractsContractWithProducts"]
    terms_accepted: bool
