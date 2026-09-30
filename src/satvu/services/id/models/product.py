from enum import Enum


class Product(str, Enum):
    ASSURED = "assured"
    STANDARD = "standard"

    def __str__(self) -> str:
        return str(self.value)
