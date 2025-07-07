from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models.get_user import GetUser
    from ..models.link import Link
    from ..models.response_context import ResponseContext


@dataclass
class GetUsers:
    """Represents response to GET users request

    Attributes:
        users (list['GetUser']): All end users associated with the reseller.
        links (list['Link']): Links to previous and/or next page.
        context (ResponseContext): Contextual information for pagination responses
    """

    users: list["GetUser"]
    links: list["Link"]
    context: "ResponseContext"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "users",
            "links",
            "context",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "users": object,
            "links": object,
            "context": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
