from enum import Enum


class FeasibilityRequestStatus(str, Enum):
    FAILED = "failed"
    FEASIBLE = "feasible"
    NOT_FEASIBLE = "not feasible"
    PENDING = "pending"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
