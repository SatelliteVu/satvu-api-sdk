# Pagination

Some SatVu API endpoints return paginated results. The SDK provides iterator methods to seamlessly handle pagination.

## Iterator Methods

For any paginated endpoint, there's a corresponding `*_iter` method:

| Standard Method   | Iterator Method        |
| ----------------- | ---------------------- |
| `get_search()`    | `get_search_iter()`    |
| `post_search()`   | `post_search_iter()`   |
| `query_orders()`  | `query_orders_iter()`  |
| `search_orders()` | `search_orders_iter()` |

## Basic Usage

```python
import os
from uuid import UUID

contract_id = UUID(os.environ["SATVU_CONTRACT_ID"])

# Iterate through pages
for page in sdk.catalog.get_search_iter(
    contract_id=contract_id,
    limit=25,
):
    for feature in page.features:
        print(feature.id)
```

## Controlling Pagination

### Limit Per Page

The `limit` parameter controls how many items are returned per page:

```python
for page in sdk.catalog.get_search_iter(
    contract_id=contract_id,
    limit=100,  # 100 items per page
):
    print(f"Page has {len(page.features)} features")
```

### Maximum Pages

Use `max_pages` to limit the total number of pages fetched:

```python
# Fetch at most 3 pages
for page in sdk.catalog.get_search_iter(
    contract_id=contract_id,
    limit=25,
    max_pages=3,
):
    process(page)

# Total items: up to 75 (3 pages x 25 per page)
```

### Fetch All Results

Omit `max_pages` to iterate through all available results:

```python
# Fetch everything (use with caution on large datasets)
all_features = []
for page in sdk.catalog.get_search_iter(
    contract_id=contract_id,
    limit=100,
):
    all_features.extend(page.features)

print(f"Total features: {len(all_features)}")
```

## POST Search with Pagination

For POST endpoints that accept a request body:

```python
from satvu_api_sdk.services.catalog.models import PostSearchInput

search_body = PostSearchInput(
    collections=["visual"],
    datetime="2024-01-01T00:00:00Z/..",
    limit=50,
)

for page in sdk.catalog.post_search_iter(
    body=search_body,
    contract_id=contract_id,
    max_pages=5,
):
    for feature in page.features:
        print(feature.id, feature.properties.datetime)
```

## COS Order Pagination

```python
# Query orders with GET pagination
for page in sdk.cos.query_orders_iter(
    contract_id=contract_id,
    limit=10,
    max_pages=3,
):
    for order in page.orders:
        print(f"Order: {order.id} - {order.name}")

# Search orders with POST pagination
from satvu_api_sdk.services.cos.models import SearchRequest

search = SearchRequest(limit=10)
for page in sdk.cos.search_orders_iter(
    contract_id=contract_id,
    body=search,
    max_pages=3,
):
    for order in page.orders:
        print(f"Order: {order.id}")
```

## How It Works

Under the hood, the SDK:

1. Makes the initial request
2. Extracts the pagination token from the response's `links` array (STAC-compliant)
3. Uses the token for subsequent requests
4. Stops when no more pages are available or `max_pages` is reached

The iterator yields the full response object for each page, giving you access to both the items and any metadata.
