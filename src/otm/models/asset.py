from pydantic import BaseModel, Field


class Asset(BaseModel):
    """
    Attributes:
        href (str): The URI to the asset object.
        type (str): The media type of the asset.
        roles (list[str]): The semantic roles of the asset.
    """

    href: str = Field(..., description="The URI to the asset object.")
    type: str = Field(..., description="The media type of the asset.")
    roles: list[str] = Field(..., description="The semantic roles of the asset.")
