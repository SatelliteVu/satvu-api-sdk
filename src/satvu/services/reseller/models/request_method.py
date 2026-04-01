from enum import Enum


class RequestMethod(str, Enum):
    GET = "GET"

    def __str__(self) -> str:
        return str(self.value)
