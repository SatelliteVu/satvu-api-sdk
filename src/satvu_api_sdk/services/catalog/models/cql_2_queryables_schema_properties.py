from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    pass


class Cql2QueryablesSchemaProperties(BaseModel):
    """A map of queryable properties to use as search filters."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
