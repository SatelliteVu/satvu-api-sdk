"""Tests for StdlibAdapter."""

import warnings

import pook
import pytest

from satvu_api_sdk.http.stdlib_adapter import StdlibAdapter


@pytest.fixture
def adapter():
    """Create a StdlibAdapter instance for testing."""
    return StdlibAdapter(base_url="https://api.example.com")


@pook.on
def test_get_request(adapter):
    """Test basic GET request."""
    pook.get("https://api.example.com/users").reply(200).json(
        {"users": ["alice", "bob"]}
    )

    response = adapter.request("GET", "/users", follow_redirects=True)

    assert response.status_code == 200
    assert response.json() == {"users": ["alice", "bob"]}


@pook.on
def test_post_request_with_json(adapter):
    """Test POST request with JSON body."""
    pook.post("https://api.example.com/users").reply(201).json(
        {"id": 123, "name": "charlie"}
    )

    response = adapter.request(
        "POST", "/users", json={"name": "charlie"}, follow_redirects=True
    )

    assert response.status_code == 201
    assert response.json() == {"id": 123, "name": "charlie"}


@pook.on
def test_request_with_query_params(adapter):
    """Test request with query parameters."""
    pook.get("https://api.example.com/users?limit=10&offset=20").reply(200).json(
        {"count": 2}
    )

    response = adapter.request(
        "GET", "/users", params={"limit": 10, "offset": 20}, follow_redirects=True
    )

    assert response.status_code == 200
    assert response.json() == {"count": 2}


@pook.on
def test_request_with_none_params(adapter):
    """Test that None params are filtered out."""
    pook.get("https://api.example.com/users?limit=10").reply(200).json({})

    response = adapter.request(
        "GET", "/users", params={"limit": 10, "offset": None}, follow_redirects=True
    )

    assert response.status_code == 200


@pook.on
def test_request_with_headers(adapter):
    """Test request with custom headers."""
    pook.get("https://api.example.com/users").header(
        "Authorization", "Bearer token123"
    ).reply(200).json({})

    response = adapter.request(
        "GET",
        "/users",
        headers={"Authorization": "Bearer token123"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert pook.isdone()  # Verify all mocks were matched


@pook.on
def test_request_with_form_data(adapter):
    """Test request with form-encoded data."""
    pook.post("https://api.example.com/login").reply(200).json({"token": "abc123"})

    response = adapter.request(
        "POST",
        "/login",
        data={"username": "user", "password": "pass"},  # pragma: allowlist secret
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert response.json() == {"token": "abc123"}


@pook.on
def test_response_text_property(adapter):
    """Test response text property."""
    pook.get("https://api.example.com/hello").reply(200).body("Hello, World!")

    response = adapter.request("GET", "/hello", follow_redirects=True)

    assert response.text == "Hello, World!"


@pook.on
def test_response_body_property(adapter):
    """Test response body property."""
    pook.get("https://api.example.com/data").reply(200).body(b"binary data")

    response = adapter.request("GET", "/data", follow_redirects=True)

    assert response.body == b"binary data"


@pook.on
def test_response_headers(adapter):
    """Test response headers."""
    pook.get("https://api.example.com/test").reply(200).header(
        "X-Custom", "value"
    ).body("test")

    response = adapter.request("GET", "/test", follow_redirects=True)

    assert "X-Custom" in response.headers or "x-custom" in response.headers


@pook.on
def test_http_error_response(adapter):
    """Test handling of HTTP error responses."""
    pook.get("https://api.example.com/notfound").reply(404).json({"error": "Not found"})

    response = adapter.request("GET", "/notfound", follow_redirects=True)

    assert response.status_code == 404
    assert response.json() == {"error": "Not found"}


@pook.on
def test_follow_redirects_warning(adapter):
    """Test that warning is emitted when follow_redirects=False."""
    pook.get("https://api.example.com/test").reply(200).body("ok")

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        adapter.request("GET", "/test", follow_redirects=False)

        assert len(w) == 1
        assert "follow_redirects=False" in str(w[0].message)
        assert issubclass(w[0].category, UserWarning)


@pook.on
def test_absolute_url_ignores_base_url():
    """Test that absolute URLs ignore the base_url."""
    adapter = StdlibAdapter(base_url="https://api.example.com")

    pook.get("https://other-api.example.com/data").reply(200).json({"ok": True})

    response = adapter.request(
        "GET", "https://other-api.example.com/data", follow_redirects=True
    )

    assert response.status_code == 200
