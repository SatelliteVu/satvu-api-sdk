from __future__ import annotations

from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class QueryableProperty(BaseModel):
    """
    Attributes:
        format_ (Union[None, str]): The format of the property.
        type_ (Union[None, str]): The type of the property.
    """

    format_: Union[None, str] = Field(
        None, description="The format of the property.", alias="format"
    )
    type_: Union[None, str] = Field(
        None, description="The type of the property.", alias="type"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
