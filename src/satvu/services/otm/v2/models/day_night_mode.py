from enum import StrEnum


class DayNightMode(StrEnum):
    DAY = "day"
    DAY_NIGHT = "day-night"
    NIGHT = "night"

    def __str__(self) -> str:
        return str(self.value)
