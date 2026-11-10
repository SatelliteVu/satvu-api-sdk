from enum import StrEnum


class Filter(StrEnum):
    DAY = "DAY"
    NIGHT = "NIGHT"

    def __str__(self) -> str:
        return str(self.value)
