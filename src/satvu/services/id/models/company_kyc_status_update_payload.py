# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..models.kyc_status import KycStatus


class CompanyKYCStatusUpdatePayload(BaseModel):
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

    company_name: str = Field(..., description="""Company name""", alias="company_name")
    company_id: str = Field(
        ..., description="""Unique identifier of end company.""", alias="company_id"
    )
    company_country: str = Field(
        ...,
        description="""Country that end company resides in.""",
        alias="company_country",
    )
    kyc_status: KycStatus = Field(..., description=None, alias="kyc_status")
    kyc_status_last_updated: datetime.datetime = Field(
        ...,
        description="""Datetime when KYC status of end company was last updated.""",
        alias="kyc_status_last_updated",
    )
    company_created_at: datetime.datetime = Field(
        ...,
        description="""Creation datetime of end company.""",
        alias="company_created_at",
    )
    user_id: str = Field(
        ..., description="""Auth0 user ID of an associated reseller""", alias="user_id"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
