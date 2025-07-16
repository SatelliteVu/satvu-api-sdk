from typing import Union

from pydantic import BaseModel, Field


class TermsUserTermsAccepted(BaseModel):
    """
    Attributes:
        accepted (Union[None, bool]):
        user_id (Union[None, str]):
    """

    accepted: Union[None, bool] = Field(None, description=None)
    user_id: Union[None, str] = Field(None, description=None)
