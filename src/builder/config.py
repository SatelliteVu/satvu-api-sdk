import os

# Environment variable to control which API environment to fetch specs from
# Values: "qa" or "prod" (default: "qa" for backward compatibility with local dev)
SATVU_SPEC_ENV_VAR = "SATVU_SPEC_ENV"


def _get_base_url() -> str:
    """Get the base URL based on SATVU_SPEC_ENV environment variable."""
    env = os.environ.get(SATVU_SPEC_ENV_VAR, "qa").strip().lower()
    if env == "prod":
        return "https://api.satellitevu.com/"
    else:
        return "https://api.qa.satellitevu.com/"


BASE_URL = _get_base_url()

APIS: dict[str, str] = {
    "catalog": "/catalog/v1",
    "cos": "/orders/v3",
    "id": "/id/v3",
    "policy": "/policy/v1",
    "otm": "/otm/v2",
    "reseller": "/resellers/v1",
    "wallet": "/wallet/v1",
}

CMD_ARGS: dict[str, str] = {
    "all": "all",
    **APIS,
}
