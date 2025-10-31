"""Tests for AuthService."""
# pragma: allowlist secret

from base64 import b64encode
from json import dumps

import pook
import pytest
from freezegun import freeze_time

from satvu_api_sdk.auth import AuthError, AuthService, MemoryCache
from satvu_api_sdk.http import create_http_client
from satvu_api_sdk.result import is_err, is_ok

# Fixed timestamp for consistent testing
FIXED_TIMESTAMP = 1640000000  # 2021-12-20 12:13:20 UTC


def create_mock_jwt_token(
    exp_seconds_from_now: int = 3600, base_time: int = FIXED_TIMESTAMP
) -> str:
    """Create a mock JWT token with specified expiration."""
    # JWT structure: header.payload.signature
    header = (
        b64encode(dumps({"alg": "RS256", "typ": "JWT"}).encode()).decode().rstrip("=")
    )

    payload = {
        "exp": base_time + exp_seconds_from_now,
        "iat": base_time,
        "aud": "https://api.satellitevu.com/",
        "scope": "read:data write:data",
    }
    payload_b64 = b64encode(dumps(payload).encode()).decode().rstrip("=")

    # Mock signature
    signature = "mock_signature"

    return f"{header}.{payload_b64}.{signature}"


@pytest.fixture
def auth_service():
    """Create an AuthService instance for testing."""
    cache = MemoryCache()
    return AuthService(env=None, token_cache=cache)


@pytest.fixture
def auth_service_with_custom_client():
    """Create an AuthService with a custom HTTP client."""
    cache = MemoryCache()
    http_client = create_http_client("stdlib", base_url="https://auth.satellitevu.com")
    return AuthService(env=None, token_cache=cache, http_client=http_client)


@freeze_time("2021-12-20 12:13:20")
@pook.on
def test_successful_token_acquisition(auth_service):
    """Test successful OAuth token acquisition."""
    access_token = create_mock_jwt_token()
    refresh_token = create_mock_jwt_token(exp_seconds_from_now=7200)

    pook.post("https://auth.satellitevu.com/oauth/token").reply(200).json(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    result = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
        scopes=["read:data", "write:data"],
    )

    assert is_ok(result)
    token = result.unwrap()
    assert token == access_token
    assert not auth_service.is_expired_token(token)


@freeze_time("2021-12-20 12:13:20")
@pook.on
def test_token_caching(auth_service):
    """Test that tokens are cached and reused."""
    access_token = create_mock_jwt_token()
    refresh_token = create_mock_jwt_token(exp_seconds_from_now=7200)

    # Mock should only be called once
    pook.post("https://auth.satellitevu.com/oauth/token").times(1).reply(200).json(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    # First call - should hit the API
    result1 = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
        scopes=["read:data"],
    )

    # Second call - should use cached token
    result2 = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
        scopes=["read:data"],
    )

    assert is_ok(result1)
    assert is_ok(result2)
    token1 = result1.unwrap()
    token2 = result2.unwrap()
    assert token1 == token2
    assert token1 == access_token


