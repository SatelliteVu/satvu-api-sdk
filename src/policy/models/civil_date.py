from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class CivilDate(BaseModel):
    """Contract end date

    Attributes:
        day (Union[None, int]):
        month (Union[None, int]):
        year (Union[None, int]):
    """

    day: Union[None, int] = Field(None, description=None, alias="Day")
    month: Union[None, int] = Field(None, description=None, alias="Month")
    year: Union[None, int] = Field(None, description=None, alias="Year")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
