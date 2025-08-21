from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    pass


class StacFeatureAssets(BaseModel):
    """A dictionary of asset objects that can be downloaded, each with a unique key."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
