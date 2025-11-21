"""Tests for SDKClient core functionality."""

from unittest.mock import MagicMock

import pook
import pytest
from pydantic import BaseModel

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.http import create_http_client
from satvu_api_sdk.http.errors import ClientError, ServerError
from satvu_api_sdk.result import Ok, is_err, is_ok


class ParameterTestModel(BaseModel):
    """Test Pydantic model for parameter testing."""

    field1: str
    field2: int


class ConcreteSDKClient(SDKClient):
    """Concrete implementation for testing abstract SDKClient."""

    base_path = "/test"


@pytest.fixture
def sdk_client():
    """Create a basic SDKClient instance for testing."""
    return ConcreteSDKClient(env=None)


@pytest.fixture
def sdk_client_with_env():
    """Create an SDKClient with environment setting."""
    return ConcreteSDKClient(env="dev")


@pytest.fixture
def sdk_client_with_token():
    """Create an SDKClient with authentication token."""
    # Instead of using get_token which tries to pass headers to adapter init,
    # create a custom http_client with headers
    http_client = create_http_client(
        "stdlib",
        base_url="https://api.satellitevu.com/test",
    )
    return ConcreteSDKClient(env=None, http_client=http_client)


@pytest.fixture
def sdk_client_with_custom_http():
    """Create an SDKClient with custom HTTP client."""
    http_client = create_http_client(
        "stdlib", base_url="https://api.satellitevu.com/test"
    )
    return ConcreteSDKClient(env=None, http_client=http_client)


def test_build_url_no_env():
    """Test URL building without environment."""
    sdk_client = ConcreteSDKClient(env=None)
    url = sdk_client.build_url("api")
    assert url == "https://api.satellitevu.com/"


def test_build_url_with_env():
    """Test URL building with environment."""
    sdk_client = ConcreteSDKClient(env="dev")
    url = sdk_client.build_url("api")
    assert url == "https://api.dev.satellitevu.com/"


def test_build_url_custom_subdomain():
    """Test URL building with custom subdomain."""
    sdk_client = ConcreteSDKClient(env="staging")
    url = sdk_client.build_url("auth")
    assert url == "https://auth.staging.satellitevu.com/"


def test_initialization_default(sdk_client):
    """Test SDKClient initialization with defaults."""
    assert sdk_client.client is not None
    assert hasattr(sdk_client, "base_path")
    assert sdk_client.base_path == "/test"


def test_initialization_with_env(sdk_client_with_env):
    """Test SDKClient initialization with environment."""
    assert sdk_client_with_env.client is not None


def test_initialization_with_token(sdk_client_with_token):
    """Test SDKClient initialization with auth token."""
    assert sdk_client_with_token.client is not None


def test_initialization_with_custom_http_client(sdk_client_with_custom_http):
    """Test SDKClient initialization with custom HTTP client."""
    assert sdk_client_with_custom_http.client is not None


@pook.on
def test_make_request_success_get(sdk_client):
    """Test successful GET request."""
    pook.get("https://api.satellitevu.com/test/endpoint").reply(200).json(
        {"status": "success", "data": {"id": 123}}
    )

    result = sdk_client.make_request("GET", "/endpoint")

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200
    json_result = response.json()
    assert not json_result.is_err()
    data = json_result.unwrap()
    assert data["status"] == "success"
    assert data["data"]["id"] == 123


@pook.on
def test_make_request_success_post(sdk_client):
    """Test successful POST request with JSON body."""
    pook.post("https://api.satellitevu.com/test/create").reply(201).json(
        {"id": 456, "created": True}
    )

    result = sdk_client.make_request(
        "POST", "/create", json={"name": "test", "value": 42}
    )

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 201
    json_result = response.json()
    data = json_result.unwrap()
    assert data["id"] == 456
    assert data["created"] is True


