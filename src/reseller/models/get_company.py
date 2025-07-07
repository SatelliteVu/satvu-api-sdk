import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel

from ..models.kyc_status import KYCStatus


class GetCompany(BaseModel):
    """
    Attributes:
        name (str): Name of the company.
        country (str): Country of the company.
        id (UUID): Unique identifier of the company.
        kyc_status (KYCStatus):
        created_date (datetime.date): The date when the user was created.
        updated_date (datetime.date): The date when the user was last updated.
        kyc_completed_on (Union[None, datetime.date]): The date when KYC was completed for the company, if applicable.
            In YYYY-MM-DD format.
    """

    name: str
    country: str
    id: UUID
    kyc_status: KYCStatus
    created_date: datetime.date
    updated_date: datetime.date
    kyc_completed_on: Union[None, datetime.date] = None
