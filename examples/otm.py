#!/usr/bin/env python3

"""
SDK usage examples for the OTM (Order Tasking Management) Service.

Demonstrates:
- Complete Assured order workflow (feasibility → order → edit → cancel)
- Paginated iterators for orders, feasibility requests, and search
- Streaming downloads with progress tracking (memory-efficient for large files)

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
- SATVU_ENV (optional, defaults to production)
"""

import tempfile
from datetime import datetime, timedelta
from os import getenv
from pathlib import Path
from pprint import pprint
from uuid import UUID

from satvu import SatVuSDK
from satvu.result import is_err, is_ok
from satvu.services.otm.models import (
    AssuredFeasibilityFields,
    AssuredOrderRequest,
    AssuredOrderRequestProperties,
    EditOrderPayload,
    EditOrderProperties,
    FeasibilityRequest,
    Point,
    SearchRequest,
)

CLIENT_ID = getenv("SATVU_CLIENT_ID")
assert CLIENT_ID is not None, "Please set the SATVU_CLIENT_ID environment variable"  # nosec B101
CLIENT_SECRET = getenv("SATVU_CLIENT_SECRET")
assert CLIENT_SECRET is not None, "Set the SATVU_CLIENT_SECRET environment variable"  # nosec B101
CONTRACT_ID = getenv("SATVU_CONTRACT_ID")
assert CONTRACT_ID is not None, "Set the SATVU_CONTRACT_ID environment variable"  # nosec B101

# Initialize SDK
sdk = SatVuSDK(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    env=getenv("SATVU_ENV", None),
)

# Set up time window for feasibility (tomorrow to 6 days from now)
tomorrow = datetime.now() + timedelta(days=1)
six_days = datetime.now() + timedelta(days=6)
datetime_range = f"{tomorrow.isoformat()}/{six_days.isoformat()}"

# Define target location (Madrid, Spain as example)
target_location = Point(coordinates=[-3.7038, 40.4168])

print("=" * 80)
print("OTM Service Example - Assured Order Workflow")
print("=" * 80)

# Step 1: Request feasibility check
print("\n1. Requesting feasibility check...")
print(f"   Target: {target_location.coordinates}")
print(f"   Time window: {datetime_range}")

feasibility_request = sdk.otm.post_tasking_feasibility(
    contract_id=UUID(CONTRACT_ID),
    body=FeasibilityRequest(
        geometry=target_location,
        properties=AssuredFeasibilityFields(datetime=datetime_range),
    ),
)

print(f"   ✓ Feasibility request created: {feasibility_request.id}")

# Step 2: Retrieve feasibility response
print("\n2. Retrieving feasibility response...")

feasibility_response = sdk.otm.get_tasking_feasibility_response(
    contract_id=UUID(CONTRACT_ID),
    id=feasibility_request.id,
)

print("   ✓ Feasibility response received")
print(f"   Features available: {len(feasibility_response.features)}")

if feasibility_response.features:
    first_feature = feasibility_response.features[0]
    print(f"   Product: {first_feature.properties.product}")
    print(f"   DateTime window: {first_feature.properties.datetime_}")
    print(f"   Signature: {first_feature.signature[:50]}...")  # type: ignore

# Step 3: Submit order based on feasibility
print("\n3. Submitting order...")

order = sdk.otm.post_tasking_orders(
    contract_id=UUID(CONTRACT_ID),
    body=AssuredOrderRequest(
        properties=AssuredOrderRequestProperties(
            signature=feasibility_response.features[0].signature,  # type: ignore
            name="Example Assured Order",
        )
    ),
)

print(f"   ✓ Order submitted: {order.id}")
print(f"   Order name: {order.properties.name}")
print(f"   Order status: {order.properties.status}")

# Step 4: Edit the order
print("\n4. Editing order name...")

updated_order = sdk.otm.edit_tasking_order(
    contract_id=UUID(CONTRACT_ID),
    order_id=order.id,
    body=EditOrderPayload(properties=EditOrderProperties(name="Updated Example Order")),
)

print("   ✓ Order updated")
print(f"   New name: {updated_order.properties.name}")

# Step 5: Retrieve order details
print("\n5. Retrieving order details...")

order_details = sdk.otm.get_tasking_order(
    contract_id=UUID(CONTRACT_ID),
    order_id=order.id,
)

