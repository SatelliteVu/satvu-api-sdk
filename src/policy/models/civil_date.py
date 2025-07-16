from typing import Union

from pydantic import BaseModel, Field


class CivilDate(BaseModel):
    """Contract end date

    Attributes:
        day (Union[None, int]):
        month (Union[None, int]):
        year (Union[None, int]):
    """

    day: Union[None, int] = Field(None, description=None)
    month: Union[None, int] = Field(None, description=None)
    year: Union[None, int] = Field(None, description=None)
