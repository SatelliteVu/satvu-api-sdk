# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.edit_order_properties import EditOrderProperties
    from ..models.point import Point


class EditOrderPayload(pydantic.BaseModel):
    """Modifications to an order. Omitted fields keep their current values.

    `geometry` can only change for standard orders that are still `staged`.

        Attributes:
            geometry (Union['Point', None]): The location of the order. Only editable for standard orders that are still
                `staged`.
            properties (Union['EditOrderProperties', None]): The properties to edit in the order.
    """

    geometry: Union[Point, None] = pydantic.Field(
        default=None,
        description="""The location of the order. Only editable for standard orders that are still `staged`.""",
        alias="geometry",
    )
    properties: Union[EditOrderProperties, None] = pydantic.Field(
        default=None,
        description="""The properties to edit in the order.""",
        alias="properties",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
