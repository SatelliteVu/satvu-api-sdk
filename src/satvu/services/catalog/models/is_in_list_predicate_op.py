from enum import StrEnum


class IsInListPredicateOp(StrEnum):
    IN = "in"

    def __str__(self) -> str:
        return str(self.value)
