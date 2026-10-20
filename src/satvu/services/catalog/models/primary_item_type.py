from enum import StrEnum


class PrimaryItemType(StrEnum):
    FEATURE = "Feature"

    def __str__(self) -> str:
        return str(self.value)
