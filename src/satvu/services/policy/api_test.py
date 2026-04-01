# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for policy service.

Generated from OpenAPI spec version v0.82.2.
Uses property-based testing with hypothesis-jsonschema.
"""

from unittest.mock import Mock

import pook
import pytest
from hypothesis import HealthCheck, given, settings

from satvu import SatVuSDK, create_http_client
from satvu.http.errors import ClientError
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

from .test_schemas import (
    get_request_body_strategy,
    get_response_strategy,
)


@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestPolicyService:
    """Property-based tests for PolicyService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        # Mock the auth token
        mock_get_token = Mock(return_value="test_token")

        # Construct base URL for the policy service
        # We need to match how SDKClient builds its base_url in __init__
        subdomain = "api"
        env_part = "qa."
        base_path = "/policy/v1"
        self.base_url = f"https://{subdomain}.{env_part}satellitevu.com{base_path}"

        # Create HTTP client with specified backend
        http_client = create_http_client(
            backend=backend,
            base_url=self.base_url,
            get_token=mock_get_token,
        )

        self.sdk = SatVuSDK(
            client_id="test_client_id",
            client_secret="test_client_secret",  # pragma: allowlist secret
            http_client=http_client,
            env="qa",
        )

        # Override the token getter with our mock
        self.sdk.policy._get_token = mock_get_token

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
        response_data=get_response_strategy("/contracts", "post", "200"),
        body_data=get_request_body_strategy("/contracts", "post"),
    )
    def test_list_active_contracts_200(
        self,
        backend,
        response_data,
        body_data,
    ):
        """
        Test list_active_contracts with 200 response.
        """
        # Generate path parameters
        path = "/contracts"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP response
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )

        # Call the service method
        # Parse body_data into Pydantic model
        body = ListActiveContractsInput.model_validate(body_data)

        result = self.sdk.policy.list_active_contracts(
            body=body,
        )

        # Assert response parses correctly
        assert result is not None

        # Assert response type matches expected type
        assert isinstance(result, RouterActiveContractsResponse)

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
        response_data=get_response_strategy("/contracts", "post", "400"),
        body_data=get_request_body_strategy("/contracts", "post"),
    )
    def test_list_active_contracts_400_error(
        self,
        backend,
        response_data,
        body_data,
    ):
        """
        Test list_active_contracts with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        # Generate path parameters
        path = "/contracts"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP error response
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )

        # Parse body_data into Pydantic model
        body = ListActiveContractsInput.model_validate(body_data)

        # HTTP 400 should raise ClientError
        with pytest.raises(ClientError) as exc_info:
            self.sdk.policy.list_active_contracts(
                body=body,
            )

        # Verify the exception contains the correct status code
        assert exc_info.value.status_code == 400

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
        response_data=get_response_strategy("/terms", "post", "200"),
        body_data=get_request_body_strategy("/terms", "post"),
    )
    def test_user_acceptance_terms_200(
        self,
        backend,
        response_data,
        body_data,
    ):
        """
        Test user_acceptance_terms with 200 response.
        """
        # Generate path parameters
        path = "/terms"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP response
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )

        # Call the service method
        # Parse body_data into Pydantic model
        body = UserAcceptanceTermsInput.model_validate(body_data)

        result = self.sdk.policy.user_acceptance_terms(
            body=body,
        )

        # Assert response parses correctly
        assert result is not None

        # Assert response type matches expected type
        assert isinstance(result, TermsUserTermsAccepted)

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
        response_data=get_response_strategy("/terms", "post", "400"),
        body_data=get_request_body_strategy("/terms", "post"),
    )
    def test_user_acceptance_terms_400_error(
        self,
        backend,
        response_data,
        body_data,
    ):
        """
        Test user_acceptance_terms with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        # Generate path parameters
        path = "/terms"
        url = f"{self.base_url}{path}"

        # Reset and activate pook for each hypothesis iteration
        pook.reset()
        pook.on()

        # Mock the HTTP error response
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )

        # Parse body_data into Pydantic model
        body = UserAcceptanceTermsInput.model_validate(body_data)

        # HTTP 400 should raise ClientError
        with pytest.raises(ClientError) as exc_info:
            self.sdk.policy.user_acceptance_terms(
                body=body,
            )

        # Verify the exception contains the correct status code
        assert exc_info.value.status_code == 400
