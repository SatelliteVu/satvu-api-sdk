from enum import Enum


class ResellerNotificationDescriptionTopic(str, Enum):
    RESELLERKYC_STATUS = "reseller:kyc_status"
    TASKINGORDER_STATUS = "tasking:order_status"

    def __str__(self) -> str:
        return str(self.value)
