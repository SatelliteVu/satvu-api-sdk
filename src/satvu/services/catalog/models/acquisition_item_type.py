from enum import Enum


class AcquisitionItemType(str, Enum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
