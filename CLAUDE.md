# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an auto-generated Python SDK for SatVu's APIs. The SDK is generated from OpenAPI specifications using a custom builder that wraps openapi-python-client. The project supports multiple SatVu APIs (catalog, cos, id, policy, otm, reseller, wallet) through a unified SDK interface.

**Requirements:** Python >= 3.13

## Development Commands

### Setup
```bash
./scripts/bootstrap.sh
```
This installs dependencies and sets up pre-commit hooks.

### Testing
```bash
./scripts/test.sh
```
Run tests with pytest. Pass pytest options directly: `./scripts/test.sh -v -k test_name`

### Linting
```bash
./scripts/lint.sh
```
Runs all pre-commit hooks (Ruff, Bandit, detect-secrets, FawltyDeps).

### SDK Generation

Generate SDK for a specific API:
```bash
uv run python -m builder <API_NAME>
```

Generate all API SDKs:
```bash
uv run python -m builder all
# OR use the hatch build hook (generates all APIs, fetches fresh specs):
uv build
```

Use `--cached` flag to use cached OpenAPI specs instead of fetching fresh ones (only works with direct builder invocation, not `uv build`).

Available API names are defined in `src/builder/config.py`: catalog, cos, id, policy, otm, reseller, wallet.

**Note:** `uv build` triggers the Hatch build hook (`hatch_build.py`) which runs `build(api_id="all", use_cached=False)` internally before packaging.

**Dagger CI:**
```bash
dagger call -v test    # Run pytest suite
dagger call -v lint    # Run linter suite
dagger -c "build-release --is-qa --build-number 123 | export './dist' --wipe"  # Build release
```

## Architecture

### SDK Structure

The SDK has three main layers:

1. **SatVuSDK (src/satvu_api_sdk/sdk.py)**: Main entry point that provides access to all API services via properties (catalog, cos, id, etc.). Uses lazy initialization for services.

2. **Service Classes (src/satvu_api_sdk/services/{api_name}/api.py)**: Auto-generated API clients for each SatVu API. These inherit from SDKClient and contain methods corresponding to API endpoints.

3. **SDKClient (src/satvu_api_sdk/core.py)**: Base class that handles HTTP communication, authentication, URL construction, and request parameter processing. Automatically converts Pydantic models to JSON and filters out None values.

### Result Type System

The SDK uses a Rust-style Result type (src/satvu_api_sdk/result.py) for explicit error handling:

**Core Types:**
- **Result[T, E]**: Union type representing either `Ok[T]` (success) or `Err[E]` (failure)
- **Ok[T]**: Contains a success value of type T
- **Err[E]**: Contains an error value of type E

**Key Methods:**
- `.unwrap()`: Extract value (raises on Err)
- `.unwrap_or(default)`: Extract value or return default
- `.map(fn)`: Transform success value
- `.map_err(fn)`: Transform error value
- `.and_then(fn)`: Chain operations that return Results (Railway-Oriented Programming)
- `.or_else(fn)`: Provide alternative on error

**Type Guards:**
- `is_ok(result)`: TypeGuard for Ok variant
- `is_err(result)`: TypeGuard for Err variant

### HTTP Adapter System

The SDK uses a pluggable HTTP adapter system (src/satvu_api_sdk/http/) for maximum flexibility:

**Core Components:**
- **HttpClient Protocol (protocol.py)**: Defines the interface all HTTP adapters must implement
- **HttpResponse Protocol**: Defines response interface with `.json()`, `.text`, `.body`, `.headers`, `.status_code`
- **HttpError Hierarchy (errors.py)**: Detailed error types for different failure modes:
  - Transport errors: `NetworkError`, `ConnectionTimeoutError`, `ReadTimeoutError`, `SSLError`, `ProxyError`
  - HTTP status errors: `ClientError` (4xx), `ServerError` (5xx)
  - Parsing errors: `JsonDecodeError`, `TextDecodeError`
  - Validation errors: `RequestValidationError`

**Available Adapters:**
- **stdlib_adapter.py**: Zero-dependency adapter using Python's urllib
- **httpx_adapter.py**: Modern async-capable adapter (requires `httpx`)
- **urllib3_adapter.py**: High-performance adapter with connection pooling (requires `urllib3`)
- **requests_adapter.py**: Popular adapter using the requests library (requires `requests`)

