from enum import StrEnum


class OrderStatus(StrEnum):
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    FAILED = "failed"
    FULFILLED = "fulfilled"
    IN_PROGRESS = "in progress"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
