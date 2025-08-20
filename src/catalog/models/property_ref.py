from pydantic import BaseModel, ConfigDict, Field


class PropertyRef(BaseModel):
    """
    Attributes:
        property_ (str):
    """

    property_: str = Field(..., description=None, alias="property")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
