from pydantic import BaseModel


class Price1(BaseModel):
    """
    Attributes:
        currency (str): The currency of the order.
        base (int): The base price of the order in minor units of the currency e.g. pence, cents.
        addon_withhold (int): The price of the order from the chosen withhold option in minor units of the currency e.g.
            pence, cents.
        total (int): The total price of the order in minor units of the currency e.g. pence, cents. This is the sum of
            the base and addon prices.
        value (int): Price of the order in minor units of the currency e.g. pence, cents.
    """

    currency: str
    base: int
    addon_withhold: int
    total: int
    value: int

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "currency",
            "base",
            "addon:withhold",
            "total",
            "value",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "currency": str,
            "base": int,
            "addon:withhold": int,
            "total": int,
            "value": int,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
