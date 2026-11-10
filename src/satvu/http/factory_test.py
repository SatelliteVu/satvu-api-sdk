"""Tests for HTTP client creation and library-client wrapping."""

from functools import partial
from typing import cast

import httpx
import httpx2
import pytest
import requests
import urllib3

from satvu.http import HttpClient, as_http_client, create_http_client
from satvu.http.httpx2_adapter import Httpx2Adapter
from satvu.http.httpx_adapter import HttpxAdapter
from satvu.http.requests_adapter import RequestsAdapter
from satvu.http.stdlib_adapter import StdlibAdapter
from satvu.http.urllib3_adapter import Urllib3Adapter


class _SessionSubclass(requests.Session):
    pass


@pytest.mark.parametrize(
    ("make_client", "adapter_cls", "attr"),
    [
        (httpx.Client, HttpxAdapter, "client"),
        (httpx2.Client, Httpx2Adapter, "client"),
        (requests.Session, RequestsAdapter, "session"),
        (_SessionSubclass, RequestsAdapter, "session"),
        (urllib3.PoolManager, Urllib3Adapter, "pool_manager"),
        (
            partial(urllib3.ProxyManager, "http://proxy.example.com:8080"),
            Urllib3Adapter,
            "pool_manager",
        ),
    ],
)
def test_as_http_client_wraps_library_client(make_client, adapter_cls, attr):
    """A library's own client (or a subclass) is wrapped in its adapter, not copied."""
    with make_client() as library_client:
        wrapped = as_http_client(library_client)

        assert isinstance(wrapped, adapter_cls)
        assert getattr(wrapped, attr) is library_client


def test_as_http_client_passes_http_client_through():
    """Anything already implementing HttpClient is returned unchanged."""
    adapter = cast(HttpClient, StdlibAdapter())

    assert as_http_client(adapter) is adapter


@pytest.mark.parametrize("async_client_cls", [httpx.AsyncClient, httpx2.AsyncClient])
def test_as_http_client_rejects_async_client(async_client_cls):
    """Async clients would return coroutines from request(), so they're refused upfront."""
    with pytest.raises(TypeError, match="Async http_client"):
        as_http_client(async_client_cls())


def test_as_http_client_rejects_unsupported():
    """An object that is neither a library client nor an HttpClient fails clearly."""
    with pytest.raises(TypeError, match="requests.Session"):
        as_http_client(object())  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("backend", "adapter_cls"),
    [
        ("httpx", HttpxAdapter),
        ("httpx2", Httpx2Adapter),
        ("requests", RequestsAdapter),
        ("urllib3", Urllib3Adapter),
        ("stdlib", StdlibAdapter),
    ],
)
def test_create_http_client_backend(backend, adapter_cls):
    assert isinstance(create_http_client(backend), adapter_cls)


def test_create_http_client_invalid_backend():
    with pytest.raises(ValueError, match="Invalid backend"):
        create_http_client("curl")  # type: ignore[arg-type]
