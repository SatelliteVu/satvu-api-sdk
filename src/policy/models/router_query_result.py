from typing import Any, Union

from pydantic import BaseModel, Field


class RouterQueryResult(BaseModel):
    """
    Attributes:
        message (Union[None, str]):
        result (Union[None, Any]): Value of any type, including null
    """

    message: Union[None, str] = Field(None, description=None)
    result: Union[None, Any] = Field(
        None, description="Value of any type, including null"
    )
