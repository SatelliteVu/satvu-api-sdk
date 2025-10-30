from enum import Enum


class SatvuFilter(str, Enum):
    DAY = "day"
    NIGHT = "night"

    def __str__(self) -> str:
        return str(self.value)
