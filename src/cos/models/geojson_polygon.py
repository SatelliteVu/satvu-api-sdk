from typing import Literal, TypedDict


class GeojsonPolygon(TypedDict):
    """
    Attributes:
        type_ (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type_: Literal["Polygon"]
    coordinates: list[list[list[float]]]
