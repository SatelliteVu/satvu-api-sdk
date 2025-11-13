# OpenAPI Extensions for SatVu API SDK Generation

This document describes custom OpenAPI extensions used by the SatVu API SDK builder to enhance generated client code.

**Audience:** This documentation is for API spec authors and maintainers who write OpenAPI specifications. If you're an SDK user looking for usage examples, see `examples/cos.py` or `examples/otm.py`.

## Table of Contents

- [Streaming Download Methods](#streaming-download-methods)
- [Testing Your Changes](#testing-your-changes)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## Streaming Download Methods

The SDK builder supports custom OpenAPI extensions for explicitly marking endpoints that should have memory-efficient streaming download methods generated.

### `x-streaming-download`

**Type:** `boolean`
**Default:** `false`
**Location:** Operation object (e.g., under a path's `get`, `post`, etc.)
**Status:** ✅ **Fully Implemented**

This extension explicitly controls streaming method generation. When set to `true`, the SDK builder generates a `*_to_file()` variant of the endpoint method that streams responses directly to disk without loading the entire file into memory.

**Generated method naming:**
- Base method: `download_order__get()` → Streaming method: `download_order_to_file()`
- Base method: `download_order()` → Streaming method: `download_order_to_file()`
- The `_to_file` suffix clearly indicates the method saves directly to disk

**Example:**
```yaml
paths:
  /{contract_id}/{order_id}/download:
    get:
      summary: Order download
      operationId: download_order__get
      x-streaming-download: true  # ← Enables streaming method generation
      x-streaming-config:
        default_chunk_size: 8192
        example_filename: "order.zip"
        description_override: "Stream high-resolution imagery to disk"
      # ... parameters and responses ...
```

### `x-streaming-config`

**Type:** `object`
**Location:** Operation object (alongside `x-streaming-download`)
**Optional:** Yes
**Status:** ✅ **Fully Implemented**

This extension customizes the behavior and documentation of generated streaming methods.

#### Supported Properties

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `default_chunk_size` | integer | 8192 | Default chunk size in bytes for streaming. Common values: 8192 (8KB), 65536 (64KB). SDK users can override this at call time. |
| `example_filename` | string | "download.zip" | Filename to use in documentation examples and parameter documentation. |
| `description_override` | string | (auto-generated from summary) | Custom description for the streaming method docstring. If not provided, the builder generates a description based on the endpoint's summary. |

**Example:**
```yaml
x-streaming-config:
  default_chunk_size: 65536          # 64KB chunks for faster downloads
  example_filename: "imagery.tif"    # Reflects actual file type
  description_override: "Stream large thermal imagery files efficiently to disk without loading into memory"
```

---

## Detection Strategy

The SDK builder generates streaming methods **only** for endpoints that are explicitly marked with `x-streaming-download: true`. There are no fallback heuristics or automatic detection.

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

### 2. Add Streaming Extensions

Mark download endpoints with the extensions:

```yaml
paths:
  /your/download/endpoint:
    get:
      # ... operationId, parameters, etc. ...

      # Add these extensions
      x-streaming-download: true
      x-streaming-config:
        default_chunk_size: 8192
        example_filename: "download.zip"
        description_override: "Stream large files to disk efficiently"
```

### 3. Test SDK Generation

Generate the SDK to verify streaming methods are created:

```bash
# In the satvu-api-sdk repository
cd /path/to/satvu-api-sdk

# Generate for your API (replace 'cos' with your API name)
uv run python -m builder cos

# Check the generated file
cat src/satvu_api_sdk/services/cos/api.py | grep -A 5 "def.*_to_file"
```

### 4. Expected Output

Look for log messages during generation:

```
Building cos service...
  [STREAMING] Adding 2 streaming method(s) to cos
    ✓ Generated download_order_to_file
    ✓ Generated download_item_to_file
  ✓ Generated to src/satvu_api_sdk/services/cos
```

---

## Best Practices

### DO ✅

- **Add `x-streaming-download: true`** to all download endpoints that return large binary files (>10MB)
- **Configure `default_chunk_size`** appropriately:
  - Use 8192 (8KB) for general-purpose downloads
  - Use 65536 (64KB) or larger for high-bandwidth, large file downloads
- **Provide `description_override`** with context about the file type and size expectations
- **Use realistic `example_filename`** that matches your domain (e.g., `.tif`, `.zip`, `.geotiff`)
- **Document file size expectations** in endpoint descriptions (e.g., "Returns large binary file, may be 1GB+")
- **Test generated methods** after spec changes to verify streaming methods appear

### DON'T ❌

- **Don't add `x-streaming-download: true`** to endpoints that return JSON or small responses
- **Don't set extremely large `default_chunk_size`** (>1MB) - it can cause memory issues
- **Don't forget to validate** your OpenAPI spec after adding extensions
- **Don't skip testing** - always verify generated code after spec changes
- **Don't use streaming for small files** (<10MB) - the overhead isn't worth it

---

## Troubleshooting

### Streaming Method Not Generated

**Problem:** Expected a `*_to_file()` method but it's not appearing in generated code.

**Solutions:**

1. **Check the OpenAPI spec**: Ensure `x-streaming-download: true` is present on the operation
   ```bash
   # Search for the extension in your spec
   grep -A 5 "x-streaming-download" path/to/openapi.yaml
   ```

2. **Verify the extension location**: The extension must be on the operation object (get/post), not on the path object
   ```yaml
   # ✅ Correct
   paths:
     /download:
       get:
         x-streaming-download: true

   # ❌ Wrong - will not work
   paths:
     /download:
       x-streaming-download: true
       get:
         # ...
   ```

3. **Check build logs** for streaming detection:
   ```
   [STREAMING] Adding 2 streaming method(s) to cos
     ✓ Generated download_order_to_file
     ✓ Generated download_item_to_file
   ```

4. **Rebuild from scratch**: Clear cache and regenerate
   ```bash
   rm -rf .cache/
   uv pip install -e . --force-reinstall --no-deps
   uv run python -m builder <api_name>
   ```

### Wrong Chunk Size Default

**Problem:** Generated method has wrong `chunk_size` default value.

**Solution:** Check the `x-streaming-config.default_chunk_size` value in your OpenAPI spec:

```yaml
x-streaming-config:
  default_chunk_size: 65536  # ← This value is used in generated code
```

If not specified, defaults to 8192 bytes.

### Wrong Method Name Generated

**Problem:** Streaming method has unexpected name like `download_order__get_to_file`.

**Solution:** The streaming method name is derived from the base method name by:
1. Taking the base method name (e.g., `download_order__get`)
2. Removing the `__get` suffix if present
3. Appending `_to_file`

Result: `download_order__get` → `download_order_to_file`

If you want cleaner names, use simpler `operationId` values:

```yaml
# Instead of:
operationId: download_order__get

# Use:
operationId: download_order

# This generates cleaner names:
# - Base: download_order()
# - Streaming: download_order_to_file()
```

### Custom Description Not Applied

**Problem:** Generated streaming method doesn't use my `description_override`.

**Solution:** Ensure `description_override` is in `x-streaming-config`, not at the top level:

```yaml
# ✅ Correct
x-streaming-download: true
x-streaming-config:
  description_override: "My custom description"

# ❌ Wrong
x-streaming-download: true
description_override: "My custom description"  # Ignored
```

---

## Extension Validation

To ensure your extensions are valid, you can use this JSONSchema:

```json
{
  "x-streaming-download": {
    "type": "boolean",
    "description": "Enable streaming download method generation"
  },
  "x-streaming-config": {
    "type": "object",
    "properties": {
      "default_chunk_size": {
        "type": "integer",
        "minimum": 1024,
        "maximum": 1048576,
        "description": "Default chunk size in bytes (1KB-1MB)"
      },
      "example_filename": {
        "type": "string",
        "pattern": "^[a-zA-Z0-9_.-]+$",
        "description": "Example filename for documentation"
      },
      "description_override": {
        "type": "string",
        "minLength": 10,
        "description": "Custom description for streaming method"
      }
    },
    "additionalProperties": false
  }
}
```

---
