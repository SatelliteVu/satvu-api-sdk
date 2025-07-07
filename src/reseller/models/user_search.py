from typing import Literal, Union

from pydantic import BaseModel

from ..models.match_type import MatchType
from ..models.user_search_fields import UserSearchFields


class UserSearch(BaseModel):
    """
    Attributes:
        string (str): Search string.
        type (Union[None, MatchType]):
        fields (Union[Literal['all'], list[UserSearchFields]]): Fields to search against. Either a list of fields or
            `all`. Defaults to `all`.
    """

    string: str
    type: Union[None, MatchType] = None
    fields: Union[Literal["all"], list[UserSearchFields]] = None
