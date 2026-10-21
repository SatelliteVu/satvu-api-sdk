"""
Collect every model that can appear inside a request body.

A request model is tested on its own, not only through the endpoint body that
contains it: callers build nested models (e.g. `Point(coordinates=...)`)
directly, so each one has to serialise to a spec-valid object by itself.
"""

from collections.abc import Iterator
from typing import Any

from openapi_python_client import Project
from openapi_python_client.parser.properties.list_property import ListProperty
from openapi_python_client.parser.properties.model_property import ModelProperty
from openapi_python_client.parser.properties.protocol import PropertyProtocol
from openapi_python_client.parser.properties.union import UnionProperty

# Component models are named by their $ref path; inline models by their property
_COMPONENT_PREFIX = "/components/schemas/"


def _model_refs(prop: PropertyProtocol) -> Iterator[str]:
    """Yield the class names of every model referenced directly by ``prop``."""
    if isinstance(prop, ModelProperty):
        yield str(prop.class_info.name)
    elif isinstance(prop, UnionProperty):
        for inner in prop.inner_properties:
            yield from _model_refs(inner)
    elif isinstance(prop, ListProperty):
        yield from _model_refs(prop.inner_property)


def collect_request_models(project: Project) -> list[ModelProperty]:
    """
    Return every model reachable from a request body, sorted by class name.

    Nested references are resolved against the project's processed models,
    because a property's own ModelProperty copy may not carry its fields.
    """
    models = {str(model.class_info.name): model for model in project.openapi.models}

    pending = [
        name
        for collection in project.openapi.endpoint_collections_by_tag.values()
        for endpoint in collection.endpoints
        for body in endpoint.bodies
        for name in _model_refs(body.prop)
    ]
    seen: dict[str, ModelProperty] = {}
    while pending:
        name = pending.pop()
        if name in seen or name not in models:
            continue
        model = models[name]
        seen[name] = model
        for prop in (model.required_properties or []) + (
            model.optional_properties or []
        ):
            pending.extend(_model_refs(prop))

    return [seen[name] for name in sorted(seen)]


def request_model_component(model: ModelProperty) -> str | None:
    """Return the component schema a model was generated from, or None if inline."""
    name = model.name.get_untrusted_value()
    if name.startswith(_COMPONENT_PREFIX):
        return name.removeprefix(_COMPONENT_PREFIX)
    return None


def request_model_schema(model: ModelProperty) -> dict[str, Any]:
    """Return the raw JSON schema the model was generated from."""
    return model.data.model_dump(mode="json", by_alias=True, exclude_none=True)
