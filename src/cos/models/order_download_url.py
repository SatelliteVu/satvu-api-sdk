from typing import TypedDict


class OrderDownloadUrl(TypedDict):
    """
    Attributes:
        url (str): The presigned download URL for the order.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str
    ttl: int
