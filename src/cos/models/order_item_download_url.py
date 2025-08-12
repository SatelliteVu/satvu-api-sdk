from pydantic import BaseModel, Field


class OrderItemDownloadUrl(BaseModel):
    """Response payload for an order item download

    Attributes:
        url (str): The presigned download URL for the item.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str = Field(..., description="The presigned download URL for the item.")
    ttl: int = Field(
        ...,
        description="The time-to-live for the presigned download URL until it expires.",
    )
