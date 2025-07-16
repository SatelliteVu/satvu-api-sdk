from pydantic import BaseModel, Field

from ..models.get_company import GetCompany
from ..models.link import Link
from ..models.response_context import ResponseContext


class GetCompanies(BaseModel):
    """Represents response to GET companies request

    Attributes:
        companies (list['GetCompany']): All end user companies associated with the reseller.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    companies: list["GetCompany"] = Field(
        ..., description="All end user companies associated with the reseller."
    )
    links: list["Link"] = Field(..., description="Links to previous and/or next page.")
    context: "ResponseContext" = Field(
        ..., description="Contextual information for pagination responses"
    )
