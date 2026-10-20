# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Literal

import pydantic

from ..models.product import Product


class TaskingOrderFulfilledPayloadV2(pydantic.BaseModel):
    """
    Attributes:
        order_id (str): Order ID
        contract_id (str): Contract ID with which the order is associated
        acquisition_window (list[datetime.datetime]): Requested datetime range of the order
        product ('Product'):
        item_id (str): Item ID
        user_id (str): Auth0 user ID of owner of order
        order_name (None | str): Order Name
        status (Literal['fulfilled']):  Default: 'fulfilled'.
    """

    order_id: str = pydantic.Field(..., description="""Order ID""", alias="order_id")
    contract_id: str = pydantic.Field(
        ...,
        description="""Contract ID with which the order is associated""",
        alias="contract_id",
    )
    acquisition_window: list[datetime.datetime] = pydantic.Field(
        ...,
        description="""Requested datetime range of the order""",
        alias="acquisition_window",
    )
    product: Product = pydantic.Field(..., description=None, alias="product")
    item_id: str = pydantic.Field(..., description="""Item ID""", alias="item_id")
    user_id: str = pydantic.Field(
        ..., description="""Auth0 user ID of owner of order""", alias="user_id"
    )
    order_name: None | str = pydantic.Field(
        default=None, description="""Order Name""", alias="order_name"
    )
    status: Literal["fulfilled"] = pydantic.Field(
        default="fulfilled", description=None, alias="status"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
