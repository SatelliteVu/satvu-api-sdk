from typing import Union

from pydantic import BaseModel

from ..models.kyc_status import KYCStatus
from ..models.user_search import UserSearch


class SearchUsers(BaseModel):
    """
    Attributes:
        limit (Union[None, int]): The number of results to return per page. Default: 100.
        token (Union[None, str]): The pagination token.
        search (Union[None, UserSearch, list['UserSearch']]): Search criteria.
        kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the user.
    """

    limit: Union[None, int] = 100
    token: Union[None, str] = None
    search: Union[None, UserSearch, list["UserSearch"]] = None
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
