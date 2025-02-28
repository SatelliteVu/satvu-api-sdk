from enum import Enum


class WebhookEvent(str, Enum):
    TASKINGORDER_STATUS = "tasking:order_status"

    def __str__(self) -> str:
        return str(self.value)
