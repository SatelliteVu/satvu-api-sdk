from dataclasses import dataclass


@dataclass
class OrderItemDownloadUrl:
    """
    Attributes:
        url (str): The presigned download URL for the item.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str
    ttl: int

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "url",
            "ttl",
        }
