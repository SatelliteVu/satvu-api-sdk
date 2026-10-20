from enum import StrEnum


class WebhookEvent(StrEnum):
    TASKING_ORDER_STATUS = "tasking:order_status"

    def __str__(self) -> str:
        return str(self.value)
