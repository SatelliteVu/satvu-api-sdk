from enum import StrEnum


class ArithmeticExpressionOp(StrEnum):
    DIV = "div"
    VALUE_0 = "+"
    VALUE_1 = "-"
    VALUE_2 = "*"
    VALUE_3 = "/"
    VALUE_4 = "^"
    VALUE_5 = "%"

    def __str__(self) -> str:
        return str(self.value)
