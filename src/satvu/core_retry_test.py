"""Tests for automatic Retry-After retry logic in SDKClient."""

from unittest.mock import MagicMock, patch

import pytest

from satvu.core import SDKClient
from satvu.http.protocol import HttpResponse
from satvu.result import Ok


class MockCatalogClient(SDKClient):
    """Mock catalog client for testing."""

    base_path = "catalog"


@pytest.fixture
def mock_http_client():
    """Create a mock HTTP client."""
    client = MagicMock()
    return client


@pytest.fixture
def sdk_client(mock_http_client):
    """Create an SDKClient instance with mocked HTTP client."""
    return MockCatalogClient(env="qa", http_client=mock_http_client, timeout=30)


def create_mock_response(status_code: int, headers: dict[str, str] | None = None):
    """Helper to create a mock HTTP response."""
    response = MagicMock(spec=HttpResponse)
    response.status_code = status_code
    response.headers = headers or {}
    return response


class TestRetryAfter202:
    """Tests for 202 Accepted responses with Retry-After header."""

    @patch("satvu.core.time.sleep")
    def test_retry_202_with_retry_after(self, mock_sleep, sdk_client, mock_http_client):
        """Test that 202 Accepted with Retry-After triggers retry."""
        # First call returns 202 with Retry-After: 2
        response_202 = create_mock_response(202, {"Retry-After": "2"})
        # Second call returns 200 OK
        response_200 = create_mock_response(200)

        mock_http_client.request.side_effect = [
            Ok(response_202),
            Ok(response_200),
        ]

        result = sdk_client.make_request("GET", "/test")

        # Should have retried once
        assert mock_http_client.request.call_count == 2
        # Should have slept for 2 seconds
        mock_sleep.assert_called_once_with(2.0)
        # Should return the 200 OK response
        assert result.is_ok()
        assert result.unwrap().status_code == 200

    @patch("satvu.core.time.sleep")
    def test_retry_202_caps_retry_after(self, mock_sleep, sdk_client, mock_http_client):
        """Test that Retry-After is capped at max_retry_after_seconds."""
        # First call returns 202 with Retry-After: 600 (10 minutes)
        response_202 = create_mock_response(202, {"Retry-After": "600"})
        # Second call returns 200 OK
        response_200 = create_mock_response(200)

        mock_http_client.request.side_effect = [
            Ok(response_202),
            Ok(response_200),
        ]

        result = sdk_client.make_request("GET", "/test")

        # Should have slept for MAX (300 seconds), not 600
        mock_sleep.assert_called_once_with(sdk_client.max_retry_after_seconds)
        assert result.is_ok()

    @patch("satvu.core.time.sleep")
    def test_retry_202_max_attempts(self, mock_sleep, sdk_client, mock_http_client):
        """Test that retries stop after max attempts (5 total)."""
        # All 5 calls return 202 with Retry-After
        response_202 = create_mock_response(202, {"Retry-After": "1"})

        mock_http_client.request.side_effect = [
            Ok(response_202),
            Ok(response_202),
            Ok(response_202),
            Ok(response_202),
            Ok(response_202),
        ]

        result = sdk_client.make_request("GET", "/test")

        # Should have made 5 attempts total (default max_retry_attempts)
        assert mock_http_client.request.call_count == 5
        # Should have slept 4 times (not after last attempt)
        assert mock_sleep.call_count == 4
        # Should return the last 202 response
        assert result.is_ok()
        assert result.unwrap().status_code == 202

    def test_retry_202_without_retry_after(self, sdk_client, mock_http_client):
        """Test that 202 Accepted without Retry-After returns immediately."""
        response_202 = create_mock_response(202)  # No Retry-After header

        mock_http_client.request.return_value = Ok(response_202)

        result = sdk_client.make_request("GET", "/test")

        # Should NOT retry (no Retry-After header)
        assert mock_http_client.request.call_count == 1
        assert result.is_ok()
        assert result.unwrap().status_code == 202

    @patch("satvu.core.time.sleep")
    def test_retry_202_case_insensitive_header(
        self, mock_sleep, sdk_client, mock_http_client
    ):
        """Test that Retry-After header is case-insensitive."""
        # Test lowercase "retry-after"
        response_202 = create_mock_response(202, {"retry-after": "1"})
        response_200 = create_mock_response(200)

        mock_http_client.request.side_effect = [
            Ok(response_202),
            Ok(response_200),
        ]

        result = sdk_client.make_request("GET", "/test")

        mock_sleep.assert_called_once_with(1.0)
        assert result.is_ok()

    @patch("satvu.core.time.sleep")
    def test_configurable_retry_parameters(self, mock_sleep, mock_http_client):
        """Test that retry parameters can be configured via constructor."""
        # Create client with custom retry config
        client = MockCatalogClient(
            env="qa",
            http_client=mock_http_client,
            timeout=30,
            max_retry_attempts=2,
            max_retry_after_seconds=60.0,
        )

        # Verify configuration was set
        assert client.max_retry_attempts == 2
        assert client.max_retry_after_seconds == 60.0

        # Test that max_retry_attempts is respected
        response_202 = create_mock_response(202, {"Retry-After": "1"})
        mock_http_client.request.side_effect = [
            Ok(response_202),
            Ok(response_202),
        ]

        client.make_request("GET", "/test")

        # Should have made only 2 attempts (custom max_retry_attempts)
        assert mock_http_client.request.call_count == 2
        # Should have slept 1 time (not after last attempt)
        assert mock_sleep.call_count == 1

    @patch("satvu.core.time.sleep")
    def test_configurable_max_retry_after_seconds(self, mock_sleep, mock_http_client):
        """Test that max_retry_after_seconds caps the retry delay."""
        # Create client with custom max retry after seconds
        client = MockCatalogClient(
            env="qa",
            http_client=mock_http_client,
            timeout=30,
            max_retry_after_seconds=10.0,
        )

        # Response with Retry-After: 100 (should be capped at 10)
        response_202 = create_mock_response(202, {"Retry-After": "100"})
        response_200 = create_mock_response(200)

        mock_http_client.request.side_effect = [
            Ok(response_202),
            Ok(response_200),
        ]

        result = client.make_request("GET", "/test")

        # Should have slept for custom max (10 seconds), not 100
        mock_sleep.assert_called_once_with(10.0)
        assert result.is_ok()


