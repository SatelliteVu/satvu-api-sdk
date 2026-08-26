# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for wallet service.

Generated from OpenAPI spec version v1.
Uses property-based testing with hypothesis-jsonschema.
"""

from unittest.mock import Mock
from uuid import uuid4

import pook
import pytest
from hypothesis import HealthCheck, given, settings

from satvu import SatVuSDK, create_http_client
from satvu.http.errors import ClientError
from satvu.services.wallet.models.batch_balance_response import BatchBalanceResponse
from satvu.services.wallet.models.credit_balance_response import CreditBalanceResponse

from .test_schemas import (
    get_response_strategy,
)


@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestWalletService:
    """Property-based tests for WalletService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        # Mock the auth token
        mock_get_token = Mock(return_value="test_token")

        # Construct base URL for the wallet service
        # We need to match how SDKClient builds its base_url in __init__
        subdomain = "api"
        env_part = "qa."
        base_path = "/wallet/v1"
        self.base_url = f"https://{subdomain}.{env_part}satellitevu.com{base_path}"

        # Create HTTP client with specified backend
        http_client = create_http_client(
            backend=backend,
            base_url=self.base_url,
            get_token=mock_get_token,
        )

        self.sdk = SatVuSDK(
            client_id="test_client_id",
            client_secret="test_client_secret",  # pragma: allowlist secret # nosec B106
            http_client=http_client,
            env="qa",
        )

        # Override the token getter with our mock
        self.sdk.wallet._get_token = mock_get_token

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy("/{contract_id}/credit", "get", "200"),
    )
    def test_get_credit_balance_200(
        self,
        backend,
        response_data,
    ):
        """
        Test get_credit_balance with 200 response.
        """
        # Generate path parameters
        contract_id = uuid4()
        path = f"/{contract_id}/credit"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP response
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )

        # Call the service method

        result = self.sdk.wallet.get_credit_balance(
            contract_id=contract_id,
        )

        # Assert response parses correctly
        assert result is not None

        # Assert response type matches expected type
        assert isinstance(result, CreditBalanceResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy("/{contract_id}/credit", "get", "422"),
    )
    def test_get_credit_balance_422_error(
        self,
        backend,
        response_data,
    ):
        """
        Test get_credit_balance with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        # Generate path parameters
        contract_id = uuid4()
        path = f"/{contract_id}/credit"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP error response
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )

        # HTTP 422 should raise ClientError
        with pytest.raises(ClientError) as exc_info:
            self.sdk.wallet.get_credit_balance(
                contract_id=contract_id,
            )

        # Verify the exception contains the correct status code
        assert exc_info.value.status_code == 422

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy("/balances", "get", "200"),
    )
    def test_get_batch_credit_balances_200(
        self,
        backend,
        response_data,
    ):
        """
        Test get_batch_credit_balances with 200 response.
        """
        # Generate path parameters
        path = "/balances"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP response
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )

        # Call the service method

        result = self.sdk.wallet.get_batch_credit_balances()

        # Assert response parses correctly
        assert result is not None

        # Assert response type matches expected type
        assert isinstance(result, BatchBalanceResponse)
