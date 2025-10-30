from enum import Enum


class ReadoutMode(str, Enum):
    ITR = "ITR"
    IWR = "IWR"

    def __str__(self) -> str:
        return str(self.value)
