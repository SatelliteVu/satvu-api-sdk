from enum import Enum


class ResellerNotificationDescriptionTopic(str, Enum):
    RESELLER_KYC_STATUS = "reseller:kyc_status"
    TASKING_ORDER_STATUS = "tasking:order_status"

    def __str__(self) -> str:
        return str(self.value)
