from enum import StrEnum


class IsBetweenPredicateOp(StrEnum):
    BETWEEN = "between"

    def __str__(self) -> str:
        return str(self.value)
