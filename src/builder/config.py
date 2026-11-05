import os
import re
from dataclasses import dataclass

# Environment variable to control which API environment to fetch specs from
# Values: "qa" or "prod" (default: "qa" for backward compatibility with local dev)
SATVU_SPEC_ENV_VAR = "SATVU_SPEC_ENV"


def _get_spec_env() -> str:
    """Get the spec environment from the SATVU_SPEC_ENV environment variable."""
    return os.environ.get(SATVU_SPEC_ENV_VAR, "qa").strip().lower()


def _get_base_url() -> str:
    """Get the base URL based on SATVU_SPEC_ENV environment variable."""
    if _get_spec_env() == "prod":
        return "https://api.satellitevu.com/"
    else:
        return "https://api.qa.satellitevu.com/"


SPEC_ENV = _get_spec_env()
BASE_URL = _get_base_url()


@dataclass(frozen=True)
class VersionedApi:
    """An API generated once per version, with ``stable`` re-exported at the API root."""

    versions: dict[str, str]
    stable: str

    def __post_init__(self):
        # Versions become package dirs, SDK attributes (sdk.otm.v2) and class names.
        invalid = [v for v in self.versions if not re.fullmatch(r"v\d+", v)]
        if invalid:
            raise ValueError(f"versions must look like 'v2', got {invalid}")
        if self.stable not in self.versions:
            raise ValueError(f"stable version {self.stable!r} not in {self.versions}")


@dataclass(frozen=True)
class ServiceTarget:
    """One generated service: an unversioned API, or a single version of one."""

    api: str
    base_path: str
    version: str | None = None

    @property
    def module_path(self) -> str:
        """
        Dotted path under ``satvu.services``, e.g. ``otm.v2``.

        Doubles as the SDK accessor (``sdk.otm.v2``): templates rely on the package
        layout mirroring attribute access.
        """
        return f"{self.api}.{self.version}" if self.version else self.api

    @property
    def class_name(self) -> str:
        return f"{self.api.title()}{(self.version or '').title()}Service"


APIS: dict[str, str | VersionedApi] = {
    "catalog": "/catalog/v1",
    "cos": "/orders/v3",
    "id": "/id/v3",
    "policy": "/policy/v1",
    "otm": VersionedApi(versions={"v2": "/otm/v2"}, stable="v2"),
    "reseller": "/resellers/v1",
    "wallet": "/wallet/v1",
}

CMD_ARGS: tuple[str, ...] = ("all", *APIS)


def service_targets(api: str) -> list[ServiceTarget]:
    """Every service generated for ``api``: one per version if it is versioned."""
    entry = APIS[api]
    if isinstance(entry, VersionedApi):
        return [
            ServiceTarget(api=api, base_path=path, version=version)
            for version, path in entry.versions.items()
        ]
    return [ServiceTarget(api=api, base_path=entry)]
