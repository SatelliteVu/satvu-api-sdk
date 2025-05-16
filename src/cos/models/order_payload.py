from typing import TypedDict, Union


class OrderPayload(TypedDict):
    """
    Attributes:
        item_id (Union[list[str], str]): Item ID.
    """

    item_id: Union[list[str], str]
