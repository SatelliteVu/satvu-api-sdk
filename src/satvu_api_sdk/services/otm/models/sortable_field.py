from enum import Enum


class SortableField(str, Enum):
    STATUS = "status"

    def __str__(self) -> str:
        return str(self.value)
