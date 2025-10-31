from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.get_user_1 import GetUser1
    from ..models.link import Link
    from ..models.response_context import ResponseContext


class GetUsers(BaseModel):
    """Represents response to GET users request

    Attributes:
        users (list[GetUser1]): All end users associated with the reseller.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    users: list[GetUser1] = Field(
        ..., description="All end users associated with the reseller.", alias="users"
    )
    links: list[Link] = Field(
        ..., description="Links to previous and/or next page.", alias="links"
    )
    context: "ResponseContext" = Field(
        ...,
        description="Contextual information for pagination responses",
        alias="context",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
