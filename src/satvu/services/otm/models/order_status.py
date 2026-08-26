from enum import Enum


class OrderStatus(str, Enum):
    CANCELLED = "cancelled"
    EXPIRED = "expired"
    FAILED = "failed"
    FULFILLED = "fulfilled"
    IN_PROGRESS = "in progress"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
