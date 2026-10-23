"""
Detect unions whose variants are told apart by a shared constant field.

OTM's standard and assured variants share `product`, but only the assured one
requires it: a body without `product` is standard. The SDK gives every
constant a default, so without a discriminator the assured variant accepts that
body too and Pydantic's smart union mode can pick it. Dispatching on the
constant - with a missing tag meaning the one variant where it is optional -
restores the spec's meaning, without needing a spec-level `discriminator:`.
"""

from dataclasses import dataclass

from openapi_python_client.parser.properties.model_property import ModelProperty
from openapi_python_client.parser.properties.none import NoneProperty
from openapi_python_client.parser.properties.union import UnionProperty
from openapi_python_client.schema import Schema, UntrustedString
from openapi_python_client.strings import in_double_quote_literal

from builder.code_strings import unwrap_code
from builder.jinja_filters.field_names import field_name_for_alias


@dataclass(frozen=True)
class ConstTag:
    alias: str
    # (variant type string, tag value), in the union's rendering order
    variants: tuple[tuple[str, str], ...]
    default: str | None
    nullable: bool

    def type_string(self) -> str:
        tagged = ", ".join(
            f"Annotated[{type_string}, pydantic.Tag({_literal(tag)})]"
            for type_string, tag in self.variants
        )
        default = _literal(self.default) if self.default is not None else "None"
        # validate_by_name accepts dicts keyed by attribute name, so look there too
        python_name = field_name_for_alias(self.alias)
        by_name = (
            f", python_name={_literal(python_name)}"
            if python_name != self.alias
            else ""
        )
        annotated = (
            f"Annotated[Union[{tagged}], pydantic.Discriminator("
            f"const_tag({_literal(self.alias)}, default={default}{by_name}))]"
        )
        return f"Union[None, {annotated}]" if self.nullable else annotated


def _literal(value: str) -> str:
    """Render a spec-sourced string as a safely escaped Python literal."""
    return f'"{in_double_quote_literal(value)}"'


def _raw(value: object) -> str | None:
    """Return the raw text of a spec string (wrapped or plain), else None."""
    if isinstance(value, UntrustedString):
        return value.get_untrusted_value()
    return value if isinstance(value, str) else None


def _const_values(model: ModelProperty, alias: str) -> tuple[str, bool] | None:
    """Return (const value, required) of ``alias`` on ``model``, if it is a str const."""
    prop_schema = (model.data.properties or {}).get(UntrustedString(alias))
    if (
        not isinstance(prop_schema, Schema)
        or (const := _raw(prop_schema.const)) is None
    ):
        return None
    required = {_raw(name) for name in model.data.required or []}
    return const, alias in required


def _shared_const_aliases(models: list[ModelProperty]) -> list[str]:
    per_model = [
        {_raw(alias) for alias in model.data.properties or {}} for model in models
    ]
    return sorted(alias for alias in set.intersection(*per_model) if alias)


def const_tag_for(union_prop: UnionProperty) -> ConstTag | None:
    """
    Return the constant-field discriminator for ``union_prop``, if one applies.

    Applies when every non-null variant is a model, they share a string
    constant with a distinct value per variant, and at most one variant has it
    optional - that variant's value is the tag a missing field maps to. With two
    or more optional, a missing tag has no single answer, so smart mode stays.
    """
    models = [p for p in union_prop.inner_properties if isinstance(p, ModelProperty)]
    others = [
        p for p in union_prop.inner_properties if not isinstance(p, ModelProperty)
    ]
    if len(models) < 2 or not all(isinstance(p, NoneProperty) for p in others):
        return None

    for alias in _shared_const_aliases(models):
        values = [value for model in models if (value := _const_values(model, alias))]
        tags = [tag for tag, _ in values]
        if len(values) != len(models) or len(set(tags)) != len(tags):
            continue
        optional = [tag for tag, required in values if not required]
        if len(optional) > 1:
            continue

        variants = sorted(
            (
                (unwrap_code(model.get_type_string(no_optional=True)), tag)
                for model, tag in zip(models, tags, strict=True)
            ),
            key=lambda variant: variant[0].lower(),
        )
        return ConstTag(
            alias=alias,
            variants=tuple(variants),
            default=optional[0] if optional else None,
            nullable=bool(others) or not union_prop.required,
        )
    return None
