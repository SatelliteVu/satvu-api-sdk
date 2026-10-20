from enum import StrEnum


class Product(StrEnum):
    ASSURED = "assured"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
