from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class AssetBandsStatistics(BaseModel):
    """Statistics

    Attributes:
        maximum (Union[None, float]): Maximum value of all the pixels in the band
        mean (Union[None, float]): Mean value of all the pixels in the band
        minimum (Union[None, float]): Minimum value of all the pixels in the band
        stddev (Union[None, float]): Standard deviation value of all the pixels in the band
        valid_percent (Union[None, float]): Percentage of valid (not nodata) pixel
    """

    maximum: Union[None, float] = Field(
        None, description="Maximum value of all the pixels in the band", alias="maximum"
    )
    mean: Union[None, float] = Field(
        None, description="Mean value of all the pixels in the band", alias="mean"
    )
    minimum: Union[None, float] = Field(
        None, description="Minimum value of all the pixels in the band", alias="minimum"
    )
    stddev: Union[None, float] = Field(
        None,
        description="Standard deviation value of all the pixels in the band",
        alias="stddev",
    )
    valid_percent: Union[None, float] = Field(
        None,
        description="Percentage of valid (not nodata) pixel",
        alias="valid_percent",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
