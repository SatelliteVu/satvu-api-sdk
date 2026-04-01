from enum import Enum


class IsNullPredicateOp(str, Enum):
    ISNULL = "isNull"

    def __str__(self) -> str:
        return str(self.value)
