from typing import TypedDict


class OrderItemDownloadUrl(TypedDict):
    """
    Attributes:
        url (str): The presigned download URL for the item.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str
    ttl: int
