from typing import TYPE_CHECKING, TypedDict, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.validation_error import ValidationError


class HTTPValidationError(TypedDict):
    """
    Attributes:
        detail (Union[Unset, list['ValidationError']]):
    """

    detail: Union[Unset, list["ValidationError"]] = UNSET
