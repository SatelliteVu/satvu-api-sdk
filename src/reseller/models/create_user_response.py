import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel

from ..models.company_address import CompanyAddress
from ..models.kyc_status import KYCStatus


class CreateUserResponse(BaseModel):
    """Represents response when creating user

    Attributes:
        company_kyc_status (KYCStatus):
        company_id (UUID): The unique identifier for the company.
        company_name (str): The name of the company.
        company_address (CompanyAddress):
        user_kyc_status (KYCStatus):
        user_email (str): The email address of the user.
        user_name (str): The full name of the user.
        user_id (str): The unique identifier for the user.
        company_kyc_completed_on (Union[None, datetime.date]): The date when KYC was completed for the company, if
            applicable. In YYYY-MM-DD format.
        user_kyc_completed_on (Union[None, datetime.date]): The date when KYC was completed for the user, if applicable.
            In YYYY-MM-DD format.
    """

    company_kyc_status: KYCStatus
    company_id: UUID
    company_name: str
    company_address: "CompanyAddress"
    user_kyc_status: KYCStatus
    user_email: str
    user_name: str
    user_id: str
    company_kyc_completed_on: Union[None, datetime.date] = None
    user_kyc_completed_on: Union[None, datetime.date] = None
