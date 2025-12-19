# Error Handling

The SDK uses a Rust-inspired `Result` type for explicit error handling. Instead of throwing exceptions, operations return either a success value or an error value.

## Why Result Types?

- **No surprise exceptions** - All errors are explicit in the return type
- **Type-safe** - Your editor knows about possible errors
- **Composable** - Chain operations cleanly with `map`, `and_then`, etc.

## Basic Pattern

```python
from satvu.result import is_ok, is_err

result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order_id,
    output_path=Path("./order.zip"),
)

if is_ok(result):
    path = result.unwrap()
    print(f"Downloaded to: {path}")
else:
    error = result.unwrap_err()
    print(f"Failed: {error}")
```

## Unwrapping Results

### Safe Unwrapping

```python
# Check first, then unwrap
if is_ok(result):
    value = result.unwrap()

# Or provide a default
value = result.unwrap_or(default_value)

# Or compute default from error
value = result.unwrap_or_else(lambda err: handle_error(err))
```

### Direct Unwrap (Use with Caution)

```python
# Raises ValueError if result is an error
value = result.unwrap()

# With custom error message
value = result.expect("Download should have succeeded")
```

## Error Types

The SDK provides specific error types for different failure modes:

```python
from satvu.http import (
    ClientError,  # 4xx responses
    ServerError,  # 5xx responses
    NetworkError,  # Connection failures
    ConnectionTimeoutError,
    ReadTimeoutError,
    SSLError,
    JsonDecodeError,
)

if is_err(result):
    error = result.unwrap_err()

    if isinstance(error, ClientError):
        if error.status_code == 404:
            print("Not found")
        elif error.status_code == 401:
            print("Unauthorized")

    elif isinstance(error, ServerError):
        print(f"Server error: {error.status_code}")

    elif isinstance(error, NetworkError):
        print("Network connectivity issue")
```

## Pattern Matching (Python 3.10+)

```python
if is_err(result):
    error = result.unwrap_err()

    match error:
        case ClientError(status_code=404):
            print("Resource not found")
        case ClientError(status_code=401):
            print("Authentication required")
        case ServerError():
            print("Server error - try again later")
        case NetworkError():
            print("Network error - check connection")
        case _:
            print(f"Unexpected error: {error}")
```

## Functional Composition

Chain operations elegantly:

```python
# Transform success values
status = result.map(lambda response: response.status_code)

# Chain operations that may fail
data = result.and_then(lambda response: response.json()).map(
    lambda data: data.get("items", [])
)

# Provide fallback on error
final = result.or_else(lambda error: Ok({"fallback": True}))
```

## Error Context

All errors include helpful context:

```python
if is_err(result):
    error = result.unwrap_err()

    print(f"Error type: {error.error_type()}")
    print(f"Message: {error.message}")

    # HTTP errors include response details
    if isinstance(error, (ClientError, ServerError)):
        print(f"Status: {error.status_code}")
        print(f"URL: {error.url}")
        print(f"Response body: {error.response_body}")

    # Timeout errors include the timeout value
    if isinstance(error, (ConnectionTimeoutError, ReadTimeoutError)):
        print(f"Timeout: {error.timeout} seconds")
```

## Complete Example

```python
import os
from pathlib import Path
from satvu import SatVuSDK
from satvu.result import is_ok, is_err
from satvu.http import ClientError, ServerError, NetworkError

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)


def download_order(contract_id, order_id, output_path):
    result = sdk.cos.download_order_to_file(
        contract_id=contract_id,
        order_id=order_id,
        output_path=output_path,
    )

    if is_ok(result):
        return result.unwrap()

    error = result.unwrap_err()

    if isinstance(error, ClientError):
        if error.status_code == 404:
            raise ValueError(f"Order {order_id} not found")
        elif error.status_code == 403:
            raise PermissionError("Access denied to this order")

    elif isinstance(error, ServerError):
        raise RuntimeError(f"Server error: {error.status_code}")

    elif isinstance(error, NetworkError):
        raise ConnectionError("Network error - check your connection")

    raise RuntimeError(f"Unexpected error: {error}")
```

## Further Reading

For advanced patterns and the complete error hierarchy, see the [Typed Errors Guide](typed-errors-guide.md).
