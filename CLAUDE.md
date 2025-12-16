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

**IMPORTANT:** Always use `uv build` to generate SDK code. This is the canonical build method that ensures templates and source files are correctly processed.

Generate all API SDKs:

```bash
uv build
```

This command:

- Triggers the Hatch build hook (`hatch_build.py`)
- Generates all API SDKs (catalog, cos, id, policy, otm, reseller, wallet)
- Fetches fresh OpenAPI specs
- Correctly processes Jinja2 templates from `src/builder/templates/`
- Packages the distribution

**Alternative (for development only):**

```bash
# Generate specific API (bypasses proper template path resolution)
uv run python -m builder <API_NAME>

# Use cached specs instead of fetching fresh ones
uv run python -m builder <API_NAME> --cached
```

Available API names are defined in `src/builder/config.py`: catalog, cos, id, policy, otm, reseller, wallet.

**Dagger CI:**

```bash
dagger call -v test    # Run pytest suite
dagger call -v lint    # Run linter suite
dagger -c "build-release --is-qa --build-number 123 | export './dist' --wipe"  # Build release
```

## Architecture

### SDK Structure

The SDK has three main layers:

1. **SatVuSDK (src/satvu/sdk.py)**: Main entry point that provides access to all API services via properties (catalog, cos, id, etc.). Uses lazy initialization for services.

2. **Service Classes (src/satvu/services/{api_name}/api.py)**: Auto-generated API clients for each SatVu API. These inherit from SDKClient and contain methods corresponding to API endpoints.

3. **SDKClient (src/satvu/core.py)**: Base class that handles HTTP communication, authentication, URL construction, and request parameter processing. Automatically converts Pydantic models to JSON and filters out None values.

### Result Type System

The SDK uses a Rust-style Result type (src/satvu/result.py) for explicit error handling:

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

The SDK uses a pluggable HTTP adapter system (src/satvu/http/) for maximum flexibility:

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
Use `create_http_client()` factory function from `satvu.http`:

```python
from satvu.http import create_http_client

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

Authentication is handled by `AuthService` (src/satvu/auth.py):

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

The SDK uses Pydantic's TypeAdapter for robust, performant response parsing (src/satvu/shared/parsing.py):

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
from satvu.shared.parsing import parse_response

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
Enable `logging.DEBUG` for `satvu.shared.parsing` to see TypeAdapter cache hits and parsing details

**Key Normalization:**
The parsing module includes a `normalize_keys()` helper function that recursively converts colons in dictionary keys to underscores (e.g., `geo:lat` → `geo_lat`). This is useful for APIs that return keys with colons, which aren't valid Python identifiers.

### Pagination Support

The SDK provides built-in pagination support for STAC-compliant endpoints through `SDKClient.extract_next_token()` (src/satvu/core.py):

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

1. **Core Implementation (src/satvu/core.py)**:

   - `SDKClient.stream_to_file()`: Base method that handles chunked streaming to disk
   - Uses `response.iter_bytes(chunk_size)` for memory-efficient downloads
   - Supports progress callbacks for UX integration
   - Returns `Path` object pointing to downloaded file

2. **Auto-Generation System**:

   **streaming_detector.py**: Detects which endpoints need streaming variants

   - Checks for `x-streaming-download` extension in OpenAPI spec
   - Separates path parameters (used in URL formatting) from query parameters (added to params dict)
   - Builds `StreamingEndpointConfig` with separate `path_params` and `query_params` lists
   - Example: `contract_id`, `order_id` are path params; `collections`, `primary_formats` are query params

   **ast_generator.py**: Generates streaming method code using Python's AST module

   - `ASTMethodBuilder` class builds syntactically correct function AST nodes
   - Path params become required positional parameters
   - Query params become keyword-only parameters with `None` defaults
   - Guarantees type-safe code generation without string template fragility
   - Key methods:
     - `build_method()`: Orchestrates complete function generation
     - `_build_arguments()`: Creates proper function signature with type annotations
     - `_build_body()`: Generates method body (URL formatting uses only path params, params dict includes query params)
     - `_build_docstring()`: Creates structured docstring with parameter documentation

   **streaming_post_processor.py**: Coordinates the generation process

   - Parses generated API file as AST
   - Uses `add_imports_to_ast()` for intelligent import handling
   - Uses `generate_streaming_method()` for AST-based code generation
   - Uses `insert_method_after_base()` for AST manipulation
   - Converts AST back to code with `ast.unparse()`
   - Formats with Black if available (graceful fallback)

**Generated Method Signature:**

```python
def download_order_to_file(
    self,
    contract_id: UUID,           # Path param (required positional)
    order_id: UUID,              # Path param (required positional)
    output_path: Path | str,     # Required positional
    *,                           # Keyword-only separator
    collections: list[...] | None = None,        # Query param (keyword-only)
    primary_formats: list[...] | None = None,   # Query param (keyword-only)
    chunk_size: int = 8192,
    progress_callback: Callable[[int, int | None], None] | None = None,
    timeout: int | None = None,
) -> Result[Path, HttpError]:
    """
    Order download - save to disk (memory-efficient for large files).

    Downloads directly to disk using streaming, avoiding loading
    the entire file into memory. Ideal for large files (1GB+).
    """
    params = {
        "redirect": True,
        "collections": collections,          # Query params in params dict
        "primary_formats": primary_formats,  # Query params in params dict
    }
    result = self.make_request(
        method="get",
        url="/{contract_id}/orders/{order_id}/download".format(
            contract_id=contract_id,  # Only path params in URL format
            order_id=order_id,        # Only path params in URL format
        ),
        params=params,
        ...
    )
