from typing import Union

from pydantic import BaseModel


class FilterFields(BaseModel):
    """
    Attributes:
        status (Union[None, list[str], str]):
        min_off_nadir (Union[None, int, list[int]]):
        max_off_nadir (Union[None, int, list[int]]):
    """

    status: Union[None, list[str], str] = None
    min_off_nadir: Union[None, int, list[int]] = None
    max_off_nadir: Union[None, int, list[int]] = None
