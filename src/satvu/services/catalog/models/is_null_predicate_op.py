from enum import StrEnum


class IsNullPredicateOp(StrEnum):
    ISNULL = "isNull"

    def __str__(self) -> str:
        return str(self.value)
