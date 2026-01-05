import pytest

from satvu.http.errors import (
    ClientError,
    ConnectionTimeoutError,
    HttpError,
    HttpStatusError,
    JsonDecodeError,
    NetworkError,
    ProxyError,
    ReadTimeoutError,
    RequestValidationError,
    ServerError,
    SSLError,
    TextDecodeError,
)


class TestNetworkError:
    """Tests for NetworkError."""

    def test_construction_minimal(self):
        """NetworkError can be constructed with just a message."""
        err = NetworkError("Connection refused")
        assert err.message == "Connection refused"
        assert err.url is None
        assert err.original_error is None

    def test_construction_full(self):
        """NetworkError can include URL and original error."""
        original = OSError("Connection refused")
        err = NetworkError(
            "Failed to connect",
            url="https://api.example.com",
            original_error=original,
        )
        assert err.message == "Failed to connect"
        assert err.url == "https://api.example.com"
        assert err.original_error is original

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert NetworkError("test").error_type() == "NetworkError"

    def test_str_without_context(self):
        """String representation without context."""
        err = NetworkError("Connection refused")
        assert str(err) == "NetworkError: Connection refused"

    def test_str_with_context(self):
        """String representation includes context."""
        err = NetworkError("Failed", url="https://example.com")
        assert "url=https://example.com" in str(err)

    def test_repr(self):
        """repr shows class name and details."""
        err = NetworkError("test", url="https://example.com")
        assert "NetworkError" in repr(err)
        assert "test" in repr(err)


class TestConnectionTimeoutError:
    """Tests for ConnectionTimeoutError."""

    def test_construction(self):
        """ConnectionTimeoutError can be constructed with timeout value."""
        err = ConnectionTimeoutError(
            "Connection timed out",
            url="https://api.example.com",
            timeout=30.0,
        )
        assert err.message == "Connection timed out"
        assert err.url == "https://api.example.com"
        assert err.timeout == 30.0

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert ConnectionTimeoutError("test").error_type() == "ConnectionTimeoutError"

    def test_context_includes_timeout(self):
        """Context includes timeout value."""
        err = ConnectionTimeoutError("test", timeout=5.0)
        assert err.context.get("timeout") == 5.0


class TestReadTimeoutError:
    """Tests for ReadTimeoutError."""

    def test_construction(self):
        """ReadTimeoutError can be constructed with timeout value."""
        err = ReadTimeoutError(
            "Read timed out",
            url="https://api.example.com",
            timeout=60.0,
        )
        assert err.timeout == 60.0

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert ReadTimeoutError("test").error_type() == "ReadTimeoutError"


class TestSSLError:
    """Tests for SSLError."""

    def test_construction(self):
        """SSLError can be constructed."""
        err = SSLError(
            "Certificate verification failed",
            url="https://api.example.com",
        )
        assert err.message == "Certificate verification failed"
        assert err.url == "https://api.example.com"

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert SSLError("test").error_type() == "SSLError"


class TestProxyError:
    """Tests for ProxyError."""

    def test_construction(self):
        """ProxyError can include proxy URL."""
        err = ProxyError(
            "Proxy authentication failed",
            url="https://api.example.com",
            proxy="http://proxy.example.com:8080",
        )
        assert err.proxy == "http://proxy.example.com:8080"

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert ProxyError("test").error_type() == "ProxyError"

    def test_context_includes_proxy(self):
        """Context includes proxy URL."""
        err = ProxyError("test", proxy="http://proxy:8080")
        assert err.context.get("proxy") == "http://proxy:8080"


class TestHttpStatusError:
    """Tests for HttpStatusError base class."""

    def test_construction(self):
        """HttpStatusError stores response details."""
        err = HttpStatusError(
            "Bad Request",
            status_code=400,
            url="https://api.example.com/endpoint",
            response_body=b'{"error": "invalid"}',
            response_headers={"Content-Type": "application/json"},
        )
        assert err.status_code == 400
        assert err.url == "https://api.example.com/endpoint"
        assert err.response_body == b'{"error": "invalid"}'
        assert err.response_headers == {"Content-Type": "application/json"}

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert HttpStatusError("test", 400).error_type() == "HttpStatusError"

    def test_context_includes_status_code(self):
        """Context includes status code."""
        err = HttpStatusError("test", 500)
        assert err.context.get("status_code") == 500


class TestClientError:
    """Tests for ClientError (4xx errors)."""

    def test_construction_400(self):
        """ClientError accepts 400 status."""
        err = ClientError("Bad Request", 400)
        assert err.status_code == 400

    def test_construction_404(self):
        """ClientError accepts 404 status."""
        err = ClientError("Not Found", 404)
        assert err.status_code == 404

    def test_construction_499(self):
        """ClientError accepts 499 status."""
        err = ClientError("Client Error", 499)
        assert err.status_code == 499

    def test_rejects_non_4xx(self):
        """ClientError rejects non-4xx status codes."""
        with pytest.raises(ValueError, match="4xx status code"):
            ClientError("Server Error", 500)

        with pytest.raises(ValueError, match="4xx status code"):
            ClientError("OK", 200)

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert ClientError("test", 400).error_type() == "ClientError"

    def test_inheritance(self):
        """ClientError inherits from HttpStatusError and HttpError."""
        err = ClientError("test", 400)
        assert isinstance(err, HttpStatusError)
        assert isinstance(err, HttpError)


