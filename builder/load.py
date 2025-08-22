import copy
from hashlib import sha1
from json import dumps, loads
from pathlib import Path
from typing import Any

from httpx import get

from builder.config import BASE_URL, APIS

BASE_DIR = (Path(__file__).parent / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"


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
        for comp_type, comp_dict in NEW_COMPONENTS.items():
            bundled["components"][comp_type].update(NEW_COMPONENTS["schemas"])
    return bundled


def load_openapi(api_id: str, use_cached: bool = False) -> tuple[dict, Path]:
    """
    Load and inline the OpenAPI specification for the given API ID.

    :param api_id: The identifier for the API to load.
    :param use_cached: If True, use cached OpenAPI spec if available; otherwise, fetch it.
    :return: The inlined OpenAPI specification as a dictionary.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    openapi_url = f"{BASE_URL.rstrip('/')}/{APIS[api_id]}/openapi.json"
    cache_file = (
        CACHE_DIR
        / f"{api_id}-{sha1(openapi_url.encode(), usedforsecurity=False).hexdigest()}.json"
    )

    if not use_cached:
        response = get(openapi_url)
        response.raise_for_status()
        openapi = response.json()

        bundled_openapi = bundle_openapi_schema(openapi)
        cache_file.write_text(dumps(bundled_openapi))

    return loads(cache_file.read_text()), cache_file
