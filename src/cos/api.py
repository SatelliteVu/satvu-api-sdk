import io
from collections.abc import Callable
from typing import Any, Union, Unpack
from uuid import UUID

from src.satvu_api_sdk.core import SDKClient
from src.shared.utils import deep_parse_from_annotation, normalize_keys

from src.cos.models.download_order_collections_type_0_item import (
    DownloadOrderCollectionsType0Item,
)
from src.cos.models.feature_collection_order import FeatureCollectionOrder
from src.cos.models.order_download_url import OrderDownloadUrl
from src.cos.models.order_edit_payload import OrderEditPayload
from src.cos.models.order_item_download_url import OrderItemDownloadUrl
from src.cos.models.order_page import OrderPage
from src.cos.models.order_submission_payload import OrderSubmissionPayload
from src.cos.models.reseller_feature_collection_order import (
    ResellerFeatureCollectionOrder,
)
from src.cos.models.reseller_submission_order_payload import (
    ResellerSubmissionOrderPayload,
)


class CosService(SDKClient):
    base_path = "/orders/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_order_details(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]:
        """
        Order details

        Retrieve order details for a specified Order ID owned by the authenticated user.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.

        Returns:
            Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()),
                Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder],
            )
        return response.json()

    def edit_order(
        self, contract_id: UUID, order_id: UUID, **kwargs: Unpack[OrderEditPayload]
    ) -> Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]:
        """
        Edit Order

        Edit the name of an order.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.
            name (Union[None, str]): Optional name of an order

        Returns:
            Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]
        """

        response = self.make_request(
            method="patch",
            url="/{contract_id}/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
            json=kwargs,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()),
                Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder],
            )
        return response.json()

    def query_orders(
        self,
        contract_id: UUID,
        limit: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> OrderPage:
        """
        Query orders

        Retrieve all existing orders owned by the authenticated user.

        Args:
            contract_id (UUID): Contract ID.
            limit (Union[None, int]): The number of orders to return per page. Default: 25.
            token (Union[None, str]): The pagination token.

        Returns:
            OrderPage
        """

        params: dict[str, Any] = {}
        json_limit: Union[None, int] = limit

        params["limit"] = json_limit

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()), OrderPage
            )
        return response.json()

    def submit_order(
        self,
        contract_id: UUID,
        **kwargs: Unpack[Union[OrderSubmissionPayload, ResellerSubmissionOrderPayload]],
    ) -> Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]:
        """
        Submit order

        Create and submit a new imagery order of one or more items (maximum 100)
        from SatVu's imagery catalog. The order will be owned by the
        authenticated user.

        Args:
            contract_id (UUID): Contract ID.
            Either (OrderSubmissionPayload):
                - item_id (Union[list[str], str]): Item ID.
            Or: (ResellerSubmissionOrderPayload):
                - item_id (Union[list[str], str]): Item ID.
                - reseller_end_user_id (UUID):

        Returns:
            Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder]
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/".format(contract_id=contract_id),
            json=kwargs,
        )

        if response.status_code == 201:
            return deep_parse_from_annotation(
                normalize_keys(response.json()),
                Union[FeatureCollectionOrder, ResellerFeatureCollectionOrder],
            )
        return response.json()

    def download_item(
        self,
        contract_id: UUID,
        order_id: UUID,
        item_id: str,
        redirect: Union[None, bool] = True,
    ) -> OrderItemDownloadUrl:
        """
        Item download

        Download an item, identified by its STAC ID, for a specified imagery order
        owned by the authenticated user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.
            item_id (str): Item ID.
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.

        Returns:
            OrderItemDownloadUrl
        """

        params: dict[str, Any] = {}
        params["redirect"] = redirect

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}/{item_id}/download".format(
                contract_id=contract_id, order_id=order_id, item_id=item_id
            ),
            params=params,
            follow_redirects=redirect,
            timeout=60 if redirect else 5,
        )

        if response.headers.get("Content-Type") == "application/zip":
            zip_bytes = io.BytesIO(response.content)
            return zip_bytes

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()), OrderItemDownloadUrl
            )
        if response.status_code == 202:
            return response.json()
        return response.json()

    def download_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        collections: Union[None, list[DownloadOrderCollectionsType0Item]] = None,
        redirect: Union[None, bool] = True,
    ) -> OrderDownloadUrl:
        """
        Order download

        Download all the items for a specified imagery order owned by the authenticated
        user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.
            collections (Union[None, list[DownloadOrderCollectionsType0Item]]): Specify a subset of
                collections to download. Defaults to None, which will download only the visual product.
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.

        Returns:
            OrderDownloadUrl
        """

        params: dict[str, Any] = {}
        json_collections: Union[None, list[str]] = collections

        if isinstance(collections, list):
            json_collections = []
            for collections_type_0_item_data in collections:
                collections_type_0_item = collections_type_0_item_data.value
                json_collections.append(collections_type_0_item)

        params["collections"] = json_collections

        params["redirect"] = redirect

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}/download".format(
                contract_id=contract_id, order_id=order_id
            ),
            params=params,
            follow_redirects=redirect,
            timeout=60 if redirect else 5,
        )

        if response.headers.get("Content-Type") == "application/zip":
            zip_bytes = io.BytesIO(response.content)
            return zip_bytes

        if response.status_code == 200:
            return deep_parse_from_annotation(
                normalize_keys(response.json()), OrderDownloadUrl
            )
        if response.status_code == 202:
            return response.json()
        return response.json()
