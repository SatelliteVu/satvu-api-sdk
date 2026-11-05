"""Build every generated service, and the stable alias for versioned APIs."""

import shutil
import sys

from jinja2 import Environment, FileSystemLoader
from openapi_python_client.parser.errors import GeneratorError

from builder.build import SRC_DIR, TEMPLATE_DIR, build_service
from builder.config import APIS, ServiceTarget, VersionedApi, service_targets


def _write_stable_alias(api_id: str, api: VersionedApi) -> None:
    """Generate the API root modules that re-export the stable version."""
    # Renders Python source, so HTML autoescaping would corrupt it.
    env = Environment(  # nosec B701
        loader=FileSystemLoader(TEMPLATE_DIR), keep_trailing_newline=True
    )
    targets = service_targets(api_id)
    context = {
        "api_id": api_id,
        "class_name": ServiceTarget(api=api_id, base_path="").class_name,
        "stable": next(t for t in targets if t.version == api.stable),
        "targets": targets,
    }
    root = SRC_DIR / api_id
    (root / "models").mkdir(parents=True, exist_ok=True)
    for template, path in (
        ("api_init.py.jinja", root / "__init__.py"),
        ("stable_alias_api.py.jinja", root / "api.py"),
        ("stable_alias_models_init.py.jinja", root / "models" / "__init__.py"),
    ):
        path.write_text(env.get_template(template).render(**context), encoding="utf-8")
    print(f"  ✓ {api_id} root re-exports stable version {api.stable}")


def build_api(
    api_id: str, use_cached: bool = False, generate_tests: bool = False
) -> list[GeneratorError]:
    """Build every service for an API, plus the stable alias if it is versioned."""
    entry = APIS[api_id]
    root = SRC_DIR / api_id
    if isinstance(entry, VersionedApi) and root.exists():
        # Everything under a versioned API's root is generated, and the library only
        # clears models/, so wipe it to drop versions (or a flat layout) since removed.
        shutil.rmtree(root)

    errors: list[GeneratorError] = []
    stable_built = False
    for target in service_targets(api_id):
        target_errors = build_service(target, use_cached, generate_tests=generate_tests)
        errors.extend(target_errors)
        if isinstance(entry, VersionedApi) and target.version == entry.stable:
            stable_built = not target_errors

    # The alias only depends on the stable version; without it `sdk.py` can't import
    # the API at all, so a failing non-stable version mustn't take it down too.
    if isinstance(entry, VersionedApi) and stable_built:
        _write_stable_alias(api_id, entry)
    return errors


def build_all(
    use_cached: bool = False, generate_tests: bool = False
) -> dict[str, list[GeneratorError]]:
    """Build all API services."""
    results = {}

    for api_id in APIS:
        print(f"\n{'=' * 60}")
        results[api_id] = build_api(api_id, use_cached, generate_tests=generate_tests)

    print(f"\n{'=' * 60}")
    successful = sum(1 for e in results.values() if not e)
    print(f"Summary: {successful}/{len(results)} services built successfully")

    return results


def build(api_id: str, use_cached: bool = False, generate_tests: bool = False) -> None:
    """Main entry point (CLI compatible)."""
    if api_id == "all":
        results = build_all(use_cached, generate_tests=generate_tests)
        if any(results.values()):
            sys.exit(1)
    else:
        errors = build_api(api_id, use_cached, generate_tests=generate_tests)
        if errors:
            print("\nErrors:")
            for error in errors:
                print(f"  {error.detail}")
            sys.exit(1)
