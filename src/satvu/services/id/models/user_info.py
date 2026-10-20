# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

import pydantic

if TYPE_CHECKING:
    from ..models.user_metadata import UserMetadata


class UserInfo(pydantic.BaseModel):
    """
    Attributes:
        user_id (str): The ID of the user.
        name (str): The name of the user.
        email (str): The email of the user.
        user_metadata (Union[None, UserMetadata]):
        last_login (None | str): The datetime at which the user last logged in.
    """

    user_id: str = pydantic.Field(
        ..., description="""The ID of the user.""", alias="user_id"
    )
    name: str = pydantic.Field(
        ..., description="""The name of the user.""", alias="name"
    )
    email: str = pydantic.Field(
        ..., description="""The email of the user.""", alias="email"
    )
    user_metadata: Union[None, UserMetadata] = pydantic.Field(
        default=None, description=None, alias="user_metadata"
    )
    last_login: None | str = pydantic.Field(
        default=None,
        description="""The datetime at which the user last logged in.""",
        alias="last_login",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
