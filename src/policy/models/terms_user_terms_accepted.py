from typing import Union

from pydantic import BaseModel, ConfigDict, Field


class TermsUserTermsAccepted(BaseModel):
    """
    Attributes:
        accepted (Union[None, bool]):
        user_id (Union[None, str]):
    """

    accepted: Union[None, bool] = Field(None, description=None, alias="accepted")
    user_id: Union[None, str] = Field(None, description=None, alias="user_id")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
