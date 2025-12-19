# HTTP Backends

The SDK supports multiple HTTP backends. Choose based on your requirements for features, performance, or dependencies.

## Available Backends

| Backend    | Package         | Async | Connection Pooling |
| ---------- | --------------- | ----- | ------------------ |
| `stdlib`   | None (built-in) | No    | No                 |
| `httpx`    | `httpx`         | Yes   | Yes                |
| `requests` | `requests`      | No    | Yes                |
| `urllib3`  | `urllib3`       | No    | Yes                |

## Choosing a Backend

**Use `stdlib` when:**

- You want zero external dependencies
- Deploying in restricted environments

**Use `httpx` when:**

- You need async/await support
- You want HTTP/2 capabilities

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
pip install satvu[http-requests]
pip install satvu[http-urllib3]

# Install multiple backends
pip install satvu[http-httpx,http-requests]
```

## Automatic Selection

By default, the SDK auto-detects the best available backend:

```python
from satvu import SatVuSDK

# Uses best available: httpx → requests → urllib3 → stdlib
sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
)
```

## Explicit Backend Selection

Use `create_http_client()` to specify a backend:

```python
from satvu import SatVuSDK
from satvu.http import create_http_client

# Use httpx explicitly
http_client = create_http_client(backend="httpx")

sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
    http_client=http_client,
)
```

## Configuration Options

All backends support common configuration:

```python
http_client = create_http_client(
    backend="httpx",
    timeout=60,  # Request timeout in seconds
)

sdk = SatVuSDK(
    client_id="...",
    client_secret="...",
    http_client=http_client,
)
```

## Implementing a Custom Backend

Implement the `HttpClient` protocol for custom HTTP handling:

```python
from satvu.http.protocol import HttpClient, HttpResponse
from satvu.result import Result, Ok, Err
from satvu.http.errors import HttpError


class CustomHttpClient(HttpClient):
    def request(
        self,
        method: str,
        url: str,
        *,
        headers: dict[str, str] | None = None,
        params: dict[str, str] | None = None,
        json: dict | None = None,
        data: bytes | None = None,
        timeout: int | None = None,
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
