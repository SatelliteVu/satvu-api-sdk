from dataclasses import dataclass


@dataclass
class ListResponseContext:
    """
    Attributes:
        per_page (int): Applied per page webhook limit.
        matched (int): Total number of results.
        returned (int): Number of returned webhooks in page.
    """

    per_page: int
    matched: int
    returned: int

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "per_page",
            "matched",
            "returned",
        }
