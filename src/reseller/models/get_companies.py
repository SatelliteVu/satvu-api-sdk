from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.get_company import GetCompany
    from ..models.link import Link
    from ..models.response_context import ResponseContext


@dataclass
class GetCompanies:
    """Represents response to GET companies request

    Attributes:
        companies (list['GetCompany']): All end user companies associated with the reseller.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    companies: list["GetCompany"]
    links: list["Link"]
    context: "ResponseContext"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "companies",
            "links",
            "context",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "companies": object,
            "links": object,
            "context": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
