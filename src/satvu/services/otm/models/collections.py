from enum import StrEnum


class Collections(StrEnum):
    FEASIBILITY_REQUESTS = "feasibility_requests"
    FEASIBILITY_RESPONSES = "feasibility_responses"
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
