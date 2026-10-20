from enum import StrEnum


class RequestMethod(StrEnum):
    GET = "GET"

    def __str__(self) -> str:
        return str(self.value)
