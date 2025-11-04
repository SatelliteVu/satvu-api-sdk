import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Sequence

from openapi_python_client import Project
from openapi_python_client.config import Config, ConfigFile, MetaType
from openapi_python_client.parser.openapi import GeneratorData, Endpoint
from openapi_python_client.parser.errors import GeneratorError
from openapi_python_client.parser.bodies import Body
from openapi_python_client.parser.properties import UnionProperty, ListProperty

from builder.config import APIS
from builder.load import load_openapi
from builder.jinja_filters import to_pydantic_model_field
from builder.openapi_preprocessor import preprocess_for_sdk_generation
import openapi_python_client.parser.openapi


BASE_DIR = (Path(__file__).parent / "..").resolve()
TEMPLATE_DIR = Path(__file__).parent / "templates"
SRC_DIR = BASE_DIR / "src" / "satvu_api_sdk" / "services"


def set_models_prefix_for_api(api_id: str) -> None:
    """
    Set the models_relative_prefix for openapi-python-client per API build.

    This tells openapi-python-client how to generate import statements.
    The builder will fix these imports in templates to match our structure:

    Generated: from {api_id}.models.foo import Bar
    Template fixes to: from satvu_api_sdk.services.{api_id}.models.foo import Bar

    Args:
        api_id: The API identifier (e.g., 'catalog', 'wallet')

    Note:
        This modifies global state in openapi-python-client. It's necessary
        because the library uses this internally during parsing. The builder
        must call this before each API build.
    """

    openapi_python_client.parser.openapi.models_relative_prefix = f"{api_id}."


@dataclass
class BuildContext:
    """Context for building a single API service."""

    api_id: str
    base_path: str
    output_dir: Path
    template_dir: Path
    strip_version_prefix: bool = True


@dataclass
class EnhancedEndpoint:
    """Endpoint with additional metadata for template rendering."""

    endpoint: Endpoint
    body_docstrings: list[str] = field(default_factory=list)


class EndpointTransformer:
    """Applies transformations to endpoints."""

    def __init__(self, context: BuildContext):
        self.context = context

    def transform(self, endpoint: Endpoint) -> EnhancedEndpoint:
        """Apply all transformations to an endpoint."""
        enhanced = EnhancedEndpoint(endpoint=endpoint)

        # Transform path (remove version prefix)
        if self.context.strip_version_prefix and endpoint.path.startswith("/v"):
            parts = endpoint.path.split("/", 2)
            if len(parts) > 2:
                endpoint.path = "/" + parts[2]

        # Generate body docstrings
        if endpoint.bodies:
            enhanced.body_docstrings = self._generate_body_docstrings(
                endpoint.bodies[0]
            )

        return enhanced

    def _generate_body_docstrings(self, body: Body) -> list[str]:
        """Generate docstrings for request body."""
        docstrings = []

        if isinstance(body.prop, UnionProperty):
            models = body.prop.inner_properties
            docstring = f"body ({body.prop.get_type_string()}):\n"
            docstring += "One of:\n"

            for model in models:
                model_docstring = f"- {model.get_type_string()}: {model.description}\n"
                docstring += model_docstring

            docstrings.append(docstring)
        else:
            body_prop = (
                body.prop.inner_property
                if isinstance(body.prop, ListProperty)
                else body.prop
            )
            docstring = f"body ({body_prop.get_type_string()}): {body_prop.description}"
            docstrings.append(docstring)

        return docstrings


