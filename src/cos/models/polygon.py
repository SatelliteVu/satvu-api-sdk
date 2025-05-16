from typing import Literal, TypedDict


class Polygon(TypedDict):
    """
    Attributes:
        type_ (Literal['Polygon']):
        coordinates (list[list[list[float]]]):
    """

    type_: Literal["Polygon"]
    coordinates: list[list[list[float]]]
