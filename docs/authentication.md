# Authentication

The SDK uses OAuth2 client credentials flow to authenticate with SatVu APIs.

## Basic Setup

> **Warning:** Never hardcode credentials in your source code. Always load them from environment variables, a secrets manager, or another secure source.

```python
import os
from satvu import SatVuSDK

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)
```

The SDK automatically:

- Fetches an access token on first API call
- Caches the token in memory
- Refreshes the token when it expires

## Token Caching

### Memory Cache (Default)

By default, tokens are cached in memory for the lifetime of the `SatVuSDK` instance:

```python
import os
from satvu import SatVuSDK

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)
# Token cached in memory - lost when process exits
```

### File-Based Cache

For long-running applications or CLI tools, use file-based caching to persist tokens across restarts:

```python
import os
from satvu import SatVuSDK
from satvu.auth import AppDirCache

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
    token_cache=AppDirCache(),
)
# Token persisted to platform-specific cache directory
```

This requires the `appdirs` package:

```bash
pip install satvu[standard]
```

## Custom HTTP Client

You can provide your own HTTP client for advanced configuration:

```python
from satvu import SatVuSDK
from satvu.http import create_http_client

# Create a custom HTTP client
http_client = create_http_client(
    backend="httpx",
    timeout=60,
)

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
    http_client=http_client,
)
```

See [HTTP Backends](http-backends.md) for more details.

## Timeout Configuration

Set request timeout (in seconds):

```python
import os
from satvu import SatVuSDK

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
    timeout=60,  # Default is 30 seconds
)
```

## Retry Configuration

The SDK automatically retries failed requests with exponential backoff:

```python
import os
from satvu import SatVuSDK

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
    max_retry_attempts=5,  # Maximum retry attempts (default: 5)
    max_retry_after_seconds=300.0,  # Maximum delay between retries (default: 300)
)
```

Retries are attempted for:

- Network errors
- 429 Too Many Requests (rate limiting)
- 5xx Server errors
