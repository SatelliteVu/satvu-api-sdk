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
# Track which source URL each component came from (for relative ref resolution)
COMPONENT_SOURCES: dict[str, str] = {}  # component_name → source_url


def _fetch_and_merge_components(url: str) -> None:
    """Fetch an external OpenAPI doc and merge its components into NEW_COMPONENTS."""
    if url in FETCHED:
        return
    response = get(url)
    response.raise_for_status()
    ext_schema = response.json()
    ext_components = ext_schema.get("components", {})

    for comp_type, comp_dict in ext_components.items():
        if comp_type not in NEW_COMPONENTS:
            NEW_COMPONENTS[comp_type] = {}
        for comp_name, comp_val in comp_dict.items():
            if comp_name not in NEW_COMPONENTS[comp_type]:
                NEW_COMPONENTS[comp_type][comp_name] = comp_val
                COMPONENT_SOURCES[comp_name] = url

    FETCHED[url] = True


def _resolve_to_absolute_url(ref_path: str, source_url: str = "") -> str:
    """Convert a relative path ref to an absolute URL.

    Resolves relative to the source document's directory if available,
    otherwise falls back to BASE_URL.
    """
    base_dir = source_url.rsplit("/", 1)[0] if source_url else BASE_URL.rstrip("/")
    path = ref_path.lstrip("/")
    return f"{base_dir}/{path}"


def resolve_external_refs(schema: Any, source_url: str = "") -> Any:
    """
    Recursively resolve all external $ref references in an OpenAPI schema,
    merge their components, and rewrite $ref to local components.

    Handles:
    - Absolute URL refs: https://example.com/spec.json#/components/schemas/Foo
    - Relative path refs with fragment: /api/v1/spec.json#/components/schemas/Foo
    - Bare relative path refs: /api/v1/spec.json (no fragment — treated as dict type)

    :param schema: The OpenAPI schema to process.
    :param source_url: URL of the document containing these refs (for relative resolution).
    :return: The OpenAPI schema with all external references resolved and merged.
    """
    if isinstance(schema, dict):
        if "$ref" in schema:
            ref_path = schema["$ref"]

            # Local refs — pass through
            if ref_path.startswith("#"):
                return schema

            # Convert relative paths to absolute URLs
            if not ref_path.startswith("http://") and not ref_path.startswith(
                "https://"
            ):
                ref_path = _resolve_to_absolute_url(ref_path, source_url)

            # Bare ref (no fragment) — fetch components but use free-form dict
            if "#" not in ref_path:
                _fetch_and_merge_components(ref_path)
                return {"type": "object"}

            # Ref with fragment — fetch, merge, and rewrite to local ref
            url, fragment = ref_path.split("#", 1)
            _section, name = fragment.split("/", 1)
            _fetch_and_merge_components(url)
            return {"$ref": f"#/components/schemas/{name.split('/')[-1]}"}
        else:
            return {
                k: resolve_external_refs(v, source_url) for k, v in list(schema.items())
            }

    elif isinstance(schema, list):
        return [resolve_external_refs(item, source_url) for item in schema]

    else:
        return schema


def bundle_openapi_schema(schema: dict) -> dict:
    """
    Returns a bundled OpenAPI schema with all external references resolved and merged.
    This function processes the OpenAPI schema, resolves all external references,
    and merges any new components into the schema.

    Iterates resolution until no new external components are discovered,
    handling transitive external refs (e.g., cql2.json → geometry.json).

    :param schema: The OpenAPI schema to process.
    :return: The processed OpenAPI schema with resolved references and merged components.
    """
    NEW_COMPONENTS.clear()
    COMPONENT_SOURCES.clear()
    bundled = copy.deepcopy(schema)
    bundled = resolve_external_refs(bundled)

    # Iteratively resolve refs in newly merged components until stable.
    # Components from external docs may have their own relative refs
    # that need resolution relative to their source document's URL.
    while NEW_COMPONENTS:
        resolved_components: dict[str, dict] = {}
        for comp_type, comp_dict in NEW_COMPONENTS.items():
            resolved_components[comp_type] = {
                name: resolve_external_refs(val, COMPONENT_SOURCES.get(name, ""))
                for name, val in comp_dict.items()
            }
            if comp_type not in bundled.setdefault("components", {}):
                bundled["components"][comp_type] = {}
            bundled["components"][comp_type].update(resolved_components[comp_type])

        # Check if resolving introduced more new components
        remaining = {}
        for comp_type, comp_dict in NEW_COMPONENTS.items():
            new_names = set(comp_dict.keys()) - set(
                resolved_components.get(comp_type, {}).keys()
            )
            if new_names:
                remaining[comp_type] = {n: comp_dict[n] for n in new_names}

        NEW_COMPONENTS.clear()
        NEW_COMPONENTS.update(remaining)
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


def spec_content_hash(spec: dict) -> str:
    """
    Hash the *content* of an OpenAPI spec, for cache keys that must track the schema.

    Deliberately not the spec URL: the URL is stable across API releases, so a
    URL-derived key never invalidates and stale artefacts (e.g. pre-generated
    hypothesis examples) survive schema changes and get replayed against models
    that no longer accept them.

    :param spec: The OpenAPI spec, ideally after preprocessing, so that changes to
                 the preprocessor invalidate derived artefacts too.
    :return: Hex sha1 of the spec serialised canonically (key order normalised).
    """
    canonical = dumps(spec, sort_keys=True, separators=(",", ":"))
    return sha1(canonical.encode(), usedforsecurity=False).hexdigest()


def load_openapi(api_id: str, use_cached: bool = False) -> tuple[dict, Path]:
    """
    Load and inline the OpenAPI specification for the given API ID.

    :param api_id: The identifier for the API to load.
    :param use_cached: If True, use cached OpenAPI spec if available; otherwise, fetch it.
                       Ignored if SATVU_TRIGGERED_API environment variable is set.
    :return: The inlined OpenAPI specification as a dictionary.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    openapi_url = f"{BASE_URL.rstrip('/')}/{APIS[api_id].lstrip('/')}/openapi.json"
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
