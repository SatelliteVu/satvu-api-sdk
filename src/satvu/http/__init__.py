"""HTTP client abstractions for the SatVu SDK."""

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
from satvu.http.factory import (
    Backend,
    HttpClientLike,
    as_http_client,
    create_http_client,
    ensure_http_client,
)
from satvu.http.protocol import HttpClient, HttpResponse
from satvu.result import Err, Ok, Result, is_err, is_ok

__all__ = [
    # Factory
    "create_http_client",
    "as_http_client",
    "ensure_http_client",
    "HttpClientLike",
    "Backend",
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
