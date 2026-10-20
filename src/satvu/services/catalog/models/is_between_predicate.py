# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.is_between_predicate_op import IsBetweenPredicateOp

if TYPE_CHECKING:
    from ..models.arithmetic_expression import ArithmeticExpression
    from ..models.property_ref import PropertyRef


class IsBetweenPredicate(pydantic.BaseModel):
    """
    Attributes:
        args (list[Union['ArithmeticExpression', 'PropertyRef', float]]):
        op ('IsBetweenPredicateOp'):
    """

    args: list[Union[ArithmeticExpression, PropertyRef, float]] = pydantic.Field(
        ..., description=None, alias="args"
    )
    op: IsBetweenPredicateOp = pydantic.Field(..., description=None, alias="op")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
