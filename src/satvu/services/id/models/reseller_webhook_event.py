from enum import StrEnum


class ResellerWebhookEvent(StrEnum):
    RESELLER_KYC_STATUS = "reseller:kyc_status"

    def __str__(self) -> str:
        return str(self.value)
