from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.company_address_country_code import CompanyAddressCountryCode


class CompanyAddress(BaseModel):
    """
    Attributes:
        country_code ('CompanyAddressCountryCode'): 2-digit country code of company.
        postcode (Union[None, str]): The postcode/zip code of the company.
        street (Union[None, str]): The street of the company.
    """

    country_code: "CompanyAddressCountryCode" = Field(
        ..., description="2-digit country code of company.", alias="country_code"
    )
    postcode: Union[None, str] = Field(
        None, description="The postcode/zip code of the company.", alias="postcode"
    )
    street: Union[None, str] = Field(
        None, description="The street of the company.", alias="street"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
