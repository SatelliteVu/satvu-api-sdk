from enum import Enum


class IsInListPredicateOp(str, Enum):
    IN = "in"

    def __str__(self) -> str:
        return str(self.value)
