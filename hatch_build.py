"""Hatch build hook to generate SDK code from OpenAPI specs."""

import sys
from pathlib import Path
from hatchling.builders.hooks.plugin.interface import BuildHookInterface  # type: ignore[import-not-found]

# Add the project root to sys.path so we can import builder
ROOT_DIR = Path(__file__).parent
sys.path.insert(0, str(ROOT_DIR))


class CustomBuildHook(BuildHookInterface):
    """Build hook to generate SDK code before packaging."""

    def initialize(self, version, build_data):
        """Run the SDK builder before packaging."""
        from builder.build import build

        # Generate all service modules (fetch specs fresh during build)
        build(api_id="all", use_cached=False)
