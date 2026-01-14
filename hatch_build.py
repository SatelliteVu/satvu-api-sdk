"""Hatch build hook to generate SDK code from OpenAPI specs."""

import os
import sys
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import (  # type: ignore[import-not-found]
    BuildHookInterface,
)

# Add src to sys.path so we can import builder
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR / "src"))

# Environment variable to control test generation during builds
# Default: False (don't generate tests - they're excluded from wheel anyway)
# Set SATVU_GENERATE_TESTS=1 to generate tests (e.g., when running test suite)
GENERATE_TESTS_ENV_VAR = "SATVU_GENERATE_TESTS"


class CustomBuildHook(BuildHookInterface):
    """Build hook to generate SDK code before packaging."""

    def initialize(self, version, build_data):
        """Run the SDK builder before packaging."""
        from builder.build import build

        # Check if test generation is requested via environment variable
        # Accepts "1", "true", "yes" (case-insensitive)
        generate_tests = os.environ.get(GENERATE_TESTS_ENV_VAR, "").lower() in (
            "1",
            "true",
            "yes",
        )

        # Generate all service modules
        # - use_cached=False: respects SATVU_TRIGGERED_API env var for selective fetching
        # - generate_tests: controlled by SATVU_GENERATE_TESTS env var
        build(api_id="all", use_cached=False, generate_tests=generate_tests)
