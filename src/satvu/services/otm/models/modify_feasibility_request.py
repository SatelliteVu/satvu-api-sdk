# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Literal, Union

import pydantic

if TYPE_CHECKING:
    from ..models.modify_feasibility_request_properties import (
        ModifyFeasibilityRequestProperties,
    )
    from ..models.point import Point


class ModifyFeasibilityRequest(pydantic.BaseModel):
    """Payload for modify feasibility request.
    Only supports Standard orders. Assured orders cannot be modified.
    All fields are optional - unspecified fields will be sourced from the existing order.

        Attributes:
            type_ (Literal['Feature']):
            properties (ModifyFeasibilityRequestProperties): Properties for modify feasibility request.
                All fields are optional - unspecified fields will be sourced from the existing order.
                Only supports Standard product (Assured orders do not support modifications).
            geometry (Union['Point', None]): The geometry of the modified order. If not provided, uses the existing order
                geometry.
    """

    type_: Literal["Feature"] = pydantic.Field(
        default="Feature", description=None, alias="type"
    )
    properties: ModifyFeasibilityRequestProperties = pydantic.Field(
        ...,
        description="""Properties for modify feasibility request.
All fields are optional - unspecified fields will be sourced from the existing order.
Only supports Standard product (Assured orders do not support modifications).""",
        alias="properties",
    )
    geometry: Union[Point, None] = pydantic.Field(
        default=None,
        description="""The geometry of the modified order. If not provided, uses the existing order geometry.""",
        alias="geometry",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
