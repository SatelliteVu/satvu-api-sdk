from enum import Enum


class ResellerWebhookEvent(str, Enum):
    RESELLER_KYC_STATUS = "reseller:kyc_status"

    def __str__(self) -> str:
        return str(self.value)