```

**Key Features:**

- **Memory Efficient**: Streams chunks to disk without loading entire file into memory
- **Progress Tracking**: Optional callback receives `(bytes_downloaded, total_bytes)`
- **Configurable Chunk Size**: Default 8KB, recommend 64KB+ for large files
- **Result Type**: Returns `Result[Path, HttpError]` for explicit error handling
- **Automatic Detection**: Builder auto-generates methods for binary download endpoints
- **Type Safety**: AST-based generation guarantees syntactically correct code
- **Proper Parameter Handling**: Path params in URL format, query params in params dict
- **Keyword-Only Query Params**: Query parameters are keyword-only with None defaults for better API ergonomics

**Usage Example:**

```python
from pathlib import Path
from satvu import SatVuSDK

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

The streaming generation system runs after initial SDK code generation:

1. **Detection Phase** (`streaming_detector.py`):

   - Scans OpenAPI spec for endpoints with `x-streaming-download: true` extension
   - Extracts endpoint metadata (path, method, parameters)
   - Separates path parameters from query parameters
   - Builds `StreamingEndpointConfig` objects with all necessary information

2. **Generation Phase** (`ast_generator.py`):

   - Constructs Python AST nodes for streaming methods
   - Builds function signature with proper type annotations
   - Path params → required positional parameters
   - Query params → keyword-only parameters with defaults
   - Generates method body with correct parameter usage
   - Creates comprehensive docstrings

3. **Integration Phase** (`streaming_post_processor.py`):

   - Parses generated API file as AST
   - Adds missing imports (Path, HttpError, Result, ResultOk)
   - Generates streaming method code using AST builder
   - Inserts new method into class AST after base method
   - Converts AST back to Python code
   - Formats with Black if available

**Benefits of AST-Based Generation:**

- Eliminates string template fragility and escaping issues
- Guarantees syntactically correct Python code
- Automatic handling of complex type annotations
- Proper line number and column offset tracking
- No manual string manipulation or formatting

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

Comprehensive unit tests in `src/satvu/core_streaming_test.py` cover:

- Various chunk patterns and sizes
- Content-Length header handling (present, missing, invalid)
- Progress callback invocation
- Binary data streaming
- Error propagation
- Parent directory requirements
- File overwriting behavior

See `examples/cos.py` and `examples/otm.py` for complete working examples.

### Automated Test Generation

The builder includes an extensible test generation system that automatically creates integration tests during SDK generation. This system uses a template-based approach with AST manipulation for reliable, type-safe test generation.

**Architecture Pattern:**

The test generation system follows a consistent pattern that can be extended for different test categories:

1. **Generator Module** (`src/builder/*_test_generator.py`):
   - Accepts metadata about endpoints that need tests
   - Uses Jinja2 templates from `src/builder/templates/macros/`
   - Parses existing test file as AST
   - Renders test code from templates
   - Parses rendered code into AST nodes
   - Appends new test methods to test class
   - Formats with ruff (auto-fix + format)

2. **Template Macros** (`src/builder/templates/macros/*_tests.jinja`):
   - Define reusable test patterns as Jinja2 macros
   - Support type-aware parameter generation
   - Include proper whitespace control with `{%-` and `-%}`
   - Generate syntactically correct Python with proper indentation

