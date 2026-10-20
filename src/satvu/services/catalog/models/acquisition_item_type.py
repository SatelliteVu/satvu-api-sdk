from enum import StrEnum


class AcquisitionItemType(StrEnum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
