from dataclasses import dataclass


@dataclass
class HttpExceptionResponse:
    """
    Attributes:
        detail (str):
    """

    detail: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "detail",
        }
