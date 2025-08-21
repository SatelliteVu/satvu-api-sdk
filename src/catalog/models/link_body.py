from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class LinkBody(BaseModel):
    """A JSON object containing fields/values that must by included in the body of the next request."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
