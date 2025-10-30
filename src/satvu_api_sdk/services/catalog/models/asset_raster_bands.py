from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.asset_raster_bands_data_type_of_the_band import (
    AssetRasterBandsDataTypeOfTheBand,
)
from ..models.asset_raster_bands_nodata_type_1 import AssetRasterBandsNodataType1
from ..models.asset_raster_bands_pixel_sampling_in_the_band import (
    AssetRasterBandsPixelSamplingInTheBand,
)

if TYPE_CHECKING:
    from ..models.asset_raster_bands_statistics import AssetRasterBandsStatistics


class AssetRasterBands(BaseModel):
    """
    Attributes:
        bits_per_sample (Union[None, int]): The actual number of bits used for this band
        data_type (Union[None, 'AssetRasterBandsDataTypeOfTheBand']): Data type of the band
        nodata (Union['AssetRasterBandsNodataType1', float]): No data pixel value
        offset (Union[None, float]): Number to be added to the pixel value to transform into the value
        sampling (Union[None, 'AssetRasterBandsPixelSamplingInTheBand']): Pixel sampling in the band
        scale (Union[None, float]): Multiplicator factor of the pixel value to transform into the value
        statistics (Union[None, AssetRasterBandsStatistics]): Statistics
        unit (Union[None, str]): Unit denomination of the pixel value
    """

    bits_per_sample: Union[None, int] = Field(
        None,
        description="The actual number of bits used for this band",
        alias="bits_per_sample",
    )
    data_type: Union[None, "AssetRasterBandsDataTypeOfTheBand"] = Field(
        None, description="Data type of the band", alias="data_type"
    )
    nodata: Union["AssetRasterBandsNodataType1", float] = Field(
        None, description="No data pixel value", alias="nodata"
    )
    offset: Union[None, float] = Field(
        None,
        description="Number to be added to the pixel value to transform into the value",
        alias="offset",
    )
    sampling: Union[None, "AssetRasterBandsPixelSamplingInTheBand"] = Field(
        None, description="Pixel sampling in the band", alias="sampling"
    )
    scale: Union[None, float] = Field(
        None,
        description="Multiplicator factor of the pixel value to transform into the value",
        alias="scale",
    )
    statistics: Union[None, "AssetRasterBandsStatistics"] = Field(
        None, description="Statistics", alias="statistics"
    )
    unit: Union[None, str] = Field(
        None, description="Unit denomination of the pixel value", alias="unit"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
