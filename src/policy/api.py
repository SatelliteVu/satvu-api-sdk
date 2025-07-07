from collections.abc import Callable
from typing import Unpack

from satvu_api_sdk.core import SDKClient
from shared.utils import deep_parse_from_annotation, normalize_keys

from policy.models.post_active_contracts_input import PostActiveContractsInput
from policy.models.router_active_contracts_response import RouterActiveContractsResponse
from policy.models.router_query_result import RouterQueryResult
from policy.models.terms_user_terms_accepted import TermsUserTermsAccepted
from policy.models.user_acceptance_terms_input import UserAcceptanceTermsInput


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
            return deep_parse_from_annotation(
                normalize_keys(response.json()), RouterActiveContractsResponse
            )
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
            return deep_parse_from_annotation(
                normalize_keys(response.json()), RouterQueryResult
            )
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
            return deep_parse_from_annotation(
                normalize_keys(response.json()), TermsUserTermsAccepted
            )
        return response.json()
