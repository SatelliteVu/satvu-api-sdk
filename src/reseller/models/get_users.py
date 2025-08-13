from pydantic import BaseModel, ConfigDict, Field

from ..models.get_user import GetUser
from ..models.link import Link
from ..models.response_context import ResponseContext


class GetUsers(BaseModel):
    """Represents response to GET users request

    Attributes:
        users (list[GetUser]): All end users associated with the reseller.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    users: list[GetUser] = Field(
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
