from pydantic import BaseModel, ConfigDict


class Filter(BaseModel):
    """Filters using Common Query Language (CQL2)."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
