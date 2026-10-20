# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING
from uuid import UUID

import pydantic

from ..models.kyc_status import KYCStatus

if TYPE_CHECKING:
    from ..models.company_address import CompanyAddress


class CreateUserResponse(pydantic.BaseModel):
    """Represents response when creating user

    Attributes:
        company_kyc_status ('KYCStatus'):
        company_id (UUID): The unique identifier for the company.
        company_name (str): The name of the company.
        company_address (CompanyAddress):
        user_kyc_status ('KYCStatus'):
        user_email (str): The email address of the user.
        user_name (str): The full name of the user.
        user_id (str): The unique identifier for the user.
        company_kyc_completed_on (datetime.date | None): The date when KYC was completed for the company, if applicable.
            In YYYY-MM-DD format.
        user_kyc_completed_on (datetime.date | None): The date when KYC was completed for the user, if applicable. In
            YYYY-MM-DD format.
    """

    company_kyc_status: KYCStatus = pydantic.Field(
        ..., description=None, alias="company_kyc_status"
    )
    company_id: UUID = pydantic.Field(
        ...,
        description="""The unique identifier for the company.""",
        alias="company_id",
    )
    company_name: str = pydantic.Field(
        ..., description="""The name of the company.""", alias="company_name"
    )
    company_address: CompanyAddress = pydantic.Field(
        ..., description=None, alias="company_address"
    )
    user_kyc_status: KYCStatus = pydantic.Field(
        ..., description=None, alias="user_kyc_status"
    )
    user_email: str = pydantic.Field(
        ..., description="""The email address of the user.""", alias="user_email"
    )
    user_name: str = pydantic.Field(
        ..., description="""The full name of the user.""", alias="user_name"
    )
    user_id: str = pydantic.Field(
        ..., description="""The unique identifier for the user.""", alias="user_id"
    )
    company_kyc_completed_on: datetime.date | None = pydantic.Field(
        default=None,
        description="""The date when KYC was completed for the company, if applicable. In YYYY-MM-DD format.""",
        alias="company_kyc_completed_on",
    )
    user_kyc_completed_on: datetime.date | None = pydantic.Field(
        default=None,
        description="""The date when KYC was completed for the user, if applicable. In YYYY-MM-DD format.""",
        alias="user_kyc_completed_on",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
