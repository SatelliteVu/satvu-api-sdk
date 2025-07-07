import datetime
from dataclasses import dataclass
from typing import Literal

from ..models.feasibility_request_status import FeasibilityRequestStatus


@dataclass
class AssuredStoredFeasibilityRequestProperties:
    """Properties of the stored assured priority feasibility request.

    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime_ (str): The closed date-time interval of the request.
        status (FeasibilityRequestStatus):
        created_at (datetime.datetime): The datetime at which the feasibility request was created.
        updated_at (datetime.datetime): The datetime at which the feasibility request was last updated.
    """

    product: Literal["assured"]
    datetime_: str
    status: FeasibilityRequestStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "product",
            "datetime",
            "status",
            "created_at",
            "updated_at",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "product": object,
            "datetime": str,
            "status": object,
            "created_at": object,
            "updated_at": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
