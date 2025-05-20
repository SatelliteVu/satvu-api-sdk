from dataclasses import dataclass


@dataclass
class Link:
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
    """

    href: str
    rel: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "href",
            "rel",
        }
