import datetime
from typing import Union
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

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

    name: str = Field(..., description="Name of the company.", alias="name")
    country: str = Field(..., description="Country of the company.", alias="country")
    id: UUID = Field(..., description="Unique identifier of the company.", alias="id")
    kyc_status: KYCStatus = Field(..., description=None, alias="kyc_status")
    created_date: datetime.date = Field(
        ..., description="The date when the user was created.", alias="created_date"
    )
    updated_date: datetime.date = Field(
        ...,
        description="The date when the user was last updated.",
        alias="updated_date",
    )
    kyc_completed_on: Union[None, datetime.date] = Field(
        None,
        description="The date when KYC was completed for the company, if applicable. In YYYY-MM-DD format.",
        alias="kyc_completed_on",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
