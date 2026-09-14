"""HTTPX2 HTTP adapter."""

try:
    import httpx2
except ImportError as exc:
    raise ImportError(
        "httpx2 is required to use Httpx2Adapter. "
        'Install it with: pip install "satvu[http-httpx2]"'
    ) from exc

from satvu.http.httpx_common import HttpxAdapterBase


class Httpx2Adapter(HttpxAdapterBase):
    """
    HTTP client adapter using httpx2 (pydantic/httpx2).
    """

    _module = httpx2

    client: httpx2.Client
