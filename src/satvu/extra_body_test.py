"""Tests for forward-compatible extra_body deep merge helper."""

from satvu.core import _deep_merge


def test_deep_merge_adds_top_level_key():
    assert _deep_merge({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}


def test_deep_merge_recurses_into_nested_dicts():
    base = {"properties": {"datetime": "2026-04-20", "collections": ["primary"]}}
    extra = {"properties": {"new_field": "x"}}
    assert _deep_merge(base, extra) == {
        "properties": {
            "datetime": "2026-04-20",
            "collections": ["primary"],
            "new_field": "x",
        }
    }


def test_deep_merge_overrides_scalars():
    assert _deep_merge({"a": 1}, {"a": 2}) == {"a": 2}


def test_deep_merge_replaces_lists():
    # Lists replace wholesale — concat/zip semantics are ambiguous.
    assert _deep_merge({"a": [1, 2]}, {"a": [3]}) == {"a": [3]}


def test_deep_merge_type_mismatch_overrides():
    # dict in base, scalar in override → override wins
    assert _deep_merge({"a": {"x": 1}}, {"a": "hello"}) == {"a": "hello"}
    # scalar in base, dict in override → override wins
    assert _deep_merge({"a": "hello"}, {"a": {"x": 1}}) == {"a": {"x": 1}}


def test_deep_merge_does_not_mutate_inputs():
    base = {"a": {"x": 1}}
    extra = {"a": {"y": 2}}
    result = _deep_merge(base, extra)
    assert base == {"a": {"x": 1}}
    assert extra == {"a": {"y": 2}}
    assert result == {"a": {"x": 1, "y": 2}}


def test_deep_merge_empty_overrides():
    assert _deep_merge({"a": 1}, {}) == {"a": 1}


def test_deep_merge_empty_base():
    assert _deep_merge({}, {"a": 1}) == {"a": 1}


def test_deep_merge_deeply_nested():
    base = {"a": {"b": {"c": {"d": 1}}}}
    extra = {"a": {"b": {"c": {"e": 2}}}}
    assert _deep_merge(base, extra) == {"a": {"b": {"c": {"d": 1, "e": 2}}}}
