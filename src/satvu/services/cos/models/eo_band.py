# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class EoBand(BaseModel):
    """
    Attributes:
        name (str): Band name
        center_wavelength (float): Centre wavelength in micrometres
        full_width_half_max (float): Full width at half maximum in micrometres
    """

    name: str = Field(..., description="""Band name""", alias="name")
    center_wavelength: float = Field(
        ...,
        description="""Centre wavelength in micrometres""",
        alias="center_wavelength",
    )
    full_width_half_max: float = Field(
        ...,
        description="""Full width at half maximum in micrometres""",
        alias="full_width_half_max",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
