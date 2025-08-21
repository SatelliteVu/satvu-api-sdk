from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from typing import Union


class QueryableProperty(BaseModel):
    """
    Attributes:
        format_ (Union[None, str]):
        type_ (Union[None, str]):
    """

    format_: Union[None, str] = Field(None, description=None, alias="format")
    type_: Union[None, str] = Field(None, description=None, alias="type")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
