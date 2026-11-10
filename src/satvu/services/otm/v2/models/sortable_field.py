from enum import StrEnum


class SortableField(StrEnum):
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