class TestHeaderParsing:
    """Tests for Retry-After header parsing logic."""

    def test_parse_retry_after_integer(self, sdk_client):
        """Test parsing integer Retry-After value."""
        result = sdk_client._parse_retry_after_from_headers(
            {"Retry-After": "5"}, max_seconds=300.0
        )
        assert result == 5.0

        # Test lowercase
        result1 = sdk_client._parse_retry_after_from_headers(
            {"retry-after": "3"}, max_seconds=300.0
        )
        assert result1 == 3.0

    def test_parse_retry_after_float(self, sdk_client):
        """Test parsing float Retry-After value."""
        result = sdk_client._parse_retry_after_from_headers(
            {"Retry-After": "2.5"}, max_seconds=300.0
        )
        assert result == 2.5

    def test_parse_retry_after_caps_at_max(self, sdk_client):
        """Test that Retry-After is capped at max_seconds."""
        result = sdk_client._parse_retry_after_from_headers(
            {"Retry-After": "1000"}, max_seconds=300.0
        )
        assert result == 300.0

    def test_parse_retry_after_none_headers(self, sdk_client):
        """Test parsing with None headers."""
        result = sdk_client._parse_retry_after_from_headers(None, max_seconds=300.0)
        assert result is None

    def test_parse_retry_after_empty_headers(self, sdk_client):
        """Test parsing with empty headers dict."""
        result = sdk_client._parse_retry_after_from_headers({}, max_seconds=300.0)
        assert result is None

    def test_parse_retry_after_missing_header(self, sdk_client):
        """Test parsing when Retry-After header is not present."""
        result = sdk_client._parse_retry_after_from_headers(
            {"Content-Type": "application/json"}, max_seconds=300.0
        )
        assert result is None
