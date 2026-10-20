from enum import StrEnum


class SatvuFilter(StrEnum):
    DAY = "day"
    NIGHT = "night"

    def __str__(self) -> str:
        return str(self.value)
