from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.is_like_predicate_op import IsLikePredicateOp

if TYPE_CHECKING:
    from ..models.property_ref import PropertyRef


class IsLikePredicate(BaseModel):
    """
    Attributes:
        op ('IsLikePredicateOp'):
        args (list[Union['PropertyRef', str]]):
    """

    op: "IsLikePredicateOp" = Field(..., description=None, alias="op")
    args: list[Union["PropertyRef", str]] = Field(..., description=None, alias="args")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
