# SatVu API SDK

[![pypi](https://img.shields.io/pypi/v/satvu)](https://pypi.org/project/satvu/)
[![GitHub License](https://img.shields.io/github/license/SatelliteVu/satvu-api-sdk)](https://github.com/SatelliteVu/satvu-api-sdk/blob/main/LICENSE)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/satellitevu)](https://x.com/intent/follow?screen_name=satellitevu)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://uk.linkedin.com/company/satvu)

Python SDK for [SatVu's](https://www.satellitevu.com/) satellite imagery platform.

## ✨ Features

- **Unified Interface** - Access all SatVu APIs through a single SDK
- **Type Safety** - Full type hints with Pydantic models for requests and responses
- **Explicit Error Handling** - Rust-inspired Result types for predictable error handling
- **Multiple HTTP Backends** - Choose httpx, requests, urllib3, or stdlib
- **Built-in Pagination** - Iterator methods for seamless pagination through large result sets
- **Streaming Downloads** - Memory-efficient downloads for large satellite imagery files

## 📦 Installation

The package is published on [PyPI](https://pypi.org/project/satvu/) and can be installed with pip:

```bash
pip install satvu-api-sdk
```

With optional HTTP backends:

```bash
pip install satvu-api-sdk[http-httpx]
pip install satvu-api-sdk[http-requests]
pip install satvu-api-sdk[http-urllib3]
```

The SDK works out of the box with Python's built-in `urllib`.

## 🚀 Quick Start

```python
import os
from uuid import UUID
from satvu_api_sdk import SatVuSDK

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)

contract_id = UUID(os.environ["SATVU_CONTRACT_ID"])

# Search the catalog
results = sdk.catalog.get_search(contract_id=contract_id, limit=10)
for feature in results.features:
    print(feature.id)
```

## Available Services

| Service        | Description                                                                               |
| -------------- | ----------------------------------------------------------------------------------------- |
| `sdk.catalog`  | Search and discover SatVu's [STAC](https://github.com/radiantearth/stac-api-spec) catalog |
| `sdk.cos`      | Order and download imagery available from SatVu's STAC catalog                            |
| `sdk.id`       | Identity and user management, including webhooks                                          |
| `sdk.otm`      | Order and manage satellite tasking                                                        |
| `sdk.policy`   | Check active contracts                                                                    |
| `sdk.reseller` | Perform reseller operations                                                               |
| `sdk.wallet`   | Check credit balances                                                                     |

## 📖 Documentation

- [Getting Started](docs/getting-started.md) - Installation, authentication, first API call
- [Authentication](docs/authentication.md) - OAuth2 flow, token caching, environments
- [Error Handling](docs/error-handling.md) - Result types and error patterns
- [Pagination](docs/pagination.md) - Working with paginated endpoints
- [Streaming Downloads](docs/streaming-downloads.md) - Downloading large imagery files
- [HTTP Backends](docs/http-backends.md) - Choosing and configuring HTTP clients
- [Changelog](CHANGELOG.md)

## Requirements

- Python 3.10+

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## Support

For bugs and feature requests, please [open an issue](https://github.com/satellitevu/satvu-api-sdk/issues).
