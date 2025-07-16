# SatVu Python SDK

Lightweight API Client SDK for interacting with SatVu's APIs.

This SDK is auto-generated from the OpenAPI specifications using the [openapi-python-client]
library.

## Development Setup

### Requirements

- Python >= 3.13 (TODO: support older versions)
- [uv]

### Getting Started

- Run `uv sync` to install dependencies

## Generating the SDK

To regenerate the SDK for an API, run:

```bash
uv run python -m builder <API_NAME>
```

You can find the available API names in `builder/config.py`.


[openapi-python-client]: https://github.com/openapi-generators/openapi-python-client
[uv]: https://docs.astral.sh/uv/