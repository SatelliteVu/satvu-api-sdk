"""Post-processor to add streaming download methods to generated API services."""

import ast
from pathlib import Path

from openapi_python_client.parser.openapi import Endpoint

from builder.ast_generator import (
    add_imports_to_ast,
    generate_streaming_method,
    insert_method_after_base,
)
from builder.streaming_detector import StreamingEndpointDetector

try:
    import subprocess

    # Check if ruff is available in PATH
    result = subprocess.run(
        ["ruff", "--version"],  # nosec B607
        capture_output=True,
        text=True,
        check=False,
    )
    HAS_RUFF = result.returncode == 0
except (ImportError, FileNotFoundError):
    HAS_RUFF = False


def add_streaming_methods(
    api_file: Path,
    api_id: str,
    endpoints: list[Endpoint],
    openapi_dict: dict,
) -> None:
    """
    Add streaming methods to generated API service file using AST.

    Args:
        api_file: Path to generated api.py file
        api_id: API identifier (e.g., 'cos', 'otm')
        endpoints: List of parsed endpoints from OpenAPI spec
        openapi_dict: Raw OpenAPI spec dict for reading x-streaming extensions
    """
    # Detect which endpoints need streaming variants
    detector = StreamingEndpointDetector(api_id, openapi_dict)
    streaming_configs = detector.detect_all(endpoints)

    if not streaming_configs:
        return  # No streaming endpoints detected

    print(
        f"  [STREAMING] Adding {len(streaming_configs)} streaming method(s) to {api_id}"
    )

    # Read and parse file as AST
    content = api_file.read_text()
    tree = ast.parse(content)

    # Add required imports
    tree = add_imports_to_ast(
        tree,
        {
            "pathlib": [("Path", None)],
            "satvu_api_sdk.http.errors": [("HttpError", None)],
            "satvu_api_sdk.result": [
                ("Result", None),
                ("Ok", "ResultOk"),
                ("Err", "ResultErr"),
                ("is_err", None),
            ],
        },
    )

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

        # Generate method code using AST
        method_code = generate_streaming_method(config)

        # Insert method into AST
        tree = insert_method_after_base(tree, config.base_method, method_code)

        print(f"    ✓ Generated {config.stream_method}")

    # Convert AST back to code
    final_code = ast.unparse(tree)

    # Format with Ruff if available
    if HAS_RUFF:
        try:
            result = subprocess.run(
                ["ruff", "format", "-"],  # nosec B607
                input=final_code,
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode == 0:
                final_code = result.stdout
            else:
                print(f"    ⚠ Ruff formatting failed: {result.stderr}")
        except Exception as e:
            print(f"    ⚠ Ruff formatting failed, using unformatted code: {e}")
    else:
        print("    ℹ Ruff not available, skipping formatting")

    # Write formatted code
    api_file.write_text(final_code)


# TODO: Add streaming to BytesIO method as well
