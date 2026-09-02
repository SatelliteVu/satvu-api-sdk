"""Pytest configuration for the repository root."""

import sys

# The builder's openapi-python-client dependency requires 3.11+, while the published SDK
# supports 3.10 (see requires-python). On 3.10 it is absent, and importing any builder
# module fails because builder/__init__.py applies the generator's monkey patches.
BUILDER_MIN_PYTHON = (3, 11)

collect_ignore = ["src/builder"] if sys.version_info < BUILDER_MIN_PYTHON else []
