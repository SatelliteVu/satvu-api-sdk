from dataclasses import dataclass


@dataclass
class ClientCredentials:
    """
    Attributes:
        client_id (str):
        client_secret (str):
    """

    client_id: str
    client_secret: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "client_id",
            "client_secret",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "client_id": str,
            "client_secret": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
