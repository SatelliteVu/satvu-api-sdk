import datetime
from typing import Literal

from pydantic import BaseModel

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

    product: Literal["assured"]
    datetime: str
    status: FeasibilityRequestStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
