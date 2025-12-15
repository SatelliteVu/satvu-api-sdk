# Streaming Downloads

The SDK provides memory-efficient streaming downloads for large satellite imagery files. Instead of loading entire files into memory, data is streamed directly to disk in chunks.

## Basic Usage

Use the `*_to_file` methods for streaming downloads:

```python
from pathlib import Path
from satvu_api_sdk.result import is_ok, is_err

# Download an order to disk
result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order_id,
    output_path=Path("./order.zip"),
)

if is_ok(result):
    path = result.unwrap()
    print(f"Downloaded to: {path}")
else:
    error = result.unwrap_err()
    print(f"Download failed: {error}")
```

## Progress Tracking

Track download progress with a callback:

```python
def show_progress(bytes_downloaded: int, total_bytes: int | None):
    if total_bytes:
        percent = (bytes_downloaded / total_bytes) * 100
        print(
            f"Progress: {percent:.1f}% ({bytes_downloaded:,} / {total_bytes:,} bytes)"
        )
    else:
        # Content-Length header not available
        print(f"Downloaded: {bytes_downloaded:,} bytes")


result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order_id,
    output_path=Path("./order.zip"),
    progress_callback=show_progress,
)
```

## Chunk Size

Adjust chunk size for performance tuning:

```python
result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order_id,
    output_path=Path("./order.zip"),
    chunk_size=65536,  # 64KB chunks (default is 8KB)
)
```

## Download Individual Items

Download a specific item from an order:

```python
result = sdk.cos.download_order_item_to_file(
    contract_id=contract_id,
    order_id=order_id,
    item_id=item_id,
    output_path=Path(f"./item_{item_id}.zip"),
    chunk_size=65536,
    progress_callback=show_progress,
)
```

## Complete Example

```python
import os
import tempfile
from pathlib import Path
from uuid import UUID

from satvu_api_sdk import SatVuSDK
from satvu_api_sdk.result import is_ok, is_err

sdk = SatVuSDK(
    client_id=os.environ["SATVU_CLIENT_ID"],
    client_secret=os.environ["SATVU_CLIENT_SECRET"],
)

contract_id = UUID(os.environ["SATVU_CONTRACT_ID"])
order_id = UUID("your-order-id")

# Create output path
output_dir = Path(tempfile.gettempdir())
output_path = output_dir / f"order_{order_id}.zip"


# Progress tracking
def progress(downloaded: int, total: int | None):
    if total:
        pct = (downloaded / total) * 100
        print(f"\rDownloading: {pct:.1f}%", end="", flush=True)


# Stream download
print(f"Downloading order {order_id}...")
result = sdk.cos.download_order_to_file(
    contract_id=contract_id,
    order_id=order_id,
    output_path=output_path,
    chunk_size=65536,
    progress_callback=progress,
)

if is_ok(result):
    saved_path = result.unwrap()
    size_mb = saved_path.stat().st_size / (1024 * 1024)
    print(f"Downloaded {size_mb:.1f} MB to {saved_path}")
else:
    print(f"Download failed: {result.unwrap_err()}")
```

## Error Handling

Streaming methods return `Result[Path, HttpError]`:

```python
from satvu_api_sdk.result import is_ok, is_err
from satvu_api_sdk.http import NetworkError, ServerError

result = sdk.cos.download_order_to_file(...)

if is_err(result):
    error = result.unwrap_err()

    if isinstance(error, NetworkError):
        print("Network error - check your connection")
    elif isinstance(error, ServerError):
        print(f"Server error: {error.status_code}")
    else:
        print(f"Download failed: {error}")
```

See [Error Handling](error-handling.md) for more details on working with Result types.