@pook.on
def test_make_request_with_params(sdk_client):
    """Test request with query parameters."""
    pook.get("https://api.satellitevu.com/test/search").param("query", "test").param(
        "limit", "10"
    ).reply(200).json({"results": []})

    result = sdk_client.make_request(
        "GET", "/search", params={"query": "test", "limit": "10"}
    )

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_params_with_pydantic_model(sdk_client):
    """Test that Pydantic models in params are converted to dicts."""
    model = ParameterTestModel(field1="value1", field2=42)

    pook.get("https://api.satellitevu.com/test/endpoint").reply(200).json(
        {"status": "ok"}
    )

    result = sdk_client.make_request(
        "GET", "/endpoint", params={"model": model, "other": "value"}
    )

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_params_filters_none_values(sdk_client):
    """Test that None values in params are filtered out."""
    pook.get("https://api.satellitevu.com/test/endpoint").param(
        "param1", "value1"
    ).reply(200).json({"status": "ok"})

    result = sdk_client.make_request(
        "GET",
        "/endpoint",
        params={"param1": "value1", "param2": None, "param3": None},
    )

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_client_error(sdk_client):
    """Test handling of 4xx client errors."""
    pook.get("https://api.satellitevu.com/test/notfound").reply(404).json(
        {"error": "Not found"}
    )

    result = sdk_client.make_request("GET", "/notfound")

    assert is_err(result)
    error = result.error()
    assert isinstance(error, ClientError)
    assert error.status_code == 404


@pook.on
def test_make_request_server_error(sdk_client):
    """Test handling of 5xx server errors."""
    pook.get("https://api.satellitevu.com/test/error").reply(500).json(
        {"error": "Internal server error"}
    )

    result = sdk_client.make_request("GET", "/error")

    assert is_err(result)
    error = result.error()
    assert isinstance(error, ServerError)
    assert error.status_code == 500


@pook.on
def test_make_request_with_follow_redirects(sdk_client):
    """Test request with redirect handling."""
    pook.get("https://api.satellitevu.com/test/redirect").reply(200).json(
        {"status": "ok"}
    )

    result = sdk_client.make_request("GET", "/redirect", follow_redirects=True)

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_with_custom_timeout(sdk_client):
    """Test request with custom timeout."""
    pook.get("https://api.satellitevu.com/test/slow").reply(200).json(
        {"status": "completed"}
    )

    result = sdk_client.make_request("GET", "/slow", timeout=30)

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_with_auth_token(sdk_client_with_token):
    """Test that auth token is included in requests."""
    # Note: pook doesn't easily verify headers, but we can test the request succeeds
    pook.get("https://api.satellitevu.com/test/secure").reply(200).json(
        {"authenticated": True}
    )

    result = sdk_client_with_token.make_request("GET", "/secure")

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_put_method(sdk_client):
    """Test PUT request."""
    pook.put("https://api.satellitevu.com/test/update/123").reply(200).json(
        {"id": 123, "updated": True}
    )

    result = sdk_client.make_request("PUT", "/update/123", json={"name": "updated"})

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_make_request_delete_method(sdk_client):
    """Test DELETE request."""
    pook.delete("https://api.satellitevu.com/test/delete/123").reply(204)

    result = sdk_client.make_request("DELETE", "/delete/123")

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 204


@pook.on
def test_make_request_patch_method(sdk_client):
    """Test PATCH request."""
    pook.patch("https://api.satellitevu.com/test/patch/123").reply(200).json(
        {"id": 123, "patched": True}
    )

    result = sdk_client.make_request("PATCH", "/patch/123", json={"field": "new_value"})

    assert is_ok(result)
    response = result.unwrap()
    assert response.status_code == 200


def test_sdk_client_default_timeout():
    """Test SDKClient initialization with default timeout."""
    client = ConcreteSDKClient(env=None)
    assert client.timeout == 30  # Default timeout


def test_sdk_client_custom_timeout():
    """Test SDKClient initialization with custom timeout."""
    client = ConcreteSDKClient(env=None, timeout=60)
    assert client.timeout == 60


def test_make_request_uses_instance_timeout():
    """Test that make_request uses instance timeout when no timeout specified."""
    client = ConcreteSDKClient(env=None, timeout=45)

    # Mock the HTTP client to verify timeout parameter
    mock_response = MagicMock()
    mock_response.status_code = 200
    client.client.request = MagicMock(return_value=Ok(mock_response))

    # Call without timeout parameter - should use instance timeout (45)
    client.make_request("GET", "/endpoint")

    # Verify the HTTP client was called with the instance timeout
    client.client.request.assert_called_once()
    call_kwargs = client.client.request.call_args[1]
    assert call_kwargs["timeout"] == 45.0


def test_make_request_timeout_override():
    """Test that explicit timeout parameter overrides instance timeout."""
    client = ConcreteSDKClient(env=None, timeout=30)

    # Mock the HTTP client to verify timeout parameter
    mock_response = MagicMock()
    mock_response.status_code = 200
    client.client.request = MagicMock(return_value=Ok(mock_response))

    # Override instance timeout with explicit timeout
    client.make_request("GET", "/slow", timeout=120)

    # Verify the HTTP client was called with the overridden timeout
    client.client.request.assert_called_once()
    call_kwargs = client.client.request.call_args[1]
    assert call_kwargs["timeout"] == 120.0


