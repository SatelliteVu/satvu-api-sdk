# SatVu Python SDK

Lightweight API Client SDK for interacting with SatVu's APIs.

This SDK is auto-generated from the OpenAPI specifications using the [openapi-python-client]
library.

## Development Setup

### Requirements

- Python >= 3.13 (TODO: support older versions)
- [uv]

### Getting Started

- `./scripts/bootstrap.sh` to install dependencies
- `./scripts/test.sh` to run the tests, pytest options and arguments can be passed to the script
- `./scripts/lint.sh` to run the linters

## Generating the SDK

To regenerate the SDK for an API, run:

```bash
uv run python -m builder <API_NAME>
```

You can find the available API names in `builder/config.py`.

If you want to generate the SDK for all APIs, run:

```bash
uv build
```

[openapi-python-client]: https://github.com/openapi-generators/openapi-python-client
[uv]: https://docs.astral.sh/uv/
