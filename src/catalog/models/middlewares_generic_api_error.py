from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.error import Error


class MiddlewaresGenericApiError(BaseModel):
    """
    Attributes:
        errors (Union[None, list[Error]]):
    """

    errors: Union[None, list[Error]] = Field(None, description=None, alias="Errors")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
