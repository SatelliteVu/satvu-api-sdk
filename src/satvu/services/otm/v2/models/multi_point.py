# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import Any, Literal

import pydantic


class MultiPoint(pydantic.BaseModel):
    """MultiPoint Model

    Attributes:
        type_ (Literal['MultiPoint']):
        coordinates (list[list[float]]):
        bbox (list[float] | None):
    """

    type_: Literal["MultiPoint"] = pydantic.Field(
        default="MultiPoint", description=None, alias="type"
    )
    coordinates: list[list[float]] = pydantic.Field(
        ..., description=None, alias="coordinates"
    )
    bbox: list[float] | None = pydantic.Field(
        default=None, description=None, alias="bbox"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["type_"])
