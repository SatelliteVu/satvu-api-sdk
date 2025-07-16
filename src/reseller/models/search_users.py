from typing import Union

from pydantic import BaseModel, Field

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

    limit: Union[None, int] = Field(
        100, description="The number of results to return per page."
    )
    token: Union[None, str] = Field(None, description="The pagination token.")
    search: Union[None, UserSearch, list["UserSearch"]] = Field(
        None, description="Search criteria."
    )
    kyc_status: Union[KYCStatus, None, list[KYCStatus]] = Field(
        None, description="The KYC status of the user."
    )
