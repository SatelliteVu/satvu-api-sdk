from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class StacPropertiesV8ProcessingSoftwareNameVersion(BaseModel):
    """ """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
