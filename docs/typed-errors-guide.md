# Typed Error Return Values Guide

This guide explains how to use the HTTP adapters' typed error return values system, which returns errors as values instead of throwing exceptions.

## Overview

All HTTP adapters return `Result[HttpResponse, HttpError]` instead of raising exceptions. This provides:

- **Type-safe error handling** - All error cases are explicit in the type system
- **No surprise exceptions** - All failures are returned as values
- **Composable error handling** - Use functional methods like `map`, `and_then`, `or_else`
- **Detailed error types** - Distinguish between network errors, timeouts, HTTP status codes, etc.

## Basic Usage

### Checking for Success or Error

```python
from satvu.http.stdlib_adapter import StdlibAdapter

adapter = StdlibAdapter()
result = adapter.request("GET", "https://api.example.com/data")

if result.is_ok():
    response = result.unwrap()
    print(f"Success! Status: {response.status_code}")
else:
    error = result.error()
    print(f"Failed: {error}")
```

### Unwrapping with Default

```python
# Get response or None if error
response = result.unwrap_or(None)

# Get response or compute from error
response = result.unwrap_or_else(lambda e: handle_error(e))
```

### Safe Unwrapping

```python
# Raises ValueError if error (use only when you're certain it's Ok)
response = result.unwrap()

# Raises ValueError with custom message if error
response = result.expect("Expected successful API response")
```

## Error Types

### HTTP Status Errors (4xx/5xx)

```python
from satvu.http import ClientError, ServerError

result = adapter.request("GET", "https://api.example.com/not-found")

if result.is_err():
    error = result.error()

    if isinstance(error, ClientError):
        # 4xx errors (bad request, unauthorized, not found, etc.)
        print(f"Client error: {error.status_code}")
        print(f"Response body: {error.response_body}")

    elif isinstance(error, ServerError):
        # 5xx errors (internal error, bad gateway, unavailable, etc.)
        print(f"Server error: {error.status_code}")
```

### Network Errors

```python
from satvu.http import NetworkError, ConnectionTimeoutError, ReadTimeoutError

result = adapter.request("GET", "https://unreachable.example.com")

if result.is_err():
    error = result.error()

    if isinstance(error, ConnectionTimeoutError):
        print(f"Connection timed out after {error.timeout} seconds")

    elif isinstance(error, ReadTimeoutError):
        print(f"Read timed out after {error.timeout} seconds")

    elif isinstance(error, NetworkError):
        print(f"Network error: {error.message}")
```

### SSL/TLS Errors

```python
from satvu.http import SSLError

result = adapter.request("GET", "https://expired-cert.example.com")

if result.is_err() and isinstance(result.error(), SSLError):
    error = result.error()
    print(f"SSL error: {error.message}")
```

### Proxy Errors

```python
from satvu.http import ProxyError

result = adapter.request("GET", "https://api.example.com")

if result.is_err() and isinstance(result.error(), ProxyError):
    error = result.error()
    print(f"Proxy error: {error.message}")
    print(f"Proxy: {error.proxy}")
```

### Parsing Errors

```python
from satvu.http import JsonDecodeError, TextDecodeError

result = adapter.request("GET", "https://api.example.com/data")

if result.is_ok():
    response = result.unwrap()

    # Try to parse JSON
    json_result = response.json()
    if json_result.is_ok():
        data = json_result.unwrap()
        print(f"Data: {data}")
    elif isinstance(json_result.error(), JsonDecodeError):
        error = json_result.error()
        print(f"Invalid JSON: {error.message}")
        print(f"Body preview: {error.context.get('body_preview')}")

    # Try to decode text
    text_result = response.text
    if text_result.is_ok():
        text = text_result.unwrap()
        print(f"Text: {text}")
    elif isinstance(text_result.error(), TextDecodeError):
        error = text_result.error()
        print(f"Encoding error: {error.message}")
```

## Functional Composition

### Mapping Results

```python
# Transform success values
result = adapter.request("GET", "https://api.example.com/data")
status_result = result.map(lambda response: response.status_code)

if status_result.is_ok():
    print(f"Status: {status_result.unwrap()}")  # Prints just the status code
```

### Chaining Operations

```python
# Chain operations that may fail
result = (
    adapter.request("GET", "https://api.example.com/data")
    .and_then(lambda response: response.json())  # Parse JSON
    .map(lambda data: data.get("items", []))  # Extract items
)

if result.is_ok():
    items = result.unwrap()
    print(f"Got {len(items)} items")
else:
    print(f"Failed: {result.error()}")
```

### Error Recovery

```python
# Provide alternative on error
result = adapter.request("GET", "https://api.example.com/data")
final_result = result.or_else(lambda error: Ok({"fallback": True}))

# Always succeeds with either real data or fallback
data = final_result.unwrap()
```

## Pattern Matching

For Python 3.10+, you can use structural pattern matching:

