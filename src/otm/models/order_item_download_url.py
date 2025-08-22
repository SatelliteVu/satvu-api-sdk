from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class OrderItemDownloadUrl(BaseModel):
    """Payload for order item download URL response without redirect.

    Attributes:
        url (str): The presigned download URL for the item.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str = Field(
        ..., description="The presigned download URL for the item.", alias="url"
    )
    ttl: int = Field(
        ...,
        description="The time-to-live for the presigned download URL until it expires.",
        alias="ttl",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
