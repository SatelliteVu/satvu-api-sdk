"""Pytest configuration for service tests."""

import os
import warnings

import hypothesis.internal.conjecture.engine as engine

# Reduce shrinking time from default (5 minutes) to 30 seconds
# See: https://hypothesis.readthedocs.io/en/latest/reference/internals.html#engine-constants
engine.MAX_SHRINKING_SECONDS = 30

# All available HTTP backends
ALL_BACKENDS = ["stdlib", "httpx", "urllib3", "requests"]

# CI mode uses only stdlib for faster runs
CI_BACKENDS = ["stdlib"]


def pytest_ignore_collect(collection_path):
    """
    Skip a service's generated tests when its hypothesis fixtures are absent.

    api_test.py is tracked so users can browse the SDK on GitHub, but test_schemas.py is
    generated (tens of MB per service) and deliberately untracked, so a fresh clone has
    one without the other and collection would die on ImportError. Generate them with
    SATVU_GENERATE_TESTS=1 uv build.

    Warns rather than ignoring quietly: a generation that silently produced nothing must
    not be indistinguishable from a clean run.
    """
    if collection_path.name != "api_test.py":
        return None

    if (collection_path.parent / "test_schemas.py").exists():
        return None

    warnings.warn(
        f"Skipping {collection_path.parent.name} service tests: test_schemas.py is "
        "missing. Generate it with: SATVU_GENERATE_TESTS=1 uv build",
        stacklevel=1,
    )
    return True


def pytest_addoption(parser):
    """Add --all-backends option to run tests against all HTTP backends."""
    parser.addoption(
        "--all-backends",
        action="store_true",
        default=False,
        help="Run tests against all HTTP backends (default: stdlib only in CI)",
    )


def pytest_collection_modifyitems(config, items):
    """Filter backend parametrization based on CI mode."""
    # Use all backends if --all-backends flag is set or ALL_BACKENDS env var is set
    use_all_backends = config.getoption("--all-backends") or os.environ.get(
        "ALL_BACKENDS", ""
    ).lower() in ("1", "true", "yes")

    if use_all_backends:
        # Run all backends - no filtering needed
        return

    # Filter to only stdlib backend
    selected = []
    deselected = []

    for item in items:
        # Check if this test has a backend parameter
        if hasattr(item, "callspec") and "backend" in item.callspec.params:
            backend = item.callspec.params["backend"]
            if backend in CI_BACKENDS:
                selected.append(item)
            else:
                deselected.append(item)
        else:
            # No backend parameter, keep the test
            selected.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = selected
