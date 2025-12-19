#!/usr/bin/env python3

"""
SDK usage examples for the Wallet Service.

Demonstrates:
- Getting credit balance for a contract

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
"""

from os import getenv
from uuid import UUID

from satvu import SatVuSDK

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
print("Wallet Service Examples")
print("=" * 80)

print("\n1. Getting credit balance for contract...")
credit_balance = sdk.wallet.get_credit_balance(contract_id=contract_id)
print("   ✓ Credit balance retrieved")
print(f"   Contract ID: {contract_id}")
print(f"   Balance: {credit_balance.balance}")
print(f"   Billing cycle: {credit_balance.billing_cycle}")

print("\n" + "=" * 80)
print("All examples completed!")
print("=" * 80)
