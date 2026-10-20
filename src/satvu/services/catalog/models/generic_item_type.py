from enum import StrEnum


class GenericItemType(StrEnum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
