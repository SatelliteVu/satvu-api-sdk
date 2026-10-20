from enum import StrEnum


class PrimaryItemCollection(StrEnum):
    PRIMARY = "primary"

    def __str__(self) -> str:
        return str(self.value)
