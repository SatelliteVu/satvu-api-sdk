from pydantic import BaseModel, ConfigDict, Field


class Link(BaseModel):
    """
    Attributes:
        href (str): The link in the format of a URL.
        rel (str): The relationship between the current document and the linked document.
    """

    href: str = Field(..., description="The link in the format of a URL.", alias="href")
    rel: str = Field(
        ...,
        description="The relationship between the current document and the linked document.",
        alias="rel",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
