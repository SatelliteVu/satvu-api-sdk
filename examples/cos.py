#!/usr/bin/env python3

"""
SDK usage examples for the COS (Catalog Ordering Service).

Demonstrates:
- Submitting an order for catalog items
- Retrieving order details
- Editing order properties
- Paginated GET query with iterator
- Paginated POST search with iterator
- Getting download URLs
- Streaming downloads with progress tracking (memory-efficient for large files)

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
"""

import sys
import tempfile
from os import getenv
from pathlib import Path
from uuid import UUID

from satvu_api_sdk import SatVuSDK
from satvu_api_sdk.services.cos.models import OrderEditPayload, SearchRequest
from satvu_api_sdk.services.cos.models import (
    OrderSubmissionPayloadV3 as OrderSubmissionPayload,
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
catalog_results = sdk.catalog.get_search(contract_id=contract_id, limit=3)
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
    licence_level="Evaluation Licence",
    name="Example COS Order - SDK",
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
    body=OrderEditPayload(name="Updated COS Order Name - sdk"),
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
            redirect=False,  # Get URL instead of downloading
        )
        print(f"   ✓ Download URL retrieved for item: {first_feature.id}")
        print(f"   URL expires: {download_url.expiry}")
    except Exception as e:
        print(f"   Note: Download may not be ready yet: {e}")

print("\n" + "=" * 80)
print("Streaming Download Examples")
print("=" * 80)

print("\n8. Download individual item to file (streaming)...")
print("   Memory-efficient streaming download for large files")

if order_details.features:
    first_feature = order_details.features[0]
    output_path = Path(tempfile.gettempdir()) / f"cos_item_{first_feature.id}.zip"

    # Progress tracking function
    def show_progress(bytes_downloaded: int, total_bytes: int | None):
        if total_bytes:
            percent = (bytes_downloaded / total_bytes) * 100
            print(
                f"   Progress: {bytes_downloaded:,} / {total_bytes:,} bytes ({percent:.1f}%)"
            )
        else:
            print(f"   Downloaded: {bytes_downloaded:,} bytes")

    result = sdk.cos.download_item_to_file(
        contract_id=contract_id,
        order_id=order.id,
        item_id=first_feature.id,
        output_path=output_path,
        chunk_size=65536,  # 64KB chunks for faster downloads
        progress_callback=show_progress,
    )

    # Handle Result type (Railway-Oriented Programming)
    if result.is_ok():
        saved_path = result.unwrap()
        print(f"   ✓ Downloaded to: {saved_path}")
    else:
        error = result.unwrap_or(None)
        print(f"   ✗ Download failed: {error}")
        print("   Note: Item may not be ready yet")

print("\n9. Download entire order to file (streaming)...")
print("   Downloads all order items as a single ZIP file")

output_path = Path(tempfile.gettempdir()) / f"cos_order_{order.id}.zip"

result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order.id,
    output_path=output_path,
    chunk_size=65536,
    progress_callback=show_progress,
)

if result.is_ok():
    saved_path = result.unwrap()
    print(f"   ✓ Downloaded to: {saved_path}")
else:
    error = result.unwrap_or(None)
    print(f"   ✗ Download failed: {error}")
    print("   Note: Order may not be ready yet")

print("\n" + "=" * 80)
print("All examples completed!")
print("=" * 80)
