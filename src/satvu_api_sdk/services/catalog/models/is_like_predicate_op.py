from enum import Enum


class IsLikePredicateOp(str, Enum):
    LIKE = "like"

    def __str__(self) -> str:
        return str(self.value)
