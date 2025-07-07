from collections.abc import Callable
from typing import Any, Dict, List, Union, Unpack
from uuid import UUID

from satvu_api_sdk.core import SDKClient

from reseller.models.create_user import CreateUser
from reseller.models.create_user_response import CreateUserResponse
from reseller.models.get_companies import GetCompanies
from reseller.models.get_users import GetUsers
from reseller.models.search_companies import SearchCompanies
from reseller.models.search_users import SearchUsers


def disambiguate_union_response(response_data: dict, response_disambiguation: dict):
    """
    Select the best-matching model class to instantiate from the union.

    Args:
        response_data (dict): The response data to disambiguate.
        response_disambiguation (dict): Configuration for disambiguation.

    Returns:
        Any: The instantiated model or the original response data.
    """
    discriminator = response_disambiguation.get("discriminator")
    mapping = response_disambiguation.get("discriminator_mapping")
    fallback_models = response_disambiguation.get("fallback_models")

    print(fallback_models)

    if discriminator and mapping and discriminator in response_data:
        disc_value = response_data[discriminator]
        model_cls = mapping.get(disc_value)
        if model_cls:
            try:
                return model_cls(**response_data)
            except Exception:
                pass

    def _type_matches(value, expected_type):
        if expected_type == UUID:
            return isinstance(value, str)
        origin = getattr(expected_type, "__origin__", None)
        if origin is not None:
            if origin is Union:
                return any(_type_matches(value, t) for t in expected_type.__args__)
            elif origin in {list, List}:
                return isinstance(value, list) and all(
                    _type_matches(v, expected_type.__args__[0]) for v in value
                )
            elif origin in {dict, Dict}:
                return isinstance(value, dict) and all(
                    _type_matches(v, expected_type.__args__[1]) for v in value.values()
                )

        if hasattr(expected_type, "get_required_fields_and_types"):
            return _required_fields_and_types_match(value, expected_type)
        return isinstance(value, expected_type)

    def _required_fields_and_types_match(data, model_cls):
        if not isinstance(data, dict):
            return False
        required = model_cls.get_required_fields_and_types()
        print(f"Required fields and types: {required}")
        return all(
            field in data and _type_matches(data[field], typ)
            for field, typ in required.items()
        )

    def _count_optional_matches(data, model_cls):
        if not isinstance(data, dict):
            return 0
        optional = model_cls.get_optional_fields_and_types()
        return sum(
            1
            for field, typ in optional.items()
            if field in data and _type_matches(data[field], typ)
        )

    response_fields = set(response_data.keys())
    candidates = []
    for model_cls in fallback_models:
        model_cls = eval(model_cls)
        if model_cls.get_required_fields().issubset(response_fields):
            print("X")
            if _required_fields_and_types_match(response_data, model_cls):
                print("Y")
                matching_optional = _count_optional_matches(response_data, model_cls)
                candidates.append((model_cls, matching_optional))

    if candidates:
        candidates.sort(
            key=lambda x: (x[1], len(x[0].get_required_fields())), reverse=True
        )
        for model_cls, _ in candidates:
            try:
                return model_cls(**response_data)
            except Exception:
                continue

    return response_data


class ResellerService(SDKClient):
    base_path = "/resellers/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def post_create_users(
        self, **kwargs: Unpack[list["CreateUser"]]
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

        response = self.make_request(
            method="post",
            url="/user",
            json=kwargs,
        )

        if response.status_code == 201:
            return list["CreateUserResponse"](**response.json())
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
            return GetUsers(**response.json())
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
            return GetCompanies(**response.json())
        return response.json()

    def search_users(self, **kwargs: Unpack[SearchUsers]) -> GetUsers:
        """
        Search end users

        Search end users.

        Args:
            limit (Union[None, int]): The number of results to return per page.
            token (Union[None, str]): The pagination token.
            search (Union['UserSearch', None, list['UserSearch']]): Search criteria.
            kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the user.

        Returns:
            GetUsers
        """

        response = self.make_request(
            method="post",
            url="/search/users",
            json=kwargs,
        )

        if response.status_code == 200:
            return GetUsers(**response.json())
        return response.json()

    def search_companies(self, **kwargs: Unpack[SearchCompanies]) -> GetCompanies:
        """
        Search end user companies

        Search end user companies.

        Args:
            limit (Union[None, int]): The number of results to return per page.
            token (Union[None, str]): The pagination token.
            search (Union['CompanySearch', None, list['CompanySearch']]): Search criteria.
            kyc_status (Union[KYCStatus, None, list[KYCStatus]]): The KYC status of the company.

        Returns:
            GetCompanies
        """

        response = self.make_request(
            method="post",
            url="/search/companies",
            json=kwargs,
        )

        if response.status_code == 200:
            return GetCompanies(**response.json())
        return response.json()