class TestServerError:
    """Tests for ServerError (5xx errors)."""

    def test_construction_500(self):
        """ServerError accepts 500 status."""
        err = ServerError("Internal Server Error", 500)
        assert err.status_code == 500

    def test_construction_503(self):
        """ServerError accepts 503 status."""
        err = ServerError("Service Unavailable", 503)
        assert err.status_code == 503

    def test_construction_599(self):
        """ServerError accepts 599 status."""
        err = ServerError("Server Error", 599)
        assert err.status_code == 599

    def test_rejects_non_5xx(self):
        """ServerError rejects non-5xx status codes."""
        with pytest.raises(ValueError, match="5xx status code"):
            ServerError("Client Error", 400)

        with pytest.raises(ValueError, match="5xx status code"):
            ServerError("OK", 200)

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert ServerError("test", 500).error_type() == "ServerError"


class TestJsonDecodeError:
    """Tests for JsonDecodeError."""

    def test_construction_minimal(self):
        """JsonDecodeError can be constructed with just message."""
        err = JsonDecodeError("Invalid JSON")
        assert err.message == "Invalid JSON"
        assert err.body is None

    def test_construction_with_body(self):
        """JsonDecodeError can include the response body."""
        err = JsonDecodeError("Invalid JSON", body="not json at all")
        assert err.body == "not json at all"

    def test_body_truncation_in_context(self):
        """Long bodies are truncated in context."""
        long_body = "x" * 300
        err = JsonDecodeError("Invalid", body=long_body)
        preview = err.context.get("body_preview", "")
        assert len(preview) < len(long_body)
        assert preview.endswith("...")

    def test_short_body_not_truncated(self):
        """Short bodies are not truncated."""
        short_body = "short"
        err = JsonDecodeError("Invalid", body=short_body)
        assert err.context.get("body_preview") == short_body

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert JsonDecodeError("test").error_type() == "JsonDecodeError"

    def test_original_error_preserved(self):
        """Original JSON parsing error can be preserved."""
        original = ValueError("Expecting value")
        err = JsonDecodeError("Invalid JSON", original_error=original)
        assert err.original_error is original
        assert "ValueError" in err.context.get("original_type", "")


class TestTextDecodeError:
    """Tests for TextDecodeError."""

    def test_construction(self):
        """TextDecodeError can include encoding info."""
        err = TextDecodeError("Failed to decode", encoding="utf-8")
        assert err.encoding == "utf-8"

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert TextDecodeError("test").error_type() == "TextDecodeError"


class TestRequestValidationError:
    """Tests for RequestValidationError."""

    def test_construction(self):
        """RequestValidationError can include parameter info."""
        err = RequestValidationError(
            "Invalid parameter",
            parameter="limit",
            value=-1,
        )
        assert err.parameter == "limit"
        assert err.value == -1

    def test_error_type(self):
        """error_type() returns correct identifier."""
        assert RequestValidationError("test").error_type() == "RequestValidationError"

    def test_context_includes_parameter(self):
        """Context includes parameter name and value."""
        err = RequestValidationError("Invalid", parameter="page", value="abc")
        assert err.context.get("parameter") == "page"
        assert err.context.get("value") == "abc"


class TestErrorHierarchy:
    """Tests for error class hierarchy."""

    def test_all_errors_inherit_from_http_error(self):
        """All error types inherit from HttpError."""
        errors = [
            NetworkError("test"),
            ConnectionTimeoutError("test"),
            ReadTimeoutError("test"),
            SSLError("test"),
            ProxyError("test"),
            ClientError("test", 400),
            ServerError("test", 500),
            JsonDecodeError("test"),
            TextDecodeError("test"),
            RequestValidationError("test"),
        ]
        for err in errors:
            assert isinstance(err, HttpError)

    def test_status_errors_inherit_from_http_status_error(self):
        """Status errors inherit from HttpStatusError."""
        assert isinstance(ClientError("test", 400), HttpStatusError)
        assert isinstance(ServerError("test", 500), HttpStatusError)

    def test_errors_are_exceptions(self):
        """All error types can be raised as exceptions."""
        errors = [
            NetworkError("network"),
            ClientError("client", 400),
            ServerError("server", 500),
            JsonDecodeError("json"),
        ]
        for err in errors:
            with pytest.raises(HttpError):
                raise err


class TestOriginalErrorTracking:
    """Tests for original error preservation."""

    def test_network_error_tracks_original(self):
        """NetworkError preserves original exception."""
        original = OSError("Connection refused")
        err = NetworkError("Failed", original_error=original)
        assert err.original_error is original
        assert "OSError" in str(err)

    def test_timeout_error_tracks_original(self):
        """Timeout errors preserve original exception."""
        original = TimeoutError("timed out")
        err = ConnectionTimeoutError("Failed", original_error=original)
        assert err.original_error is original

    def test_ssl_error_tracks_original(self):
        """SSLError preserves original exception."""
        original = Exception("certificate verify failed")
        err = SSLError("SSL failed", original_error=original)
        assert err.original_error is original
