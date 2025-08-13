from pydantic import BaseModel, ConfigDict, Field

from ..models.civil_date import CivilDate
from ..models.contracts_addon import ContractsAddon
from ..models.contracts_geometry import ContractsGeometry
from ..models.contracts_product import ContractsProduct


class ContractsContractWithProducts(BaseModel):
    """
    Attributes:
        active (bool): Whether the contract is active Example: True.
        addons (list[ContractsAddon]): Addons associated with this contract
        allowed_geographical_area (ContractsGeometry): Allowed geographical area of the contract
        contract_id (str): Contract ID Example: bc5bb4dc-a007-4419-8093-184408cdb2d7.
        end_date (CivilDate): Contract end date
        geographical_summary (str): Descriptive summary of a contract's geographical area Example: Northern Europe.
        name (str): Contract name Example: my-contract.
        products (list[ContractsProduct]): List of products the contract has access to
        reseller (bool): Whether the contract is marked for reselling Example: True.
        start_date (CivilDate): Contract end date
    """

    active: bool = Field(
        ..., description="Whether the contract is active", alias="active"
    )
    addons: list[ContractsAddon] = Field(
        ..., description="Addons associated with this contract", alias="addons"
    )
    allowed_geographical_area: "ContractsGeometry" = Field(
        ...,
        description="Allowed geographical area of the contract",
        alias="allowed_geographical_area",
    )
    contract_id: str = Field(..., description="Contract ID", alias="contract_id")
    end_date: "CivilDate" = Field(
        ..., description="Contract end date", alias="end_date"
    )
    geographical_summary: str = Field(
        ...,
        description="Descriptive summary of a contract's geographical area",
        alias="geographical_summary",
    )
    name: str = Field(..., description="Contract name", alias="name")
    products: list[ContractsProduct] = Field(
        ..., description="List of products the contract has access to", alias="products"
    )
    reseller: bool = Field(
        ...,
        description="Whether the contract is marked for reselling",
        alias="reseller",
    )
    start_date: "CivilDate" = Field(
        ..., description="Contract end date", alias="start_date"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
