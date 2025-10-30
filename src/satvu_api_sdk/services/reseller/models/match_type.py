from enum import Enum


class MatchType(str, Enum):
    EXACT = "exact"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
