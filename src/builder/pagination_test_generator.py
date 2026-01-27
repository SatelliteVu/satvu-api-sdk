"""Generate integration tests for pagination iterator methods (*_iter)."""

import ast
import subprocess
from pathlib import Path

from jinja2 import Environment

from builder.pagination_detector import PaginationEndpointConfig

# Imports required by pagination tests (added via AST since base tests are ruff-cleaned first)
PAGINATION_TEST_IMPORTS = [
    ("hypothesis_jsonschema", "from_schema"),
    (".test_schemas", "get_response_schema"),
]


def generate_pagination_tests(
    api_name: str,
    pagination_configs: list[PaginationEndpointConfig],
    test_file: Path,
    jinja_env: Environment,
) -> None:
    """
    Generate and append pagination iterator tests to existing test file.

    Args:
        api_name: API identifier (e.g., 'catalog', 'cos')
        pagination_configs: List of detected pagination endpoints
        test_file: Path to existing api_test.py file
        jinja_env: Jinja2 environment with templates loaded
    """
    if not pagination_configs:
        return  # No pagination endpoints detected

    if not test_file.exists():
        print(f"    [PAGINATION TESTS] Test file not found: {test_file}")
        return

    print(
        f"  [PAGINATION TESTS] Generating {len(pagination_configs)} pagination test(s) for {api_name}"
    )

    # Read existing test file
    content = test_file.read_text()
    tree = ast.parse(content)

    # Add required imports for pagination tests
    _add_pagination_imports(tree)

    # Find the test class
    test_class = _find_test_class(tree)
    if not test_class:
        print(f"    [PAGINATION TESTS] No test class found in {test_file}")
        return

    # Render pagination tests using template macros
    for config in pagination_configs:
        context = {"config": config, "api_name": api_name}

        # Render each test type
        multi_page_test_code = jinja_env.from_string(
            "{% from 'macros/pagination_tests.jinja' import pagination_multi_page_test %}"
            "{{ pagination_multi_page_test(config, api_name) }}"
        ).render(context)

        max_pages_test_code = jinja_env.from_string(
            "{% from 'macros/pagination_tests.jinja' import pagination_max_pages_test %}"
            "{{ pagination_max_pages_test(config, api_name) }}"
        ).render(context)

        empty_page_test_code = jinja_env.from_string(
            "{% from 'macros/pagination_tests.jinja' import pagination_empty_page_test %}"
            "{{ pagination_empty_page_test(config, api_name) }}"
        ).render(context)

        # Parse rendered tests as AST and append to class
        added_count = 0
        for test_code in [
            multi_page_test_code,
            max_pages_test_code,
            empty_page_test_code,
        ]:
            test_method = _parse_test_method(test_code)
            if test_method:
                test_class.body.append(test_method)
                added_count += 1

        print(
            f"    [PAGINATION TESTS] Generated {added_count} tests for {config.iter_method}"
        )

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


def _add_pagination_imports(tree: ast.Module) -> None:
    """
    Add required imports for pagination tests if not already present.

    Pagination tests are added via AST after base tests are generated and
    ruff-cleaned, so imports like `from_schema` need to be added here.

    Args:
        tree: AST module to modify in-place
    """
    # Collect existing imports
    existing_imports: set[tuple[str, str]] = set()
    for node in tree.body:
        if isinstance(node, ast.ImportFrom) and node.module:
            for alias in node.names:
                existing_imports.add((node.module, alias.name))

    # Find insertion point (after last import)
    insert_idx = 0
    for i, node in enumerate(tree.body):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            insert_idx = i + 1

    # Add missing imports
    imports_added = 0
    for module, name in PAGINATION_TEST_IMPORTS:
        if (module, name) not in existing_imports:
            # Handle relative imports (module starts with '.')
            if module.startswith("."):
                level = 1
                actual_module = module[1:] or None  # Strip leading dot
            else:
                level = 0
                actual_module = module
            import_node = ast.ImportFrom(
                module=actual_module,
                names=[ast.alias(name=name, asname=None)],
                level=level,
            )
            tree.body.insert(insert_idx + imports_added, import_node)
            imports_added += 1


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
        print(f"    [PAGINATION TESTS] Failed to parse test code: {e}")
        print(f"    Generated code:\n{test_code}")
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
        print("    [PAGINATION TESTS] Formatted with ruff")
    except (ImportError, FileNotFoundError):
        print("    [PAGINATION TESTS] Ruff not available, skipping formatting")
