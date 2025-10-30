from enum import Enum


class Filter(str, Enum):
    DAY = "DAY"
    NIGHT = "NIGHT"

    def __str__(self) -> str:
        return str(self.value)
