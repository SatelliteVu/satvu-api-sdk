from enum import StrEnum


class IsLikePredicateOp(StrEnum):
    LIKE = "like"

    def __str__(self) -> str:
        return str(self.value)
