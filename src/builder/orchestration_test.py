import pytest
from openapi_python_client.parser.errors import GeneratorError

from builder import orchestration
from builder.config import APIS, VersionedApi


@pytest.fixture
def two_version_otm(monkeypatch, tmp_path):
    monkeypatch.setitem(
        APIS,
        "otm",
        VersionedApi(versions={"v2": "/otm/v2", "v3": "/otm/v3"}, stable="v2"),
    )
    monkeypatch.setattr(orchestration, "SRC_DIR", tmp_path)
    aliases: list[str] = []
    monkeypatch.setattr(
        orchestration, "_write_stable_alias", lambda api_id, _: aliases.append(api_id)
    )
    return aliases


@pytest.mark.parametrize(
    ("failing_version", "alias_written"),
    [(None, True), ("v3", True), ("v2", False)],
)
def test_stable_alias_depends_only_on_stable_version(
    monkeypatch, two_version_otm, failing_version, alias_written
):
    def fake_build_service(target, use_cached, generate_tests):
        if target.version == failing_version:
            return [GeneratorError(detail="boom")]
        return []

    monkeypatch.setattr(orchestration, "build_service", fake_build_service)

    errors = orchestration.build_api("otm")

    assert len(errors) == (1 if failing_version else 0)
    assert two_version_otm == (["otm"] if alias_written else [])


def test_versioned_root_is_wiped_before_build(monkeypatch, tmp_path, two_version_otm):
    stale = tmp_path / "otm" / "models" / "removed_model.py"
    stale.parent.mkdir(parents=True)
    stale.write_text("")
    monkeypatch.setattr(orchestration, "build_service", lambda *_, **__: [])

    orchestration.build_api("otm")

    assert not stale.exists()
