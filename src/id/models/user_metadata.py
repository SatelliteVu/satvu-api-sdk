from typing import TYPE_CHECKING, TypedDict, Union

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.verbose_notification import VerboseNotification


class UserMetadata(TypedDict):
    """
    Attributes:
        client_id (Union[None, Unset, str]): The client ID of the user
        notifications (Union[None, Unset, list['VerboseNotification']]): The notifications configured for the user.
    """

    client_id: Union[None, Unset, str] = UNSET
    notifications: Union[None, Unset, list["VerboseNotification"]] = UNSET
