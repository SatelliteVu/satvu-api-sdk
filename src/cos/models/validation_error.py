from typing import TypedDict, Union


class ValidationError(TypedDict):
    """
    Attributes:
        loc (list[Union[int, str]]):
        msg (str):
        type_ (str):
    """

    loc: list[Union[int, str]]
    msg: str
    type_: str
