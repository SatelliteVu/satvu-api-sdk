#!/usr/bin/env python3

"""
Simple SDK usage example for the OTM (Order Tasking Management) Service.

This example demonstrates the complete workflow for ordering satellite imagery:
1. Request a feasibility check (Assured tier)
2. Retrieve feasibility results
3. Submit an order based on feasibility results
4. Edit the order
5. Retrieve order details

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
- SATVU_ENV (optional, defaults to production)
"""

from datetime import datetime, timedelta
from os import getenv
from pprint import pprint
from uuid import UUID

from satvu_api_sdk import SatVuSDK
from satvu_api_sdk.services.otm.models import (
    AssuredFeasibilityFields,
    AssuredOrderRequest,
    AssuredOrderRequestProperties,
    EditOrderPayload,
    EditOrderProperties,
    FeasibilityRequest,
    Point,
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
