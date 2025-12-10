import copy
import os
from hashlib import sha1
from json import dumps, loads
from pathlib import Path
from typing import Any

from httpx import get

from builder.config import APIS, BASE_URL

BASE_DIR = (Path(__file__).parent / ".." / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"

# Environment variable for selective spec fetching in CI
# When set to an API name (e.g., "catalog"), only that API fetches fresh specs
# Other APIs use cached specs (with fallback to fresh if cache doesn't exist)
SATVU_TRIGGERED_API_ENV_VAR = "SATVU_TRIGGERED_API"

FETCHED = {}
NEW_COMPONENTS = {}


def resolve_external_refs(schema: Any) -> Any:
    """
    Recursively resolve all external $ref references in an OpenAPI schema,
    merge their components, and rewrite $ref to local components.

    :param schema: The OpenAPI schema to process.
    :return: The OpenAPI schema with all external references resolved and merged.
    """
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref_path = schema["$ref"]
            if ref_path.startswith("http://") or ref_path.startswith("https://"):
                url, fragment = ref_path.split("#")
                section, name = fragment.split("/", 1)

                # Check if the external URL has already been fetched
                if url not in FETCHED:
                    response = get(url)
                    response.raise_for_status()
                    ext_schema = response.json()
                    ext_components = ext_schema.get("components", {})

                    # Merge external components
                    for comp_type, comp_dict in ext_components.items():
                        if comp_type not in NEW_COMPONENTS:
                            NEW_COMPONENTS[comp_type] = {}
                        for comp_name, comp_val in comp_dict.items():
                            if comp_name not in NEW_COMPONENTS[comp_type]:
                                NEW_COMPONENTS[comp_type][comp_name] = comp_val

                    FETCHED[url] = True

                # Rewrite $ref to local component
                return {"$ref": f"#/components/schemas/{name.split('/')[-1]}"}
            else:
                return schema
        else:
            return {k: resolve_external_refs(v) for k, v in list(schema.items())}

    elif isinstance(schema, list):
        # Recursively resolve refs in list items
        return [resolve_external_refs(item) for item in schema]

    else:
        # Base case: return the value as is
        return schema


def bundle_openapi_schema(schema: dict) -> dict:
    """
    Returns a bundled OpenAPI schema with all external references resolved and merged.
    This function processes the OpenAPI schema, resolves all external references,
    and merges any new components into the schema.

    :param schema: The OpenAPI schema to process.
    :return: The processed OpenAPI schema with resolved references and merged components.
    """
    NEW_COMPONENTS.clear()
    bundled = copy.deepcopy(schema)
    bundled = resolve_external_refs(bundled)
    if NEW_COMPONENTS:
        for comp_type in NEW_COMPONENTS:
            bundled["components"][comp_type].update(NEW_COMPONENTS["schemas"])
    return bundled


def _should_fetch_fresh(api_id: str, use_cached: bool) -> bool:
    """
    Determine whether to fetch a fresh spec or use cached.

    Logic:
    - If SATVU_TRIGGERED_API env var is set:
        - "none" = use cached for all APIs (no specific API triggered)
        - "<api_name>" = fetch fresh for that API, cached for others
    - If SATVU_TRIGGERED_API env var is not set:
        - Use the use_cached parameter (backward compatible for local dev)
    """
    if SATVU_TRIGGERED_API_ENV_VAR not in os.environ:
        # Env var not set = local dev, use parameter
        return not use_cached

    triggered_api = os.environ[SATVU_TRIGGERED_API_ENV_VAR].strip()

    if triggered_api == "none" or triggered_api == "":
        # "none" or empty = no specific API triggered, use cached for all
        return False
    else:
        # Specific API triggered = fetch fresh only for that API
        return api_id == triggered_api


def load_openapi(api_id: str, use_cached: bool = False) -> tuple[dict, Path]:
    """
    Load and inline the OpenAPI specification for the given API ID.

    :param api_id: The identifier for the API to load.
    :param use_cached: If True, use cached OpenAPI spec if available; otherwise, fetch it.
                       Ignored if SATVU_TRIGGERED_API environment variable is set.
    :return: The inlined OpenAPI specification as a dictionary.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    openapi_url = f"{BASE_URL.rstrip('/')}/{APIS[api_id]}/openapi.json"
    cache_file = (
        CACHE_DIR
        / f"{api_id}-{sha1(openapi_url.encode(), usedforsecurity=False).hexdigest()}.json"
    )

    fetch_fresh = _should_fetch_fresh(api_id, use_cached)
    cache_exists = cache_file.exists()

    # Fetch fresh if needed, or if cache doesn't exist (graceful fallback)
    if fetch_fresh or not cache_exists:
        if not fetch_fresh and not cache_exists:
            print(f"  [CACHE] No cached spec for {api_id}, fetching fresh")
        elif fetch_fresh:
            triggered = os.environ.get(SATVU_TRIGGERED_API_ENV_VAR, "")
            if triggered:
                print(f"  [CACHE] Fetching fresh spec for triggered API: {api_id}")
            else:
                print(f"  [CACHE] Fetching fresh spec for {api_id}")

        response = get(openapi_url)
        response.raise_for_status()
        openapi = response.json()

        bundled_openapi = bundle_openapi_schema(openapi)
        cache_file.write_text(dumps(bundled_openapi))
    else:
        print(f"  [CACHE] Using cached spec for {api_id}")

    return loads(cache_file.read_text()), cache_file
