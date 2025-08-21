from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class StacMetadataAssets(BaseModel):
    """A dictionary of asset objects that can be downloaded, each with a unique key."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
