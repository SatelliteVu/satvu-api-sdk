from dataclasses import dataclass


@dataclass
class RouterHttpError:
    """
    Attributes:
        id (str): A unique identifier for the type of error
        message (str): An error message describing what went wrong
    """

    id: str
    message: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "id",
            "message",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "id": str,
            "message": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
