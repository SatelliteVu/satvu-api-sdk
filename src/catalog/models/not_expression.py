from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.and_or_expression import AndOrExpression
from ..models.binary_comparison_predicate import BinaryComparisonPredicate
from ..models.is_between_predicate import IsBetweenPredicate
from ..models.is_in_list_predicate import IsInListPredicate
from ..models.is_like_predicate import IsLikePredicate
from ..models.is_null_predicate import IsNullPredicate
from ..models.not_expression_op import NotExpressionOp


class NotExpression(BaseModel):
    """
    Attributes:
        op (NotExpressionOp):
        args (list[Union['AndOrExpression', 'BinaryComparisonPredicate', 'IsBetweenPredicate', 'IsInListPredicate',
            'IsLikePredicate', 'IsNullPredicate', 'NotExpression', bool]]):
    """

    op: NotExpressionOp = Field(..., description=None, alias="op")
    args: list[
        Union[
            "AndOrExpression",
            "BinaryComparisonPredicate",
            "IsBetweenPredicate",
            "IsInListPredicate",
            "IsLikePredicate",
            "IsNullPredicate",
            "NotExpression",
            bool,
        ]
    ] = Field(..., description=None, alias="args")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
