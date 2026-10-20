# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.arithmetic_expression_op import ArithmeticExpressionOp

if TYPE_CHECKING:
    from ..models.property_ref import PropertyRef


class ArithmeticExpression(pydantic.BaseModel):
    """
    Attributes:
        args (list[Union['ArithmeticExpression', 'PropertyRef', float]]):
        op ('ArithmeticExpressionOp'):
    """

    args: list[Union[ArithmeticExpression, PropertyRef, float]] = pydantic.Field(
        ..., description=None, alias="args"
    )
    op: ArithmeticExpressionOp = pydantic.Field(..., description=None, alias="op")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
