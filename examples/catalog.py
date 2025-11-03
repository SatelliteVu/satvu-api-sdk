# /usr/bin/env python3

"""
Simple SDK usage example for the CatalogService.

Set the following environment variables before running:
- SATVU_CLIENT_ID
- SATVU_CLIENT_SECRET
- SATVU_CONTRACT_ID
"""

from os import getenv
from pprint import pprint
from uuid import UUID

from satvu_api_sdk import SatVuSDK


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

result = sdk.catalog.get_search(contract_id=UUID(CONTRACT_ID))
pprint(result.features)
