from collections.abc import Callable
from typing import Union

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.shared.utils import deep_parse_from_annotation

from satvu_api_sdk.services.reseller.models.create_user import CreateUser
from satvu_api_sdk.services.reseller.models.create_user_response import CreateUserResponse
from satvu_api_sdk.services.reseller.models.get_companies import GetCompanies
from satvu_api_sdk.services.reseller.models.get_users import GetUsers
from satvu_api_sdk.services.reseller.models.search_companies import SearchCompanies
from satvu_api_sdk.services.reseller.models.search_users import SearchUsers


class ResellerService(SDKClient):
    base_path = "/resellers/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def post_create_users(
        self,
        items: list[CreateUser],
    ) -> list[CreateUserResponse]:
        """
        Create end users

        Create end users.

        Args:
            body (CreateUser): Represents payload to create a user

        Returns:
            list[CreateUserResponse]
        """

        json_body = [item.model_dump() for item in items]

        response = self.make_request(
            method="post",
            url="/user",
            json=json_body,
        )

        if response.status_code == 201:
            return deep_parse_from_annotation(
                response.json(), list[CreateUserResponse], self.__class__
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

        params = {
            "limit": limit,
            "token": token,
        }

        response = self.make_request(
            method="get",
            url="/users",
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), GetUsers, self.__class__)
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

        params = {
            "limit": limit,
            "token": token,
        }

        response = self.make_request(
            method="get",
            url="/companies",
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                response.json(), GetCompanies, self.__class__
            )
        return response.json()

    def search_users(self, body: SearchUsers) -> GetUsers:
        """
        Search end users

        Search end users.

        Args:
            body (SearchUsers):

        Returns:
            GetUsers
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/search/users",
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), GetUsers, self.__class__)
        return response.json()

    def search_companies(self, body: SearchCompanies) -> GetCompanies:
        """
        Search end user companies

        Search end user companies.

        Args:
            body (SearchCompanies):

        Returns:
            GetCompanies
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/search/companies",
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                response.json(), GetCompanies, self.__class__
            )
        return response.json()
