from pydantic import BaseModel


class Link(BaseModel):
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

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "href": str,
            "rel": str,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
