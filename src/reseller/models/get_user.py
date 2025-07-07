import datetime
from dataclasses import dataclass
from typing import Union
from uuid import UUID

from ..models.kyc_status import KYCStatus


@dataclass
class GetUser:
    """Represents response to user

    Attributes:
        company_kyc_status (KYCStatus):
        company_id (UUID): The unique identifier for the company.
        company_name (str): The name of the company.
        user_kyc_status (KYCStatus):
        user_email (str): The email address of the user.
        user_name (str): The full name of the user.
        user_id (str): The unique identifier for the user.
        user_created_date (datetime.date): The date when the user was created.
        user_updated_date (datetime.date): The date when the user was last updated.
        company_kyc_completed_on (Union[None, datetime.date]): The date when KYC was completed for the company, if
            applicable. In YYYY-MM-DD format.
        user_kyc_completed_on (Union[None, datetime.date]): The date when KYC was completed for the user, if applicable.
            In YYYY-MM-DD format.
    """

    company_kyc_status: KYCStatus
    company_id: UUID
    company_name: str
    user_kyc_status: KYCStatus
    user_email: str
    user_name: str
    user_id: str
    user_created_date: datetime.date
    user_updated_date: datetime.date
    company_kyc_completed_on: Union[None, datetime.date] = None
    user_kyc_completed_on: Union[None, datetime.date] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "company_kyc_status",
            "company_id",
            "company_name",
            "user_kyc_status",
            "user_email",
            "user_name",
            "user_id",
            "user_created_date",
            "user_updated_date",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "company_kyc_status": object,
            "company_id": UUID,
            "company_name": str,
            "user_kyc_status": object,
            "user_email": str,
            "user_name": str,
            "user_id": str,
            "user_created_date": object,
            "user_updated_date": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "company_kyc_completed_on": object,
            "user_kyc_completed_on": object,
        }
