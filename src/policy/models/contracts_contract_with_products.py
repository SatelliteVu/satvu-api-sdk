from pydantic import BaseModel

from ..models.civil_date import CivilDate
from ..models.contracts_addon import ContractsAddon
from ..models.contracts_geometry import ContractsGeometry
from ..models.contracts_product import ContractsProduct


class ContractsContractWithProducts(BaseModel):
    """
    Attributes:
        active (bool): Whether the contract is active Example: True.
        addons (list['ContractsAddon']): Addons associated with this contract
        allowed_geographical_area (ContractsGeometry): Allowed geographical area of the contract
        contract_id (str): Contract ID Example: bc5bb4dc-a007-4419-8093-184408cdb2d7.
        end_date (CivilDate): Contract end date
        geographical_summary (str): Descriptive summary of a contract's geographical area Example: Northern Europe.
        name (str): Contract name Example: my-contract.
        products (list['ContractsProduct']): List of products the contract has access to
        reseller (bool): Whether the contract is marked for reselling Example: True.
        start_date (CivilDate): Contract end date
    """

    active: bool
    addons: list["ContractsAddon"]
    allowed_geographical_area: "ContractsGeometry"
    contract_id: str
    end_date: "CivilDate"
    geographical_summary: str
    name: str
    products: list["ContractsProduct"]
    reseller: bool
    start_date: "CivilDate"