print("   ✓ Order details retrieved")
print(f"   Order ID: {order_details.id}")
print(f"   Name: {order_details.properties.name}")
print(f"   Status: {order_details.properties.status}")
print(f"   Created: {order_details.properties.created_at}")

print("\n6. Canceling order...")
sdk.otm.cancel_tasking_order(
    contract_id=UUID(CONTRACT_ID),
    order_id=order.id,
)
print(f"   ✓ Order canceled: {order.id}")

print("\n" + "=" * 80)
print("Example completed successfully!")
print("=" * 80)
print("\nFull order details:")
print("=" * 80)
pprint(order_details.model_dump(mode="json"))

# ============================================================================
# Iterator Examples
# ============================================================================

print("\n" + "=" * 80)
print("Iterator Examples")
print("=" * 80)

print("\n7. Paginated orders iterator...")
print("   Fetching up to 2 pages with 5 orders each...")
total_orders = 0
for page_num, page in enumerate(
    sdk.otm.get_tasking_orders_iter(
        contract_id=UUID(CONTRACT_ID),
        per_page=5,
        max_pages=2,
    ),
    start=1,
):
    print(f"   Page {page_num}: {len(page.features)} orders")
    total_orders += len(page.features)
    for feature in page.features[:2]:  # Show first 2 from each page
        print(f"      - Order ID: {feature.id} | Status: {feature.properties.status}")
print(f"   Total orders retrieved: {total_orders}")

print("\n8. Paginated feasibility requests iterator...")
print("   Fetching up to 2 pages with 5 requests each...")
total_requests = 0
for page_num, page in enumerate(
    sdk.otm.get_tasking_feasibility_requests_iter(
        contract_id=UUID(CONTRACT_ID),
        per_page=5,
        max_pages=2,
    ),
    start=1,
):
    print(f"   Page {page_num}: {len(page.features)} feasibility requests")
    total_requests += len(page.features)
    for feature in page.features[:2]:  # Show first 2 from each page
        print(
            f"      - Request ID: {feature.id} | Product: {feature.properties.product}"
        )
print(f"   Total feasibility requests retrieved: {total_requests}")

print("\n9. Search with pagination iterator...")

search_body = SearchRequest(limit=5)
print("   Searching with pagination (up to 2 pages)...")
total_features = 0
for page_num, page in enumerate(
    sdk.otm.search_iter(
        contract_id=UUID(CONTRACT_ID),
        body=search_body,
        max_pages=2,
    ),
    start=1,
):
    print(f"   Page {page_num}: {len(page.features)} features")
    total_features += len(page.features)
print(f"   Total search features retrieved: {total_features}")

print("\n" + "=" * 80)
print("Streaming Download Example")
print("=" * 80)

print("\n10. Download tasking order to file (streaming)...")
print("   Memory-efficient download for large fulfilled tasking orders")
print("   Note: This will only work for fulfilled orders")


# Progress tracking function
def show_progress(bytes_downloaded: int, total_bytes: int | None):
    if total_bytes:
        percent = (bytes_downloaded / total_bytes) * 100
        mb_downloaded = bytes_downloaded / (1024 * 1024)
        mb_total = total_bytes / (1024 * 1024)
        print(f"   Progress: {mb_downloaded:.2f} / {mb_total:.2f} MB ({percent:.1f}%)")
    else:
        mb_downloaded = bytes_downloaded / (1024 * 1024)
        print(f"   Downloaded: {mb_downloaded:.2f} MB")


output_path = Path(tempfile.gettempdir()) / f"otm_order_{order.id}.zip"

result = sdk.otm.download_tasking_order_to_file(
    contract_id=UUID(CONTRACT_ID),
    order_id=order.id,
    output_path=output_path,
    chunk_size=65536,  # 64KB chunks for faster downloads
    progress_callback=show_progress,
)

# Handle Result type (Railway-Oriented Programming)
if is_ok(result):
    saved_path = result.unwrap()
    print(f"   ✓ Downloaded to: {saved_path}")
    print("   Note: Order must be fulfilled before download is available")
elif is_err(result):
    error = result.error()
    print(f"   ✗ Download failed: {error}")
    print("   Note: Order must be fulfilled before download is available")

print("\n" + "=" * 80)
print("All examples completed!")
print("=" * 80)