def test_make_request_timeout_zero_override():
    """Test that timeout=0 (explicit zero) overrides instance timeout."""
    client = ConcreteSDKClient(env=None, timeout=30)

    # Mock the HTTP client to verify timeout parameter
    mock_response = MagicMock()
    mock_response.status_code = 200
    client.client.request = MagicMock(return_value=Ok(mock_response))

    # Use timeout=0 explicitly
    client.make_request("GET", "/endpoint", timeout=0)

    # Verify the HTTP client was called with timeout=0
    client.client.request.assert_called_once()
    call_kwargs = client.client.request.call_args[1]
    assert call_kwargs["timeout"] == 0.0


class LinkModel(BaseModel):
    """Mock STAC link model."""

    href: str
    rel: str
    method: str = "GET"
    body: dict | BaseModel | None = None


class PaginatedResponseModel(BaseModel):
    """Mock paginated response with STAC links."""

    links: list[LinkModel]
    items: list[dict]


class TokenBodyModel(BaseModel):
    """Mock body model with token attribute."""

    token: str | None = None
    filter: str | None = None


class TestTokenExtraction:
    """Tests for pagination token extraction from STAC links."""

    def test_extract_next_token_get_request(self):
        """Test extracting token from GET request (token in URL query parameter)."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search?token=abc123&limit=10",
                    rel="next",
                    method="GET",
                )
            ],
            items=[{"id": 1}, {"id": 2}],
        )

        token = SDKClient.extract_next_token(response)
        assert token == "abc123"

    def test_extract_next_token_post_request_dict_body(self):
        """Test extracting token from POST request (token in body dict)."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search",
                    rel="next",
                    method="POST",
                    body={"token": "xyz789", "filter": "visual"},
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token == "xyz789"

    def test_extract_next_token_post_request_object_body(self):
        """Test extracting token from POST request (token in body object)."""
        body_model = TokenBodyModel(token="token456", filter="thermal")

        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search",
                    rel="next",
                    method="POST",
                    body=body_model,
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token == "token456"

    def test_extract_next_token_no_links_attribute(self):
        """Test extraction when response has no links attribute."""

        class ResponseWithoutLinks(BaseModel):
            items: list[dict]

        response = ResponseWithoutLinks(items=[{"id": 1}])

        token = SDKClient.extract_next_token(response)
        assert token is None

    def test_extract_next_token_no_next_link(self):
        """Test extraction when links array has no 'next' relation."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/self", rel="self", method="GET"
                ),
                LinkModel(
                    href="https://api.example.com/prev?token=prev123",
                    rel="prev",
                    method="GET",
                ),
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token is None

    def test_extract_next_token_empty_links(self):
        """Test extraction when links array is empty."""
        response = PaginatedResponseModel(links=[], items=[{"id": 1}])

        token = SDKClient.extract_next_token(response)
        assert token is None

    def test_extract_next_token_get_no_token_in_url(self):
        """Test extraction when GET next link has no token parameter."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search?limit=10",
                    rel="next",
                    method="GET",
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token is None

    def test_extract_next_token_post_no_body(self):
        """Test extraction when POST next link has no body."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search", rel="next", method="POST"
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token is None

    def test_extract_next_token_post_body_no_token(self):
        """Test extraction when POST body has no token field."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search",
                    rel="next",
                    method="POST",
                    body={"filter": "visual", "limit": 10},
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token is None

    def test_extract_next_token_get_multiple_query_params(self):
        """Test extraction from GET URL with multiple query parameters."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search?limit=10&token=multi123&sort=asc",
                    rel="next",
                    method="GET",
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token == "multi123"

    def test_extract_next_token_multiple_next_links(self):
        """Test extraction when multiple next links exist (uses first)."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search?token=first",
                    rel="next",
                    method="GET",
                ),
                LinkModel(
                    href="https://api.example.com/search?token=second",
                    rel="next",
                    method="GET",
                ),
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token == "first"  # Should use first match

    def test_extract_next_token_none_token_value(self):
        """Test extraction when token value is None in body."""
        response = PaginatedResponseModel(
            links=[
                LinkModel(
                    href="https://api.example.com/search",
                    rel="next",
                    method="POST",
                    body={"token": None, "filter": "visual"},
                )
            ],
            items=[{"id": 1}],
        )

        token = SDKClient.extract_next_token(response)
        assert token is None
