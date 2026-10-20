# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic

from ..models.direction import Direction
from ..models.sortable_field import SortableField


class SortEntities(pydantic.BaseModel):
    """
    Attributes:
        field ('SortableField'):
        direction ('Direction'): The directionality of the sort.
    """

    field: SortableField = pydantic.Field(..., description=None, alias="field")
    direction: Direction = pydantic.Field(
        ..., description="""The directionality of the sort.""", alias="direction"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
