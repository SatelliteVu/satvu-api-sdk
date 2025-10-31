"""
HTTP error types for type-safe error handling.

This module defines a detailed hierarchy of HTTP-related errors that can occur
during request execution, from network issues to parsing failures.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional


class HttpError(Exception, ABC):
    """Base class for all HTTP-related errors."""

    def __init__(self, message: str, context: Optional[dict[str, Any]] = None) -> None:
        """
        Initialize an HTTP error.

        Args:
            message: Human-readable error message
            context: Additional context information
        """
        super().__init__(message)
        self.message = message
        self.context = context or {}

    @abstractmethod
    def error_type(self) -> str:
        """Get the error type identifier."""
        ...

    def __str__(self) -> str:
        if self.context:
            context_str = ", ".join(f"{k}={v}" for k, v in self.context.items())
            return f"{self.error_type()}: {self.message} ({context_str})"
        return f"{self.error_type()}: {self.message}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.message!r}, context={self.context!r})"


# ============================================================================
# Transport Errors - Network, connection, and protocol-level errors
# ============================================================================


class NetworkError(HttpError):
    """
    Network-level error occurred during request.

    This includes connection refused, host unreachable, DNS resolution failures,
    and other network-layer issues.
    """

    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize a network error.

        Args:
            message: Error description
            url: URL that failed
            original_error: Original exception from underlying library
        """
        context = {}
        if url:
            context["url"] = url
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.url = url
        self.original_error = original_error

    def error_type(self) -> str:
        return "NetworkError"


class ConnectionTimeoutError(HttpError):
    """
    Timeout occurred while establishing connection.

    This indicates the TCP connection could not be established within
    the specified timeout period.
    """

    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        timeout: Optional[float] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize a connection timeout error.

        Args:
            message: Error description
            url: URL that timed out
            timeout: Timeout value in seconds
            original_error: Original exception from underlying library
        """
        context = {}
        if url:
            context["url"] = url
        if timeout is not None:
            context["timeout"] = timeout
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.url = url
        self.timeout = timeout
        self.original_error = original_error

    def error_type(self) -> str:
        return "ConnectionTimeoutError"


class ReadTimeoutError(HttpError):
    """
    Timeout occurred while reading response.

    This indicates the connection was established but the server did not
    send a complete response within the timeout period.
    """

    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        timeout: Optional[float] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize a read timeout error.

        Args:
            message: Error description
            url: URL that timed out
            timeout: Timeout value in seconds
            original_error: Original exception from underlying library
        """
        context = {}
        if url:
            context["url"] = url
        if timeout is not None:
            context["timeout"] = timeout
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.url = url
        self.timeout = timeout
        self.original_error = original_error

    def error_type(self) -> str:
        return "ReadTimeoutError"


class SSLError(HttpError):
    """
    SSL/TLS error occurred during secure connection.

    This includes certificate validation failures, handshake errors,
    and other TLS-related issues.
    """

    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize an SSL error.

        Args:
            message: Error description
            url: URL that failed
            original_error: Original exception from underlying library
        """
        context = {}
        if url:
            context["url"] = url
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.url = url
        self.original_error = original_error

    def error_type(self) -> str:
        return "SSLError"


class ProxyError(HttpError):
    """
    Proxy-related error occurred.

    This includes proxy connection failures, authentication issues,
    and proxy configuration problems.
    """

    def __init__(
        self,
        message: str,
        url: Optional[str] = None,
        proxy: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize a proxy error.

        Args:
            message: Error description
            url: URL that failed
            proxy: Proxy URL
            original_error: Original exception from underlying library
        """
        context = {}
        if url:
            context["url"] = url
        if proxy:
            context["proxy"] = proxy
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.url = url
        self.proxy = proxy
        self.original_error = original_error

    def error_type(self) -> str:
        return "ProxyError"


# ============================================================================
# HTTP Status Errors - 4xx and 5xx response codes
# ============================================================================


