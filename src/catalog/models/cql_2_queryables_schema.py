from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.cql_2_queryables_schema_properties import Cql2QueryablesSchemaProperties


class Cql2QueryablesSchema(BaseModel):
    """
    Attributes:
        id (str): The URL of the endpoint.
        schema (str): The schema of the response. Example: http://json-schema.org/draft-07/schema#.
        type_ (str): The type of the resource. Example: object.
        properties (Union[None, Cql2QueryablesSchemaProperties]): A list of queryable properties to use as search
            filters.
    """

    id: str = Field(..., description="The URL of the endpoint.", alias="$id")
    schema: str = Field(..., description="The schema of the response.", alias="$schema")
    type_: str = Field(..., description="The type of the resource.", alias="type")
    properties: Union[None, "Cql2QueryablesSchemaProperties"] = Field(
        None,
        description="A list of queryable properties to use as search filters.",
        alias="properties",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
