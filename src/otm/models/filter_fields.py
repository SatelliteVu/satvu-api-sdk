from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class FilterFields(BaseModel):
    """
    Attributes:
        status (Union[None, list[str], str]):
        min_off_nadir (Union[None, int, list[int]]):
        max_off_nadir (Union[None, int, list[int]]):
    """

    status: Union[None, list[str], str] = Field(None, description=None, alias="status")
    min_off_nadir: Union[None, int, list[int]] = Field(
        None, description=None, alias="min_off_nadir"
    )
    max_off_nadir: Union[None, int, list[int]] = Field(
        None, description=None, alias="max_off_nadir"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
