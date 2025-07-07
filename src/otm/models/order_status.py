from enum import Enum


class OrderStatus(str, Enum):
    CANCELLED = "cancelled"
    COMMITTED = "committed"
    EXPIRED = "expired"
    FAILED = "failed"
    FULFILLED = "fulfilled"
    IN_PROGRESS = "in progress"
    REJECTED = "rejected"
    STAGED = "staged"

    def __str__(self) -> str:
        return str(self.value)
