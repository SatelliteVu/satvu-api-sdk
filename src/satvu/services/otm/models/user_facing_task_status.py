from enum import Enum


class UserFacingTaskStatus(str, Enum):
    FAILED = "failed"
    FULFILLED = "fulfilled"
    IN_PROGRESS = "in progress"
    NOT_FULFILLED = "not fulfilled"
    PLANNED = "planned"
    PROCESSING = "processing"
    REJECTED = "rejected"

    def __str__(self) -> str:
        return str(self.value)
