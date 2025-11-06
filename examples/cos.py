#!/usr/bin/env python3

"""
SDK usage examples for the COS (Catalog Ordering Service).

Demonstrates:
- Submitting an order for catalog items
- Retrieving order details
- Editing order properties
- Paginated GET query with iterator
- Paginated POST search with iterator
- Downloading order items

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
"""

from os import getenv
from uuid import UUID
import sys

from satvu_api_sdk import SatVuSDK
from satvu_api_sdk.services.cos.models import (
    OrderEditPayload,
    OrderSubmissionPayload,
    SearchRequest,
)


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
print("COS Service Examples")
print("=" * 80)

# First, get some catalog items to order
print("\n1. Searching catalog for items to order...")
catalog_results = sdk.catalog.get_search(contract_id=contract_id, limit=1)
print(f"   Found {len(catalog_results.features)} catalog items")

if not catalog_results.features:
    print("   No catalog items found. Cannot proceed with order examples.")
    sys.exit(0)

# Extract feature IDs for ordering
feature_ids = [feature.id for feature in catalog_results.features[:3]]
print(f"   Using {len(feature_ids)} items for order")

print("\n2. Submitting a new order...")
order_payload = OrderSubmissionPayload(
    item_id=feature_ids,
    name="Example COS Order",
)

order = sdk.cos.submit_order__post(
    contract_id=contract_id,
    body=order_payload,
)

print(f"   ✓ Order submitted: {order.id}")
print(f"   Order name: {order.name}")
print(f"   Items: {len(order.features)}")

print("\n3. Retrieving order details...")
order_details = sdk.cos.order_details__get(
    contract_id=contract_id,
    order_id=order.id,
)
print("   ✓ Order details retrieved")
print(f"   Order ID: {order_details.id}")
print(f"   Name: {order_details.name}")

print("\n4. Editing order...")
updated_order = sdk.cos.edit_order__patch(
    contract_id=contract_id,
    order_id=order.id,
    body=OrderEditPayload(name="Updated COS Order Name"),
)
print("   ✓ Order updated")
print(f"   New name: {updated_order.name}")

print("\n" + "=" * 80)
print("Iterator Examples")
print("=" * 80)

print("\n5. Query orders with GET pagination iterator...")
print("   Fetching up to 2 pages with 10 orders each...")
total_orders = 0
for page_num, page in enumerate(
    sdk.cos.query_orders__get_iter(
        contract_id=contract_id,
        limit=10,
        max_pages=2,
    ),
    start=1,
):
    print(f"   Page {page_num}: {len(page.orders)} orders")
    total_orders += len(page.orders)
    # Show first 2 orders from each page
    for order_item in page.orders[:2]:
        print(f"      - Order ID: {order_item.id} | Name: {order_item.name}")
print(f"   Total orders retrieved: {total_orders}")

print("\n6. Search orders with POST pagination iterator...")
search_body = SearchRequest(
    limit=5,
    # You can add filters here like:
    # ids=[order.id],  # Search for specific order IDs
)
print("   Searching orders with pagination (up to 2 pages)...")
total_searched = 0
for page_num, page in enumerate(
    sdk.cos.search_orders__post_iter(
        contract_id=contract_id,
        body=search_body,
        max_pages=2,
    ),
    start=1,
):
    print(f"   Page {page_num}: {len(page.orders)} orders")
    total_searched += len(page.orders)
    # Show details from each page
    for order_item in page.orders[:2]:
        print(f"      - Order ID: {order_item.id} | Items: {len(order_item.features)}")
print(f"   Total orders from search: {total_searched}")

print("\n7. Getting download URLs for order items...")
if order_details.features:
    first_feature = order_details.features[0]
    try:
        download_url = sdk.cos.download_item__get(
            contract_id=contract_id,
            order_id=order.id,
            item_id=first_feature.id,
        )
        print(f"   ✓ Download URL retrieved for item: {first_feature.id}")
        print(f"   URL expires: {download_url.expiry}")
    except Exception as e:
        print(f"   Note: Download may not be ready yet: {e}")

print("\n" + "=" * 80)
print("All examples completed!")
print("=" * 80)
