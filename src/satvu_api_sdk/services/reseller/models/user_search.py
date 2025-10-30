from __future__ import annotations

from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.match_type import MatchType
from ..models.user_search_fields import UserSearchFields


class UserSearch(BaseModel):
    """
    Attributes:
        string (str): Search string.
        type_ (Union[None, 'MatchType']):
        fields (Union[Literal['all'], list['UserSearchFields']]): Fields to search against. Either a list of fields or
            `all`. Defaults to `all`.
    """

    string: str = Field(..., description="Search string.", alias="string")
    type_: Union[None, "MatchType"] = Field(None, description=None, alias="type")
    fields: Union[Literal["all"], list["UserSearchFields"]] = Field(
        None,
        description="Fields to search against. Either a list of fields or `all`. Defaults to `all`.",
        alias="fields",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
