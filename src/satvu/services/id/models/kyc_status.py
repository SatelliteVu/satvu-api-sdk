from enum import Enum


class KycStatus(str, Enum):
    FAILED = "Failed"
    NOT_COMPLETED = "Not completed"
    PASSED = "Passed"

    def __str__(self) -> str:
        return str(self.value)
