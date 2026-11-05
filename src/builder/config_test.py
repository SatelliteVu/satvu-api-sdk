import pytest

from builder.config import APIS, ServiceTarget, VersionedApi, service_targets


@pytest.mark.parametrize(
    ("target", "module_path", "class_name"),
    [
        (
            ServiceTarget(api="catalog", base_path="/catalog/v1"),
            "catalog",
            "CatalogService",
        ),
        (ServiceTarget(api="id", base_path="/id/v3"), "id", "IdService"),
        (
            ServiceTarget(api="otm", base_path="/otm/v2", version="v2"),
            "otm.v2",
            "OtmV2Service",
        ),
    ],
)
def test_service_target_naming(target, module_path, class_name):
    assert target.module_path == module_path
    assert target.class_name == class_name


def test_unversioned_api_has_single_target(monkeypatch):
    monkeypatch.setitem(APIS, "wallet", "/wallet/v1")

    assert service_targets("wallet") == [
        ServiceTarget(api="wallet", base_path="/wallet/v1")
    ]


def test_versioned_api_has_target_per_version(monkeypatch):
    monkeypatch.setitem(
        APIS,
        "otm",
        VersionedApi(versions={"v2": "/otm/v2", "v3": "/otm/v3"}, stable="v2"),
    )

    assert service_targets("otm") == [
        ServiceTarget(api="otm", base_path="/otm/v2", version="v2"),
        ServiceTarget(api="otm", base_path="/otm/v3", version="v3"),
    ]


def test_versioned_api_rejects_unknown_stable():
    with pytest.raises(ValueError, match="stable version 'v3'"):
        VersionedApi(versions={"v2": "/otm/v2"}, stable="v3")


@pytest.mark.parametrize("version", ["v2.1", "v3-beta", "V2", "2"])
def test_versioned_api_rejects_non_identifier_versions(version):
    with pytest.raises(ValueError, match="versions must look like 'v2'"):
        VersionedApi(versions={version: "/otm/x"}, stable=version)
