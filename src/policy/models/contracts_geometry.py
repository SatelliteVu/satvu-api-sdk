from typing import Any, Union

from pydantic import BaseModel


class ContractsGeometry(BaseModel):
    """Allowed geographical area of the contract

    Attributes:
        coordinates (Union[None, Any]): Value of any type, including null
        type (Union[None, str]):
    """

    coordinates: Union[None, Any] = None
    type: Union[None, str] = None
