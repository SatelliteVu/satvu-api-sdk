from enum import Enum


class DayNightMode(str, Enum):
    DAY = "day"
    DAY_NIGHT = "day-night"
    NIGHT = "night"

    def __str__(self) -> str:
        return str(self.value)
