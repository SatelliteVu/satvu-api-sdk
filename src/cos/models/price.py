from dataclasses import dataclass


@dataclass
class Price:
    """
    Attributes:
        value (int): The price of the order in minor units of the currency e.g. pence, cents.
        currency (str): The currency of the order.
    """

    value: int
    currency: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "value",
            "currency",
        }
