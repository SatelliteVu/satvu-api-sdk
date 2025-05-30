from enum import Enum


class ResellerWebhookEvent(str, Enum):
    RESELLERKYC_STATUS = "reseller:kyc_status"

    def __str__(self) -> str:
        return str(self.value)
