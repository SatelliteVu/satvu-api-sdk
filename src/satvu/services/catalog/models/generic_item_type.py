from enum import Enum


class GenericItemType(str, Enum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
