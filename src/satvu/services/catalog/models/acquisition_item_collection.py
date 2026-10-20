from enum import StrEnum


class AcquisitionItemCollection(StrEnum):
    ACQUISITION = "acquisition"

    def __str__(self) -> str:
        return str(self.value)
