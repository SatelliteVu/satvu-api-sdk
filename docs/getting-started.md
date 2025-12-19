# Getting Started

This guide walks you through installing the SDK, authenticating, and making your first API call.

## 📦 Installation

Install from PyPI:

```bash
pip install satvu
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add satvu
```

### Optional Dependencies

The SDK includes a zero-dependency HTTP client using Python's built-in `urllib`. For better performance or additional features, install an optional HTTP backend:

```bash
pip install satvu[http-httpx]
pip install satvu[http-requests]
pip install satvu[http-urllib3]
```

## 🔐 Authentication

The SDK uses OAuth2 client credentials.

### Getting Your Credentials

1. Sign up for a SatVu account and navigate to your [User Profile](https://app.satellitevu.com/id/profile)
2. Click **Generate New Credentials**
3. Save your `client_id` and `client_secret` securely

> **Note:** You'll also need a `contract_id` which represents your data access agreement. Contact your SatVu account manager if you don't have one. Available contracts can be found on the [dashboard](https://app.satellitevu.com).

> **Warning:** Never hardcode credentials in your source code. Always load them from environment variables, a secrets manager, or another secure source.

```python
import os
from satvu import SatVuSDK

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)
```

The SDK handles token management automatically - fetching, caching, and refreshing tokens as needed.

## 🚀 Your First API Call

Here's a complete example that searches the catalog:

```python
import os
from uuid import UUID
from satvu import SatVuSDK

# Initialize the SDK
sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)

# Your contract ID (from the SatVu platform)
contract_id = UUID(os.environ["SATVU_CONTRACT_ID"])

# Search the catalog
results = sdk.catalog.get_search(
    contract_id=contract_id,
    limit=10,
)

# Process results
print(f"Found {len(results.features)} features")
for feature in results.features:
    print(f"  - {feature.id}")
```

## Working with Results

Most SDK methods return Pydantic models with full type hints:

```python
results = sdk.catalog.get_search(contract_id=contract_id, limit=10)

# Access typed properties
for feature in results.features:
    print(feature.id)
    print(feature.geometry)
    print(feature.properties)
```

Some methods return `Result` types for explicit error handling. See [Error Handling](error-handling.md) for details.

## Pagination

Some endpoints support pagination. Use the `*_iter` methods to automatically handle pagination:

```python
# Iterate through all pages (up to max_pages)
for page in sdk.catalog.get_search_iter(
    contract_id=contract_id,
    limit=10,
    max_pages=5,
):
    for feature in page.features:
        print(feature.id)
```

See [Pagination](pagination.md) for more details.

## 🔍 Troubleshooting

### Authentication Errors

If you see `401 Unauthorized` errors:

- Verify your `client_id` and `client_secret` are correct
- Check that your credentials haven't expired

### Authorization Errors

If you see `403 Forbidden` errors:

- Verify your `contract_id` is correct
- Check that your contract has access to the requested resource
- Contact your SatVu account manager if access issues persist

### Rate Limiting

The SDK automatically retries on `429 Too Many Requests` errors. To customize retry behavior, see [Retry Configuration](authentication.md#retry-configuration).

## 📚 Next Steps

- [Authentication](authentication.md) - Token caching, custom HTTP clients
- [Error Handling](error-handling.md) - Working with Result types
- [Pagination](pagination.md) - Handling large result sets
- [Streaming Downloads](streaming-downloads.md) - Downloading imagery files
