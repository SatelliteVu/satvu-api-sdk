from enum import StrEnum


class FeasibilityRequestStatus(StrEnum):
    FAILED = "failed"
    FEASIBLE = "feasible"
    NOT_FEASIBLE = "not feasible"
    PENDING = "pending"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
