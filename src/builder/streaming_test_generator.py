"""Generate integration tests for streaming download methods (*_to_file)."""

import ast
import subprocess
from pathlib import Path

from jinja2 import Environment

from builder.streaming_detector import StreamingEndpointConfig


def generate_streaming_tests(
    api_name: str,
    streaming_configs: list[StreamingEndpointConfig],
    test_file: Path,
    jinja_env: Environment,
) -> None:
    """
    Generate and append streaming method tests to existing test file.

    Args:
        api_name: API identifier (e.g., 'cos', 'otm')
        streaming_configs: List of detected streaming endpoints
        test_file: Path to existing api_test.py file
        jinja_env: Jinja2 environment with templates loaded
    """
    if not streaming_configs:
        return  # No streaming endpoints detected

    if not test_file.exists():
        print(f"    ⚠ Test file not found: {test_file}")
        return

    print(
        f"  [TESTS] Generating {len(streaming_configs)} streaming test(s) for {api_name}"
    )

    # Read existing test file
    content = test_file.read_text()
    tree = ast.parse(content)

    # Find the test class (should be named Test{ApiName}Service)
    test_class = _find_test_class(tree)
    if not test_class:
        print(f"    ⚠ No test class found in {test_file}")
        return

    # Render streaming tests using template macros
    # We need to render the template with context, then call the macros
    for config in streaming_configs:
        # Create context for template
        context = {"config": config, "api_name": api_name}

        # Render each test type using Jinja2 {% call %} style
        success_test_code = jinja_env.from_string(
            "{% from 'macros/streaming_tests.jinja' import streaming_success_test %}"
            "{{ streaming_success_test(config, api_name) }}"
        ).render(context)

        progress_test_code = jinja_env.from_string(
            "{% from 'macros/streaming_tests.jinja' import streaming_progress_test %}"
            "{{ streaming_progress_test(config, api_name) }}"
        ).render(context)

        error_test_code = jinja_env.from_string(
            "{% from 'macros/streaming_tests.jinja' import streaming_error_test %}"
            "{{ streaming_error_test(config, api_name) }}"
        ).render(context)

        # Parse rendered tests as AST and append to class
        added_count = 0
        for test_code in [success_test_code, progress_test_code, error_test_code]:
            test_method = _parse_test_method(test_code)
            if test_method:
                test_class.body.append(test_method)
                added_count += 1

        print(f"    ✓ Generated {added_count} tests for {config.stream_method}")

    # Convert AST back to code
    final_code = ast.unparse(tree)

    # Write back to file
    test_file.write_text(final_code)

    # Format with ruff if available
    _format_with_ruff(test_file)


def _find_test_class(tree: ast.Module) -> ast.ClassDef | None:
    """Find the test class in the AST."""
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
            return node
    return None


def _parse_test_method(test_code: str) -> ast.FunctionDef | None:
    """
    Parse rendered test code into AST FunctionDef node.

    Args:
        test_code: Rendered test method code as string

    Returns:
        AST FunctionDef node, or None if parsing fails
    """
    try:
        # Parse the test code
        test_tree = ast.parse(test_code)

        # Extract the function definition (handles decorators correctly)
        for node in test_tree.body:
            if isinstance(node, ast.FunctionDef):
                return node

        return None
    except SyntaxError as e:
        print(f"    ⚠ Failed to parse test code: {e}")
        return None


def _format_with_ruff(test_file: Path) -> None:
    """
    Format generated test file with ruff.

    Args:
        test_file: Path to test file
    """
    try:
        # First apply autofixes (remove unused imports, etc.)
        subprocess.run(  # nosec B607
            ["ruff", "check", "--fix", str(test_file)],
            check=False,
            capture_output=True,
        )
        # Then format the code
        subprocess.run(  # nosec B607
            ["ruff", "format", str(test_file)],
            check=False,
            capture_output=True,
        )
        print("    ✓ Formatted with ruff")
    except (ImportError, FileNotFoundError):
        print("    ℹ Ruff not available, skipping formatting")
