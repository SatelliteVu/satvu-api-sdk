# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.and_or_expression_op import AndOrExpressionOp

if TYPE_CHECKING:
    from ..models.binary_comparison_predicate import BinaryComparisonPredicate
    from ..models.is_between_predicate import IsBetweenPredicate
    from ..models.is_in_list_predicate import IsInListPredicate
    from ..models.is_like_predicate import IsLikePredicate
    from ..models.is_null_predicate import IsNullPredicate
    from ..models.not_expression import NotExpression


class AndOrExpression(pydantic.BaseModel):
    """
    Attributes:
        args (list[Union['AndOrExpression', 'BinaryComparisonPredicate', 'IsBetweenPredicate', 'IsInListPredicate',
            'IsLikePredicate', 'IsNullPredicate', 'NotExpression', bool]]):
        op ('AndOrExpressionOp'):
    """

    args: list[
        Union[
            AndOrExpression,
            BinaryComparisonPredicate,
            IsBetweenPredicate,
            IsInListPredicate,
            IsLikePredicate,
            IsNullPredicate,
            NotExpression,
            bool,
        ]
    ] = pydantic.Field(..., description=None, alias="args")
    op: AndOrExpressionOp = pydantic.Field(..., description=None, alias="op")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
