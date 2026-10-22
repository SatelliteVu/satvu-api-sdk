"""Callable union discriminators used by generated models."""

from collections.abc import Callable
from typing import Any

from pydantic import BaseModel


def const_tag(
    alias: str, default: str | None = None, python_name: str | None = None
) -> Callable[[Any], Any]:
    """
    Build a discriminator that dispatches on a constant field.

    Reads ``alias`` (or ``python_name``) from a dict, or the field with that
    alias from a model instance. A missing field maps to ``default``: the
    variant where the spec makes the constant optional. ``None`` lets Pydantic
    report a missing tag.

    :param alias: The constant's wire name, e.g. ``"type"``.
    :param default: The tag for a value that omits the field.
    :param python_name: The attribute name, when it differs from ``alias``
        (e.g. ``"type_"``). Models accept both, so dicts may use either.
    """

    def tag(value: Any) -> Any:
        if isinstance(value, dict):
            if alias in value:
                return value[alias]
            return value.get(python_name, default) if python_name else default
        if isinstance(value, BaseModel):
            for name, field in type(value).model_fields.items():
                if (field.alias or name) == alias:
                    return getattr(value, name)
        return default

    return tag
