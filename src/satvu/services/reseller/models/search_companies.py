# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.kyc_status import KYCStatus

if TYPE_CHECKING:
    from ..models.company_search import CompanySearch


class SearchCompanies(pydantic.BaseModel):
    """
    Attributes:
        limit (Union[None, int]): The number of results to return per page. Default: 100.
        token (None | str): The pagination token.
        search (Union['CompanySearch', list[CompanySearch], None]): Search criteria.
        kyc_status (Union['KYCStatus', list['KYCStatus'], None]): The KYC status of the company.
    """

    limit: Union[None, int] = pydantic.Field(
        default=100,
        description="""The number of results to return per page.""",
        alias="limit",
    )
    token: None | str = pydantic.Field(
        default=None, description="""The pagination token.""", alias="token"
    )
    search: Union[CompanySearch, list[CompanySearch], None] = pydantic.Field(
        default=None, description="""Search criteria.""", alias="search"
    )
    kyc_status: Union[KYCStatus, list[KYCStatus], None] = pydantic.Field(
        default=None,
        description="""The KYC status of the company.""",
        alias="kyc_status",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
