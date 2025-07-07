from dataclasses import dataclass
from typing import TYPE_CHECKING, Union

from ..models.kyc_status import KYCStatus

if TYPE_CHECKING:
    from ..models.company_search import CompanySearch


@dataclass
class SearchCompanies:
    """
    Attributes:
        limit (Union[None, int]): The number of results to return per page. Default: 100.
        token (Union[None, str]): The pagination token.
        search (Union['CompanySearch', None, list['CompanySearch']]): Search criteria.
        kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the company.
    """

    limit: Union[None, int] = 100
    token: Union[None, str] = None
    search: Union["CompanySearch", None, list["CompanySearch"]] = None
    kyc_status: Union[KYCStatus, None, list[KYCStatus]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "limit": int,
            "token": object,
            "search": object,
            "kyc_status": object,
        }
