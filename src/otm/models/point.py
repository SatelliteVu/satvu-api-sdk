from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class Point(BaseModel):
    """Point Model

    Attributes:
        type_ (Literal['Point']):
        coordinates (list[float]):
        bbox (Union[None, list[float]]):
    """

    type_: Literal["Point"] = Field("Point", description=None, alias="type")
    coordinates: list[float] = Field(..., description=None, alias="coordinates")
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
