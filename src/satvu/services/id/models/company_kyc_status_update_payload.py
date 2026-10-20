# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime

import pydantic

from ..models.kyc_status import KycStatus


class CompanyKYCStatusUpdatePayload(pydantic.BaseModel):
    """
    Attributes:
        company_name (str): Company name
        company_id (str): Unique identifier of end company.
        company_country (str): Country that end company resides in.
        kyc_status ('KycStatus'):
        kyc_status_last_updated (datetime.datetime): Datetime when KYC status of end company was last updated.
        company_created_at (datetime.datetime): Creation datetime of end company.
        user_id (str): Auth0 user ID of an associated reseller
    """

    company_name: str = pydantic.Field(
        ..., description="""Company name""", alias="company_name"
    )
    company_id: str = pydantic.Field(
        ..., description="""Unique identifier of end company.""", alias="company_id"
    )
    company_country: str = pydantic.Field(
        ...,
        description="""Country that end company resides in.""",
        alias="company_country",
    )
    kyc_status: KycStatus = pydantic.Field(..., description=None, alias="kyc_status")
    kyc_status_last_updated: datetime.datetime = pydantic.Field(
        ...,
        description="""Datetime when KYC status of end company was last updated.""",
        alias="kyc_status_last_updated",
    )
    company_created_at: datetime.datetime = pydantic.Field(
        ...,
        description="""Creation datetime of end company.""",
        alias="company_created_at",
    )
    user_id: str = pydantic.Field(
        ..., description="""Auth0 user ID of an associated reseller""", alias="user_id"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
