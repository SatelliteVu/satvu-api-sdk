from typing import Union

from pydantic import BaseModel

from ..models.company_address_country_code import CompanyAddressCountryCode


class CompanyAddress(BaseModel):
    """
    Attributes:
        country_code (CompanyAddressCountryCode): 2-digit country code of company.
        postcode (Union[None, str]): The postcode/zip code of the company.
        street (Union[None, str]): The street of the company.
    """

    country_code: CompanyAddressCountryCode
    postcode: Union[None, str] = None
    street: Union[None, str] = None
