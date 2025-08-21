from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    pass


class TypesTemporalExtent(BaseModel):
    """Potential temporal extents covered by the Collection.

    Attributes:
        interval (list[Any]): Potential temporal extents covered by the Collection.
    """

    interval: list[Any] = Field(
        ...,
        description="Potential temporal extents covered by the Collection.",
        alias="interval",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
