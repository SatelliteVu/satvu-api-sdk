"""Post-processor to add streaming download methods to generated API services."""

from pathlib import Path

from openapi_python_client.parser.openapi import Endpoint

from builder.streaming_detector import (
    StreamingEndpointConfig,
    StreamingEndpointDetector,
)

# Template for streaming methods
STREAMING_METHOD_TEMPLATE = """
    def {stream_method}(
        self,
{params_signature}        output_path: Path | str,
{collections_param_signature}        chunk_size: int = {default_chunk_size},
        progress_callback: Callable[[int, int | None], None] | None = None,
        timeout: int | None = None,
    ) -> Result[Path, HttpError]:
        \"\"\"
        {docstring}

        Downloads directly to disk using streaming, avoiding loading
        the entire file into memory. Ideal for large files (1GB+).

        Args:
{params_docs}            output_path (Path | str): Where to save the downloaded file.
{collections_param_docs}            chunk_size (int): Bytes per chunk (default: {default_chunk_size}). Use 64KB+ for faster downloads.
            progress_callback: Optional callback for download progress tracking.
                             Signature: callback(bytes_downloaded: int, total_bytes: int | None)
            timeout: Optional request timeout in seconds. Overrides the instance timeout.

        Returns:
            Result[Path, HttpError]: Ok(Path) on success, Err(HttpError) on failure
        \"\"\"
        params = {{
            "redirect": True,  # Always use redirect for streaming
{extra_params}        }}

        result = self.make_request(
            method="get",
            url="{url_pattern}".format(
{url_format_args}            ),
            params=params,
            follow_redirects=True,
            timeout=timeout,
        )

        # Return error if request failed
        if result.is_err():
            return result  # type: ignore

        response = result.unwrap()

        # Stream to disk and return Path
        downloaded_path = self.stream_to_file(
            response=response,
            output_path=output_path,
            chunk_size=chunk_size,
            progress_callback=progress_callback,
        )

        return ResultOk(downloaded_path)
"""


def add_streaming_methods(
    api_file: Path,
    api_id: str,
    endpoints: list[Endpoint],
) -> None:
    """
    Add streaming methods to generated API service file.

    Args:
        api_file: Path to generated api.py file
        api_id: API identifier (e.g., 'cos', 'otm')
        endpoints: List of parsed endpoints from OpenAPI spec
    """
    # Detect which endpoints need streaming variants
    detector = StreamingEndpointDetector(api_id)
    streaming_configs = detector.detect_all(endpoints)

    if not streaming_configs:
        return  # No streaming endpoints detected

    print(
        f"  [STREAMING] Adding {len(streaming_configs)} streaming method(s) to {api_id}"
    )

    # Read file
    content = api_file.read_text()

    # Add imports if needed
    content = _add_streaming_imports(content)

    # Generate and insert streaming methods
    for config in streaming_configs:
        # Check if base method exists
        if f"def {config.base_method}(" not in content:
            print(f"    ⚠ Base method {config.base_method} not found, skipping")
            continue

        # Check if streaming method already exists
        if f"def {config.stream_method}(" in content:
            print(f"    ℹ Streaming method {config.stream_method} already exists")
            continue

        # Generate method code
        method_code = _generate_streaming_method(api_id, config)

        # Insert after base method
        content = _insert_after_method(content, config.base_method, method_code)

        print(f"    ✓ Generated {config.stream_method}")

    # Write back
    api_file.write_text(content)


