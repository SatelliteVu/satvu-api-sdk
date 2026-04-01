from enum import Enum


class NotExpressionOp(str, Enum):
    NOT = "not"

    def __str__(self) -> str:
        return str(self.value)
