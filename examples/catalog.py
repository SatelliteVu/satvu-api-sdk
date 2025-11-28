# /usr/bin/env python3

"""
SDK usage examples for the CatalogService.

Demonstrates:
- Simple GET search
- Paginated GET search with iterator
- POST search with filters
- Paginated POST search with iterator

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
"""

from os import getenv
from uuid import UUID

from satvu_api_sdk import SatVuSDK
from satvu_api_sdk.services.catalog.models.post_search_input import PostSearchInput

CLIENT_ID = getenv("SATVU_CLIENT_ID")
assert CLIENT_ID is not None, "Please set the SATVU_CLIENT_ID environment variable"  # nosec B101
CLIENT_SECRET = getenv("SATVU_CLIENT_SECRET")
assert CLIENT_SECRET is not None, "Set the SATVU_CLIENT_SECRET environment variable"  # nosec B101
CONTRACT_ID = getenv("SATVU_CONTRACT_ID")
assert CONTRACT_ID is not None, "Set the SATVU_CONTRACT_ID environment variable"  # nosec B101

sdk = SatVuSDK(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    env=getenv("SATVU_ENV", None),
)

contract_id = UUID(CONTRACT_ID)

print("=" * 80)
print("Example 1: Simple GET search (single page)")
print("=" * 80)
result = sdk.catalog.get_search(contract_id=contract_id, limit=10)
print(f"Found {len(result.features)} features on this page")
print(f"Links: {[link.rel for link in result.links]}")
print()

print("=" * 80)
print("Example 2: Paginated GET search with iterator")
print("=" * 80)
print("Fetching up to 3 pages with 10 items each...")
total_features = 0
for page_num, page in enumerate(
    sdk.catalog.get_search_iter(
        contract_id=contract_id,
        limit=10,
        max_pages=3,
    ),
    start=1,
):
    print(f"Page {page_num}: {len(page.features)} features")
    total_features += len(page.features)
    # Access individual features
    for feature in page.features:
        print(f"  - Feature ID: {feature.id}")
print(f"Total features retrieved: {total_features}")
print()

print("=" * 80)
print("Example 3: POST search with filters")
print("=" * 80)
search_body = PostSearchInput(
    collections=["visual"],  # Filter by collection
    limit=10,
    datetime_="2024-01-01T00:00:00Z/..",  # From 2024 onwards
)
result = sdk.catalog.post_search(body=search_body, contract_id=contract_id)
print(f"Found {len(result.features)} features matching filters")
print()

print("=" * 80)
print("Example 4: Paginated POST search with iterator")
print("=" * 80)
print("Searching with filters and pagination...")
search_body = PostSearchInput(
    collections=["visual"],
    limit=5,
    datetime_="2024-01-01T00:00:00Z/..",
)
total_features = 0
for page_num, page in enumerate(
    sdk.catalog.post_search_iter(
        body=search_body,
        contract_id=contract_id,
        max_pages=2,
    ),
    start=1,
):
    print(f"Page {page_num}: {len(page.features)} features")
    total_features += len(page.features)
    # Process each feature
    for feature in page.features:
        print(f"  - Feature ID: {feature.id}")
print(f"Total features retrieved: {total_features}")
print()

print("=" * 80)
print("Example 5: Control total items with limit × max_pages")
print("=" * 80)
print("Get exactly 30 features (3 pages × 10 per page)...")
total_features = 0
for page in sdk.catalog.get_search_iter(
    contract_id=contract_id,
    limit=10,
    max_pages=3,
):
    total_features += len(page.features)
print(f"Retrieved {total_features} features")
print()

print("All examples completed!")
