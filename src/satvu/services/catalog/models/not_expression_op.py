from enum import StrEnum


class NotExpressionOp(StrEnum):
    NOT = "not"

    def __str__(self) -> str:
        return str(self.value)
