# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.series_price import SeriesPrice


class SeriesPriceResponse(pydantic.BaseModel):
    """Price estimate for a series before creation.

    Attributes:
        price (SeriesPrice): Price breakdown for a series, calculated at creation time.
    """

    price: SeriesPrice = pydantic.Field(
        ...,
        description="""Price breakdown for a series, calculated at creation time.""",
        alias="price",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
