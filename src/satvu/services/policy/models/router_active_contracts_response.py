# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.contracts_contract_with_products import ContractsContractWithProducts


class RouterActiveContractsResponse(pydantic.BaseModel):
    """
    Attributes:
        result (list[ContractsContractWithProducts]): Result of the active contracts query
        terms_accepted (bool): User has accepted terms of service
    """

    result: list[ContractsContractWithProducts] = pydantic.Field(
        ..., description="""Result of the active contracts query""", alias="result"
    )
    terms_accepted: bool = pydantic.Field(
        ...,
        description="""User has accepted terms of service""",
        alias="terms_accepted",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
