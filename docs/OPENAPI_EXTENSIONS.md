# OpenAPI Extensions for SatVu API SDK Generation

This document describes custom OpenAPI extensions used by the SatVu API SDK builder to enhance generated client code.

## Table of Contents

- [Streaming Download Methods](#streaming-download-methods)
- [Auto-Detection Rules](#auto-detection-rules)
- [Examples](#examples)
- [Testing Your Changes](#testing-your-changes)

---

## Streaming Download Methods

### `x-streaming-download`

**Type:** `boolean`
**Default:** `false`
**Location:** Operation object (e.g., under a path's `get`, `post`, etc.)
**Status:** ⚠️ **Planned for future implementation**

This extension is documented for future use to explicitly mark endpoints that should generate streaming download variants. Currently, the SDK builder uses **automatic pattern-based detection** instead (see Auto-Detection Rules below).

When implemented, setting `x-streaming-download: true` will create an additional `*_to_file()` method that downloads files directly to disk without loading them into memory.

**Generated method naming:**
- Base method: `download_order__get()` → Streaming method: `download_order_to_file()`
- The `_to_file` suffix clearly indicates the method saves directly to disk

**Current behavior:**
The builder automatically detects download endpoints by pattern matching (GET requests with `/download` in the path and a `redirect` parameter), so adding this extension has no effect yet.

### `x-streaming-config`

**Type:** `object`
**Location:** Operation object (alongside `x-streaming-download`)
**Optional:** Yes

Customizes the behavior of the generated streaming method.

#### Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `default_chunk_size` | integer | 8192 | Default chunk size in bytes for streaming. Common values: 8192 (8KB), 65536 (64KB) |
| `example_filename` | string | "download.zip" | Filename to use in documentation examples |
| `description_override` | string | (auto-generated) | Custom description for the streaming method |

---

## Auto-Detection Rules

The SDK builder will **automatically detect** download endpoints using these heuristics:

### Detection Strategy (in order)

1. **Pattern-Based Detection** (primary)
   - HTTP method is `GET`
   - Path contains `/download`
   - Has a `redirect` query parameter with type `boolean`

2. **Response-Based Detection** (fallback)
   - Returns a 3xx redirect response (common for presigned URLs)
   - OR returns binary Content-Type headers

**Note:** The `x-streaming-download` extension is documented for future use but is **not currently implemented**. Auto-detection based on patterns works for all SatVu download endpoints.

---

## Examples

### Example 1: Basic Streaming Download (COS API)

```yaml
openapi: 3.0.3
info:
  title: Customer Order Service API
  version: 2.0.0

paths:
  /{contract_id}/{order_id}/download:
    get:
      summary: Order download
      description: |
        Download all items for a specified imagery order.
        Returns either a presigned URL or redirects to the file.
      operationId: download_order__get

      # ✨ Add this extension to enable streaming
      x-streaming-download: true

      parameters:
        - name: contract_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: order_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: redirect
          in: query
          description: If true, redirect to file; if false, return presigned URL
          schema:
            type: boolean
            default: true

      responses:
        '200':
          description: Presigned download URL with expiry
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderDownloadUrl'
        '302':
          description: Redirect to file download
          headers:
            Location:
              schema:
                type: string
                format: uri
```

**Generated SDK Methods:**

```python
# Standard method (auto-generated from OpenAPI)
def download_order__get(
    self,
    contract_id: UUID,
    order_id: UUID,
    redirect: bool = True,
    timeout: int | None = None,
) -> Union[OrderDownloadUrl, Any, io.BytesIO]:
    """Order download - Download all items for a specified imagery order."""
    ...

# Streaming method (generated because of x-streaming-download: true)
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
    ...
```

### Example 2: Streaming Download with Custom Configuration (OTM API)

```yaml
paths:
  /{contract_id}/tasking/orders/{order_id}/download:
    get:
      summary: Download a tasking order
      description: |
        Download the fulfilled imagery for a tasking order.
        Only available once the order status is 'fulfilled'.
      operationId: download_tasking_order

      # ✨ Enable streaming with custom configuration
      x-streaming-download: true
      x-streaming-config:
        default_chunk_size: 65536  # Use 64KB chunks (faster for large files)
        example_filename: "tasking_order.tif"  # Custom example for docs
        description_override: "Stream high-resolution tasking imagery to disk"

      parameters:
        - name: contract_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: order_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: redirect
          in: query
          schema:
            type: boolean
            default: true

      responses:
        '200':
          description: Download URL
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/OrderItemDownloadUrl'
        '202':
          description: Order not yet fulfilled
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: "Order processing, not yet available for download"
        '302':
          description: Redirect to imagery file
```

**Generated SDK Methods:**

```python
# Standard method
def download_tasking_order(
    self,
    contract_id: UUID,
    order_id: UUID,
    redirect: bool = True,
    timeout: int | None = None,
) -> Union[OrderItemDownloadUrl, Any, io.BytesIO]:
    """Download a tasking order."""
    ...

# Streaming method with custom chunk size
def download_tasking_order_to_file(
    self,
    contract_id: UUID,
    order_id: UUID,
    output_path: Path | str,
    chunk_size: int = 65536,  # ← Custom default from x-streaming-config
    progress_callback: Callable[[int, int | None], None] | None = None,
    timeout: int | None = None,
) -> Result[Path, HttpError]:
    """
    Save high-resolution tasking imagery to disk.

    Downloads directly to disk using streaming, avoiding loading
    the entire file into memory. Ideal for large files (1GB+).

    Example:
        >>> result = sdk.otm.download_tasking_order_to_file(
        ...     contract_id=UUID(...),
        ...     order_id=UUID(...),
        ...     output_path="tasking_order.tif",  # ← Custom example
        ...     chunk_size=65536,
        ... )
    """
    ...
```

### Example 3: Auto-Detection Without Extension

If you don't add the extension, this endpoint will still be detected:

```yaml
paths:
  /{contract_id}/{order_id}/{item_id}/download:
    get:
      summary: Item download
      operationId: download_item__get
      # ❌ No x-streaming-download extension

      parameters:
        - name: contract_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: order_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: item_id
          in: path
          required: true
          schema:
            type: string
        - name: redirect
          in: query
          schema:
            type: boolean
            default: true

      responses:
        '302':
          description: Redirect to file
```

**Auto-detection will trigger because:**
- ✅ Method is GET
- ✅ Path contains `/download`
- ✅ Has `redirect` query parameter
- ✅ Returns 3xx redirect response

**Result:** Streaming method `download_item_to_file()` will be generated automatically.

---

## Testing Your Changes

### 1. Validate Your OpenAPI Spec

Before committing, ensure your spec is valid:

```bash
# Using openapi-generator-cli
openapi-generator-cli validate -i path/to/your/openapi.yaml

# Or using Spectral
spectral lint path/to/your/openapi.yaml
```

### 2. Test SDK Generation

Generate the SDK to verify streaming methods are created:

```bash
# In the satvu-api-sdk repository
cd /path/to/satvu-api-sdk

# Generate for your API (replace 'cos' with your API name)
uv run python -m builder cos

# Check the generated file
cat src/satvu_api_sdk/services/cos/api.py | grep -A 20 "def.*_to_file"
```

### 3. Expected Output

Look for log messages during generation:

```
Building cos service...
  [PAGINATION] Detected for query_orders__get: items_field=orders, items_type=Order
  [STREAMING] Adding 2 streaming method(s) to cos
    ✓ Generated download_order_to_file
    ✓ Generated download_item_to_file
  ✓ Generated to src/satvu_api_sdk/services/cos
```

### 4. Verify Generated Methods

Check that both methods exist:

```python
# In Python REPL
from satvu_api_sdk import SatVuSDK
from uuid import UUID

sdk = SatVuSDK(...)

# Standard method exists
result = sdk.cos.download_order__get(
    contract_id=UUID(...),
    order_id=UUID(...),
    redirect=False,
)

# Streaming method exists
result = sdk.cos.download_order_to_file(
    contract_id=UUID(...),
    order_id=UUID(...),
    output_path="./order.zip",
)
```

---

## Best Practices

### DO ✅

- **Use explicit extensions** for clarity, even when auto-detection works
- **Add descriptive summaries** to help users understand when to use streaming
- **Set appropriate chunk sizes** based on typical file sizes:
  - Small files (<10MB): 8192 (8KB)
  - Medium files (10-100MB): 65536 (64KB)
  - Large files (>100MB): 1048576 (1MB)
- **Document file size expectations** in endpoint descriptions
- **Use realistic example filenames** that match your domain (e.g., `.tif`, `.zip`, `.geotiff`)

### DON'T ❌

- **Don't add streaming to JSON endpoints** - streaming is for binary files only
- **Don't use streaming for small payloads** (<1MB) - standard methods are fine
- **Don't forget the `redirect` parameter** - it's required for proper detection
- **Don't skip testing** - always verify generated code after spec changes

---

## Troubleshooting

### Streaming Method Not Generated

**Problem:** Added `x-streaming-download: true` but no `*_to_file()` method appears.

**Solutions:**
1. Check the build logs for warnings:
   ```
   ⚠ Base method download_foo not found, skipping
   ```
2. Verify your `operationId` matches the base method name
3. Ensure the endpoint is actually in the spec being used for generation
4. Try rebuilding with `--no-cache` flag

### Wrong Method Name Generated

**Problem:** Streaming method has unexpected name like `download_order__get_to_file`.

**Solution:** The method name is derived from `operationId`. Update your `operationId` to control the base name:

```yaml
# Instead of:
operationId: download_order__get

# Use:
operationId: download_order

# This generates:
# - Base: download_order()
# - Streaming: download_order_to_file()
```

### Import Errors in Generated Code

**Problem:** Generated code has import errors for `Path`, `Result`, etc.

**Solution:** This should not happen - file a bug report. The post-processor automatically adds required imports.

---

## Questions?

For questions about OpenAPI extensions:
- **SDK Repository:** https://github.com/satellitevu/satvu-api-sdk
- **Internal Slack:** #api-sdk-support
- **Email:** api-support@satellitevu.com

For questions about OpenAPI specifications:
- **OpenAPI Spec:** https://swagger.io/specification/
- **Extensions Guide:** https://swagger.io/docs/specification/openapi-extensions/
