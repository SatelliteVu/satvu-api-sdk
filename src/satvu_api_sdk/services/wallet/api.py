from collections.abc import Callable
from uuid import UUID

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.shared.utils import deep_parse_from_annotation

from satvu_api_sdk.services.wallet.models.credit_balance_response import (
    CreditBalanceResponse,
)


class WalletService(SDKClient):
    base_path = "/wallet/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_credit(
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
            return deep_parse_from_annotation(
                response.json(), CreditBalanceResponse, self.__class__
            )
        return response.json()
