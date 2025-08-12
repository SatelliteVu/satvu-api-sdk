from pydantic import BaseModel, ConfigDict, Field


class Asset(BaseModel):
    """
    Attributes:
        href (str): The URI to the asset object.
        type_ (str): The media type of the asset.
        roles (list[str]): The semantic roles of the asset.
    """

    href: str = Field(..., description="The URI to the asset object.", alias="href")
    type_: str = Field(..., description="The media type of the asset.", alias="type")
    roles: list[str] = Field(
        ..., description="The semantic roles of the asset.", alias="roles"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
