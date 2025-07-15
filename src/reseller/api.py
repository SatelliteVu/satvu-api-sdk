from collections.abc import Callable
from typing import Any, Union

from satvu_api_sdk.core import SDKClient
from shared.utils import deep_parse_from_annotation, normalize_keys

from reseller.models.create_user import CreateUser
from reseller.models.create_user_response import CreateUserResponse
from reseller.models.get_companies import GetCompanies
from reseller.models.get_users import GetUsers
from reseller.models.search_companies import SearchCompanies
from reseller.models.search_users import SearchUsers


class ResellerService(SDKClient):
    base_path = "/resellers/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def post_create_users(
        self,
        items: list["CreateUser"],
    ) -> list["CreateUserResponse"]:
        """
        Create end users

        Create end users.

        Args:
            user_email (str): The email address of the user.
            user_name (str): The full name of the user.
            company_name (str): The name of the company.
            company_address (CompanyAddress):

        Returns:
            list['CreateUserResponse']
        """

        json_body = [item.model_dump() for item in items]

        response = self.make_request(
            method="post",
            url="/user",
            json=json_body,
        )

        if response.status_code == 201:
            return deep_parse_from_annotation(
                normalize_keys(response.json()), list["CreateUserResponse"]
            )
        return response.json()

    def get_users(
        self,
        limit: Union[None, int] = 100,
        token: Union[None, str] = None,
    ) -> GetUsers:
        """
        Get end users

        List end users.

        Args:
            limit (Union[None, int]): The number of end users to return per page. Default: 100.
            token (Union[None, str]): The pagination token.

        Returns:
            GetUsers
        """

        params: dict[str, Any] = {}
        params["limit"] = limit

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/users",
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(normalize_keys(response.json()), GetUsers)
        return response.json()

    def get_companies(
        self,
        limit: Union[None, int] = 100,
        token: Union[None, str] = None,
    ) -> GetCompanies:
        """
        Get end user companies

        List end user companies.

        Args:
            limit (Union[None, int]): The number of end user companies to return per page. Default:
                100.
            token (Union[None, str]): The pagination token.

        Returns:
            GetCompanies
        """

        params: dict[str, Any] = {}
        params["limit"] = limit

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/companies",
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()), GetCompanies
            )
        return response.json()

    def search_users(self, body: SearchUsers) -> GetUsers:
        """
        Search end users

        Search end users.

        Args:
            limit (Union[None, int]): The number of results to return per page.
            token (Union[None, str]): The pagination token.
            search (Union[None, UserSearch, list['UserSearch']]): Search criteria.
            kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the user.

        Returns:
            GetUsers
        """

        json_body = body.model_dump()

        response = self.make_request(
            method="post",
            url="/search/users",
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(normalize_keys(response.json()), GetUsers)
        return response.json()

    def search_companies(self, body: SearchCompanies) -> GetCompanies:
        """
        Search end user companies

        Search end user companies.

        Args:
            limit (Union[None, int]): The number of results to return per page.
            token (Union[None, str]): The pagination token.
            search (Union[CompanySearch, None, list['CompanySearch']]): Search criteria.
            kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the company.

        Returns:
            GetCompanies
        """

        json_body = body.model_dump()

        response = self.make_request(
            method="post",
            url="/search/companies",
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()), GetCompanies
            )
        return response.json()
