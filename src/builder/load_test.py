"""Tests for OpenAPI spec loading helpers."""

from builder.load import spec_content_hash


def _spec(status_enum: list[str]) -> dict:
    return {
        "openapi": "3.1.0",
        "info": {"title": "otm", "version": "v2"},
        "components": {
            "schemas": {
                "OrderStatus": {"type": "string", "enum": status_enum},
            }
        },
    }


def test_hash_changes_when_enum_narrows():
    """
    A schema change must produce a new hash.
    """
    before = spec_content_hash(_spec(["staged", "fulfilled", "rejected", "committed"]))
    after = spec_content_hash(_spec(["staged", "fulfilled"]))

    assert before != after


def test_hash_is_independent_of_key_order():
    """Serialisation is canonical, so dict ordering must not change the hash."""
    ordered = {"openapi": "3.1.0", "info": {"title": "otm", "version": "v2"}}
    shuffled = {"info": {"version": "v2", "title": "otm"}, "openapi": "3.1.0"}

    assert spec_content_hash(ordered) == spec_content_hash(shuffled)


def test_hash_is_deterministic_across_calls():
    """Repeat builds of an unchanged spec must reuse the same cache entry."""
    spec = _spec(["staged", "fulfilled"])

    assert spec_content_hash(spec) == spec_content_hash(spec)
