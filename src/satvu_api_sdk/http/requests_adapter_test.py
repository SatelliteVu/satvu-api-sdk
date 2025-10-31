"""Tests for RequestsAdapter."""

import pook
import pytest
import requests

from satvu_api_sdk.http import is_ok
from satvu_api_sdk.http.requests_adapter import RequestsAdapter


@pytest.fixture
def adapter():
    """Create a RequestsAdapter instance for testing."""
    return RequestsAdapter(base_url="https://api.example.com")


@pook.on
def test_get_request(adapter):
    """Test basic GET request."""
    pook.get("https://api.example.com/users").reply(200).json(
        {"users": ["alice", "bob"]}
    )

    result = adapter.request("GET", "/users")

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 200
    json_result = response.json()

    assert is_ok(json_result), f"Expected Ok but got: {json_result}"

    assert json_result.unwrap() == {"users": ["alice", "bob"]}


@pook.on
def test_post_request_with_json(adapter):
    """Test POST request with JSON body."""
    pook.post("https://api.example.com/users").reply(201).json(
        {"id": 123, "name": "charlie"}
    )

    result = adapter.request("POST", "/users", json={"name": "charlie"})

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 201
    json_result = response.json()

    assert is_ok(json_result), f"Expected Ok but got: {json_result}"

    assert json_result.unwrap() == {"id": 123, "name": "charlie"}


@pook.on
def test_request_with_query_params(adapter):
    """Test request with query parameters."""
    pook.get("https://api.example.com/users?limit=10&offset=20").reply(200).json(
        {"count": 2}
    )

    result = adapter.request("GET", "/users", params={"limit": 10, "offset": 20})

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 200
    json_result = response.json()

    assert is_ok(json_result), f"Expected Ok but got: {json_result}"

    assert json_result.unwrap() == {"count": 2}


@pook.on
def test_request_with_none_params(adapter):
    """Test that None params are filtered out."""
    pook.get("https://api.example.com/users?limit=10").reply(200).json({})

    result = adapter.request("GET", "/users", params={"limit": 10, "offset": None})

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 200


@pook.on
def test_request_with_headers(adapter):
    """Test request with custom headers."""
    pook.get("https://api.example.com/users").header(
        "Authorization", "Bearer token123"
    ).reply(200).json({})

    result = adapter.request(
        "GET", "/users", headers={"Authorization": "Bearer token123"}
    )

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 200
    assert pook.isdone()


@pook.on
def test_request_with_form_data(adapter):
    """Test request with form-encoded data."""
    pook.post("https://api.example.com/login").reply(200).json({"token": "abc123"})

    result = adapter.request(
        "POST",
        "/login",
        data={"username": "user", "password": "pass"},  # pragma: allowlist secret
    )

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 200
    json_result = response.json()

    assert is_ok(json_result), f"Expected Ok but got: {json_result}"

    assert json_result.unwrap() == {"token": "abc123"}


@pook.on
def test_response_text_property(adapter):
    """Test response text property."""
    pook.get("https://api.example.com/hello").reply(200).body("Hello, World!")

    result = adapter.request("GET", "/hello")

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    text_result = response.text

    assert is_ok(text_result), f"Expected Ok but got: {text_result}"

    assert text_result.unwrap() == "Hello, World!"


@pook.on
def test_response_body_property(adapter):
    """Test response body property."""
    pook.get("https://api.example.com/data").reply(200).body(b"binary data")

    result = adapter.request("GET", "/data")

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.body == b"binary data"


@pook.on
def test_response_headers(adapter):
    """Test response headers."""
    pook.get("https://api.example.com/test").reply(200).header(
        "X-Custom", "value"
    ).body("test")

    result = adapter.request("GET", "/test")

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()

    assert "X-Custom" in response.headers or "x-custom" in response.headers


@pook.on
def test_http_error_response(adapter):
    """Test handling of HTTP error responses."""
    pook.get("https://api.example.com/notfound").reply(404).json({"error": "Not found"})

    result = adapter.request("GET", "/notfound")

    # 404 should now return Err(ClientError)
    assert result.is_err(), f"Expected Err but got: {result}"
    error = result.error()
    assert error.status_code == 404
    # Can still access response body from error
    assert error.response_body is not None


@pook.on
def test_follow_redirects_false(adapter):
    """Test that follow_redirects=False is respected."""
    pook.get("https://api.example.com/redirect").reply(302).header(
        "Location", "https://api.example.com/target"
    )

    result = adapter.request("GET", "/redirect", follow_redirects=False)

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 302


@pook.on
def test_follow_redirects_true(adapter):
    """Test that follow_redirects=True follows redirects."""
    pook.get("https://api.example.com/redirect").reply(302).header(
        "Location", "https://api.example.com/target"
    )
    pook.get("https://api.example.com/target").reply(200).json({"final": "destination"})

    result = adapter.request("GET", "/redirect", follow_redirects=True)

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()
    assert response.status_code == 200
    json_result = response.json()

    assert is_ok(json_result), f"Expected Ok but got: {json_result}"

    assert json_result.unwrap() == {"final": "destination"}


@pook.on
def test_absolute_url_ignores_base_url():
    """Test that absolute URLs ignore the base_url."""
    adapter = RequestsAdapter(base_url="https://api.example.com")

    pook.get("https://other-api.example.com/data").reply(200).json({"ok": True})

    result = adapter.request("GET", "https://other-api.example.com/data")

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()

    assert response.status_code == 200


def test_custom_session():
    """Test using a custom requests.Session instance."""
    custom_session = requests.Session()
    custom_session.headers.update({"X-Custom": "header"})

    adapter = RequestsAdapter(
        base_url="https://custom.example.com", session=custom_session
    )

    pook.activate()
    pook.get("https://custom.example.com/test").header("X-Custom", "header").reply(
        200
    ).json({"ok": True})

    result = adapter.request("GET", "/test")

    assert is_ok(result), f"Expected Ok but got: {result}"

    response = result.unwrap()

    assert response.status_code == 200

    json_result = response.json()

    assert is_ok(json_result), f"Expected Ok but got: {json_result}"

    assert json_result.unwrap() == {"ok": True}
    assert adapter._owns_session is False
    pook.off()


def test_adapter_cleanup():
    """Test that adapter closes session when it owns it."""
    adapter = RequestsAdapter(base_url="https://api.example.com")

    # Manually trigger cleanup
    assert adapter._owns_session is True
    adapter.__del__()

    # Session should be closed (attempting to use it will raise an error)
    # Note: requests doesn't actually prevent usage after close, but we test ownership
    assert adapter._owns_session is True
