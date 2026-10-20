# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class OrderEditPayload(pydantic.BaseModel):
    """Request payload for editing an order.

    Attributes:
        name (None | str): The optional name of the order
    """

    name: None | str = pydantic.Field(
        default=None, description="""The optional name of the order""", alias="name"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
