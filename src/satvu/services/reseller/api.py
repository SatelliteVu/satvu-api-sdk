# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja

from collections.abc import Callable, Generator
from typing import Union

from satvu.core import SDKClient
from satvu.http import HttpClient
from satvu.services.reseller.models.create_user import CreateUser
from satvu.services.reseller.models.create_user_response import CreateUserResponse
from satvu.services.reseller.models.get_companies import GetCompanies
from satvu.services.reseller.models.get_users import GetUsers
from satvu.services.reseller.models.search_companies import SearchCompanies
from satvu.services.reseller.models.search_users import SearchUsers
from satvu.shared.parsing import parse_response


class ResellerService(SDKClient):
    base_path = "/resellers/v1"

    def __init__(
        self,
        env: str | None,
        get_token: Callable[[], str],
        http_client: HttpClient | None = None,
        timeout: int = 30,
        max_retry_attempts: int = 5,
        max_retry_after_seconds: float = 300.0,
    ):
        super().__init__(
            env=env,
            get_token=get_token,
            http_client=http_client,
            timeout=timeout,
            max_retry_attempts=max_retry_attempts,
            max_retry_after_seconds=max_retry_after_seconds,
        )

    def create_users(
        self,
        items: list[CreateUser],
        timeout: int | None = None,
    ) -> list[CreateUserResponse]:
        """
        Create end users

        Create end users.

        Args:
            body (CreateUser): Represents payload to create a user
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            list[CreateUserResponse]
        """

        json_body = [item.model_dump(mode="json") for item in items]

        result = self.make_request(
            method="post",
            url="/user",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 201:
            return parse_response(response.json().unwrap(), list[CreateUserResponse])
        return response.json().unwrap()

    def get_users(
        self,
        limit: Union[None, int] = 100,
        token: None | str = None,
        timeout: int | None = None,
    ) -> GetUsers:
        """
        Get end users

        List all end users.

        Args:
            limit (Union[None, int]): The number of end users to return per page. Default: 100.
            token (None | str): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            GetUsers
        """

        params = {
            "limit": limit,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url="/users",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), GetUsers)
        return response.json().unwrap()

    def get_users_iter(
        self,
        limit: Union[None, int] = 100,
        max_pages: int | None = None,
    ) -> Generator[GetUsers, None, None]:
        """
        Get end users (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            limit (Union[None, int]): The number of end users to return per page. Default: 100.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.reseller.get_users_iter(
                max_pages=10
            ):
                for item in page.users:
                    print(item)
            ```
        """
        token = None
        page_count = 0

        while True:
            if max_pages and page_count >= max_pages:
                break

            response = self.get_users(
                limit=limit,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def get_companies(
        self,
        limit: Union[None, int] = 100,
        token: None | str = None,
        timeout: int | None = None,
    ) -> GetCompanies:
        """
        Get end user companies

        List end user companies.

        Args:
            limit (Union[None, int]): The number of end user companies to return per page. Default:
                100.
            token (None | str): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            GetCompanies
        """

        params = {
            "limit": limit,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url="/companies",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), GetCompanies)
        return response.json().unwrap()

    def get_companies_iter(
        self,
        limit: Union[None, int] = 100,
        max_pages: int | None = None,
    ) -> Generator[GetCompanies, None, None]:
        """
        Get end user companies (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            limit (Union[None, int]): The number of end user companies to return per page. Default:
            100.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.reseller.get_companies_iter(
                max_pages=10
            ):
                for item in page.companies:
                    print(item)
            ```
        """
        token = None
        page_count = 0

        while True:
            if max_pages and page_count >= max_pages:
                break

            response = self.get_companies(
                limit=limit,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def search_users(
        self,
        body: SearchUsers,
        timeout: int | None = None,
    ) -> GetUsers:
        """
        Search end users

        Search end users.

        Args:
            body (SearchUsers):
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            GetUsers
        """

        json_body = body.model_dump(by_alias=True, mode="json")

        result = self.make_request(
            method="post",
            url="/search/users",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), GetUsers)
        return response.json().unwrap()

    def search_users_iter(
        self,
        body: SearchUsers,
        max_pages: int | None = None,
    ) -> Generator[GetUsers, None, None]:
        """
        Search end users (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (SearchUsers):
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.reseller.search_users_iter(
                body=...,
                max_pages=10
            ):
                for item in page.users:
                    print(item)
            ```
        """
        token = None
        page_count = 0

        while True:
            if max_pages and page_count >= max_pages:
                break

            body_with_token = body.model_copy(update={"token": token})
            response = self.search_users(
                body=body_with_token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def search_companies(
        self,
        body: SearchCompanies,
        timeout: int | None = None,
    ) -> GetCompanies:
        """
        Search end user companies

        Search end user companies.

        Args:
            body (SearchCompanies):
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            GetCompanies
        """

        json_body = body.model_dump(by_alias=True, mode="json")

        result = self.make_request(
            method="post",
            url="/search/companies",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), GetCompanies)
        return response.json().unwrap()

    def search_companies_iter(
        self,
        body: SearchCompanies,
        max_pages: int | None = None,
    ) -> Generator[GetCompanies, None, None]:
        """
        Search end user companies (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (SearchCompanies):
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.reseller.search_companies_iter(
                body=...,
                max_pages=10
            ):
                for item in page.companies:
                    print(item)
            ```
        """
        token = None
        page_count = 0

        while True:
            if max_pages and page_count >= max_pages:
                break

            body_with_token = body.model_copy(update={"token": token})
            response = self.search_companies(
                body=body_with_token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break
