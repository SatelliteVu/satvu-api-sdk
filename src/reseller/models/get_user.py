from __future__ import annotations

import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from ..models.kyc_status import KYCStatus


class GetUser(BaseModel):
    """Represents response to user

    Attributes:
        company_kyc_status ('KYCStatus'):
        company_id (UUID): The unique identifier for the company.
        company_name (str): The name of the company.
        user_kyc_status ('KYCStatus'):
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

    company_kyc_status: "KYCStatus" = Field(
        ..., description=None, alias="company_kyc_status"
    )
    company_id: UUID = Field(
        ..., description="The unique identifier for the company.", alias="company_id"
    )
    company_name: str = Field(
        ..., description="The name of the company.", alias="company_name"
    )
    user_kyc_status: "KYCStatus" = Field(..., description=None, alias="user_kyc_status")
    user_email: str = Field(
        ..., description="The email address of the user.", alias="user_email"
    )
    user_name: str = Field(
        ..., description="The full name of the user.", alias="user_name"
    )
    user_id: str = Field(
        ..., description="The unique identifier for the user.", alias="user_id"
    )
    user_created_date: datetime.date = Field(
        ...,
        description="The date when the user was created.",
        alias="user_created_date",
    )
    user_updated_date: datetime.date = Field(
        ...,
        description="The date when the user was last updated.",
        alias="user_updated_date",
    )
    company_kyc_completed_on: Union[None, datetime.date] = Field(
        None,
        description="The date when KYC was completed for the company, if applicable. In YYYY-MM-DD format.",
        alias="company_kyc_completed_on",
    )
    user_kyc_completed_on: Union[None, datetime.date] = Field(
        None,
        description="The date when KYC was completed for the user, if applicable. In YYYY-MM-DD format.",
        alias="user_kyc_completed_on",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
