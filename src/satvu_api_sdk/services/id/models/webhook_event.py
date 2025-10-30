from enum import Enum


class WebhookEvent(str, Enum):
    TASKING_ORDER_STATUS = "tasking:order_status"

    def __str__(self) -> str:
        return str(self.value)
