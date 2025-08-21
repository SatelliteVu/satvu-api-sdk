from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class StacFeatureProperties(BaseModel):
    """A dictionary of additional metadata for the item."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
