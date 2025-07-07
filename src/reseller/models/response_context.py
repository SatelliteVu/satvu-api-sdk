from dataclasses import dataclass


@dataclass
class ResponseContext:
    """Contextual information for pagination responses

    Attributes:
        limit (int): Applied per page results limit.
        matched (int): Total number of results.
        returned (int): Number of returned users in page.
    """

    limit: int
    matched: int
    returned: int

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "limit",
            "matched",
            "returned",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "limit": int,
            "matched": int,
            "returned": int,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
