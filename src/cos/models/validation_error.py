from dataclasses import dataclass
from typing import Union


@dataclass
class ValidationError:
    """
    Attributes:
        loc (list[Union[int, str]]):
        msg (str):
        type (str):
    """

    loc: list[Union[int, str]]
    msg: str
    type: str

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "loc",
            "msg",
            "type",
        }
