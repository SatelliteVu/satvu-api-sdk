import datetime
from typing import TYPE_CHECKING, Literal, TypedDict, Union
from uuid import UUID

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.feature_order import FeatureOrder
    from ..models.price import Price


class ResellerFeatureCollectionOrder(TypedDict):
    """
    Attributes:
        id (UUID): Order ID.
        features (list['FeatureOrder']): An array of Item objects.
        owned_by (str): The owner of the order.
        created_at (datetime.datetime): The datetime at which the order was created.
        contract_id (UUID): Contract ID.
        price (Price):
        reseller_end_user_id (UUID):
        type_ (Union[Literal['FeatureCollection'], Unset]):  Default: 'FeatureCollection'.
        updated_at (Union[None, Unset, datetime.datetime]): The datetime at which the order was updated.
    """

    id: UUID
    features: list["FeatureOrder"]
    owned_by: str
    created_at: datetime.datetime
    contract_id: UUID
    price: "Price"
    reseller_end_user_id: UUID
    type_: Union[Literal["FeatureCollection"], Unset] = "FeatureCollection"
    updated_at: Union[None, Unset, datetime.datetime] = UNSET
