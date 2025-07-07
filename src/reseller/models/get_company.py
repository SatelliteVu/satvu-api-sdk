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

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "name",
            "country",
            "id",
            "kyc_status",
            "created_date",
            "updated_date",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "name": str,
            "country": str,
            "id": UUID,
            "kyc_status": object,
            "created_date": object,
            "updated_date": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "kyc_completed_on": object,
        }
