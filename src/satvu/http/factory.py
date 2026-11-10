"""Create HTTP clients, or wrap a supported library's own client."""

import inspect
from typing import TYPE_CHECKING, Any, Literal, TypeAlias, cast

from satvu.http.protocol import HttpClient

if TYPE_CHECKING:
    import httpx
    import httpx2
    import requests
    import urllib3

    HttpClientLike: TypeAlias = (
        HttpClient
        | httpx.Client
        | httpx2.Client
        | requests.Session
        | urllib3.PoolManager
    )
else:
    HttpClientLike: TypeAlias = HttpClient

Backend = Literal["httpx", "httpx2", "requests", "urllib3", "stdlib"]

# Order matters: "auto" walks this list and takes the first backend that imports.
_BACKENDS: tuple[Backend, ...] = ("httpx", "httpx2", "requests", "urllib3", "stdlib")

# Matched by (top-level module, class name) so detection never imports an optional library.
_LIBRARY_CLIENTS: dict[tuple[str, str], Backend] = {
    ("httpx", "Client"): "httpx",
    ("httpx2", "Client"): "httpx2",
    ("requests", "Session"): "requests",
    ("urllib3", "PoolManager"): "urllib3",
}


def create_http_client(backend: Backend | Literal["auto"] = "auto") -> HttpClient:
    """
    Create an HTTP client using the given library, with its default settings.

    To configure the transport (proxies, TLS, pool size), build the library's own
    client instead and pass that to ``SatVuSDK(http_client=...)``.

    Args:
        backend: HTTP library to use. Options:
            - "auto": Auto-detect best available (httpx → httpx2 → requests → urllib3 → stdlib)
            - "httpx": Use httpx library (requires httpx)
            - "httpx2": Use httpx2 library (requires httpx2)
            - "requests": Use requests library (requires requests)
            - "urllib3": Use urllib3 library (requires urllib3)
            - "stdlib": Use standard library urllib (no dependencies)

    Returns:
        HttpClient: An HTTP client implementing the HttpClient protocol

    Raises:
        ValueError: If an invalid backend is specified
        ImportError: If a specific backend is requested but not installed

    Examples:
        >>> client = create_http_client()  # best available library
        >>> client = create_http_client(backend="stdlib")  # zero dependencies
    """
    if backend == "auto":
        for backend_name in _BACKENDS:
            try:
                return _create_backend(backend_name)
            except ImportError:
                continue
        # stdlib should always work as it has no dependencies
        raise RuntimeError("Failed to create HTTP client with any backend")

    if backend not in _BACKENDS:
        raise ValueError(
            f"Invalid backend '{backend}'. Must be one of: {', '.join([*_BACKENDS, 'auto'])}"
        )

    return _create_backend(backend)


def as_http_client(client: HttpClientLike) -> HttpClient:
    """
    Return ``client`` as an ``HttpClient``, wrapping a supported library's own client.

    Accepts an ``httpx.Client``, ``httpx2.Client``, ``requests.Session`` or
    ``urllib3.PoolManager`` (or a subclass), or anything already implementing
    ``HttpClient``, which is returned unchanged.

    Raises:
        TypeError: If ``client`` is neither a supported library client nor an HttpClient
    """
    backend = _library_backend(client)
    if backend is not None:
        return _create_backend(backend, client)
    request = getattr(client, "request", None)
    if inspect.iscoroutinefunction(request):
        raise TypeError(
            f"Async http_client {type(client).__name__!r} is not supported: "
            "pass a synchronous client"
        )
    if callable(request):
        return cast(HttpClient, client)
    supported = ", ".join(f"{module}.{name}" for module, name in _LIBRARY_CLIENTS)
    raise TypeError(
        f"Unsupported http_client {type(client).__name__!r}: pass one of {supported}, "
        "or an object implementing satvu.http.HttpClient"
    )


def ensure_http_client(client: HttpClientLike | None) -> HttpClient:
    """Wrap ``client`` with ``as_http_client``, or create the default client if None."""
    return as_http_client(client) if client is not None else create_http_client()


def _library_backend(client: object) -> Backend | None:
    """Find which backend wraps ``client``, if it is a supported library's client."""
    for cls in type(client).__mro__:
        backend = _LIBRARY_CLIENTS.get((cls.__module__.partition(".")[0], cls.__name__))
        if backend is not None:
            return backend
    return None


def _create_backend(backend: Backend, library_client: Any | None = None) -> HttpClient:
    """Instantiate a backend's adapter, optionally around an existing library client."""
    # Imported per branch so only the chosen library is loaded, keeping cold starts cheap.
    if backend == "httpx":
        from satvu.http.httpx_adapter import HttpxAdapter

        return cast(HttpClient, HttpxAdapter(client=library_client))

    elif backend == "httpx2":
        from satvu.http.httpx2_adapter import Httpx2Adapter

        return cast(HttpClient, Httpx2Adapter(client=library_client))

    elif backend == "requests":
        from satvu.http.requests_adapter import RequestsAdapter

        return cast(HttpClient, RequestsAdapter(session=library_client))

    elif backend == "urllib3":
        from satvu.http.urllib3_adapter import Urllib3Adapter

        return cast(HttpClient, Urllib3Adapter(pool_manager=library_client))

    elif backend == "stdlib":
        from satvu.http.stdlib_adapter import StdlibAdapter

        return cast(HttpClient, StdlibAdapter())

    raise ValueError(f"Unknown backend: {backend}")
