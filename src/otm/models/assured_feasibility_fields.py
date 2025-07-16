from typing import Literal

from pydantic import BaseModel, Field


class AssuredFeasibilityFields(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the request.
    """

    product: Literal["assured"] = Field("assured", description="Assured Priority.")
    datetime: str = Field(
        ..., description="The closed date-time interval of the request."
    )
