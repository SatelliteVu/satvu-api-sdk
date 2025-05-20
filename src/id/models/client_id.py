from dataclasses import dataclass


@dataclass
class ClientID:
    """
    Attributes:
        client_id (str):
    """

    client_id: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "client_id",
        }
