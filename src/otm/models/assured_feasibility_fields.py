from typing import Literal

from pydantic import BaseModel


class AssuredFeasibilityFields(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the request.
    """

    product: Literal["assured"] = "assured"
    datetime: str
