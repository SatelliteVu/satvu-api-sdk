from collections.abc import Callable
from uuid import UUID

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.services.wallet.models.batch_balance_response import (
    BatchBalanceResponse,
)
from satvu_api_sdk.services.wallet.models.credit_balance_response import (
    CreditBalanceResponse,
)
from satvu_api_sdk.shared.parsing import parse_response


class WalletService(SDKClient):
    base_path = "/wallet/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def credit__get(
        self,
        contract_id: UUID,
    ) -> CreditBalanceResponse:
        """
        Credit

        Returns the credit balance for the current billing cycle (UTC calendar month). This is calculated
        as the monthly credit limit for the contract minus the total credits used this month.

        Args:
            contract_id (UUID): Contract ID.

        Returns:
            CreditBalanceResponse
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/credit".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return parse_response(response.json(), CreditBalanceResponse)
        return response.json()

    def batch_balances__get(
        self,
    ) -> BatchBalanceResponse:
        """
        Batch Balances

        Calculate credit balances for multiple contracts in a single database query.
        Uses advisory locks to prevent race conditions during balance calculations.
        Returns a dictionary mapping contract IDs to their balance responses.

        Maximum 100 contracts per request to prevent resource exhaustion.

        Args:

        Returns:
            BatchBalanceResponse
        """

        response = self.make_request(
            method="get",
            url="/balances",
        )

        if response.status_code == 200:
            return parse_response(response.json(), BatchBalanceResponse)
        return response.json()