**Creating HTTP Clients:**
Use `create_http_client()` factory function from `satvu_api_sdk.http`:
```python
from satvu_api_sdk.http import create_http_client

# Auto-detect best available library (httpx → requests → urllib3 → stdlib)
client = create_http_client()

# Specify backend explicitly
client = create_http_client(backend="httpx", base_url="https://api.example.com")

# Zero dependencies - always works
client = create_http_client(backend="stdlib")
```

**Error Handling Pattern:**
All adapters return `Result[HttpResponse, HttpError]`, allowing callers to handle errors explicitly:
```python
result = client.request("GET", url)
match result:
    case Ok(response):
        # Handle successful response
        json_result = response.json()
    case Err(error):
        # Handle specific error types
        if isinstance(error, NetworkError):
            # Retry logic
        elif isinstance(error, ClientError):
            # Client error handling
```

### Authentication

Authentication is handled by `AuthService` (src/satvu_api_sdk/auth.py):
- Uses OAuth2 client credentials flow
- Supports token caching via `TokenCache` protocol
- Two cache implementations: `MemoryCache` (default) and `AppDirCache` (file-based)
- Automatically checks token expiration and refreshes when needed

### Builder System

The builder system (`src/builder/`) generates SDK code from OpenAPI specifications:

**Key Files:**
1. **load.py**: Fetches OpenAPI specs from SatVu APIs, resolves external $refs, and bundles them into a single schema. Uses caching in `.cache/` directory.

2. **build.py**: Orchestrates SDK generation using a custom `SatVuProject` class that extends openapi-python-client's Project. Key features:
   - Strips version prefixes (e.g., `/v2/`) from endpoint paths
   - Generates body docstrings for request bodies including Union types
   - Detects and adds pagination support for STAC-compliant endpoints
   - Uses custom Jinja2 templates from `src/builder/templates/`

3. **openapi_preprocessor.py**: Preprocesses OpenAPI specs before generation to handle SatVu-specific patterns

4. **patches.py**: Monkey patches openapi-python-client to customize code generation behavior

**Templates:**
Jinja2 templates in `src/builder/templates/` define the structure of generated code:
- `endpoint_module.py.jinja`: Main template for service classes with endpoint methods
- `macros/return_annotation.jinja`: Generates return type annotations (handles 204 No Content, Union types, redirects)
- `model.py.jinja`: Template for Pydantic model classes
- Property templates: Define how different property types are rendered

**CRITICAL - Template Whitespace:**
When modifying Jinja2 templates, use `{%-` and `-%}` to strip whitespace. Regular `{%` and `%}` will introduce line breaks in generated code. This is especially important in `macros/return_annotation.jinja` which renders inline in function signatures.

### Response Parsing

The SDK uses Pydantic's TypeAdapter for robust, performant response parsing (src/satvu_api_sdk/shared/parsing.py):

**Core Parsing Function:**
- `parse_response()`: Wrapper around Pydantic's TypeAdapter
- Handles Union types, nested models, type coercion, and validation
- Leverages Pydantic's Rust core for optimal performance
- Returns strongly-typed Pydantic models from JSON responses

**Key Advantages:**

1. **Native Union Resolution**: Pydantic's smart discriminator detection automatically handles Union types efficiently
2. **Type Coercion**: Automatically converts types (e.g., `"100"` → `100`, `"2025-01-01"` → `datetime`)
3. **TypeAdapter Caching**: Type adapters are cached and reused for performance
4. **Comprehensive Validation**: Full Pydantic validation with detailed error messages
5. **Zero Custom Logic**: No manual type introspection or try-each loops

**Example:**
```python
from satvu_api_sdk.shared.parsing import parse_response

# Parse Union types - Pydantic handles discrimination
annotation = FeatureCollectionOrder | ResellerFeatureCollectionOrder

data_without_reseller = {"id": "...", "features": [...]}
result1 = parse_response(data_without_reseller, annotation)
# → FeatureCollectionOrder (no reseller_end_user_id field)

data_with_reseller = {"reseller_end_user_id": "...", "id": "...", "features": [...]}
result2 = parse_response(data_with_reseller, annotation)
# → ResellerFeatureCollectionOrder (has reseller_end_user_id field)

# Type coercion works automatically
data_with_string_int = {"id": "...", "amount": "100"}  # amount is string
result3 = parse_response(data_with_string_int, Order)
# → Order with amount=100 (coerced to int)
```

