from enum import Enum


class WebhookFailureTitle(str, Enum):
    HTTP_STATUS_ERROR = "HTTP Status Error"
    TIMEOUT = "Timeout"
    UNREACHABLE = "Unreachable"

    def __str__(self) -> str:
        return str(self.value)
