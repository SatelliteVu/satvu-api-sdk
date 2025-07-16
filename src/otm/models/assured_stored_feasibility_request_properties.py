from typing import Literal

from pydantic import BaseModel, Field

from ..models.feasibility_request_status import FeasibilityRequestStatus


class AssuredStoredFeasibilityRequestProperties(BaseModel):
    """Properties of the stored assured priority feasibility request.

    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the request.
        status (FeasibilityRequestStatus):
        created_at (datetime.datetime): The datetime at which the feasibility request was created.
        updated_at (datetime.datetime): The datetime at which the feasibility request was last updated.
    """

    product: Literal["assured"] = Field("assured", description="Assured Priority.")
    datetime: str = Field(
        ..., description="The closed date-time interval of the request."
    )
    status: FeasibilityRequestStatus = Field(..., description=None)
    created_at: datetime.datetime = Field(
        ..., description="The datetime at which the feasibility request was created."
    )
    updated_at: datetime.datetime = Field(
        ...,
        description="The datetime at which the feasibility request was last updated.",
    )
