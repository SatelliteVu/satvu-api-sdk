# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.get_user import GetUser
    from ..models.link import Link
    from ..models.response_context import ResponseContext


class GetUsers(pydantic.BaseModel):
    """Represents response to GET users request

    Attributes:
        users (list[GetUser]): All end users associated with the reseller.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    users: list[GetUser] = pydantic.Field(
        ...,
        description="""All end users associated with the reseller.""",
        alias="users",
    )
    links: list[Link] = pydantic.Field(
        ..., description="""Links to previous and/or next page.""", alias="links"
    )
    context: ResponseContext = pydantic.Field(
        ...,
        description="""Contextual information for pagination responses""",
        alias="context",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
