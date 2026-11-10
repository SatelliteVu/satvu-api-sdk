# HTTP Backends

The SDK supports multiple HTTP backends. Choose based on your requirements for features, performance, or dependencies.

## Available Backends

| Backend    | Package         | Async | Connection Pooling |
| ---------- | --------------- | ----- | ------------------ |
| `stdlib`   | None (built-in) | No    | No                 |
| `httpx`    | `httpx`         | Yes   | Yes                |
| `httpx2`   | `httpx2`        | Yes   | Yes                |
| `requests` | `requests`      | No    | Yes                |
| `urllib3`  | `urllib3`       | No    | Yes                |

## Choosing a Backend

**Use `stdlib` when:**

- You want zero external dependencies
- Deploying in restricted environments

**Use `httpx` when:**

- You need async/await support
- You want HTTP/2 capabilities

**Use `httpx2` when:**

- You are already on `httpx2` ([pydantic/httpx2](https://github.com/pydantic/httpx2))
- It behaves the same as the `httpx` backend, which the SDK achieves by backing both with
  one implementation.

**Use `requests` when:**

- It's already in your project dependencies
- You need broad ecosystem compatibility

**Use `urllib3` when:**

- You need high-performance connection pooling
- Making many concurrent requests

## Installation

```bash
# Zero dependencies - stdlib works out of the box
pip install satvu

# Install with specific backend
pip install satvu[http-httpx]
pip install satvu[http-httpx2]
pip install satvu[http-requests]
pip install satvu[http-urllib3]

# Install multiple backends
pip install satvu[http-httpx,http-requests]
```

## Automatic Selection

By default, the SDK auto-detects the best available backend:

```python
from satvu import SatVuSDK

# Uses best available: httpx → httpx2 → requests → urllib3 → stdlib
sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
)
```

## Configuring the HTTP Client

Pass your own configured client from any supported library. The SDK wraps it, adds the
base URL and auth token to every request, and shares it across every service:

```python
import ssl

import httpx

from satvu import SatVuSDK

sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
    http_client=httpx.Client(
        proxy="http://proxy.internal:8080",
        verify=ssl.create_default_context(cafile="ca-bundle.pem"),
    ),
    timeout=60,  # Request timeout in seconds
)
```

| Backend    | Pass                  |
| ---------- | --------------------- |
| `httpx`    | `httpx.Client`        |
| `httpx2`   | `httpx2.Client`       |
| `requests` | `requests.Session`    |
| `urllib3`  | `urllib3.PoolManager` |

Leave out `base_url` and auth on the client you pass, since the SDK sets both.

## Explicit Backend Selection

To pick a library but keep its default settings, use `create_http_client()`:

```python
from satvu.http import create_http_client

sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
    http_client=create_http_client(backend="requests"),
)
```

## Implementing a Custom Backend

Implement the `HttpClient` protocol for custom HTTP handling. The SDK always passes
an absolute `url` and includes the `Authorization` header in `headers`:

```python
from typing import Any

from satvu.http.protocol import HttpClient, HttpMethod, HttpResponse
from satvu.result import Result, Ok, Err
from satvu.http.errors import HttpError


class CustomHttpClient(HttpClient):
    def request(
        self,
        method: HttpMethod,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | list | None = None,
        data: dict[str, str] | None = None,
        timeout: float = 5.0,
        follow_redirects: bool = False,
    ) -> Result[HttpResponse, HttpError]:
        # Your implementation here
        ...


sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
    http_client=CustomHttpClient(),
)
```

See the [HttpClient protocol](../src/satvu/http/protocol.py) for the full interface.
