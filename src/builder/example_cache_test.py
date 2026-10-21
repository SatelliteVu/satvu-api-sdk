"""Tests for pre-generated hypothesis example caching."""

import json
from pathlib import Path

import pytest

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


@pytest.fixture
def cache_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(example_cache, "EXAMPLES_CACHE_DIR", tmp_path)
    return tmp_path


@pytest.fixture
def generated(monkeypatch):
    """Record each schema examples are generated for; every generation fails."""
    calls: list[dict] = []

    def fail(schema, num_examples):
        calls.append(schema)
        return []

    monkeypatch.setattr(example_cache, "_generate_examples", fail)
    return calls


_MODELS = {"Point": {"type": "object"}}


@pytest.mark.parametrize(
    ("cached", "request_models", "regenerates"),
    [
        pytest.param({}, _MODELS, True, id="pre-request-model cache rebuilt"),
        pytest.param(
            {example_cache.REQUEST_MODELS_KEY: ["Point"]},
            _MODELS,
            False,
            id="cache with marker reused",
        ),
        pytest.param(
            {example_cache.REQUEST_MODELS_KEY: ["Polygon"]},
            _MODELS,
            True,
            id="cache for other request models rebuilt",
        ),
        pytest.param({}, None, False, id="no request models reuses any cache"),
    ],
)
def test_existing_cache_freshness(
    cache_dir, generated, cached, request_models, regenerates
):
    (cache_dir / "otm-prod-2a64c436.json").write_text(
        json.dumps(cached), encoding="utf-8"
    )

    example_cache.generate_examples_cache(
        "otm", {}, "prod-2a64c436", request_models=request_models
    )

    assert bool(generated) is regenerates


def test_failed_request_models_still_mark_cache_fresh(cache_dir, generated):
    """Otherwise an API whose request models all fail rebuilds on every build."""
    example_cache.generate_examples_cache(
        "otm", {}, "prod-2a64c436", request_models=_MODELS
    )
    generated.clear()

    example_cache.generate_examples_cache(
        "otm", {}, "prod-2a64c436", request_models=_MODELS
    )

    assert generated == []
