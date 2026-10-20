from enum import StrEnum


class NotificationCategory(StrEnum):
    TASKING = "tasking"

    def __str__(self) -> str:
        return str(self.value)
