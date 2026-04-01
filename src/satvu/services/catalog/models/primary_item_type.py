from enum import Enum


class PrimaryItemType(str, Enum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
