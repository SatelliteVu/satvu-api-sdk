from enum import StrEnum


class MatchType(StrEnum):
    EXACT = "exact"
    PARTIAL = "partial"

    def __str__(self) -> str:
        return str(self.value)
