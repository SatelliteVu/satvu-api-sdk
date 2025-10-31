"""Tests for Urllib3Adapter."""

import pook
import pytest
import urllib3

from satvu_api_sdk.http.urllib3_adapter import Urllib3Adapter


@pytest.fixture
def adapter():
    """Create a Urllib3Adapter instance for testing."""
    return Urllib3Adapter(base_url="https://api.example.com")


@pook.on
def test_get_request(adapter):
    """Test basic GET request."""
    pook.get("https://api.example.com/users").reply(200).json(
        {"users": ["alice", "bob"]}
    )

    response = adapter.request("GET", "/users")

    assert response.status_code == 200
    assert response.json() == {"users": ["alice", "bob"]}


@pook.on
def test_post_request_with_json(adapter):
    """Test POST request with JSON body."""
    pook.post("https://api.example.com/users").reply(201).json(
        {"id": 123, "name": "charlie"}
    )

    response = adapter.request("POST", "/users", json={"name": "charlie"})

    assert response.status_code == 201
    assert response.json() == {"id": 123, "name": "charlie"}


@pook.on
def test_request_with_query_params(adapter):
    """Test request with query parameters."""
    pook.get("https://api.example.com/users?limit=10&offset=20").reply(200).json(
        {"count": 2}
    )

    response = adapter.request("GET", "/users", params={"limit": 10, "offset": 20})

    assert response.status_code == 200
    assert response.json() == {"count": 2}


@pook.on
def test_request_with_none_params(adapter):
    """Test that None params are filtered out."""
    pook.get("https://api.example.com/users?limit=10").reply(200).json({})

    response = adapter.request("GET", "/users", params={"limit": 10, "offset": None})

    assert response.status_code == 200


@pook.on
def test_request_with_headers(adapter):
    """Test request with custom headers."""
    pook.get("https://api.example.com/users").header(
        "Authorization", "Bearer token123"
    ).reply(200).json({})

    response = adapter.request(
        "GET", "/users", headers={"Authorization": "Bearer token123"}
    )

    assert response.status_code == 200
    assert pook.isdone()


@pook.on
def test_request_with_form_data(adapter):
    """Test request with form-encoded data."""
    pook.post("https://api.example.com/login").reply(200).json({"token": "abc123"})

    response = adapter.request(
        "POST",
        "/login",
        data={"username": "user", "password": "pass"},  # pragma: allowlist secret
    )

    assert response.status_code == 200
    assert response.json() == {"token": "abc123"}


@pook.on
def test_response_text_property(adapter):
    """Test response text property."""
    pook.get("https://api.example.com/hello").reply(200).body("Hello, World!")

    response = adapter.request("GET", "/hello")

    assert response.text == "Hello, World!"


@pook.on
def test_response_body_property(adapter):
    """Test response body property."""
    pook.get("https://api.example.com/data").reply(200).body(b"binary data")

    response = adapter.request("GET", "/data")

    assert response.body == b"binary data"


@pook.on
def test_response_headers(adapter):
    """Test response headers."""
    pook.get("https://api.example.com/test").reply(200).header("X-Custom", "value").body(
        "test"
    )

    response = adapter.request("GET", "/test")

    assert "X-Custom" in response.headers or "x-custom" in response.headers


@pook.on
def test_http_error_response(adapter):
    """Test handling of HTTP error responses."""
    pook.get("https://api.example.com/notfound").reply(404).json({"error": "Not found"})

    response = adapter.request("GET", "/notfound")

    assert response.status_code == 404
    assert response.json() == {"error": "Not found"}


@pook.on
def test_follow_redirects_false(adapter):
    """Test that follow_redirects=False is respected."""
    pook.get("https://api.example.com/redirect").reply(302).header(
        "Location", "https://api.example.com/target"
    )

    response = adapter.request("GET", "/redirect", follow_redirects=False)

    assert response.status_code == 302


@pook.on
def test_follow_redirects_true(adapter):
    """Test that follow_redirects=True follows redirects."""
    pook.get("https://api.example.com/redirect").reply(302).header(
        "Location", "https://api.example.com/target"
    )
    pook.get("https://api.example.com/target").reply(200).json({"final": "destination"})

    response = adapter.request("GET", "/redirect", follow_redirects=True)

    assert response.status_code == 200
    assert response.json() == {"final": "destination"}


@pook.on
def test_absolute_url_ignores_base_url():
    """Test that absolute URLs ignore the base_url."""
    adapter = Urllib3Adapter(base_url="https://api.example.com")

    pook.get("https://other-api.example.com/data").reply(200).json({"ok": True})

    response = adapter.request("GET", "https://other-api.example.com/data")

    assert response.status_code == 200


def test_custom_pool_manager():
    """Test using a custom urllib3.PoolManager instance."""
    custom_pool = urllib3.PoolManager(
        timeout=urllib3.Timeout(connect=5.0, read=10.0), maxsize=20
    )

    adapter = Urllib3Adapter(
        base_url="https://custom.example.com", pool_manager=custom_pool
    )

    pook.activate()
    pook.get("https://custom.example.com/test").reply(200).json({"ok": True})

    response = adapter.request("GET", "/test")

    assert response.status_code == 200
    assert response.json() == {"ok": True}
    assert adapter._owns_pool is False
    pook.off()


def test_adapter_cleanup():
    """Test that adapter clears pool when it owns it."""
    adapter = Urllib3Adapter(base_url="https://api.example.com")

    # Manually trigger cleanup
    assert adapter._owns_pool is True
    pool = adapter.pool_manager
    adapter.__del__()

    # Pool should be cleared (pool.pools will be empty)
    assert len(pool.pools) == 0
