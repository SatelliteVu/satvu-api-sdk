# Testing Guide

This document explains how testing works in the SatVu API SDK project, including the auto-generation system, test infrastructure, and CI/CD integration.

## Overview

The SDK uses a hybrid testing approach:

| Test Category          | Approach                            | Files                                |
| ---------------------- | ----------------------------------- | ------------------------------------ |
| **Service Tests**      | Auto-generated property-based tests | `services/{api}/api_test.py`         |
| **Core Tests**         | Hand-written unit tests             | `auth_test.py`, `core_test.py`, etc. |
| **HTTP Adapter Tests** | Hand-written unit tests             | `http/*_adapter_test.py`             |

**Key technologies:**

- **pytest** - Test framework
- **hypothesis** + **hypothesis-jsonschema** - Property-based testing from JSON schemas
- **pook** - HTTP mocking
- **pytest-xdist** - Parallel test execution
- **pytest-cov** - Coverage reporting

## Test Generation Flow

The SDK automatically generates property-based tests for all API service endpoints during the build process. Here's how it works:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         TEST GENERATION PIPELINE                            │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌───────────────┐
    │  uv build     │  ◄── Entry point: triggers Hatch build hook
    └───────┬───────┘
            │
            ▼
    ┌───────────────────┐
    │  hatch_build.py   │  Iterates over all APIs (catalog, cos, id, etc.)
    └───────┬───────────┘
            │
            ▼
    ┌───────────────────┐
    │  build.py         │  ServiceCodeGenerator.generate()
    │  build_service()  │
    └───────┬───────────┘
            │
            │  For each API:
            │
            ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                           SCHEMA PREPARATION                              │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  1. _prepare_components()                                           │  │
