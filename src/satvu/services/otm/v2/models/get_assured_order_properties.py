# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Any, Literal, Union

import pydantic

from ..models.day_night_mode import DayNightMode
from ..models.order_status import OrderStatus

if TYPE_CHECKING:
    from ..models.status_history_entry import StatusHistoryEntry


class GetAssuredOrderProperties(pydantic.BaseModel):
    """Feature properties model for get assured order request

    Attributes:
        product (Literal['assured']): The tasking product. Always `assured` (Assured tasking).
        datetime_ (str): The tasking window: the interval within which the order may be acquired, as an ISO 8601
            interval (`start/end`). Both bounds are required.
        signature (str): The signature token from an assured feasibility response.
        status ('OrderStatus'):
        created_at (datetime.datetime): When the order was created.
        updated_at (datetime.datetime): When the order was last updated.
        stac_item_id (None | str): The ID of the STAC item that fulfilled the order. Omitted until the order is
            fulfilled.
        stac_datetime (datetime.datetime | None): When the imagery that fulfilled the order was acquired. Omitted until
            the order is fulfilled.
        stac_metadata (dict | None): The metadata of the STAC item that fulfilled the order, including presigned URLs
            for its high-resolution assets. Omitted until the order is fulfilled, or when it has no high-resolution assets.
        satvu_day_night_mode (Union[None, 'DayNightMode']):
        max_cloud_cover (Union[None, int]): The maximum acceptable cloud cover. Measured in percent. Default: 25.
        min_off_nadir (Union[None, int]): The minimum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Default: 0.
        max_off_nadir (Union[None, int]): The maximum angle from the sensor between nadir and the scene center. Measured
            in decimal degrees. Must be greater than `min_off_nadir`. Default: 30.
        licence_level (None | str): The licence level for the order. Licence levels are specific to the contract.
            Defaults to the contract's licence level with the smallest uplift.
        addon_withhold (None | str): How long the order's imagery is withheld from the public catalog, as an ISO 8601
            duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.
        name (None | str): The name of the order.
        status_history (Union[None, list[StatusHistoryEntry]]): Chronological history of status changes for this order,
            newest first.
    """

    product: Literal["assured"] = pydantic.Field(
        default="assured",
        description="""The tasking product. Always `assured` (Assured tasking).""",
        alias="product",
    )
    datetime_: str = pydantic.Field(
        ...,
        description="""The tasking window: the interval within which the order may be acquired, as an ISO 8601 interval (`start/end`). Both bounds are required.""",
        alias="datetime",
    )
    signature: str = pydantic.Field(
        ...,
        description="""The signature token from an assured feasibility response.""",
        alias="signature",
    )
    status: OrderStatus = pydantic.Field(..., description=None, alias="status")
    created_at: datetime.datetime = pydantic.Field(
        ..., description="""When the order was created.""", alias="created_at"
    )
    updated_at: datetime.datetime = pydantic.Field(
        ..., description="""When the order was last updated.""", alias="updated_at"
    )
    stac_item_id: None | str = pydantic.Field(
        default=None,
        description="""The ID of the STAC item that fulfilled the order. Omitted until the order is fulfilled.""",
        alias="stac:item_id",
    )
    stac_datetime: datetime.datetime | None = pydantic.Field(
        default=None,
        description="""When the imagery that fulfilled the order was acquired. Omitted until the order is fulfilled.""",
        alias="stac:datetime",
    )
    stac_metadata: dict | None = pydantic.Field(
        default=None,
        description="""The metadata of the STAC item that fulfilled the order, including presigned URLs for its high-resolution assets. Omitted until the order is fulfilled, or when it has no high-resolution assets.""",
        alias="stac:metadata",
    )
    satvu_day_night_mode: Union[None, DayNightMode] = pydantic.Field(
        default=None, description=None, alias="satvu:day_night_mode"
    )
    max_cloud_cover: Union[None, int] = pydantic.Field(
        default=25,
        description="""The maximum acceptable cloud cover. Measured in percent.""",
        alias="max_cloud_cover",
    )
    min_off_nadir: Union[None, int] = pydantic.Field(
        default=0,
        description="""The minimum angle from the sensor between nadir and the scene center. Measured in decimal degrees.""",
        alias="min_off_nadir",
    )
    max_off_nadir: Union[None, int] = pydantic.Field(
        default=30,
        description="""The maximum angle from the sensor between nadir and the scene center. Measured in decimal degrees. Must be greater than `min_off_nadir`.""",
        alias="max_off_nadir",
    )
    licence_level: None | str = pydantic.Field(
        default=None,
        description="""The licence level for the order. Licence levels are specific to the contract. Defaults to the contract's licence level with the smallest uplift.""",
        alias="licence_level",
    )
    addon_withhold: None | str = pydantic.Field(
        default=None,
        description="""How long the order's imagery is withheld from the public catalog, as an ISO 8601 duration. Withhold options are specific to the contract. Defaults to the contract's default withhold option.""",
        alias="addon:withhold",
    )
    name: None | str = pydantic.Field(
        default=None, description="""The name of the order.""", alias="name"
    )
    status_history: Union[None, list[StatusHistoryEntry]] = pydantic.Field(
        default=None,
        description="""Chronological history of status changes for this order, newest first.""",
        alias="status_history",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )

    def model_post_init(self, context: Any, /) -> None:
        # Required fields the SDK fills in (constants, spec defaults) must survive
        # model_dump(exclude_unset=True)
        self.__pydantic_fields_set__ = self.model_fields_set.union(["product"])