**Error Handling:**
When validation fails, provides detailed error messages showing:
- Which fields failed validation
- Why each field failed
- Data structure that was provided
- Full Pydantic ValidationError details

**Debug Logging:**
Enable `logging.DEBUG` for `satvu_api_sdk.shared.parsing` to see TypeAdapter cache hits and parsing details

**Key Normalization:**
The parsing module includes a `normalize_keys()` helper function that recursively converts colons in dictionary keys to underscores (e.g., `geo:lat` → `geo_lat`). This is useful for APIs that return keys with colons, which aren't valid Python identifiers.

### Pagination Support

The SDK provides built-in pagination support for STAC-compliant endpoints through `SDKClient.extract_next_token()` (src/satvu_api_sdk/core.py):

**How it works:**
- Extracts pagination tokens from STAC `links` array with `rel="next"`
- Handles both GET (token in URL query param) and POST (token in request body) patterns
- Returns `None` when no more pages are available

**Auto-detection:**
The builder system automatically detects paginated endpoints during SDK generation based on:
1. Presence of `token` query parameter or token field in request body
2. Response has `links` array field
3. Response has an items array field (e.g., `features`, `orders`, `users`)

When detected, generated service methods include pagination support with `items_field`, `items_type`, and `has_limit_param` metadata.

### Streaming Downloads

The SDK provides memory-efficient streaming download functionality for large binary files (1GB+) through auto-generated `*_to_file()` methods.

**Architecture:**

1. **Core Implementation (src/satvu_api_sdk/core.py)**:
   - `SDKClient.stream_to_file()`: Base method that handles chunked streaming to disk
   - Uses `response.iter_bytes(chunk_size)` for memory-efficient downloads
   - Supports progress callbacks for UX integration
   - Returns `Path` object pointing to downloaded file

2. **Auto-Generation (src/builder/streaming_post_processor.py)**:
   - Detects download endpoints based on response Content-Type (application/zip, application/octet-stream)
   - Automatically generates `*_to_file()` variants for each download endpoint
   - Adds proper imports, type hints, and Result type handling

**Generated Method Signature:**
```python
def download_order_to_file(
    self,
    contract_id: UUID,
    order_id: UUID,
    output_path: Path | str,
    chunk_size: int = 8192,
    progress_callback: Callable[[int, int | None], None] | None = None,
    timeout: int | None = None,
) -> Result[Path, HttpError]:
    """
    Order download - save to disk (memory-efficient for large files).

    Downloads directly to disk using streaming, avoiding loading
    the entire file into memory. Ideal for large files (1GB+).
    """
```

**Key Features:**

- **Memory Efficient**: Streams chunks to disk without loading entire file into memory
- **Progress Tracking**: Optional callback receives `(bytes_downloaded, total_bytes)`
- **Configurable Chunk Size**: Default 8KB, recommend 64KB+ for large files
- **Result Type**: Returns `Result[Path, HttpError]` for explicit error handling
- **Automatic Detection**: Builder auto-generates methods for binary download endpoints

**Usage Example:**
```python
from pathlib import Path
from satvu_api_sdk import SatVuSDK

sdk = SatVuSDK(client_id="...", client_secret="...")

# Progress callback for UX
def show_progress(bytes_downloaded: int, total_bytes: int | None):
    if total_bytes:
        percent = (bytes_downloaded / total_bytes) * 100
        print(f"Progress: {percent:.1f}%")

# Download with streaming
result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order_id,
    output_path=Path("/tmp/order.zip"),
    chunk_size=65536,  # 64KB chunks
    progress_callback=show_progress,
)

# Handle Result type
if result.is_ok():
    path = result.unwrap()
    print(f"Downloaded to: {path}")
else:
    error = result.unwrap_or(None)
    print(f"Download failed: {error}")
```

**Builder Integration:**

