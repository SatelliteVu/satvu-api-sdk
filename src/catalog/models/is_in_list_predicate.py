from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union

    from ..models.arithmetic_expression import ArithmeticExpression
    from ..models.date_instant import DateInstant
    from ..models.is_in_list_predicate_op import IsInListPredicateOp
    from ..models.property_ref import PropertyRef
    from ..models.timestamp_instant import TimestampInstant


class IsInListPredicate(BaseModel):
    """
    Attributes:
        op (IsInListPredicateOp):
        args (list[Union['ArithmeticExpression', 'DateInstant', 'PropertyRef', 'TimestampInstant', bool, float,
            list[Union['ArithmeticExpression', 'DateInstant', 'PropertyRef', 'TimestampInstant', bool, float, str]], str]]):
    """

    op: IsInListPredicateOp = Field(..., description=None, alias="op")
    args: list[
        Union[
            "ArithmeticExpression",
            "DateInstant",
            "PropertyRef",
            "TimestampInstant",
            bool,
            float,
            list[
                Union[
                    "ArithmeticExpression",
                    "DateInstant",
                    "PropertyRef",
                    "TimestampInstant",
                    bool,
                    float,
                    str,
                ]
            ],
            str,
        ]
    ] = Field(..., description=None, alias="args")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
