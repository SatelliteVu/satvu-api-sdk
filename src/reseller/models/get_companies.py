from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.get_company import GetCompany
    from ..models.link import Link
    from ..models.response_context import ResponseContext


class GetCompanies(BaseModel):
    """Represents response to GET companies request

    Attributes:
        companies (list[GetCompany]): All end user companies associated with the reseller.
        links (list[Link]): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    companies: list[GetCompany] = Field(
        ...,
        description="All end user companies associated with the reseller.",
        alias="companies",
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
