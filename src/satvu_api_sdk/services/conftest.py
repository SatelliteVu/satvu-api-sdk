"""Pytest configuration for service tests."""

import os

import hypothesis.internal.conjecture.engine as engine

# Reduce shrinking time from default (5 minutes) to 30 seconds
# See: https://hypothesis.readthedocs.io/en/latest/reference/internals.html#engine-constants
engine.MAX_SHRINKING_SECONDS = 30

# All available HTTP backends
ALL_BACKENDS = ["stdlib", "httpx", "urllib3", "requests"]

# CI mode uses only stdlib for faster runs
CI_BACKENDS = ["stdlib"]


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
