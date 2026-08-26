"""Tests for pre-generated hypothesis example caching."""

from pathlib import Path

from builder import example_cache


def _cache(dir_: Path, name: str) -> Path:
    path = dir_ / f"{name}.json"
    path.write_text("{}", encoding="utf-8")
    return path


def test_prune_keeps_the_other_spec_env(tmp_path, monkeypatch):
    """prod and qa share one CI cache, so pruning must not evict across environments."""
    monkeypatch.setattr(example_cache, "EXAMPLES_CACHE_DIR", tmp_path)
    current = _cache(tmp_path, "otm-prod-2a64c436")
    superseded = _cache(tmp_path, "otm-prod-877ee26e")
    other_env = _cache(tmp_path, "otm-qa-d0ae428c")

    example_cache._prune_stale_caches(current)

    assert current.exists()
    assert other_env.exists()
    assert not superseded.exists()


def test_prune_keeps_other_apis(tmp_path, monkeypatch):
    """Each API is cached independently; pruning one must not touch another."""
    monkeypatch.setattr(example_cache, "EXAMPLES_CACHE_DIR", tmp_path)
    current = _cache(tmp_path, "otm-prod-2a64c436")
    other_api = _cache(tmp_path, "policy-prod-e78c5a67")

    example_cache._prune_stale_caches(current)

    assert current.exists()
    assert other_api.exists()
