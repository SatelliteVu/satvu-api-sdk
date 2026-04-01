from enum import Enum


class VisualItemCollection(str, Enum):
    VISUAL = "visual"

    def __str__(self) -> str:
        return str(self.value)
