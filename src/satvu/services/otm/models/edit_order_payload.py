# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.edit_order_properties import EditOrderProperties
    from ..models.point import Point


class EditOrderPayload(BaseModel):
    """Payload for editing an order.

    Geometry can be edited for Standard orders in Created/Staged states.
    All property fields are optional - only provided fields will be updated.

        Attributes:
            geometry (Union['Point', None]): The location of the order. Only editable for Standard orders in Created/Staged
                states.
            properties (Union['EditOrderProperties', None]): The properties to edit in the order.
    """

    geometry: Union[Point, None] = Field(
        default=None,
        description="""The location of the order. Only editable for Standard orders in Created/Staged states.""",
        alias="geometry",
    )
    properties: Union[EditOrderProperties, None] = Field(
        default=None,
        description="""The properties to edit in the order.""",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
