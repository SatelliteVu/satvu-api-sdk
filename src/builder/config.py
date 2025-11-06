BASE_URL = "https://api.qa.satellitevu.com/"

APIS: dict[str, str] = {
    "catalog": "/catalog/v1",
    "cos": "/orders/v2",
    "id": "/id/v2",
    "policy": "/policy/v1",
    "otm": "/otm/v2",
    "reseller": "/resellers/v1",
    "wallet": "/wallet/v1",
}

CMD_ARGS: dict[str, str] = {
    "all": "all",
    **APIS,
}