class HttpStatusError(HttpError):
    """
    HTTP response with error status code (4xx or 5xx).

    Base class for client and server errors. Includes the response
    object for accessing headers, body, etc.
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        url: Optional[str] = None,
        response_body: Optional[bytes] = None,
        response_headers: Optional[dict[str, str]] = None,
    ) -> None:
        """
        Initialize an HTTP status error.

        Args:
            message: Error description
            status_code: HTTP status code
            url: Request URL
            response_body: Response body bytes
            response_headers: Response headers
        """
        context: dict[str, Any] = {"status_code": status_code}
        if url:
            context["url"] = url

        super().__init__(message, context)
        self.status_code = status_code
        self.url = url
        self.response_body = response_body
        self.response_headers = response_headers

    def error_type(self) -> str:
        return "HttpStatusError"


class ClientError(HttpStatusError):
    """
    HTTP 4xx client error response.

    Indicates the client made an invalid request (bad request, unauthorized,
    not found, etc.).
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        url: Optional[str] = None,
        response_body: Optional[bytes] = None,
        response_headers: Optional[dict[str, str]] = None,
    ) -> None:
        """
        Initialize a client error.

        Args:
            message: Error description
            status_code: HTTP 4xx status code
            url: Request URL
            response_body: Response body bytes
            response_headers: Response headers
        """
        if not (400 <= status_code < 500):
            raise ValueError(f"ClientError requires 4xx status code, got {status_code}")
        super().__init__(message, status_code, url, response_body, response_headers)

    def error_type(self) -> str:
        return "ClientError"


class ServerError(HttpStatusError):
    """
    HTTP 5xx server error response.

    Indicates the server failed to process a valid request (internal error,
    bad gateway, service unavailable, etc.).
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        url: Optional[str] = None,
        response_body: Optional[bytes] = None,
        response_headers: Optional[dict[str, str]] = None,
    ) -> None:
        """
        Initialize a server error.

        Args:
            message: Error description
            status_code: HTTP 5xx status code
            url: Request URL
            response_body: Response body bytes
            response_headers: Response headers
        """
        if not (500 <= status_code < 600):
            raise ValueError(f"ServerError requires 5xx status code, got {status_code}")
        super().__init__(message, status_code, url, response_body, response_headers)

    def error_type(self) -> str:
        return "ServerError"


# ============================================================================
# Parsing Errors - Response body decoding/parsing issues
# ============================================================================


class JsonDecodeError(HttpError):
    """
    Failed to decode JSON from response body.

    This occurs when response.json() is called but the response
    body is not valid JSON.
    """

    def __init__(
        self,
        message: str,
        body: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize a JSON decode error.

        Args:
            message: Error description
            body: Response body that failed to parse
            original_error: Original exception from JSON parser
        """
        context = {}
        if body is not None:
            # Truncate long bodies
            body_preview = body[:200] + "..." if len(body) > 200 else body
            context["body_preview"] = body_preview
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.body = body
        self.original_error = original_error

    def error_type(self) -> str:
        return "JsonDecodeError"


class TextDecodeError(HttpError):
    """
    Failed to decode text from response body.

    This occurs when response.text is accessed but the response
    body cannot be decoded with the specified or detected encoding.
    """

    def __init__(
        self,
        message: str,
        encoding: Optional[str] = None,
        original_error: Optional[Exception] = None,
    ) -> None:
        """
        Initialize a text decode error.

        Args:
            message: Error description
            encoding: Encoding that failed
            original_error: Original exception from decoder
        """
        context = {}
        if encoding:
            context["encoding"] = encoding
        if original_error:
            context["original_error"] = str(original_error)
            context["original_type"] = type(original_error).__name__

        super().__init__(message, context)
        self.encoding = encoding
        self.original_error = original_error

    def error_type(self) -> str:
        return "TextDecodeError"


# ============================================================================
# Validation Errors - Request parameter validation issues
# ============================================================================


class RequestValidationError(HttpError):
    """
    Invalid request parameters provided.

    This indicates a programming error where invalid parameters
    were passed to the request method.
    """

    def __init__(
        self,
        message: str,
        parameter: Optional[str] = None,
        value: Any = None,
    ) -> None:
        """
        Initialize a request validation error.

        Args:
            message: Error description
            parameter: Name of invalid parameter
            value: Invalid value provided
        """
        context = {}
        if parameter:
            context["parameter"] = parameter
        if value is not None:
            context["value"] = str(value)

        super().__init__(message, context)
        self.parameter = parameter
        self.value = value

    def error_type(self) -> str:
        return "RequestValidationError"


__all__ = [
    "HttpError",
    # Transport errors
    "NetworkError",
    "ConnectionTimeoutError",
    "ReadTimeoutError",
    "SSLError",
    "ProxyError",
    # HTTP status errors
    "HttpStatusError",
    "ClientError",
    "ServerError",
    # Parsing errors
    "JsonDecodeError",
    "TextDecodeError",
    # Validation errors
    "RequestValidationError",
]
