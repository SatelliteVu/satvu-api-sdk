from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.arithmetic_expression_op import ArithmeticExpressionOp

if TYPE_CHECKING:
    from ..models.property_ref import PropertyRef


class ArithmeticExpression(BaseModel):
    """
    Attributes:
        op ('ArithmeticExpressionOp'):
        args (list[Union['ArithmeticExpression', 'PropertyRef', float]]):
    """

    op: "ArithmeticExpressionOp" = Field(..., description=None, alias="op")
    args: list[Union["ArithmeticExpression", "PropertyRef", float]] = Field(
        ..., description=None, alias="args"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
