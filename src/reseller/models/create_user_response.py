import datetime
from dataclasses import dataclass
from typing import TYPE_CHECKING, Union
from uuid import UUID

from ..models.kyc_status import KYCStatus

if TYPE_CHECKING:
    from ..models.company_address import CompanyAddress


@dataclass
class CreateUserResponse:
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

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "company_kyc_status",
            "company_id",
            "company_name",
            "company_address",
            "user_kyc_status",
            "user_email",
            "user_name",
            "user_id",
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
            "company_address": object,
            "user_kyc_status": object,
            "user_email": str,
            "user_name": str,
            "user_id": str,
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
