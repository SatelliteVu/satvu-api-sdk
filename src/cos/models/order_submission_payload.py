from typing import Union

from pydantic import BaseModel


class OrderSubmissionPayload(BaseModel):
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
        name (Union[None, str]): Optional name of an order
    """

    item_id: Union[list[str], str]
    name: Union[None, str] = None
