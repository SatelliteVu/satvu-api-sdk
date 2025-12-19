#!/usr/bin/env python3

"""
SDK usage examples for the ID (Identity) Service.

Demonstrates:
- User details and settings management
- Client credential management
- Webhook management (create, list, edit, test, delete)
- Paginated webhook listing with iterator

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
"""

from os import getenv

from satvu import SatVuSDK
from satvu.services.id.models import (
    CoreWebhook,
    EditWebhookPayload,
    NotificationCategory,
    NotificationConfig,
    NotificationUpdate,
    UserSettings,
    WebhookEvent,
)

CLIENT_ID = getenv("SATVU_CLIENT_ID")
assert CLIENT_ID is not None, "Please set the SATVU_CLIENT_ID environment variable"  # nosec B101
CLIENT_SECRET = getenv("SATVU_CLIENT_SECRET")
assert CLIENT_SECRET is not None, "Set the SATVU_CLIENT_SECRET environment variable"  # nosec B101

sdk = SatVuSDK(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    env=getenv("SATVU_ENV", None),
)

print("=" * 80)
print("ID Service Examples")
print("=" * 80)

print("\n1. Getting user details...")
user_info = sdk.id.get_user_details()
print("   ✓ User details retrieved")
print(f"   Email: {user_info.email}")
print(f"   User ID: {user_info.user_id}")

print("\n2. Getting user client ID...")
try:
    client_info = sdk.id.get_user_client()
    if client_info:
        print(f"   ✓ Client ID: {client_info.client_id}")
    else:
        print("   No client credentials exist yet")
except Exception as e:
    print(f"   Note: {e}")

print("\n3. Updating user settings...")
# Update user settings (e.g., email preferences)
updated_user = sdk.id.edit_user_settings(
    body=UserSettings(
        notifications=[
            NotificationUpdate(
                category=NotificationCategory.TASKING,
                settings=[NotificationConfig(topic="tasking:order_status", email=True)],
            )
        ]
    )
)
print("   ✓ User settings updated")
if updated_user.user_metadata:
    print(f"   Notifications: {updated_user.user_metadata.notifications}")

print("\n" + "=" * 80)
print("Webhook Management Examples")
print("=" * 80)

print("\n4. Getting available webhook event types...")
events = sdk.id.get_webhook_events()
print(f"   ✓ Found {len(events)} webhook event types:")
for event in events[:5]:  # Show first 5
    print(f"      - {event.name}: {event.description}")
if len(events) > 5:
    print(f"      ... and {len(events) - 5} more")

print("\n5. Creating a webhook...")
# Create a test webhook using the first available event type
webhook_payload = CoreWebhook(
    url="https://example.com/webhook",
    name="Example Webhook",
    event_types=[WebhookEvent(events[0].topic)],
)

webhook = sdk.id.create_webhook(body=webhook_payload)
print(f"   ✓ Webhook created: {webhook.id}")
print(f"   Name: {webhook.name}")
print(f"   URL: {webhook.url}")
print(f"   Events: {webhook.event_types}")

print("\n6. Getting webhook details...")
webhook_details = sdk.id.get_webhook(id=webhook.id)
print("   ✓ Webhook details retrieved")
print(f"   ID: {webhook_details.id}")
print(f"   Name: {webhook_details.name}")
print(f"   Active: {webhook_details.active}")

print("\n7. Editing webhook...")
updated_webhook = sdk.id.edit_webhook(
    id=webhook.id,
    body=EditWebhookPayload(
        name="Updated Example Webhook",
    ),
)
print("   ✓ Webhook updated")
print(f"   New name: {updated_webhook.name}")

print("\n8. Testing webhook...")
test_result = sdk.id.test_webhook(id=webhook.id)
print("   ✓ Test webhook sent")
if test_result.webhook_result.success:
    print("   ✓ Webhook test succeeded")
    print(f"   Status Code: {test_result.webhook_result.status_code}")
else:
    print("   ✗ Webhook test failed")
    print(f"   Status Code: {test_result.webhook_result.status_code}")
    print(f"   Message: {test_result.webhook_result.detail}")

print("\n" + "=" * 80)
print("Iterator Examples")
print("=" * 80)

print("\n9. Listing webhooks with pagination iterator...")
print("   Fetching up to 2 pages with 5 webhooks each...")
total_webhooks = 0
for page_num, page in enumerate(
    sdk.id.list_webhooks_iter(
        per_page=5,
        max_pages=2,
    ),
    start=1,
):
    print(f"   Page {page_num}: {len(page.webhooks)} webhooks")
    total_webhooks += len(page.webhooks)
    # Show details from each page
    for wh in page.webhooks[:3]:  # Show first 3 from each page
        print(f"      - ID: {wh.id} | Name: {wh.name} | Active: {wh.active}")
print(f"   Total webhooks retrieved: {total_webhooks}")

print("\n10. Rotating webhook signing key...")
rotated = sdk.id.rotate_webhook_signing_key(id=webhook.id)
print(f"   ✓ Signing key rotated for webhook: {webhook.id}")
print(f"   New signing key: {rotated.signing_key[:20]}...")

print("\n11. Cleaning up - deleting webhook...")
sdk.id.delete_webhook(id=webhook.id)
print(f"   ✓ Webhook deleted: {webhook.id}")

print("\n" + "=" * 80)
print("All examples completed!")
print("=" * 80)
