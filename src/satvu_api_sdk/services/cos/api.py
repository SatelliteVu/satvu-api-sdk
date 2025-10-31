import io
from collections.abc import Callable
from typing import Any, Union
from uuid import UUID

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.services.cos.models.download_order_collections_type_0_item import (
    DownloadOrderCollectionsType0Item,
)
from satvu_api_sdk.services.cos.models.feature_collection_order import (
    FeatureCollectionOrder,
)
from satvu_api_sdk.services.cos.models.order_download_url import OrderDownloadUrl
from satvu_api_sdk.services.cos.models.order_edit_payload import OrderEditPayload
from satvu_api_sdk.services.cos.models.order_item_download_url import (
    OrderItemDownloadUrl,
)
from satvu_api_sdk.services.cos.models.order_page import OrderPage
from satvu_api_sdk.services.cos.models.order_submission_payload import (
    OrderSubmissionPayload,
)
from satvu_api_sdk.services.cos.models.reseller_feature_collection_order import (
    ResellerFeatureCollectionOrder,
)
from satvu_api_sdk.services.cos.models.reseller_submission_order_payload import (
    ResellerSubmissionOrderPayload,
)
from satvu_api_sdk.shared.parsing import parse_response


class CosService(SDKClient):
    base_path = "/orders/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_order_details(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Order details

        Retrieve order details for a specified Order ID owned by the authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            return parse_response(
                response.json(), FeatureCollectionOrder | ResellerFeatureCollectionOrder
            )
        return response.json()

    def edit_order(
        self, contract_id: UUID, order_id: UUID, body: OrderEditPayload
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Edit Order

        Edit the name of an order owned by the authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.
            body (OrderEditPayload): Request payload for editing an order.

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="patch",
            url="/{contract_id}/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
            json=json_body,
        )

        if response.status_code == 200:
            return parse_response(
                response.json(), FeatureCollectionOrder | ResellerFeatureCollectionOrder
            )
        return response.json()

    def query_orders(
        self,
        contract_id: UUID,
        limit: int | None = 25,
        token: None | str = None,
    ) -> OrderPage:
        """
        Query orders

        Retrieve all existing orders owned by the authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            limit (int | None): The number of orders to return per page. Default: 25.
            token (None | str): The pagination token.

        Returns:
            OrderPage
        """

        params = {
            "limit": limit,
            "token": token,
        }

        response = self.make_request(
            method="get",
            url="/{contract_id}/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return parse_response(response.json(), OrderPage)
        return response.json()

    def submit_order(
        self,
        contract_id: UUID,
        body: Union["OrderSubmissionPayload", "ResellerSubmissionOrderPayload"],
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Submit order

        Create and submit a new imagery order of one or more items (maximum 100)
        from SatVu's imagery catalog. The order will be owned by the
        authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            body (Union['OrderSubmissionPayload', 'ResellerSubmissionOrderPayload']):
                One of:
                - OrderSubmissionPayload: Request payload for submitting an order.
                - ResellerSubmissionOrderPayload: Order payload for resellers

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 201:
            return parse_response(
                response.json(), FeatureCollectionOrder | ResellerFeatureCollectionOrder
            )
        return response.json()

    def download_item(
        self,
        contract_id: UUID,
        order_id: UUID,
        item_id: str,
        redirect: Union[None, bool] = True,
    ) -> Union[OrderItemDownloadUrl, Any, io.BytesIO]:
        """
        Item download

        Download an item, identified by its STAC ID, for a specified imagery order
        owned by the authenticated user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.
            item_id (str): The item ID.
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.

        Returns:
            Union[OrderItemDownloadUrl, Any, io.BytesIO]
        """

        params = {
            "redirect": redirect,
        }

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
            return parse_response(response.json(), OrderItemDownloadUrl)
        if response.status_code == 202:
            return response.json()
        return response.json()

    def download_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        collections: list["DownloadOrderCollectionsType0Item"] | None = None,
        redirect: Union[None, bool] = True,
    ) -> Union[OrderDownloadUrl, Any, io.BytesIO]:
        """
        Order download

        Download all the items for a specified imagery order owned by the authenticated
        user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.
            collections (list['DownloadOrderCollectionsType0Item'] | None): Specify a subset of
                collections to download.
                            Defaults to None, which will download only the ordered product.
                            To specify multiple collections, repeat the query parameter.

            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.

        Returns:
            Union[OrderDownloadUrl, Any, io.BytesIO]
        """

        params = {
            "collections": collections,
            "redirect": redirect,
        }

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
            return parse_response(response.json(), OrderDownloadUrl)
        if response.status_code == 202:
            return response.json()
        return response.json()