def _add_streaming_imports(content: str) -> str:
    """Add required imports for streaming methods."""
    # Check if Path import already exists
    has_path_import = "from pathlib import Path" in content

    # Check if Result imports already exist
    has_result_imports = (
        "from satvu_api_sdk.http.errors import HttpError" in content
        and "from satvu_api_sdk.result import" in content
    )

    if has_path_import and has_result_imports:
        return content  # Already has all imports

    # Find insertion point (after existing imports)
    lines = content.split("\n")

    # Find last import line
    insert_idx = next(
        (
            i + 1
            for i, line in enumerate(lines)
            if line.startswith(
                ("from satvu_api_sdk", "from typing", "from collections")
            )
        ),
        0,
    )

    new_imports = []
    if not has_path_import:
        new_imports.append("from pathlib import Path")
    if not has_result_imports:
        new_imports.extend(
            [
                "from satvu_api_sdk.http.errors import HttpError",
                "from satvu_api_sdk.result import Ok as ResultOk",
                "from satvu_api_sdk.result import Result",
            ]
        )

    # Insert all at once
    lines[insert_idx:insert_idx] = new_imports
    return "\n".join(lines)


def _generate_streaming_method(api_id: str, config: StreamingEndpointConfig) -> str:
    """Generate streaming method code from config."""
    # Separate required params (path params) from optional params (query params like collections)
    required_params = [
        (name, type_) for name, type_ in config.params if name != "collections"
    ]

    # Build required params signature (goes before output_path)
    params_signature = (
        "\n".join(f"        {name}: {type_}," for name, type_ in required_params) + "\n"
        if required_params
        else ""
    )

    # Build docs for required params
    params_docs = (
        "\n".join(
            f"            {name} ({type_}): {_get_param_description(name)}"
            for name, type_ in required_params
        )
        + "\n"
        if required_params
        else ""
    )

    # Build URL format args (only path params, not collections)
    param_names = [name for name, _ in required_params]
    url_format_args = (
        "\n".join(f"                {p}={p}," for p in param_names) + "\n"
        if param_names
        else ""
    )

    # Build example call (only path params, not collections)
    example_call = ""
    for name, type_ in required_params:
        value = "UUID(...)" if "UUID" in type_ else "'...'" if "str" in type_ else "..."
        example_call += f"            ...     {name}={value},\n"

    # Build collections handling - add as optional param after output_path
    has_collections = any(name == "collections" for name, _ in config.params)
    extra_params = ""
    collections_param_signature = ""
    collections_param_docs = ""

    if has_collections:
        collections_type = next(
            type_ for name, type_ in config.params if name == "collections"
        )
        collections_param_signature = (
            f"        collections: {collections_type} = None,\n"
        )
        collections_param_docs = (
            "            collections: Specify subset of collections to download\n"
        )
        extra_params = '            "collections": collections,\n'

    return STREAMING_METHOD_TEMPLATE.format(
        stream_method=config.stream_method,
        params_signature=params_signature,
        collections_param_signature=collections_param_signature,
        collections_param_docs=collections_param_docs,
        docstring=config.docstring,
        params_docs=params_docs,
        api_id=api_id,
        example_call=example_call,
        example_filename=config.example_filename,
        url_pattern=config.url_pattern,
        url_format_args=url_format_args,
        default_chunk_size=config.default_chunk_size,
        extra_params=extra_params,
    )


def _get_param_description(param_name: str) -> str:
    """Get a generic description for a parameter."""
    descriptions = {
        "contract_id": "The contract ID",
        "order_id": "The order ID",
        "item_id": "The item ID",
        "collections": "Specify subset of collections to download",
    }
    return descriptions.get(param_name, "Parameter")


def _insert_after_method(content: str, base_method: str, method_code: str) -> str:
    """Insert streaming method after base method in source code."""
    lines = content.split("\n")

    # Find base method with a generator expression
    try:
        method_start_idx = next(
            i for i, line in enumerate(lines) if f"def {base_method}(" in line
        )
    except StopIteration:
        return content  # Base method not found

    base_indent = len(lines[method_start_idx]) - len(lines[method_start_idx].lstrip())

    # Find method end
    method_end_idx = next(
        (
            i
            for i in range(method_start_idx + 1, len(lines))
            if lines[i].strip()
            and (len(lines[i]) - len(lines[i].lstrip())) <= base_indent
            and lines[i].strip().startswith("def ")
        ),
        len(lines),
    )

    lines.insert(method_end_idx, method_code)
    return "\n".join(lines)
