from typing import Union

from pydantic import BaseModel, Field

from ..models.company_search import CompanySearch
from ..models.kyc_status import KYCStatus


class SearchCompanies(BaseModel):
    """
    Attributes:
        limit (Union[None, int]): The number of results to return per page. Default: 100.
        token (Union[None, str]): The pagination token.
        search (Union[CompanySearch, None, list['CompanySearch']]): Search criteria.
        kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the company.
    """

    limit: Union[None, int] = Field(
        100, description="The number of results to return per page."
    )
    token: Union[None, str] = Field(None, description="The pagination token.")
    search: Union[CompanySearch, None, list["CompanySearch"]] = Field(
        None, description="Search criteria."
    )
    kyc_status: Union[KYCStatus, None, list[KYCStatus]] = Field(
        None, description="The KYC status of the company."
    )