class ServiceCodeGenerator:
    """Generates service code using custom templates."""

    def __init__(self, project: Project, context: BuildContext):
        self.project = project
        self.context = context
        self.transformer = EndpointTransformer(context)

    def generate(self) -> Sequence[GeneratorError]:
        """Generate service code."""
        errors = []

        # Build models (standard)
        self.project._build_models()

        # Build API with customizations
        try:
            self._build_service_class()
        except Exception as e:
            errors.append(GeneratorError(detail=f"Failed to build service class: {e}"))

        # Run post hooks
        self.project._run_post_hooks()

        return errors + list(self.project._get_errors())

    def _build_service_class(self):
        """Generate the service class file."""
        api_dir = self.project.package_dir
        api_init_path = api_dir / "__init__.py"

        # Generate __init__.py
        api_init_template = self.project.env.get_template("api_init.py.jinja")
        api_init_path.write_text(
            api_init_template.render(), encoding=self.project.config.file_encoding
        )

        # Transform endpoints
        enhanced_endpoints = []
        for collection in self.project.openapi.endpoint_collections_by_tag.values():
            for endpoint in collection.endpoints:
                enhanced = self.transformer.transform(endpoint)
                enhanced_endpoints.append(enhanced)

        # Generate api.py
        api_class_path = api_dir / "api.py"
        endpoint_template = self.project.env.get_template(
            "endpoint_module.py.jinja",
            globals={"isbool": lambda obj: obj.get_base_type_string() == "bool"},
        )
        endpoint_template.environment.filters["split"] = lambda s, sep: s.split(sep)

        # Prepare template context
        template_context = {
            "endpoints": [e.endpoint for e in enhanced_endpoints],
            "api_id": self.context.api_id,
            "base_path": self.context.base_path,
        }

        # Add body_docstrings to endpoints
        for enhanced, endpoint in zip(
            enhanced_endpoints, template_context["endpoints"]
        ):
            endpoint.body_docstrings = enhanced.body_docstrings

        api_class_path.write_text(
            endpoint_template.render(**template_context),
            encoding=self.project.config.file_encoding,
        )


def build_service(api_id: str, use_cached: bool = False) -> Sequence[GeneratorError]:
    """
    Build an API service.

    Args:
        api_id: API identifier
        use_cached: Use cached OpenAPI spec

    Returns:
        List of errors (empty on success)
    """
    print(f"Building {api_id} service...")

    # Create build context
    context = BuildContext(
        api_id=api_id,
        base_path=APIS[api_id],
        output_dir=SRC_DIR / api_id,
        template_dir=TEMPLATE_DIR,
        strip_version_prefix=True,
    )

    # Set models prefix for this API (needed by library for import generation)
    set_models_prefix_for_api(api_id)

    # Load OpenAPI spec
    try:
        openapi_dict, openapi_src = load_openapi(api_id, use_cached)
        # Preprocess the spec to fix issues that would require patching
        openapi_dict = preprocess_for_sdk_generation(openapi_dict)
    except Exception as e:
        return [GeneratorError(detail=f"Failed to load OpenAPI spec: {e}")]

    # Ensure output directory exists (important for build environments)
    context.output_dir.mkdir(parents=True, exist_ok=True)

    # Configure generator
    config = Config.from_sources(
        config_file=ConfigFile(),
        meta_type=MetaType.NONE,
        document_source=openapi_src,
        file_encoding="utf-8",
        overwrite=True,
        output_path=context.output_dir,
    )

    # Parse OpenAPI
    openapi = GeneratorData.from_dict(openapi_dict, config=config)
    if isinstance(openapi, GeneratorError):
        return [openapi]

    # Create project with custom templates
    project = Project(
        openapi=openapi,
        custom_template_path=context.template_dir,
        config=config,
    )

    # Register custom Jinja filters
    project.env.filters["to_pydantic_field"] = to_pydantic_model_field

    # Generate using our custom generator
    generator = ServiceCodeGenerator(project, context)
    errors = generator.generate()

    if errors:
        print(f"  ✗ Failed with {len(errors)} error(s)")
        for error in errors:
            print(f"    - {error.detail}")
    else:
        print(f"  ✓ Generated to {context.output_dir}")

    return errors


def build_all(use_cached: bool = False) -> dict[str, list[GeneratorError]]:
    """Build all API services."""
    results = {}

    for api_id in APIS.keys():
        print(f"\n{'=' * 60}")
        errors = build_service(api_id, use_cached)
        results[api_id] = errors

    print(f"\n{'=' * 60}")
    successful = sum(1 for e in results.values() if not e)
    print(f"Summary: {successful}/{len(results)} services built successfully")

    return results


def build(api_id: str, use_cached: bool = False) -> None:
    """Main entry point (CLI compatible)."""
    if api_id == "all":
        results = build_all(use_cached)
        if any(results.values()):
            sys.exit(1)
    else:
        errors = build_service(api_id, use_cached)
        if errors:
            print("\nErrors:")
            for error in errors:
                print(f"  {error.detail}")
            sys.exit(1)
