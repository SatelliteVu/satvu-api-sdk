# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from ..models.product import Product


class TaskingOrderFulfilledPayloadV3(BaseModel):
    """
    Attributes:
        order_id (str): Order ID
        contract_id (str): Contract ID with which the order is associated
        acquisition_window (list[datetime.datetime]): Requested datetime range of the order
        product ('Product'):
        item_id (str): Item ID
        acquisition_id (str): Acquisition ID
        user_id (str): Auth0 user ID of owner of order
        order_name (None | str): Order Name
        status (Literal['fulfilled']):  Default: 'fulfilled'.
    """

    order_id: str = Field(..., description="""Order ID""", alias="order_id")
    contract_id: str = Field(
        ...,
        description="""Contract ID with which the order is associated""",
        alias="contract_id",
    )
    acquisition_window: list[datetime.datetime] = Field(
        ...,
        description="""Requested datetime range of the order""",
        alias="acquisition_window",
    )
    product: Product = Field(..., description=None, alias="product")
    item_id: str = Field(..., description="""Item ID""", alias="item_id")
    acquisition_id: str = Field(
        ..., description="""Acquisition ID""", alias="acquisition_id"
    )
    user_id: str = Field(
        ..., description="""Auth0 user ID of owner of order""", alias="user_id"
    )
    order_name: None | str = Field(
        default=None, description="""Order Name""", alias="order_name"
    )
    status: Literal["fulfilled"] = Field(
        default="fulfilled", description=None, alias="status"
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
