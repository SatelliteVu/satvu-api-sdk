# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.asset_bands_nodata_type_1 import AssetBandsNodataType1
from ..models.data_type_of_the_band import DataTypeOfTheBand
from ..models.pixel_sampling_in_the_band import PixelSamplingInTheBand

if TYPE_CHECKING:
    from ..models.asset_bands_statistics import AssetBandsStatistics


class AssetBands(BaseModel):
    """Bands

    Attributes:
        bits_per_sample (Union[None, int]): The actual number of bits used for this band
        data_type (Union[None, 'DataTypeOfTheBand']): Data type of the band
        nodata (Union[None, Union['AssetBandsNodataType1', float]]): No data pixel value
        offset (Union[None, float]): Number to be added to the pixel value to transform into the value
        sampling (Union[None, 'PixelSamplingInTheBand']): Pixel sampling in the band
        scale (Union[None, float]): Multiplicator factor of the pixel value to transform into the value
        statistics (Union[None, AssetBandsStatistics]): Statistics
        unit (Union[None, str]): Unit denomination of the pixel value
    """

    bits_per_sample: Union[None, int] = Field(
        default=None,
        description="""The actual number of bits used for this band""",
        alias="bits_per_sample",
    )
    data_type: Union[None, DataTypeOfTheBand] = Field(
        default=None, description="""Data type of the band""", alias="data_type"
    )
    nodata: Union[None, Union[AssetBandsNodataType1, float]] = Field(
        default=None, description="""No data pixel value""", alias="nodata"
    )
    offset: Union[None, float] = Field(
        default=None,
        description="""Number to be added to the pixel value to transform into the value""",
        alias="offset",
    )
    sampling: Union[None, PixelSamplingInTheBand] = Field(
        default=None, description="""Pixel sampling in the band""", alias="sampling"
    )
    scale: Union[None, float] = Field(
        default=None,
        description="""Multiplicator factor of the pixel value to transform into the value""",
        alias="scale",
    )
    statistics: Union[None, AssetBandsStatistics] = Field(
        default=None, description="""Statistics""", alias="statistics"
    )
    unit: Union[None, str] = Field(
        default=None,
        description="""Unit denomination of the pixel value""",
        alias="unit",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
