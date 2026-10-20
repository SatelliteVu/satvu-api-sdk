from enum import StrEnum


class KycStatus(StrEnum):
    FAILED = "Failed"
    NOT_COMPLETED = "Not completed"
    PASSED = "Passed"

    def __str__(self) -> str:
        return str(self.value)
