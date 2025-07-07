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
