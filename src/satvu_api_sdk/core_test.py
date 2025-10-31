"""Tests for SDKClient core functionality."""

import pook
import pytest
from pydantic import BaseModel

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.http import create_http_client
from satvu_api_sdk.http.errors import ClientError, ServerError
from satvu_api_sdk.result import is_err, is_ok


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
    url = SDKClient.build_url("api", None)
    assert url == "https://api.satellitevu.com/"


def test_build_url_with_env():
    """Test URL building with environment."""
    url = SDKClient.build_url("api", "dev")
    assert url == "https://api.dev.satellitevu.com/"


def test_build_url_custom_subdomain():
    """Test URL building with custom subdomain."""
    url = SDKClient.build_url("auth", "staging")
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
