# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.contracts_addon import ContractsAddon
    from ..models.contracts_geometry import ContractsGeometry
    from ..models.contracts_product_summary import ContractsProductSummary


class ContractsContractWithProducts(pydantic.BaseModel):
    """
    Attributes:
        active (bool): Whether the contract is active Example: True.
        addons (list[ContractsAddon]): Addons associated with this contract
        allowed_geographical_area (ContractsGeometry): Allowed geographical area of the contract
        contract_id (str): Contract ID Example: bc5bb4dc-a007-4419-8093-184408cdb2d7.
        end_date (datetime.date | None): Contract end date
        geographical_summary (str): Descriptive summary of a contract's geographical area Example: Northern Europe.
        name (str): Contract name Example: my-contract.
        products (list[ContractsProductSummary]): List of products the contract has access to
        reseller (bool): Whether the contract is marked for reselling Example: True.
        start_date (datetime.date | None): Contract start date
        credit_limit (Union[None, int]):
        satellite_access (Union[None, list[str]]): Satellite access for the contract
    """

    active: bool = pydantic.Field(
        ..., description="""Whether the contract is active""", alias="active"
    )
    addons: list[ContractsAddon] = pydantic.Field(
        ..., description="""Addons associated with this contract""", alias="addons"
    )
    allowed_geographical_area: ContractsGeometry = pydantic.Field(
        ...,
        description="""Allowed geographical area of the contract""",
        alias="allowed_geographical_area",
    )
    contract_id: str = pydantic.Field(
        ..., description="""Contract ID""", alias="contract_id"
    )
    end_date: datetime.date | None = pydantic.Field(
        ..., description="""Contract end date""", alias="end_date"
    )
    geographical_summary: str = pydantic.Field(
        ...,
        description="""Descriptive summary of a contract's geographical area""",
        alias="geographical_summary",
    )
    name: str = pydantic.Field(..., description="""Contract name""", alias="name")
    products: list[ContractsProductSummary] = pydantic.Field(
        ...,
        description="""List of products the contract has access to""",
        alias="products",
    )
    reseller: bool = pydantic.Field(
        ...,
        description="""Whether the contract is marked for reselling""",
        alias="reseller",
    )
    start_date: datetime.date | None = pydantic.Field(
        ..., description="""Contract start date""", alias="start_date"
    )
    credit_limit: Union[None, int] = pydantic.Field(
        default=None, description=None, alias="credit_limit"
    )
    satellite_access: Union[None, list[str]] = pydantic.Field(
        default=None,
        description="""Satellite access for the contract""",
        alias="satellite_access",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
