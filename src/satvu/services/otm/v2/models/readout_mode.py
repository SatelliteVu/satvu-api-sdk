from enum import StrEnum


class ReadoutMode(StrEnum):
    ITR = "ITR"
    IWR = "IWR"

    def __str__(self) -> str:
        return str(self.value)
