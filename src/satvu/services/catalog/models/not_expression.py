# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

from ..models.not_expression_op import NotExpressionOp

if TYPE_CHECKING:
    from ..models.and_or_expression import AndOrExpression
    from ..models.binary_comparison_predicate import BinaryComparisonPredicate
    from ..models.is_between_predicate import IsBetweenPredicate
    from ..models.is_in_list_predicate import IsInListPredicate
    from ..models.is_like_predicate import IsLikePredicate
    from ..models.is_null_predicate import IsNullPredicate


class NotExpression(pydantic.BaseModel):
    """
    Attributes:
        args (list[Union['AndOrExpression', 'BinaryComparisonPredicate', 'IsBetweenPredicate', 'IsInListPredicate',
            'IsLikePredicate', 'IsNullPredicate', 'NotExpression', bool]]):
        op ('NotExpressionOp'):
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
    op: NotExpressionOp = pydantic.Field(..., description=None, alias="op")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