│  │     ├── Extract components/schemas from OpenAPI spec               │  │
│  │     ├── clean_schema(): Convert JSON Schema 2020-12 → draft-07     │  │
│  │     └── remove_excluded_refs(): Remove problematic schemas         │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                    │                                      │
│                                    ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  2. find_recursive_refs()                                           │  │
│  │     └── DFS to detect schemas with circular references             │  │
│  │         (e.g., CQL2's booleanExpression → andOrExpression → ...)   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                    │                                      │
│                                    ▼                                      │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  3. remove_recursive_refs()                                         │  │
│  │     └── Strip recursive variants from oneOf/anyOf                  │  │
│  │         (prevents hypothesis from hanging on infinite recursion)   │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
└───────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                         OPERATION EXTRACTION                              │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │  _extract_operations()                                              │  │
│  │     For each endpoint in OpenAPI spec:                             │  │
│  │     ├── extract_response_schema() → 200, 201, 4xx, 5xx responses   │  │
│  │     ├── extract_request_body_schema() → POST/PUT/PATCH bodies      │  │
│  │     ├── extract_query_param_schema() → required query params       │  │
│  │     └── _prepare_schema_for_hypothesis() → attach $definitions     │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                           │
│  Output: operations dict + endpoints_data list                           │
└───────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                         TEMPLATE RENDERING                                │
│                                                                           │
│  ┌──────────────────────────┐     ┌────────────────────────────────────┐ │
│  │  test_module.py.jinja    │     │  test_schemas.py.jinja             │ │
│  │                          │     │                                    │ │
│  │  • Test class structure  │     │  • operations dict                 │ │
│  │  • @pytest.mark params   │     │  • components/definitions          │ │
│  │  • Fixture setup         │     │  • Helper functions:               │ │
│  │  • Imports               │     │    - get_response_schema()         │ │
│  │                          │     │    - get_request_body_schema()     │ │
│  │  Includes macros:        │     │    - get_parameter_schema()        │ │
│  │  ├── test_success.jinja  │     │    - has_request_body()            │ │
│  │  ├── test_error.jinja    │     │    - has_parameter()               │ │
│  │  └── test_no_content.jinja     │    - is_error_response()           │ │
│  └──────────────────────────┘     └────────────────────────────────────┘ │
└───────────────────────────────────────────────────────────────────────────┘
                                     │
                                     ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                         OUTPUT FILES                                      │
│                                                                           │
│    src/satvu_api_sdk/services/{api_name}/                                │
│    ├── api_test.py         (~1000+ lines per API)                        │
│    │   └── TestCatalogService, TestCosService, etc.                     │
│    └── test_schemas.py     (~2MB+ per API)                               │
│        └── OPERATIONS dict with all endpoint schemas                     │
│                                                                           │
│    Final step: Format with ruff (check --fix + format)                   │
└───────────────────────────────────────────────────────────────────────────┘
```

## Generated Test Structure

Each generated test file follows this pattern:

```python
@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestCatalogService:
    """Property-based tests for CatalogService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        # Create mock auth token
        mock_get_token = Mock(return_value="test_token")

        # Create HTTP client with specified backend
        http_client = create_http_client(
            backend=backend,
            base_url=self.base_url,
            get_token=mock_get_token,
        )

        # Initialize SDK
        self.sdk = SatVuSDK(
            client_id="test_client_id",
            client_secret="test_client_secret",  # pragma: allowlist secret
            http_client=http_client,
            env="qa",
        )

    # ---- Success Tests (2xx) ----
    @settings(max_examples=10, deadline=None, suppress_health_check=[...])
    @given(response_data=from_schema(get_response_schema("/endpoint/", "get", "200")))
    def test_endpoint_200(self, backend, response_data):
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data)

        result = self.sdk.catalog.endpoint()
        assert isinstance(result, ExpectedModel)

    # ---- Error Tests (4xx/5xx) ----
    @settings(max_examples=10, deadline=None)
    @given(response_data=from_schema(get_response_schema("/endpoint/", "get", "422")))
    def test_endpoint_422(self, backend, response_data):
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data)

        result = self.sdk.catalog.endpoint()
        assert is_err(result)

    # ---- No Content Tests (204) ----
    def test_endpoint_204(self, backend):
        pook.reset()
        pook.on()
        pook.delete(url).reply(204)

        result = self.sdk.catalog.endpoint()
        assert result is None
```

### Test Types Generated

| HTTP Status | Test Type                  | Assertion                         |
| ----------- | -------------------------- | --------------------------------- |
| 200, 201    | Property-based with schema | Response parses to Pydantic model |
| 204         | Static (no body)           | Returns `None`                    |
| 4xx         | Property-based or static   | Returns `Err(ClientError)`        |
| 5xx         | Property-based or static   | Returns `Err(ServerError)`        |

## Schema Processing

The test generator handles several JSON Schema challenges:

### 1. JSON Schema Dialect Conversion

OpenAPI 3.1 uses JSON Schema 2020-12, but hypothesis-jsonschema only supports draft-07:

```python
# Before (2020-12)
{"prefixItems": [{"type": "string"}, {"type": "integer"}]}

# After (draft-07)
{"items": [{"type": "string"}, {"type": "integer"}]}
```

### 2. Recursive Schema Handling

Schemas like CQL2's `booleanExpression` reference themselves, causing hypothesis to hang:

```
booleanExpression
├── andOrExpression  ←─┐
│   └── booleanExpression ──┘  (cycle!)
├── notExpression
│   └── booleanExpression ──┘  (cycle!)
└── boolean  ←── non-recursive (keep this)
```

The generator:

1. Detects cycles via DFS (`find_recursive_refs`)
2. Removes recursive variants from `oneOf`/`anyOf` (`remove_recursive_refs`)
3. Leaves non-recursive paths for hypothesis to generate

### 3. Excluded Schemas

Some schemas like `GeometryCollection` are excluded entirely (`EXCLUDED_SCHEMA_REFS`) because they cause hypothesis to timeout.

## Running Tests

### Local Development

```bash
# Run all tests
./scripts/test.sh

# Run with verbose output
./scripts/test.sh -v

# Run specific test file
./scripts/test.sh src/satvu_api_sdk/auth_test.py

# Run specific test
./scripts/test.sh -k test_get_token_success

# Run with all HTTP backends (slower)
./scripts/test.sh --all-backends

# Run with coverage
./scripts/test.sh --cov=src --cov-report=term-missing
```

### Backend Filtering

By default, CI runs tests only against the `stdlib` backend for speed. To run all backends:

```bash
# Via flag
./scripts/test.sh --all-backends

# Via environment variable
ALL_BACKENDS=1 ./scripts/test.sh
```

Available backends: `stdlib`, `httpx`, `urllib3`, `requests`

### CI/CD with Dagger

```bash
# Run tests (Python 3.13, with coverage)
dagger call -v test

# Run tests without coverage (faster)
dagger call -v test --with-coverage=false

# Run tests on specific Python version
dagger call -v test --python-version=3.11

# Run tests across all Python versions in parallel
dagger call -v test_all

# Run specific tests via pytest options
dagger call -v test --add-opts="-k test_auth"
```

## Test Infrastructure

### Directory Structure

```
src/satvu_api_sdk/
├── auth_test.py                    # Authentication tests (manual)
├── core_test.py                    # SDKClient core tests (manual)
├── core_retry_test.py              # Retry logic tests (manual)
├── core_streaming_test.py          # Streaming download tests (manual)
├── shared/
│   └── parsing_test.py             # TypeAdapter parsing tests (manual)
├── http/
│   ├── stdlib_adapter_test.py      # stdlib HTTP adapter (manual)
│   ├── httpx_adapter_test.py       # httpx adapter (manual)
│   ├── requests_adapter_test.py    # requests adapter (manual)
│   └── urllib3_adapter_test.py     # urllib3 adapter (manual)
└── services/
    ├── conftest.py                 # Pytest hooks for backend filtering
    ├── catalog/
    │   ├── api_test.py             # Generated tests
    │   └── test_schemas.py         # Generated schemas
    ├── cos/
    ├── id/
    ├── otm/
    ├── policy/
    ├── reseller/
    └── wallet/
```

### conftest.py Configuration

The services `conftest.py` provides:

1. **Backend filtering** - Runs only `stdlib` in CI by default
2. **Shrinking timeout** - Reduces hypothesis shrinking from 5 min to 30 sec
3. **CLI option** - `--all-backends` flag for comprehensive testing

```python
# src/satvu_api_sdk/services/conftest.py
engine.MAX_SHRINKING_SECONDS = 30

ALL_BACKENDS = ["stdlib", "httpx", "urllib3", "requests"]
CI_BACKENDS = ["stdlib"]

def pytest_addoption(parser):
    parser.addoption("--all-backends", action="store_true", default=False)

def pytest_collection_modifyitems(config, items):
    # Filter tests to CI_BACKENDS unless --all-backends
```

### Hypothesis Settings

Generated tests use conservative settings to balance coverage vs. speed:

```python
@settings(
    max_examples=10,           # Generate 10 examples per test
    deadline=None,             # No time limit per example
    suppress_health_check=[
        HealthCheck.filter_too_much,
        HealthCheck.too_slow,
        HealthCheck.large_base_example,
        HealthCheck.data_too_large,
    ],
)
```

## Mocking Patterns

### HTTP Mocking with pook

All HTTP tests use [pook](https://github.com/h2non/pook) for request/response mocking:

```python
import pook

@pook.on
def test_example():
    # Mock a GET request
    pook.get("https://api.qa.satellitevu.com/catalog/v2/contracts/")
        .reply(200)
        .json({"data": "value"})
        .header("Content-Type", "application/json")

    # Make request through SDK
    result = sdk.catalog.contracts()

    # Assertions...
```

For hypothesis tests, reset pook between examples:

```python
@given(response_data=from_schema(...))
def test_property_based(self, response_data):
    pook.reset()  # Clear previous mocks
    pook.on()  # Re-enable mocking
    pook.get(url).reply(200).json(response_data)
    # ...
```

### Time Mocking with freezegun

Used in authentication tests for JWT expiration:

```python
from freezegun import freeze_time


@freeze_time("2024-01-15 12:00:00")
def test_token_not_expired():
    # Token created at frozen time
    token = create_token(exp=datetime(2024, 1, 15, 13, 0, 0))
    assert not is_expired(token)
```

## Coverage Configuration

Coverage is configured in `pyproject.toml`:

```toml
[tool.coverage.report]
show_missing = true
skip_empty = true
sort = "Cover"
omit = [
    "**/*_test.py",      # Exclude test files
    "**/conftest.py",    # Exclude pytest config
    "src/builder/**"     # Exclude builder code
]
```

## Adding Manual Tests

When writing manual tests:

1. **File naming**: Use `*_test.py` suffix (not `test_*.py`)
2. **Location**: Place alongside the code being tested
3. **HTTP mocking**: Use `pook` for HTTP layer isolation
4. **Result types**: Use `is_ok()` / `is_err()` type guards for Result assertions

Example:

```python
# src/satvu_api_sdk/feature_test.py
import pook
import pytest
from satvu_api_sdk.result import is_ok, is_err

class TestFeature:
    @pook.on
    def test_feature_success(self):
        pook.get("https://api.satellitevu.com/endpoint")
            .reply(200)
            .json({"status": "ok"})

        result = feature_function()

        assert is_ok(result)
        assert result.unwrap().status == "ok"

    @pook.on
    def test_feature_error(self):
        pook.get("https://api.satellitevu.com/endpoint")
            .reply(500)
            .json({"error": "Internal Server Error"})

        result = feature_function()

        assert is_err(result)
```

## Regenerating Tests

Tests are regenerated automatically when building the SDK:

```bash
# Regenerate all SDK code + tests
uv build

# For development: regenerate specific API (may not resolve templates correctly)
uv run python -m builder catalog --cached
```

**Note**: Always use `uv build` for production builds to ensure templates are resolved correctly.

## Troubleshooting

### Hypothesis Hanging

If hypothesis hangs on a specific test:

1. Check for recursive schemas in the endpoint's response
2. Add the problematic schema to `EXCLUDED_SCHEMA_REFS` in `schema_utils.py`
3. Rebuild: `uv build`

### Test Failures After OpenAPI Changes

When OpenAPI specs change:

1. Rebuild SDK and tests: `uv build`
2. Check for new recursive schemas in output
3. Review generated test file for correct assertions

### Backend-Specific Failures

If tests pass with `stdlib` but fail with other backends:

```bash
# Run with specific backend
./scripts/test.sh -k "test_name" --all-backends

# Or debug specific backend
./scripts/test.sh -k "test_name[httpx]"
```
