from typing import Union

from pydantic import BaseModel


class TermsUserTermsAccepted(BaseModel):
    """
    Attributes:
        accepted (Union[None, bool]):
        user_id (Union[None, str]):
    """

    accepted: Union[None, bool] = None
    user_id: Union[None, str] = None
