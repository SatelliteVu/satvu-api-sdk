from pydantic import BaseModel, ConfigDict


class Cql2QueryablesSchemaProperties(BaseModel):
    """A list of queryable properties to use as search filters."""

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
