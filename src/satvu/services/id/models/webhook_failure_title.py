from enum import StrEnum


class WebhookFailureTitle(StrEnum):
    HTTP_STATUS_ERROR = "HTTP Status Error"
    TIMEOUT = "Timeout"
    UNREACHABLE = "Unreachable"

    def __str__(self) -> str:
        return str(self.value)
