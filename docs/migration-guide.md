# Migration Guide: satellitevu → satvu

This guide helps you migrate from the deprecated [`satellitevu`](https://pypi.org/project/satellitevu/) package to the new [`satvu`](https://pypi.org/project/satvu/) SDK.

## Installation

```diff
- pip install satellitevu
+ pip install satvu
```

Optional HTTP backends (the SDK works without any extras using Python's built-in `urllib`):

```bash
pip install satvu[http-httpx]      # modern, async-capable
pip install satvu[http-requests]   # requests library
pip install satvu[http-urllib3]    # high-performance pooling
pip install satvu[standard]        # file-based token caching (appdirs)
```

## Package & Import Changes

```diff
- from satellitevu import Client
+ from satvu import SatVuSDK
```

The PyPI package name, Python package name, and all import paths have changed:

| Old                                         | New                              |
| ------------------------------------------- | -------------------------------- |
| `satellitevu`                               | `satvu`                          |
| `satellitevu.Client`                        | `satvu.SatVuSDK`                 |
| `satellitevu.Auth`                          | `satvu.auth.AuthService`         |
| `satellitevu.http.AbstractClient`           | `satvu.http.protocol.HttpClient` |
| `satellitevu.http.UrllibClient`             | `satvu.http.stdlib_adapter`      |
| `satellitevu.http.requests.RequestsSession` | `satvu.http.requests_adapter`    |
| `satellitevu.auth.AbstractCache`            | `satvu.auth.TokenCache`          |
| `satellitevu.auth.AppDirCache`              | `satvu.auth.AppDirCache`         |
| `satellitevu.auth.MemoryCache`              | `satvu.auth.MemoryCache`         |

## Client Initialization

```diff
- from satellitevu import Client
+ from satvu import SatVuSDK

- client = Client(
-     client_id,
-     client_secret,
-     gateway_url="https://api.satellitevu.com",
- )
+ sdk = SatVuSDK(
+     client_id=client_id,
+     client_secret=client_secret,
+     env=None,  # None = production, "qa" = QA
+ )
```

Key differences:

- Constructor uses **keyword arguments** for `client_id` / `client_secret` (positional no longer supported).
- `gateway_url` is replaced by the `env` parameter (`None` for production, `"qa"` for QA). URLs are constructed automatically.
- `audience` parameter is removed.
- `cache` → `token_cache`.
- New parameters: `timeout`, `max_retry_attempts`, `max_retry_after_seconds`.

## Service Access

API version suffixes are gone. Services are accessed as simple properties:

```diff
- client.catalog_v1.search(...)
+ sdk.catalog.post_search(...)

- client.orders_v2.submit(...)
+ sdk.cos.submit_order(...)

- client.otm_v2.post_feasibility(...)
+ sdk.otm.post_tasking_feasibility(...)

- client.id_v2
+ sdk.id

- client.contracts_v1
+ sdk.policy
```

Full service mapping:

| Old                   | New            | Notes                                     |
| --------------------- | -------------- | ----------------------------------------- |
| `client.catalog_v1`   | `sdk.catalog`  |                                           |
| `client.orders_v2`    | `sdk.cos`      | Renamed to "COS" (Customer Order Service) |
| `client.otm_v2`       | `sdk.otm`      |                                           |
| `client.id_v2`        | `sdk.id`       |                                           |
| `client.contracts_v1` | `sdk.policy`   | Renamed to "Policy"                       |
| —                     | `sdk.wallet`   | New service                               |
| —                     | `sdk.reseller` | New service                               |

## Method Name Changes

Methods now follow the naming convention generated from the OpenAPI spec. The old SDK used hand-written convenience names.

### Catalog

```diff
- client.catalog_v1.search(
-     contract_id=contract_id,
-     date_from=datetime(2024, 1, 1),
-     date_to=datetime(2024, 6, 1),
-     limit=10,
-     page_token=token,
- )
+ sdk.catalog.post_search(
+     contract_id=contract_id,
+     body=PostSearchInput(
+         datetime="2024-01-01T00:00:00Z/2024-06-01T00:00:00Z",
+         limit=10,
+     ),
+     token=token,
+ )
```

- `date_from` / `date_to` convenience params are gone — pass `datetime` as an ISO 8601 range string in the request body.
- Search parameters are now passed as a Pydantic model via `body=`.
- `page_token` → `token`.
- `**kwargs` pass-through is removed; all parameters are generated from OpenAPI docs and explicitly typed.

### Orders (COS)

```diff
- client.orders_v2.submit(contract_id=cid, item_ids=["item1"])
+ sdk.cos.submit_order(contract_id=cid, body=OrderSubmissionPayload(item_id=["item1"]))

- client.orders_v2.get_orders(contract_id=cid)
+ sdk.cos.query_orders(contract_id=cid)

- client.orders_v2.get_order_details(contract_id=cid, order_id=oid)
+ sdk.cos.get_order(contract_id=cid, order_id=oid)
```

### OTM (Tasking)

```diff
- client.otm_v2.post_feasibility(
-     contract_id=cid,
-     coordinates=(-1.06, 51.16),
-     date_from=dt1,
-     date_to=dt2,
-     product="standard",
-     max_cloud_cover=15,
-     min_off_nadir=0,
-     max_off_nadir=30,
- )
+ sdk.otm.post_tasking_feasibility(
+     contract_id=cid,
+     body=FeasibilityRequest(...),
+ )

- client.otm_v2.get_order(contract_id=cid, order_id=oid)
+ sdk.otm.get_tasking_order(contract_id=cid, order_id=oid)

- client.otm_v2.cancel_order(contract_id=cid, order_id=oid)
+ sdk.otm.cancel_tasking_order(contract_id=cid, order_id=oid)

- client.otm_v2.list_orders(contract_id=cid, per_page=25, page_token=tok)
+ sdk.otm.get_tasking_orders(contract_id=cid, per_page=25, token=tok)
```

- Individual keyword arguments (coordinates, date_from, etc.) are replaced by typed Pydantic request body models.
- Client-side parameter validation (e.g., off-nadir/GSD mutual exclusivity) is removed — the API validates instead.

## Response Types

The old SDK returned raw `ResponseWrapper` objects (you called `.json()` to get dicts). The new SDK returns **Pydantic models** directly:

```diff
- response = client.catalog_v1.search(contract_id=cid)
- data = response.json()  # dict
- for item in data["features"]:
-     print(item["id"])
+ results = sdk.catalog.post_search(contract_id=cid, body=search)
+ for feature in results.features:  # typed Pydantic models
+     print(feature.id)
```

Benefits:

- IDE autocompletion and type checking.
- No manual dict key access — use attribute access instead.
- Serialize back to dicts with `model_dump()`.

## Error Handling

### Old: Exceptions

The old SDK raised domain-specific exceptions or returned raw responses:

```python
from satellitevu.apis.exceptions import OrdersAPIError, OTMOrderError

try:
    client.orders_v2.get_orders(contract_id=cid)
except OrdersAPIError as e:
    print(e.message)
```

### New: Result Types

The new SDK uses a Rust-inspired `Result[T, E]` type for explicit error handling on HTTP-level operations (downloads, streaming). Standard service methods raise `SatVuAPIError` exceptions.

```python
from satvu.result import is_ok, is_err

# Service methods — raise on HTTP errors
try:
    results = sdk.catalog.get_search(contract_id=cid, limit=10)
except SatVuAPIError as e:
    print(e.status_code, e.response_body)

# Streaming downloads — return Result type
result = sdk.cos.download_order_to_file(
    contract_id=cid,
    order_id=oid,
    output_path="order.zip",
)
if is_ok(result):
    path = result.unwrap()
elif is_err(result):
    error = result.error()
```

The `Result` type supports functional chaining:

```python
result.map(lambda path: print(f"Saved to {path}"))
result.map_err(lambda err: log_error(err))
result.unwrap_or(default_value)
```

See [Error Handling](error-handling.md) for the full guide.

## Downloads

The old SDK loaded entire files into memory. The new SDK streams to disk:

```diff
- path = client.orders_v2.download_order(
-     contract_id=cid,
-     order_id=oid,
-     destdir="/tmp",
-     retry_factor=1.0,
- )
+ result = sdk.cos.download_order_to_file(
+     contract_id=cid,
+     order_id=oid,
+     output_path="/tmp/order.zip",
+     chunk_size=65536,
+     progress_callback=lambda downloaded, total: print(f"{downloaded}/{total}"),
+ )
+ path = result.unwrap()
```

Key differences:

- `destdir` (directory) → `output_path` (full file path).
- `retry_factor` is removed — retries are handled at the SDK level.
- Downloads stream in chunks — safe for files >1 GB.
- Optional `progress_callback` for progress tracking.
- Returns `Result[Path, HttpError]` instead of a plain string path.

The old two-step pattern (`*_download_url()` + manual download) is replaced by single `*_to_file()` methods.

## Pagination

The old SDK required manual token passing:

```python
# Old — manual pagination
response = client.otm_v2.list_orders(contract_id=cid, per_page=25)
data = response.json()
next_token = extract_token(data)  # manual extraction from links
```

The new SDK provides `*_iter` generator methods:

```python
# New — automatic pagination
for page in sdk.otm.get_tasking_orders_iter(
    contract_id=cid,
    per_page=25,
    max_pages=10,
):
    for order in page.features:
        process(order)
```

See [Pagination](pagination.md) for details.

## HTTP Client Selection

```diff
- from satellitevu.http.requests import RequestsSession
- from requests import Session
- http_client = RequestsSession(instance=Session())
- client = Client(cid, secret, http_client=http_client)
+ from satvu.http import create_http_client
+ http_client = create_http_client(backend="requests")
+ sdk = SatVuSDK(client_id=cid, client_secret=secret, http_client=http_client)
```

The new SDK auto-detects the best available backend (httpx → requests → urllib3 → stdlib). Explicit selection via `create_http_client(backend=...)` is optional.

## Token Caching

```diff
- from satellitevu.auth import AppDirCache
- client = Client(cid, secret, cache=AppDirCache())
+ from satvu.auth import AppDirCache
+ sdk = SatVuSDK(client_id=cid, client_secret=secret, token_cache=AppDirCache())
```

- `cache` → `token_cache`.
- `AbstractCache` → `TokenCache` protocol.
- `MemoryCache` remains the default.
- `AppDirCache` requires `pip install satvu[standard]`.

## Quick Reference

| Concept        | Old (`satellitevu`)          | New (`satvu`)                              |
| -------------- | ---------------------------- | ------------------------------------------ |
| Package        | `pip install satellitevu`    | `pip install satvu`                        |
| Entry point    | `Client(id, secret)`         | `SatVuSDK(client_id=, client_secret=)`     |
| Environment    | `gateway_url=`               | `env=None \| "qa"`                         |
| Service access | `client.catalog_v1`          | `sdk.catalog`                              |
| Responses      | `response.json()` → dict     | Pydantic models                            |
| Errors         | Domain exceptions            | `SatVuAPIError` + `Result` types           |
| Pagination     | Manual token passing         | `*_iter()` generators                      |
| Downloads      | In-memory, `destdir=`        | Streaming, `output_path=`, `Result` return |
| HTTP client    | `RequestsSession(instance=)` | `create_http_client(backend=)`             |
| Token cache    | `cache=AppDirCache()`        | `token_cache=AppDirCache()`                |