The streaming post-processor (`add_streaming_methods()`) runs after initial code generation:
1. Parses generated API file to find download endpoints
2. Detects endpoints with binary response types (ZIP, octet-stream)
3. Generates `*_to_file()` method that wraps the base download endpoint
4. Injects code at the end of the service class with proper formatting

**For OpenAPI Spec Authors:**

Mark download endpoints with specific response content types:
```yaml
responses:
  '200':
    content:
      application/zip:  # Auto-detected for streaming
        schema:
          type: string
          format: binary
```

Supported content types for auto-detection:
- `application/zip`
- `application/octet-stream`
- Any binary format returning large files

**Testing:**

Comprehensive unit tests in `src/satvu_api_sdk/core_streaming_test.py` cover:
- Various chunk patterns and sizes
- Content-Length header handling (present, missing, invalid)
- Progress callback invocation
- Binary data streaming
- Error propagation
- Parent directory requirements
- File overwriting behavior

See `examples/cos.py` and `examples/otm.py` for complete working examples.

### Generated Code

Generated code lives in `src/satvu_api_sdk/services/{api_name}/`:
- `api.py`: Service class with endpoint methods
- `models/`: Pydantic models for request/response types
- Models are generated per-API to avoid naming conflicts

## Key Implementation Notes

### Exception Handling

The SDK provides two error handling approaches:

**1. Legacy Exceptions (src/satvu_api_sdk/exceptions.py):**
- `SatVuAPIError`: Base exception with detailed context (status_code, response_body, request_url, request_method)
- Specific exceptions: `AuthenticationError` (401), `AuthorizationError` (403), `NotFoundError` (404), `ValidationError` (422), `RateLimitError` (429), `ServerError` (5xx)
- Used by the older `SDKClient` implementation

**2. Result Type System (src/satvu_api_sdk/http/):**
- Modern approach using `Result[Ok[T], Err[E]]` types for explicit error handling
- No exceptions thrown during normal operation
- Used by the HTTP adapter system
- Enables Railway-Oriented Programming patterns with `.map()`, `.and_then()`, `.or_else()` methods
- See `docs/TYPED_ERRORS_GUIDE.md` for comprehensive guide with examples and best practices

### When Regenerating SDKs

- The builder clears `NEW_COMPONENTS` before each run to avoid component pollution
- Set `openapi_python_client.parser.openapi.models_relative_prefix` to API name to ensure proper model imports
- Generated code overwrites existing files (overwrite=True in Config)

### Environment Configuration

- `env` parameter controls which SatVu environment to use (None = production, "qa" = QA environment)
- Base URLs are constructed as: `https://{subdomain}.{env}.satellitevu.com/`
- Auth service uses "auth" subdomain, all others use "api" subdomain

### Working with API Clients

Service methods:
- Accept Pydantic models or primitives as parameters
- Return Pydantic models for successful responses (status 200)
- Return `None` for 204 No Content responses (empty body)
- Return raw JSON dict for error responses
- Use `model_dump(by_alias=True)` when serializing request bodies

**Response Code Handling:**
Generated endpoint methods handle different HTTP status codes:
- **200 OK**: Parse and return response body as Pydantic model
- **201 Created**: Parse and return response body as Pydantic model
- **204 No Content**: Return `None` (no body to parse)
- **3xx Redirects**: Some endpoints handle redirects for file downloads, returning `io.BytesIO`
- **4xx/5xx Errors**: Return `HttpError` via Result type

The template system (`endpoint_module.py.jinja` and `macros/return_annotation.jinja`) automatically generates the correct handling logic and return type annotations based on the OpenAPI spec.

### Dependencies

**Core Dependencies:**
- `pydantic>=2.11.7`: Data validation and models (required)

**Optional Dependencies:**
- `[standard]`: Includes `appdirs` for file-based token caching
- `[http-httpx]`: Includes `httpx` for httpx adapter (modern, async-capable)
- `[http-urllib3]`: Includes `urllib3` for urllib3 adapter (high-performance with connection pooling)
- `[http-requests]`: Includes `requests` for requests adapter (popular, widely-used)

The SDK includes a zero-dependency stdlib adapter that uses Python's built-in `urllib`, so HTTP functionality works without any optional dependencies.

Install with extras: `uv pip install satvu-api-sdk[standard,http-httpx,http-urllib3,http-requests]`
