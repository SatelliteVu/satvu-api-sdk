from enum import Enum


class AcquisitionItemCollection(str, Enum):
    ACQUISITION = "acquisition"

    def __str__(self) -> str:
        return str(self.value)
