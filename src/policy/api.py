from collections.abc import Callable
from typing import Dict, List, Union, Unpack
from uuid import UUID

from satvu_api_sdk.core import SDKClient

from policy.models.post_active_contracts_input import PostActiveContractsInput
from policy.models.router_active_contracts_response import RouterActiveContractsResponse
from policy.models.router_query_result import RouterQueryResult
from policy.models.terms_user_terms_accepted import TermsUserTermsAccepted
from policy.models.user_acceptance_terms_input import UserAcceptanceTermsInput


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


class PolicyService(SDKClient):
    base_path = "/policy/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def post_active_contracts(
        self, **kwargs: Unpack[PostActiveContractsInput]
    ) -> RouterActiveContractsResponse:
        """
        Active Contracts

        Get active contracts for a user.

        Args:
            token (str): User access token

        Returns:
            RouterActiveContractsResponse
        """

        response = self.make_request(
            method="post",
            url="/contracts",
            json=kwargs,
        )

        if response.status_code == 200:
            return RouterActiveContractsResponse(**response.json())
        return response.json()

    def policy_query(
        self,
    ) -> RouterQueryResult:
        """
        Policy Query

        Query policy decisions.

        Args:

        Returns:
            RouterQueryResult
        """

        response = self.make_request(
            method="post",
            url="/policy/query/*query",
        )

        if response.status_code == 200:
            return RouterQueryResult(**response.json())
        return response.json()

    def user_acceptance_terms(
        self, **kwargs: Unpack[UserAcceptanceTermsInput]
    ) -> TermsUserTermsAccepted:
        """
        User Acceptance Terms

        Defines if a user has accepted terms and conditions of service.

        Args:
            accepted (bool): Terms and Conditions have been accepted
            token (str): User access token

        Returns:
            TermsUserTermsAccepted
        """

        response = self.make_request(
            method="post",
            url="/terms",
            json=kwargs,
        )

        if response.status_code == 200:
            return TermsUserTermsAccepted(**response.json())
        return response.json()
