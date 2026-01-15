"""
Example cache loader for property-based tests.

Provides transparent access to pre-generated hypothesis examples
with automatic fallback to on-demand generation via from_schema().

This module is used by generated test files to load cached examples
at test collection time, avoiding expensive schema parsing.

Cache Format
------------
Cache files are located at: .cache/hypothesis-examples/{api_name}-{spec_hash}.json

Cache keys are pipe-separated: {path}|{method}|{type}|{status_or_name}
Where type is one of: response, body, param

The cache is automatically invalidated when the OpenAPI spec changes
because the spec_hash in the filename changes.
"""

import json
import logging
from collections.abc import Callable
from functools import lru_cache
from pathlib import Path
from typing import Any

from hypothesis import strategies as st
from hypothesis_jsonschema import from_schema

logger = logging.getLogger(__name__)

# Cache directory relative to repo root
# Path: repo/.cache/hypothesis-examples/
_CACHE_DIR = (
    Path(__file__).parent.parent.parent.parent / ".cache" / "hypothesis-examples"
)


@lru_cache(maxsize=32)
def load_cached_examples(api_name: str, spec_hash: str) -> dict[str, list[Any]] | None:
    """
    Load cached examples for an API.

    Uses @lru_cache so each API's examples are loaded once per Python process.
    Cache is bounded to 32 entries (typically 7 APIs, allowing for multiple spec versions).

    Args:
        api_name: API identifier (e.g., 'catalog', 'otm')
        spec_hash: Hash of OpenAPI spec (for cache key)

    Returns:
        Dict mapping cache keys to example lists, or None if cache doesn't exist
    """
    cache_file = _CACHE_DIR / f"{api_name}-{spec_hash}.json"

    if not cache_file.exists():
        logger.debug("Cache file not found: %s", cache_file)
        return None

    try:
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            logger.warning(
                "Cache file has invalid structure (not a dict): %s", cache_file
            )
            return None
        logger.debug("Loaded %d cached examples for %s", len(data), api_name)
        return data
    except json.JSONDecodeError as e:
        logger.warning("Cache file corrupted (invalid JSON): %s - %s", cache_file, e)
        return None
    except OSError as e:
        logger.warning("Failed to read cache file: %s - %s", cache_file, e)
        return None


def get_cached_example_strategy(
    api_name: str,
    spec_hash: str,
    path: str,
    method: str,
    example_type: str,  # "response", "body", "param"
    key: str,  # status code or param name
    schema_getter: Callable[[], dict],
) -> st.SearchStrategy:
    """
    Get a hypothesis strategy that uses cached examples or falls back to generation.

    This function returns a strategy that hypothesis can use in @given decorators.
    It first tries to use pre-generated examples from cache, falling back to
    from_schema() if cache is unavailable.

    Args:
        api_name: API identifier (e.g., 'catalog', 'otm')
        spec_hash: OpenAPI spec hash (for cache lookup)
        path: Endpoint path (e.g., '/{contract_id}/')
        method: HTTP method (e.g., 'get', 'post')
        example_type: Type of example ('response', 'body', 'param')
        key: Status code (for responses) or parameter name
        schema_getter: Callable that returns the schema (for fallback)

    Returns:
        Hypothesis strategy that generates examples
    """
    # Try to load cached examples
    cache = load_cached_examples(api_name, spec_hash)
    cache_key = f"{path}|{method}|{example_type}|{key}"

    if cache and cache_key in cache:
        examples = cache[cache_key]
        if examples:
            # Return strategy that samples from cached examples
            return st.sampled_from(examples)

    # Fallback: generate on-demand from schema
    schema = schema_getter()
    return from_schema(schema)
