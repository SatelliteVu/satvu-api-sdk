from pydantic import BaseModel, ConfigDict, Field


class OrderDownloadUrl(BaseModel):
    """Response payload for an order download

    Attributes:
        url (str): The presigned download URL for the order.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str = Field(
        ..., description="The presigned download URL for the order.", alias="url"
    )
    ttl: int = Field(
        ...,
        description="The time-to-live for the presigned download URL until it expires.",
        alias="ttl",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
