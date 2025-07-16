from pydantic import BaseModel, Field


class OrderDownloadUrl(BaseModel):
    """
    Attributes:
        url (str): The presigned download URL for the order.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str = Field(..., description="The presigned download URL for the order.")
    ttl: int = Field(
        ...,
        description="The time-to-live for the presigned download URL until it expires.",
    )
