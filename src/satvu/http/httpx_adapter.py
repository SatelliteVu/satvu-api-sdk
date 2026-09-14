"""HTTPX HTTP adapter."""

try:
    import httpx
except ImportError as exc:
    raise ImportError(
        "httpx is required to use HttpxAdapter. "
        'Install it with: pip install "satvu[http-httpx]"'
    ) from exc

from satvu.http.httpx_common import HttpxAdapterBase


class HttpxAdapter(HttpxAdapterBase):
    """
    HTTP client adapter using httpx library.

    Provides advanced features like connection pooling, HTTP/2 support,
    and better performance than stdlib.
    """

    _module = httpx

    client: httpx.Client
