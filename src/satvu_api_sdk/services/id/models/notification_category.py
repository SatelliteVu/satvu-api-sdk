from enum import Enum


class NotificationCategory(str, Enum):
    TASKING = "tasking"

    def __str__(self) -> str:
        return str(self.value)
