from enum import Enum


class ResellerNotificationConfigTopic(str, Enum):
    RESELLER_KYC_STATUS = "reseller:kyc_status"
    TASKING_ORDER_STATUS = "tasking:order_status"

    def __str__(self) -> str:
        return str(self.value)