3. **Integration Hook** (in post-processors or `build.py`):
   - Called after main code generation
   - Receives `Project` object for Jinja2 environment access
   - Graceful error handling with warnings (non-fatal)

**Example: Streaming Test Generator**

Location: `src/builder/streaming_test_generator.py`

Generates three test types for each streaming download method:
- **Success test**: Validates file writing with mocked content
- **Progress callback test**: Validates progress callback invocation
- **Error test**: Validates error propagation (404, etc.)

Key implementation details:
```python
def generate_streaming_tests(
    api_name: str,
    streaming_configs: list[StreamingEndpointConfig],
    test_file: Path,
    jinja_env: Environment,
) -> None:
    """Generate and append streaming method tests to existing test file."""

    # Parse existing test file
    content = test_file.read_text()
    tree = ast.parse(content)

    # Find test class
    test_class = _find_test_class(tree)

    # Render tests from templates
    for config in streaming_configs:
        context = {"config": config, "api_name": api_name}

        test_code = jinja_env.from_string(
            "{% from 'macros/streaming_tests.jinja' import streaming_success_test %}"
            "{{ streaming_success_test(config, api_name) }}"
        ).render(context)

        # Parse rendered test into AST node
        test_method = ast.parse(test_code).body[0]

        # Append to test class
        test_class.body.append(test_method)

    # Write back and format
    final_code = ast.unparse(tree)
    test_file.write_text(final_code)
    _format_with_ruff(test_file)
```

**Template Example** (`src/builder/templates/macros/streaming_tests.jinja`):
```jinja
{%- macro streaming_success_test(config, api_name) -%}
@pook.on
def test_{{ config.stream_method }}_success(self, backend, tmp_path):
    """Test {{ config.stream_method }} writes file correctly."""
    output_path = tmp_path / "{{ config.example_filename }}"
    mock_content = b"fake zip content"

    {#- Type-aware parameter generation -#}
    {% for param_name, param_type in config.path_params %}
    {{ param_name }} = {% if param_type == "str" %}str(uuid4()){% else %}uuid4(){% endif %}

    {% endfor %}
    path = "{{ config.url_pattern }}".format(
    {%- for param_name, param_type in config.path_params %}
        {{ param_name }}={{ param_name }}{% if not loop.last %},{% endif %}
    {%- endfor %}
    )

    # Test implementation...
{%- endmacro -%}
```

**Key Design Principles:**

1. **Type-Aware Generation**: Templates use conditional logic to generate correct code based on parameter types (e.g., `str(uuid4())` vs `uuid4()`)

2. **Whitespace Control**: Critical for Jinja2 templates - use `{%-` and `-%}` to prevent unwanted line breaks. Always add explicit blank lines in template loops.

3. **AST-Based Manipulation**: Guarantees syntactically correct Python without string fragility. Use `ast.parse()` and `ast.unparse()` for reliability.

4. **Graceful Degradation**: Test generation failures should warn but not fail the build. Wrap in try/except with traceback printing.

5. **Ruff Formatting**: Always format generated code with `ruff check --fix` then `ruff format` for consistency.

6. **Reusable Pattern**: This architecture can be extended for other test categories (pagination, webhooks, rate limiting, etc.) by following the same structure.

**Extending for New Test Categories:**

To add tests for a new feature category (e.g., pagination):

1. Create `src/builder/pagination_test_generator.py` following the pattern
2. Create `src/builder/templates/macros/pagination_tests.jinja` with test macros
3. Call generator from post-processor or build system
4. Ensure generator receives `Project.env` for Jinja2 access
5. Follow existing patterns for AST manipulation and formatting

The streaming test generator serves as a reference implementation for this extensible pattern.

### Generated Code

Generated code lives in `src/satvu/services/{api_name}/`:

- `api.py`: Service class with endpoint methods
- `models/`: Pydantic models for request/response types
- Models are generated per-API to avoid naming conflicts

## Key Implementation Notes

### Exception Handling

The SDK provides two error handling approaches:

**1. Legacy Exceptions (src/satvu/exceptions.py):**

- `SatVuAPIError`: Base exception with detailed context (status_code, response_body, request_url, request_method)
- Specific exceptions: `AuthenticationError` (401), `AuthorizationError` (403), `NotFoundError` (404), `ValidationError` (422), `RateLimitError` (429), `ServerError` (5xx)
- Used by the older `SDKClient` implementation

**2. Result Type System (src/satvu/http/):**

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

Install with extras: `uv pip install satvu[standard,http-httpx,http-urllib3,http-requests]`
