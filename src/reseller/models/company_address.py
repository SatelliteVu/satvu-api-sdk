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

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "country_code",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "country_code": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "postcode": object,
            "street": object,
        }
