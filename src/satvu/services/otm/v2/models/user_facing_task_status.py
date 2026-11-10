from enum import StrEnum


class UserFacingTaskStatus(StrEnum):
    FAILED = "failed"
    FULFILLED = "fulfilled"
    IN_PROGRESS = "in progress"
    NOT_FULFILLED = "not fulfilled"
    PROCESSING = "processing"

    def __str__(self) -> str:
        return str(self.value)
