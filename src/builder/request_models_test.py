"""Tests for collecting the models reachable from request bodies."""

import json
from types import SimpleNamespace
from typing import cast

import pytest
from openapi_python_client import Project
from openapi_python_client.config import Config, ConfigFile, MetaType
from openapi_python_client.parser.openapi import GeneratorData

from builder.request_models import collect_request_models, request_model_component


def _json_body(ref: str) -> dict:
    return {"content": {"application/json": {"schema": {"$ref": ref}}}}


_SPEC = {
    "openapi": "3.1.0",
    "info": {"title": "test", "version": "1"},
    "paths": {
        "/orders": {
            "post": {
                "operationId": "create_order",
                "requestBody": {
                    "required": True,
                    **_json_body("#/components/schemas/order_request"),
                },
                "responses": {
                    "200": {
                        "description": "ok",
                        **_json_body("#/components/schemas/OrderResponse"),
                    }
                },
            }
        }
    },
    "components": {
        "schemas": {
            "order_request": {
                "type": "object",
                "required": ["type", "geometry", "props"],
                "properties": {
                    "type": {"const": "Feature"},
                    "geometry": {
                        "anyOf": [
                            {"$ref": "#/components/schemas/Point"},
                            {
                                "type": "array",
                                "items": {"$ref": "#/components/schemas/Polygon"},
                            },
                        ]
                    },
                    "props": {
                        "type": "object",
                        "required": ["product"],
                        "properties": {"product": {"const": "assured"}},
                    },
                },
            },
            "Point": {
                "type": "object",
                "required": ["type"],
                "properties": {"type": {"const": "Point"}},
            },
            "Polygon": {
                "type": "object",
                "required": ["type"],
                "properties": {"type": {"const": "Polygon"}},
            },
            "OrderResponse": {
                "type": "object",
                "required": ["type"],
                "properties": {"type": {"const": "Feature"}},
            },
        }
    },
}


@pytest.fixture(scope="module")
def project(tmp_path_factory) -> Project:
    spec_file = tmp_path_factory.mktemp("spec") / "openapi.json"
    spec_file.write_text(json.dumps(_SPEC), encoding="utf-8")
    config = Config.from_sources(
        config_file=ConfigFile(),
        meta_type=MetaType.NONE,
        document_source=spec_file,
        file_encoding="utf-8",
        overwrite=True,
        output_path=None,
    )
    openapi = GeneratorData.from_dict(_SPEC, config=config)
    assert isinstance(openapi, GeneratorData)
    return cast(Project, SimpleNamespace(openapi=openapi))


@pytest.fixture(scope="module")
def collected_names(project) -> list[str]:
    return [str(model.class_info.name) for model in collect_request_models(project)]


def test_collects_body_models_through_unions_lists_and_inline_objects(collected_names):
    assert set(collected_names) == {
        "OrderRequest",
        "OrderRequestProps",
        "Point",
        "Polygon",
    }


def test_response_only_models_are_not_request_models(collected_names):
    assert "OrderResponse" not in collected_names


def test_collected_models_are_sorted_by_class_name(collected_names):
    assert collected_names == sorted(collected_names)


@pytest.mark.parametrize(
    ("class_name", "component"),
    [
        ("OrderRequest", "order_request"),
        ("Point", "Point"),
        ("OrderRequestProps", None),
    ],
)
def test_request_model_component(project, class_name, component):
    model = next(
        model
        for model in collect_request_models(project)
        if model.class_info.name == class_name
    )
    assert request_model_component(model) == component
