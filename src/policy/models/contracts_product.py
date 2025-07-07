from pydantic import BaseModel


class ContractsProduct(BaseModel):
    """
    Attributes:
        code (str): Product code Example: PRODUCT.
        currency (str): Product currency Example: GBP.
        priority (int): Product priority Example: 40.
    """

    code: str
    currency: str
    priority: int

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "code",
            "currency",
            "priority",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "code": str,
            "currency": str,
            "priority": int,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
