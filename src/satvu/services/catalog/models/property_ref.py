# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class PropertyRef(pydantic.BaseModel):
    """
    Attributes:
        property_ (str):
    """

    property_: str = pydantic.Field(..., description=None, alias="property")

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
