"""Tests for openapi-python-client patches."""

import pytest
from openapi_python_client.config import Config, ConfigFile, MetaType
from openapi_python_client.parser.openapi import GeneratorData
from openapi_python_client.parser.properties.enum_property import EnumProperty


def _model_with_op(values: list[str | None]) -> dict:
    return {
        "type": "object",
        "properties": {"op": {"type": "string", "enum": values, "title": "Op"}},
        "required": ["op"],
    }


def _spec(schemas: dict) -> dict:
    return {
        "openapi": "3.1.0",
        "info": {"title": "test", "version": "1"},
        "paths": {},
        "components": {"schemas": schemas},
    }


def _generate(tmp_path, spec: dict) -> GeneratorData:
    config = Config.from_sources(
        config_file=ConfigFile(),
        meta_type=MetaType.NONE,
        document_source=tmp_path / "openapi.json",
        file_encoding="utf-8",
        overwrite=True,
        output_path=None,
    )
    openapi = GeneratorData.from_dict(spec, config=config)
    assert isinstance(openapi, GeneratorData)
    return openapi


def _class_names(openapi: GeneratorData) -> set[str]:
    return {str(model.class_info.name) for model in openapi.models} | {
        str(enum.class_info.name) for enum in openapi.enums
    }


@pytest.fixture
def clashing_titles(tmp_path) -> GeneratorData:
    """Same shape as cql2alchemy's CQL2 schemas: every `op` enum is titled "Op"."""
    return _generate(
        tmp_path,
        _spec(
            {
                "CQL2Combination": _model_with_op(["and", "or"]),
                "CQL2Comparison": _model_with_op(["=", "<>"]),
            }
        ),
    )


def test_clashing_enum_titles_keep_both_models(clashing_titles):
    names = _class_names(clashing_titles)

    assert {"CQL2Combination", "CQL2Comparison"} <= names
    assert clashing_titles.errors == []


def test_clashing_enum_title_falls_back_to_parent_prefix(clashing_titles):
    assert {"Op", "CQL2ComparisonOp"} <= _class_names(clashing_titles)


def test_clashing_nullable_enum_keeps_its_values(tmp_path):
    """The first, unprefixed build attempt must not consume the retry's schema."""
    openapi = _generate(
        tmp_path,
        _spec(
            {
                "A": _model_with_op(["x", "y"]),
                "B": _model_with_op(["p", "q", None]),
            }
        ),
    )

    enums = {str(enum.class_info.name): enum for enum in openapi.enums}
    assert openapi.errors == []
    assert isinstance(enums["BOp"], EnumProperty)
    assert set(enums["BOp"].values.values()) == {"p", "q"}


@pytest.mark.parametrize(
    "schemas",
    [
        pytest.param({"A": _model_with_op(["x"])}, id="unique-title"),
        pytest.param(
            {"A": _model_with_op(["x", "y"]), "B": _model_with_op(["x", "y"])},
            id="identical-values-share-a-title",
        ),
    ],
)
def test_non_clashing_title_is_used_without_prefix(tmp_path, schemas):
    openapi = _generate(tmp_path, _spec(schemas))

    assert [str(enum.class_info.name) for enum in openapi.enums] == ["Op"]
