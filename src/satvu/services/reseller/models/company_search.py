# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Literal, Union

import pydantic

from ..models.company_search_fields import CompanySearchFields
from ..models.match_type import MatchType


class CompanySearch(pydantic.BaseModel):
    """
    Attributes:
        string (str): Search string.
        type_ (Union[None, 'MatchType']):
        fields (Union[None, list['CompanySearchFields'] | Literal['all']]): Fields to search against. Either a list of
            fields or `all`. Defaults to `all`.
    """

    string: str = pydantic.Field(..., description="""Search string.""", alias="string")
    type_: Union[None, MatchType] = pydantic.Field(
        default=None, description=None, alias="type"
    )
    fields: Union[None, list[CompanySearchFields] | Literal["all"]] = pydantic.Field(
        default=None,
        description="""Fields to search against. Either a list of fields or `all`. Defaults to `all`.""",
        alias="fields",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
