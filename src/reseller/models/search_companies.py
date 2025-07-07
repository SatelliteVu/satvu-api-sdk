from typing import Union

from pydantic import BaseModel

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

    limit: Union[None, int] = 100
    token: Union[None, str] = None
    search: Union[CompanySearch, None, list["CompanySearch"]] = None
    kyc_status: Union[KYCStatus, None, list[KYCStatus]] = None
