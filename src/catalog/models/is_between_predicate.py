from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.arithmetic_expression import ArithmeticExpression
    from ..models.is_between_predicate_op import IsBetweenPredicateOp
    from ..models.property_ref import PropertyRef


class IsBetweenPredicate(BaseModel):
    """
    Attributes:
        op (IsBetweenPredicateOp):
        args (list[Union['ArithmeticExpression', 'PropertyRef', float]]):
    """

    op: IsBetweenPredicateOp = Field(..., description=None, alias="op")
    args: list[Union["ArithmeticExpression", "PropertyRef", float]] = Field(
        ..., description=None, alias="args"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
