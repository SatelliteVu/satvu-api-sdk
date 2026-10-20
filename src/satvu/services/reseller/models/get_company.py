# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from uuid import UUID

import pydantic

from ..models.country_code import CountryCode
from ..models.kyc_status import KYCStatus


class GetCompany(pydantic.BaseModel):
    """
    Attributes:
        name (str): The name of the company.
        country (str): Country of the company.
        country_code ('CountryCode'): 2-digit ISO country code of the company.
        id (UUID): Unique identifier of the company.
        kyc_status ('KYCStatus'):
        created_date (datetime.date): The date when the user was created.
        updated_date (datetime.date): The date when the user was last updated.
        kyc_completed_on (datetime.date | None): The date when KYC was completed for the company, if applicable. In
            YYYY-MM-DD format.
    """

    name: str = pydantic.Field(
        ..., description="""The name of the company.""", alias="name"
    )
    country: str = pydantic.Field(
        ..., description="""Country of the company.""", alias="country"
    )
    country_code: CountryCode = pydantic.Field(
        ...,
        description="""2-digit ISO country code of the company.""",
        alias="country_code",
    )
    id: UUID = pydantic.Field(
        ..., description="""Unique identifier of the company.""", alias="id"
    )
    kyc_status: KYCStatus = pydantic.Field(..., description=None, alias="kyc_status")
    created_date: datetime.date = pydantic.Field(
        ..., description="""The date when the user was created.""", alias="created_date"
    )
    updated_date: datetime.date = pydantic.Field(
        ...,
        description="""The date when the user was last updated.""",
        alias="updated_date",
    )
    kyc_completed_on: datetime.date | None = pydantic.Field(
        default=None,
        description="""The date when KYC was completed for the company, if applicable. In YYYY-MM-DD format.""",
        alias="kyc_completed_on",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