@freeze_time("2021-12-20 12:13:20")
@pook.on
def test_expired_token_refresh(auth_service):
    """Test that expired tokens are refreshed."""
    # Create an expired token
    expired_token = create_mock_jwt_token(exp_seconds_from_now=-100)
    fresh_token = create_mock_jwt_token(exp_seconds_from_now=3600)
    refresh_token = create_mock_jwt_token(exp_seconds_from_now=7200)

    # First response with expired token
    pook.post("https://auth.satellitevu.com/oauth/token").times(1).reply(200).json(
        {
            "access_token": expired_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    # Get the expired token
    result1 = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
    )

    assert is_ok(result1)
    token1 = result1.unwrap()
    assert auth_service.is_expired_token(token1)

    # Second response with fresh token
    pook.post("https://auth.satellitevu.com/oauth/token").times(1).reply(200).json(
        {
            "access_token": fresh_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    # Should fetch a new token because the cached one is expired
    result2 = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
    )

    assert is_ok(result2)
    token2 = result2.unwrap()
    assert token2 == fresh_token
    assert not auth_service.is_expired_token(token2)


@pook.on
def test_auth_error_non_200_response(auth_service):
    """Test that non-200 responses return AuthError."""
    pook.post("https://auth.satellitevu.com/oauth/token").reply(401).json(
        {
            "error": "invalid_client",
            "error_description": "Client authentication failed",
        }
    )

    result = auth_service.token(
        client_id="invalid_client",
        client_secret="invalid_secret",  # pragma: allowlist secret
    )

    assert is_err(result)
    error = result.error()
    assert isinstance(error, AuthError)
    assert "Auth request failed with status 401" in str(error)


@pook.on
def test_auth_error_invalid_json_response(auth_service):
    """Test that invalid JSON responses return AuthError."""
    # Return 200 but with invalid JSON - this should raise when we try to parse it
    pook.post("https://auth.satellitevu.com/oauth/token").reply(200).type(
        "text/plain"
    ).body("not valid json content")

    result = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
    )

    assert is_err(result)
    error = result.error()
    assert isinstance(error, AuthError)
    assert "Unexpected response body" in str(error)


@freeze_time("2021-12-20 12:13:20")
@pook.on
def test_auth_with_custom_http_client(auth_service_with_custom_client):
    """Test authentication with a custom HTTP client."""
    access_token = create_mock_jwt_token()
    refresh_token = create_mock_jwt_token(exp_seconds_from_now=7200)

    pook.post("https://auth.satellitevu.com/oauth/token").reply(200).json(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    result = auth_service_with_custom_client.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
    )

    assert is_ok(result)
    token = result.unwrap()
    assert token == access_token


@freeze_time("2021-12-20 12:13:20")
@pook.on
def test_different_scopes_use_different_cache_keys(auth_service):
    """Test that different scopes result in different cache keys."""

    # Create tokens with different payloads to make them truly different
    def create_token_with_scope(exp_offset, scope_value):
        header = (
            b64encode(dumps({"alg": "RS256", "typ": "JWT"}).encode())
            .decode()
            .rstrip("=")
        )
        payload = {
            "exp": FIXED_TIMESTAMP + exp_offset,
            "iat": FIXED_TIMESTAMP,
            "aud": "https://api.satellitevu.com/",
            "scope": scope_value,  # Different scope in payload
        }
        payload_b64 = b64encode(dumps(payload).encode()).decode().rstrip("=")
        return f"{header}.{payload_b64}.mock_signature_{scope_value}"

    token1_access = create_token_with_scope(3600, "read")
    token2_access = create_token_with_scope(3600, "write")
    refresh_token = create_mock_jwt_token(exp_seconds_from_now=14400)

    # Setup mocks for both requests upfront
    pook.post("https://auth.satellitevu.com/oauth/token").reply(200).json(
        {
            "access_token": token1_access,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    result1 = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
        scopes=["read:data"],
    )

    # Setup second mock
    pook.post("https://auth.satellitevu.com/oauth/token").reply(200).json(
        {
            "access_token": token2_access,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    result2 = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
        scopes=["write:data"],
    )

    # Main test: different scopes should produce different tokens
    assert is_ok(result1)
    assert is_ok(result2)
    token1 = result1.unwrap()
    token2 = result2.unwrap()
    assert token1 != token2


@freeze_time("2021-12-20 12:13:20")
def test_is_expired_token():
    """Test token expiration checking."""
    # Create expired and valid tokens
    expired = create_mock_jwt_token(exp_seconds_from_now=-100)
    valid = create_mock_jwt_token(exp_seconds_from_now=3600)

    assert AuthService.is_expired_token(expired)
    assert not AuthService.is_expired_token(valid)


@freeze_time("2021-12-20 12:13:20")
@pook.on
def test_form_encoded_request_format(auth_service):
    """Test that the OAuth request uses correct form-encoded format."""
    access_token = create_mock_jwt_token()
    refresh_token = create_mock_jwt_token(exp_seconds_from_now=7200)

    # Verify the request has correct content-type and data format
    pook.post("https://auth.satellitevu.com/oauth/token").header(
        "content-type", "application/x-www-form-urlencoded"
    ).reply(200).json(
        {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600,
        }
    )

    result = auth_service.token(
        client_id="test_client_id",
        client_secret="test_client_secret",  # pragma: allowlist secret
        scopes=["read:data"],
    )

    # Verify we got a valid token back
    assert is_ok(result)
    token = result.unwrap()
    assert token == access_token
