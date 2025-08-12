from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Polygon(BaseModel):
    """
    Attributes:
        type_ (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type_: Literal["Polygon"] = Field("Polygon", description=None, alias="type")
    coordinates: list[list[list[float]]] = Field(
        ..., description=None, alias="coordinates"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
