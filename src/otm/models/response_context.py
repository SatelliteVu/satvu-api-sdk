from dataclasses import dataclass


@dataclass
class ResponseContext:
    """
    Attributes:
        limit (int): Applied per page item limit.
        matched (int): Total number of results.
        returned (int): Number of returned items in page.
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
