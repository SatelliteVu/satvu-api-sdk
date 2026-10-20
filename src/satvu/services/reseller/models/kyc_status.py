from enum import StrEnum


class KYCStatus(StrEnum):
    FAILED = "Failed"
    NOT_COMPLETED = "Not completed"
    PASSED = "Passed"

    def __str__(self) -> str:
        return str(self.value)
