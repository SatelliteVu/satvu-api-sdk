# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja

from collections.abc import Callable
from typing import Any

from satvu.core import SDKClient, _deep_merge
from satvu.http import HttpClient
from satvu.services.policy.models.list_active_contracts_input import (
    ListActiveContractsInput,
)
from satvu.services.policy.models.router_active_contracts_response import (
    RouterActiveContractsResponse,
)
from satvu.services.policy.models.terms_user_terms_accepted import (
    TermsUserTermsAccepted,
)
from satvu.services.policy.models.user_acceptance_terms_input import (
    UserAcceptanceTermsInput,
)
from satvu.shared.parsing import parse_response


class PolicyService(SDKClient):
    base_path = "/policy/v1"

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

    def list_active_contracts(
        self,
        body: ListActiveContractsInput,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> RouterActiveContractsResponse:
        """
        Active Contracts

        Get active contracts for a user.

        Args:
            body (ListActiveContractsInput):
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            RouterActiveContractsResponse
        """

        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)

        result = self.make_request(
            method="post",
            url="/contracts",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), RouterActiveContractsResponse
            )
        return response.json().unwrap()

    def user_acceptance_terms(
        self,
        body: UserAcceptanceTermsInput,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> TermsUserTermsAccepted:
        """
        User Acceptance Terms

        Defines if a user has accepted terms and conditions of service.

        Args:
            body (UserAcceptanceTermsInput):
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            TermsUserTermsAccepted
        """

        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)

        result = self.make_request(
            method="post",
            url="/terms",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), TermsUserTermsAccepted)
        return response.json().unwrap()
