from typing import Any, Union

from pydantic import BaseModel


class RouterQueryResult(BaseModel):
    """
    Attributes:
        message (Union[None, str]):
        result (Union[None, Any]): Value of any type, including null
    """

    message: Union[None, str] = None
    result: Union[None, Any] = None
