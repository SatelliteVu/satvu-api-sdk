from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.binary_comparison_predicate_op import BinaryComparisonPredicateOp

if TYPE_CHECKING:
    from ..models.arithmetic_expression import ArithmeticExpression
    from ..models.date_instant import DateInstant
    from ..models.property_ref import PropertyRef
    from ..models.timestamp_instant import TimestampInstant


class BinaryComparisonPredicate(BaseModel):
    """
    Attributes:
        op ('BinaryComparisonPredicateOp'):
        args (list[Union['ArithmeticExpression', 'DateInstant', 'PropertyRef', 'TimestampInstant', bool, float, str]]):
    """

    op: "BinaryComparisonPredicateOp" = Field(..., description=None, alias="op")
    args: list[
        Union[
            "ArithmeticExpression",
            "DateInstant",
            "PropertyRef",
            "TimestampInstant",
            bool,
            float,
            str,
        ]
    ] = Field(..., description=None, alias="args")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
