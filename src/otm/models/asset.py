from pydantic import BaseModel


class Asset(BaseModel):
    """
    Attributes:
        href (str): The URI to the asset object.
        type (str): The media type of the asset.
        roles (list[str]): The semantic roles of the asset.
    """

    href: str
    type: str
    roles: list[str]

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "href",
            "type",
            "roles",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "href": str,
            "type": str,
            "roles": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