```python
result = adapter.request("GET", "https://api.example.com/data")

# Note: Pattern matching with Ok/Err requires using is_ok/is_err checks
if result.is_ok():
    response = result.unwrap()
    print(f"Success: {response.status_code}")
elif result.is_err():
    error = result.error()

    # Match on error type
    match error:
        case ClientError(status_code=404):
            print("Not found")
        case ClientError(status_code=401):
            print("Unauthorized")
        case ServerError():
            print("Server error")
        case NetworkError():
            print("Network error")
        case _:
            print(f"Other error: {error}")
```

## Complete Example

```python
from satvu.http.stdlib_adapter import StdlibAdapter
from satvu.http import (
    ClientError,
    ServerError,
    NetworkError,
    ConnectionTimeoutError,
    ReadTimeoutError,
    SSLError,
    JsonDecodeError,
)


def fetch_user_data(user_id: str):
    adapter = StdlibAdapter(base_url="https://api.example.com")

    # Make request
    result = adapter.request("GET", f"/users/{user_id}")

    # Handle errors
    if result.is_err():
        error = result.error()

        if isinstance(error, ClientError):
            if error.status_code == 404:
                print(f"User {user_id} not found")
                return None
            elif error.status_code == 401:
                print("Authentication required")
                return None

        elif isinstance(error, ServerError):
            print(f"Server error: {error.status_code}")
            return None

        elif isinstance(error, (ConnectionTimeoutError, ReadTimeoutError)):
            print(f"Request timed out after {error.timeout} seconds")
            return None

        elif isinstance(error, NetworkError):
            print(f"Network error: {error.message}")
            return None

        else:
            print(f"Unexpected error: {error}")
            return None

    # Parse JSON response
    response = result.unwrap()
    json_result = response.json()

    if json_result.is_err():
        print(f"Failed to parse JSON: {json_result.error()}")
        return None

    return json_result.unwrap()


# Usage
user = fetch_user_data("12345")
if user:
    print(f"User: {user}")
```

## Functional Style Example

```python
def fetch_user_data_functional(user_id: str):
    adapter = StdlibAdapter(base_url="https://api.example.com")

    return (
        adapter.request("GET", f"/users/{user_id}")
        .and_then(lambda response: response.json())
        .map(lambda data: data.get("user"))
        .unwrap_or(None)
    )


# Usage
user = fetch_user_data_functional("12345")
```

## Error Type Hierarchy

```
HttpError (base)
├── NetworkError
│   └── Connection failures, DNS errors
├── ConnectionTimeoutError
│   └── Timeout establishing TCP connection
├── ReadTimeoutError
│   └── Timeout reading response
├── SSLError
│   └── Certificate/TLS errors
├── ProxyError
│   └── Proxy connection/auth failures
├── HttpStatusError
│   ├── ClientError (4xx)
│   │   ├── 400 Bad Request
│   │   ├── 401 Unauthorized
│   │   ├── 403 Forbidden
│   │   ├── 404 Not Found
│   │   └── etc.
│   └── ServerError (5xx)
│       ├── 500 Internal Server Error
│       ├── 502 Bad Gateway
│       ├── 503 Service Unavailable
│       └── etc.
├── JsonDecodeError
│   └── Invalid JSON in response
├── TextDecodeError
│   └── Text encoding errors
└── RequestValidationError
    └── Invalid request parameters
```

## Error Context

All errors include context information:

```python
if result.is_err():
    error = result.error()

    print(f"Error type: {error.error_type()}")
    print(f"Message: {error.message}")
    print(f"Context: {error.context}")

    # HTTP status errors include response data
    if isinstance(error, (ClientError, ServerError)):
        print(f"Status: {error.status_code}")
        print(f"URL: {error.url}")
        print(f"Headers: {error.response_headers}")
        print(f"Body: {error.response_body}")

    # Timeout errors include timeout value
    if isinstance(error, (ConnectionTimeoutError, ReadTimeoutError)):
        print(f"Timeout: {error.timeout} seconds")

    # All errors can include original exception
    if error.context.get("original_error"):
        print(f"Original: {error.context['original_error']}")
```

## Best Practices

1. **Always check if Result is Ok or Err** before unwrapping
2. **Use specific error types** when you need to handle different cases
3. **Use functional composition** for cleaner code
4. **Include error context** in logs and debugging
5. **Use `unwrap_or` or `unwrap_or_else`** instead of `unwrap()` when a default makes sense
6. **Chain operations** with `and_then` for sequential operations that may fail
7. **Use `map`** to transform success values without changing error handling
8. **Consider error recovery** with `or_else` when appropriate

## Adapter-Specific Notes

All adapters (StdlibAdapter, HttpxAdapter, Urllib3Adapter, RequestsAdapter) follow the same Result-based API, but they map their library-specific exceptions differently:

- **stdlib**: Maps `urllib.error.URLError`, `socket.timeout`, etc.
- **httpx**: Maps `httpx.TimeoutException`, `httpx.ConnectError`, etc.
- **urllib3**: Maps `urllib3.exceptions.*`
- **requests**: Maps `requests.exceptions.*`

The error types you receive are unified across all adapters, making it easy to switch between implementations.
