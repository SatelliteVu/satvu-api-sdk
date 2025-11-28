"""Pytest configuration for service tests."""

import hypothesis.internal.conjecture.engine as engine

# Reduce shrinking time from default (5 minutes) to 30 seconds
# See: https://hypothesis.readthedocs.io/en/latest/reference/internals.html#engine-constants
engine.MAX_SHRINKING_SECONDS = 30
