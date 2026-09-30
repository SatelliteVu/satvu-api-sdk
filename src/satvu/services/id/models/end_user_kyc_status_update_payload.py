# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime

from pydantic import BaseModel, ConfigDict, Field

from ..models.kyc_status import KycStatus


class EndUserKYCStatusUpdatePayload(BaseModel):
    """
    Attributes:
        reseller_end_user_email (str): Email address of end user.
        reseller_end_user_id (str): Unique identifier of reseller end user.
        kyc_status ('KycStatus'):
        kyc_status_last_updated (datetime.datetime): Datetime when KYC status of end user was last updated.
        reseller_end_user_company_id (str): Unique identifier of reseller end user company.
        reseller_end_user_created_at (datetime.datetime): Creation datetime of reseller end user.
        user_id (str): Auth0 user ID of an associated reseller
    """

    reseller_end_user_email: str = Field(
        ...,
        description="""Email address of end user.""",
        alias="reseller_end_user_email",
    )
    reseller_end_user_id: str = Field(
        ...,
        description="""Unique identifier of reseller end user.""",
        alias="reseller_end_user_id",
    )
    kyc_status: KycStatus = Field(..., description=None, alias="kyc_status")
    kyc_status_last_updated: datetime.datetime = Field(
        ...,
        description="""Datetime when KYC status of end user was last updated.""",
        alias="kyc_status_last_updated",
    )
    reseller_end_user_company_id: str = Field(
        ...,
        description="""Unique identifier of reseller end user company.""",
        alias="reseller_end_user_company_id",
    )
    reseller_end_user_created_at: datetime.datetime = Field(
        ...,
        description="""Creation datetime of reseller end user.""",
        alias="reseller_end_user_created_at",
    )
    user_id: str = Field(
        ..., description="""Auth0 user ID of an associated reseller""", alias="user_id"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
