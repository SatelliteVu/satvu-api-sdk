# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.is_like_predicate_op import IsLikePredicateOp

if TYPE_CHECKING:
    from ..models.property_ref import PropertyRef


class IsLikePredicate(pydantic.BaseModel):
    """
    Attributes:
        args (list[Union['PropertyRef', str]]):
        op ('IsLikePredicateOp'):
    """

    args: list[Union[PropertyRef, str]] = pydantic.Field(
        ..., description=None, alias="args"
    )
    op: IsLikePredicateOp = pydantic.Field(..., description=None, alias="op")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
