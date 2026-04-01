# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja

from collections.abc import Callable
from uuid import UUID

from satvu.core import SDKClient
from satvu.http import HttpClient
from satvu.services.wallet.models.batch_balance_response import BatchBalanceResponse
from satvu.services.wallet.models.credit_balance_response import CreditBalanceResponse
from satvu.shared.parsing import parse_response


class WalletService(SDKClient):
    base_path = "/wallet/v1"

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

    def get_credit_balance(
        self,
        contract_id: UUID,
        timeout: int | None = None,
    ) -> CreditBalanceResponse:
        """
        Credit

        Returns the credit balance for the current billing cycle (UTC calendar month). This is calculated
        as the monthly credit limit for the contract minus the total credits used this month.

        Args:
            contract_id (UUID): Contract ID.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            CreditBalanceResponse
        """

        result = self.make_request(
            method="get",
            url=f"/{contract_id}/credit",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), CreditBalanceResponse)
        return response.json().unwrap()

    def get_batch_credit_balances(
        self,
        timeout: int | None = None,
    ) -> BatchBalanceResponse:
        """
        Batch Balances

        Calculate credit balances for multiple contracts.
        Returns a JSON mapping contract IDs to their balances.

        Args:
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            BatchBalanceResponse
        """

        result = self.make_request(
            method="get",
            url="/balances",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), BatchBalanceResponse)
        return response.json().unwrap()
