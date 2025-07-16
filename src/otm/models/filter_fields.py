from typing import Union

from pydantic import BaseModel, Field


class FilterFields(BaseModel):
    """
    Attributes:
        status (Union[None, list[str], str]):
        min_off_nadir (Union[None, int, list[int]]):
        max_off_nadir (Union[None, int, list[int]]):
    """

    status: Union[None, list[str], str] = Field(None, description=None)
    min_off_nadir: Union[None, int, list[int]] = Field(None, description=None)
    max_off_nadir: Union[None, int, list[int]] = Field(None, description=None)
