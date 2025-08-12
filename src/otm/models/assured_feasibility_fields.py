from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AssuredFeasibilityFields(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
    """

    product: Literal["assured"] = Field(
        "assured", description="Assured Priority.", alias="product"
    )
    datetime_: str = Field(
        ...,
        description="The closed date-time interval of the request.",
        alias="datetime",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
