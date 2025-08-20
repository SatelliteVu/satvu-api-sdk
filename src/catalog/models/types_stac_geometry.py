from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class TypesStacGeometry(BaseModel):
    """Searches items by performing intersection between their geometry and provided GeoJSON geometry.

    Attributes:
        bbox (Union[None, list[int]]): Bounding box.
        coordinates (Union[None, list[int]]): The coordinates of the Geometry object.
        geometries (Union[None, list[int]]):
        type_ (Union[None, str]): The type of geometry represented.
    """

    bbox: Union[None, list[int]] = Field(
        None, description="Bounding box.", alias="bbox"
    )
    coordinates: Union[None, list[int]] = Field(
        None, description="The coordinates of the Geometry object.", alias="coordinates"
    )
    geometries: Union[None, list[int]] = Field(
        None, description=None, alias="geometries"
    )
    type_: Union[None, str] = Field(
        None, description="The type of geometry represented.", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
