from enum import StrEnum


class Method(StrEnum):
    GET = "GET"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
