"""
Pre-generate hypothesis-jsonschema examples for test caching.

This module generates examples during SDK build time and stores them
in .cache/hypothesis-examples/{api_name}-{spec_hash}.json

Cache invalidation is automatic: when the OpenAPI spec changes,
the spec_hash changes, creating a new cache file.

Cache Format
------------
Location: .cache/hypothesis-examples/{api_name}-{spec_hash}.json

Cache keys are pipe-separated: {path}|{method}|{type}|{status_or_name}
Types: response, body, param

Example:
    {
        "/{contract_id}/|get|response|200": [{"id": "abc", ...}, ...],
        "/search|post|body|requestBody": [{"query": "test"}, ...],
    }
"""

import json
import tempfile
from pathlib import Path
from typing import Any

from hypothesis import HealthCheck, Phase, given, settings
from hypothesis_jsonschema import from_schema

# Cache directory in project root (use cwd since builder always runs from repo root)
# This ensures cache is written to the correct location regardless of where
# the builder package is installed
EXAMPLES_CACHE_DIR = Path.cwd() / ".cache" / "hypothesis-examples"


def generate_examples_cache(
    api_name: str,
    operations: dict,
    spec_hash: str,
    num_examples: int = 10,
) -> Path:
    """
    Pre-generate hypothesis examples for all testable operations.

    For each operation, generates examples for:
    - Response schemas (per status code)
    - Request body schemas
    - Query parameter schemas

    Args:
        api_name: API identifier (e.g., 'catalog', 'otm')
        operations: Operations dict from test_generator._extract_operations
        spec_hash: Hash of OpenAPI spec (for cache invalidation)
        num_examples: Number of examples to generate per schema

    Returns:
        Path to cached examples file
    """
    EXAMPLES_CACHE_DIR.mkdir(parents=True, exist_ok=True)

    cache_file = EXAMPLES_CACHE_DIR / f"{api_name}-{spec_hash}.json"

    # Skip generation if cache already exists for this spec_hash
    if cache_file.exists():
        print(f"  [EXAMPLES] Using existing cache for {api_name} -> {cache_file.name}")
        return cache_file

    print(f"  [EXAMPLES] Generating {num_examples} examples per schema for {api_name}")

    # Structure: {"path|method|type|key": [example1, example2, ...]}
    all_examples: dict[str, list[Any]] = {}
    schemas_processed = 0
    schemas_failed = 0

    for (path, method), op_data in operations.items():
        # Generate response examples
        for status, response_data in op_data.get("responses", {}).items():
            schema = response_data["schema"]
            key = f"{path}|{method}|response|{status}"
            examples = _generate_examples(schema, num_examples)
            if examples:
                all_examples[key] = examples
                schemas_processed += 1
            else:
                schemas_failed += 1

        # Generate request body examples
        if "requestBody" in op_data:
            schema = op_data["requestBody"]["schema"]
            key = f"{path}|{method}|body|requestBody"
            examples = _generate_examples(schema, num_examples)
            if examples:
                all_examples[key] = examples
                schemas_processed += 1
            else:
                schemas_failed += 1

        # Generate parameter examples
        for param_name, param_data in op_data.get("parameters", {}).items():
            schema = param_data["schema"]
            key = f"{path}|{method}|param|{param_name}"
            examples = _generate_examples(schema, num_examples)
            if examples:
                all_examples[key] = examples
                schemas_processed += 1
            else:
                schemas_failed += 1

    # Write to cache atomically (prevents corruption from parallel builds)
    with tempfile.NamedTemporaryFile(
        mode="w",
        dir=EXAMPLES_CACHE_DIR,
        delete=False,
        suffix=".json",
        encoding="utf-8",
    ) as tmp:
        json.dump(all_examples, tmp, separators=(",", ":"))
        tmp_path = Path(tmp.name)

    # Atomic rename (replaces existing file safely)
    tmp_path.replace(cache_file)

    total_examples = sum(len(examples) for examples in all_examples.values())
    print(
        f"  [EXAMPLES] Generated {total_examples} examples "
        f"across {schemas_processed} schemas "
        f"({schemas_failed} failed) -> {cache_file.name}"
    )

    return cache_file


def _generate_examples(schema: dict, num_examples: int) -> list[Any]:
    """
    Generate examples from a JSON schema using hypothesis.

    Uses hypothesis in generation-only mode (no shrinking) for speed.
    Examples are JSON-serialized to ensure they can be stored in cache.

    Args:
        schema: JSON Schema dict with definitions for $ref resolution
        num_examples: Number of examples to generate

    Returns:
        List of generated examples, or empty list on failure
    """
    examples: list[Any] = []

    try:
        strategy = from_schema(schema)
    except Exception as e:
        # Schema may be invalid or unsupported
        print(f"  [EXAMPLES] Warning: Failed to create strategy: {e}")
        return []

    @settings(
        max_examples=num_examples,
        phases=[Phase.generate],  # Skip shrinking for speed
        deadline=None,
        database=None,  # Don't use hypothesis database during generation
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(data=strategy)
    def collect_example(data):
        # Serialize to JSON and back to ensure it's serializable
        try:
            json_str = json.dumps(data, default=str)
            examples.append(json.loads(json_str))
        except (TypeError, ValueError):
            # Skip unserializable examples (rare edge cases)
            pass

    # Run hypothesis to collect examples
    try:
        collect_example()
    except Exception as e:
        # If generation fails completely, return empty list
        print(f"  [EXAMPLES] Warning: Failed to generate examples: {e}")
        return []

    return examples[:num_examples]  # Ensure we don't exceed requested count
