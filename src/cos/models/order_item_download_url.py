from pydantic import BaseModel


class OrderItemDownloadUrl(BaseModel):
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

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "url": str,
            "ttl": int,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
