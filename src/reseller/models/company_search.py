from typing import Literal, Union

from pydantic import BaseModel, Field

from ..models.company_search_fields import CompanySearchFields
from ..models.match_type import MatchType


class CompanySearch(BaseModel):
    """
    Attributes:
        string (str): Search string.
        type (Union[None, MatchType]):
        fields (Union[Literal['all'], list[CompanySearchFields]]): Fields to search against. Either a list of fields or
            `all`. Defaults to `all`.
    """

    string: str = Field(..., description="Search string.")
    type: Union[None, MatchType] = Field(None, description=None)
    fields: Union[Literal["all"], list[CompanySearchFields]] = Field(
        None,
        description="Fields to search against. Either a list of fields or `all`. Defaults to `all`.",
    )
