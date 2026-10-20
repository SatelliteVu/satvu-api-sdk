# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Union

import pydantic


class AssetBandsStatistics(pydantic.BaseModel):
    """Statistics

    Attributes:
        maximum (Union[None, float]): Maximum value of all the pixels in the band
        mean (Union[None, float]): Mean value of all the pixels in the band
        minimum (Union[None, float]): Minimum value of all the pixels in the band
        stddev (Union[None, float]): Standard deviation value of all the pixels in the band
        valid_percent (Union[None, float]): Percentage of valid (not nodata) pixel
    """

    maximum: Union[None, float] = pydantic.Field(
        default=None,
        description="""Maximum value of all the pixels in the band""",
        alias="maximum",
    )
    mean: Union[None, float] = pydantic.Field(
        default=None,
        description="""Mean value of all the pixels in the band""",
        alias="mean",
    )
    minimum: Union[None, float] = pydantic.Field(
        default=None,
        description="""Minimum value of all the pixels in the band""",
        alias="minimum",
    )
    stddev: Union[None, float] = pydantic.Field(
        default=None,
        description="""Standard deviation value of all the pixels in the band""",
        alias="stddev",
    )
    valid_percent: Union[None, float] = pydantic.Field(
        default=None,
        description="""Percentage of valid (not nodata) pixel""",
        alias="valid_percent",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
