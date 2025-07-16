from typing import Any, Union

from pydantic import BaseModel, Field


class ContractsGeometry(BaseModel):
    """Allowed geographical area of the contract

    Attributes:
        coordinates (Union[None, Any]): Value of any type, including null
        type (Union[None, str]):
    """

    coordinates: Union[None, Any] = Field(
        None, description="Value of any type, including null"
    )
    type: Union[None, str] = Field(None, description=None)
