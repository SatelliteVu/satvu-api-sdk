from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.kyc_status import KYCStatus

if TYPE_CHECKING:
    from ..models.user_search import UserSearch


class SearchUsers(BaseModel):
    """
    Attributes:
        limit (Union[None, int]): The number of results to return per page. Default: 100.
        token (None | str): The pagination token.
        search (Union['UserSearch', list[UserSearch], None]): Search criteria.
        kyc_status (Union['KYCStatus', list['KYCStatus'], None]): The KYC status of the user.
    """

    limit: Union[None, int] = Field(
        100, description="The number of results to return per page.", alias="limit"
    )
    token: None | str = Field(None, description="The pagination token.", alias="token")
    search: Union["UserSearch", list[UserSearch], None] = Field(
        None, description="Search criteria.", alias="search"
    )
    kyc_status: Union["KYCStatus", list["KYCStatus"], None] = Field(
        None, description="The KYC status of the user.", alias="kyc_status"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
