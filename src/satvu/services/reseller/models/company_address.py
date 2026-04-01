# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field

from ..models.country_code import CountryCode


class CompanyAddress(BaseModel):
    """
    Attributes:
        country_code ('CountryCode'): 2-digit country code of company.
        postcode (None | str): The postcode/zip code of the company.
        street (None | str): The street of the company.
    """

    country_code: CountryCode = Field(
        ..., description="""2-digit country code of company.""", alias="country_code"
    )
    postcode: None | str = Field(
        default=None,
        description="""The postcode/zip code of the company.""",
        alias="postcode",
    )
    street: None | str = Field(
        default=None, description="""The street of the company.""", alias="street"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
