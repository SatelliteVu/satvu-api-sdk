from typing import Union

from pydantic import BaseModel


class CivilDate(BaseModel):
    """Contract end date

    Attributes:
        day (Union[None, int]):
        month (Union[None, int]):
        year (Union[None, int]):
    """

    day: Union[None, int] = None
    month: Union[None, int] = None
    year: Union[None, int] = None
