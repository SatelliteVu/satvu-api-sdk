"""HTTP client abstractions for the SatVu SDK."""

from typing import Any, Literal, cast

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
from satvu.http.protocol import HttpClient, HttpResponse
from satvu.result import Err, Ok, Result, is_err, is_ok


def create_http_client(
    backend: Literal["auto", "httpx", "requests", "urllib3", "stdlib"] = "auto",
    base_url: str | None = None,
    **options: Any,
) -> HttpClient:
    """
    Create an HTTP client with the specified backend.

    Args:
        backend: HTTP library to use. Options:
            - "auto": Auto-detect best available (httpx → requests → urllib3 → stdlib)
            - "httpx": Use httpx library (requires httpx)
            - "requests": Use requests library (requires requests)
            - "urllib3": Use urllib3 library (requires urllib3)
            - "stdlib": Use standard library urllib (no dependencies)
        base_url: Optional base URL for all requests
        **options: Additional backend-specific options (e.g., timeout, headers)

    Returns:
        HttpClient: An HTTP client implementing the HttpClient protocol

    Raises:
        ValueError: If an invalid backend is specified
        ImportError: If a specific backend is requested but not installed

    Examples:
        >>> # Auto-detect best available library
        >>> client = create_http_client()

        >>> # Use specific backend
        >>> client = create_http_client(backend="httpx", base_url="https://api.example.com")

        >>> # Use stdlib (zero dependencies)
        >>> client = create_http_client(backend="stdlib")
    """
    if backend == "auto":
        # Try backends in order of preference
        for backend_name in ["httpx", "requests", "urllib3", "stdlib"]:
            try:
                return _create_backend(backend_name, base_url, **options)
            except ImportError:
                continue
        # stdlib should always work as it has no dependencies
        raise RuntimeError("Failed to create HTTP client with any backend")

    # Explicit backend selection
    valid_backends = ["httpx", "requests", "urllib3", "stdlib"]
    if backend not in valid_backends:
        raise ValueError(
            f"Invalid backend '{backend}'. Must be one of: {', '.join(valid_backends + ['auto'])}"
        )

    return _create_backend(backend, base_url, **options)


def _create_backend(
    backend: str, base_url: str | None = None, **options: Any
) -> HttpClient:
    """Internal helper to instantiate a specific backend."""
    if backend == "httpx":
        from satvu.http.httpx_adapter import HttpxAdapter

        return cast(HttpClient, HttpxAdapter(base_url=base_url, **options))

    elif backend == "requests":
        from satvu.http.requests_adapter import RequestsAdapter

        return cast(HttpClient, RequestsAdapter(base_url=base_url, **options))

    elif backend == "urllib3":
        from satvu.http.urllib3_adapter import Urllib3Adapter

        return cast(HttpClient, Urllib3Adapter(base_url=base_url, **options))

    elif backend == "stdlib":
        from satvu.http.stdlib_adapter import StdlibAdapter

        return cast(HttpClient, StdlibAdapter(base_url=base_url, **options))

    raise ValueError(f"Unknown backend: {backend}")


__all__ = [
    # Factory
    "create_http_client",
    # Protocol
    "HttpClient",
    "HttpResponse",
    # Result types
    "Result",
    "Ok",
    "Err",
    "is_ok",
    "is_err",
    # Error types
    "HttpError",
    "NetworkError",
    "ConnectionTimeoutError",
    "ReadTimeoutError",
    "SSLError",
    "ProxyError",
    "HttpStatusError",
    "ClientError",
    "ServerError",
    "JsonDecodeError",
    "TextDecodeError",
    "RequestValidationError",
]
