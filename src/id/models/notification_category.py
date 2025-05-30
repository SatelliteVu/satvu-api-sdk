from enum import Enum


class NotificationCategory(str, Enum):
    RESELLER = "reseller"
    TASKING = "tasking"

    def __str__(self) -> str:
        return str(self.value)
