"""HTTP client abstractions for the SatVu SDK."""

from satvu_api_sdk.http.errors import (
    ClientError,
    ConnectionTimeoutError,
    HttpError,
    HttpStatusError,
    JsonDecodeError,
    NetworkError,
    ProxyError,
    ReadTimeoutError,
    RequestValidationError,
    SSLError,
    ServerError,
    TextDecodeError,
)
from satvu_api_sdk.http.protocol import HttpClient, HttpResponse
from satvu_api_sdk.http.result import Err, Ok, Result, is_err, is_ok

__all__ = [
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
