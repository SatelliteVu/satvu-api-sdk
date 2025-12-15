# Contributing

Thank you for your interest in contributing to the SatVu API SDK!

## Development Setup

### Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

### Getting Started

1. Clone the repository:

```bash
git clone https://github.com/satellitevu/satvu-api-sdk.git
cd satvu-api-sdk
```

2. Run the bootstrap script to install dependencies and set up pre-commit hooks:

```bash
./scripts/bootstrap.sh
```

### Running Tests

```bash
./scripts/test.sh
```

Pass pytest options directly:

```bash
./scripts/test.sh -v                    # Verbose output
./scripts/test.sh -k test_name          # Run specific tests
./scripts/test.sh --all-backends        # Test all HTTP backends
```

### Running Linters

```bash
./scripts/lint.sh
```

This runs all pre-commit hooks including Ruff, Bandit, and type checking.

## SDK Generation

The SDK is auto-generated from OpenAPI specifications. To regenerate:

```bash
# Regenerate all APIs (canonical method)
uv build

# Regenerate specific API (development only)
uv run python -m builder <API_NAME>

# Use cached specs instead of fetching fresh ones
uv run python -m builder <API_NAME> --cached
```

Available API names: `catalog`, `cos`, `id`, `policy`, `otm`, `reseller`, `wallet`

## Project Structure

```
satvu-api-sdk/
├── src/
│   ├── satvu_api_sdk/          # Main SDK package
│   │   ├── sdk.py              # SatVuSDK entry point
│   │   ├── core.py             # SDKClient base class
│   │   ├── auth.py             # Authentication
│   │   ├── result.py           # Result type
│   │   ├── http/               # HTTP adapters
│   │   ├── shared/             # Shared utilities
│   │   └── services/           # Generated API services
│   │       ├── catalog/
│   │       ├── cos/
│   │       └── ...
│   └── builder/                # SDK generator
├── docs/                       # Documentation
├── examples/                   # Usage examples
└── scripts/                    # Development scripts
```

## CI/CD with Dagger

[Dagger](https://docs.dagger.io) provides portable CI:

```bash
dagger call -v test              # Run pytest suite
dagger call -v lint              # Run linters
dagger call -v test-all          # Test all Python versions
```

## Code Style

- We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- Type hints are required for all public APIs
- Tests use pytest with the `*_test.py` naming convention

## Pull Requests

1. Create a feature branch from `main`
2. Make your changes
3. Ensure tests pass: `./scripts/test.sh`
4. Ensure linting passes: `./scripts/lint.sh`
5. Submit a pull request

## Testing Guidelines

- Unit tests go alongside the code they test (e.g., `auth_test.py` next to `auth.py`)
- Use `pook` for HTTP mocking
- Use the `is_ok()` / `is_err()` type guards for Result assertions
- Generated service tests are in `services/{api}/api_test.py`

See [docs/testing.md](docs/testing.md) for detailed testing documentation.

## Questions?

Open an [issue](https://github.com/satellitevu/satvu-api-sdk/issues) for bugs and feature requests, or start a [discussion](https://github.com/satellitevu/satvu-api-sdk/discussions) for questions.
