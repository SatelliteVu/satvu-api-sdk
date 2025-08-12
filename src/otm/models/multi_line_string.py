from typing import Literal, Union

from pydantic import BaseModel, ConfigDict, Field


class MultiLineString(BaseModel):
    """MultiLineString Model

    Attributes:
        type_ (Literal['MultiLineString']):
        coordinates (list[list[list[float]]]):
        bbox (Union[None, list[float]]):
    """

    type_: Literal["MultiLineString"] = Field(
        "MultiLineString", description=None, alias="type"
    )
    coordinates: list[list[list[float]]] = Field(
        ..., description=None, alias="coordinates"
    )
    bbox: Union[None, list[float]] = Field(None, description=None, alias="bbox")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
