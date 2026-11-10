# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class OrderItemDownloadUrl(pydantic.BaseModel):
    """Payload for order item download URL response without redirect.

    Attributes:
        url (str): The presigned download URL for the item.
        ttl (int): The time-to-live for the presigned download URL until it expires.
    """

    url: str = pydantic.Field(
        ..., description="""The presigned download URL for the item.""", alias="url"
    )
    ttl: int = pydantic.Field(
        ...,
        description="""The time-to-live for the presigned download URL until it expires.""",
        alias="ttl",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
