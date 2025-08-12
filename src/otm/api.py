import io
from collections.abc import Callable
from typing import Any, Union
from uuid import UUID

from satvu_api_sdk.core import SDKClient
from shared.utils import deep_parse_from_annotation

from otm.models.assured_order_request import AssuredOrderRequest
from otm.models.edit_order_payload import EditOrderPayload
from otm.models.feasibility_request import FeasibilityRequest
from otm.models.feasibility_response import FeasibilityResponse
from otm.models.get_order import GetOrder
from otm.models.order_item_download_url import OrderItemDownloadUrl
from otm.models.order_price import OrderPrice
from otm.models.price_request import PriceRequest
from otm.models.reseller_assured_order_request import ResellerAssuredOrderRequest
from otm.models.reseller_get_order import ResellerGetOrder
from otm.models.reseller_standard_order_request import ResellerStandardOrderRequest
from otm.models.reseller_stored_order_request import ResellerStoredOrderRequest
from otm.models.search_request import SearchRequest
from otm.models.search_response import SearchResponse
from otm.models.stac_feature import StacFeature
from otm.models.standard_order_request import StandardOrderRequest
from otm.models.stored_feasibility_feature_collection import (
    StoredFeasibilityFeatureCollection,
)
from otm.models.stored_feasibility_request import StoredFeasibilityRequest
from otm.models.stored_order_request import StoredOrderRequest
from otm.models.stored_order_request_list import StoredOrderRequestList


class OtmService(SDKClient):
    base_path = "/otm/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_tasking_orders(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> StoredOrderRequestList:
        """
        List all tasking orders.

        Returns a list of your tasking orders. The orders are returned sorted by creation
        date, with the most recent orders appearing first.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            token (Union[None, str]): The pagination token

        Returns:
            StoredOrderRequestList
        """

        params: dict[str, Any] = {}
        params["per_page"] = per_page

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), StoredOrderRequestList)
        return response.json()

    def post_tasking_orders(
        self,
        contract_id: UUID,
        body: Union[
            AssuredOrderRequest,
            ResellerAssuredOrderRequest,
            ResellerStandardOrderRequest,
            StandardOrderRequest,
        ],
    ) -> Union[ResellerStoredOrderRequest, StoredOrderRequest]:
        """
        Create a tasking order request.

        Creates a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            body (Union[AssuredOrderRequest, ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest, StandardOrderRequest]):
                One of:
                - StandardOrderRequest: Feature model for incoming order request.
                - AssuredOrderRequest:
                - ResellerStandardOrderRequest:
                - ResellerAssuredOrderRequest:

        Returns:
            Union[ResellerStoredOrderRequest, StoredOrderRequest]
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/orders/".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 201:
            return deep_parse_from_annotation(
                response.json(), Union[ResellerStoredOrderRequest, StoredOrderRequest]
            )
        return response.json()

    def get_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union[GetOrder, ResellerGetOrder]:
        """
        Retrieve a tasking order.

        Retrieves the tasking order with a given ID.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            Union[GetOrder, ResellerGetOrder]
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                response.json(), Union[GetOrder, ResellerGetOrder]
            )
        return response.json()

    def edit_tasking_order(
        self, contract_id: UUID, order_id: UUID, body: EditOrderPayload
    ) -> Union[GetOrder, ResellerGetOrder]:
        """
        Edit a tasking order request.

        Edits a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            body (EditOrderPayload): Payload for editing an order.

        Returns:
            Union[GetOrder, ResellerGetOrder]
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="patch",
            url="/{contract_id}/tasking/orders/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                response.json(), Union[GetOrder, ResellerGetOrder]
            )
        return response.json()

    def cancel_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Any:
        """
        Cancel a tasking order request.

        Cancels a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            Any
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/orders/{order_id}/cancel".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 204:
            return response.json()
        return response.json()

    def download_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        redirect: Union[None, bool] = True,
    ) -> OrderItemDownloadUrl:
        """
        Download a tasking order.

        Download the item for a specified tasking order owned by the authenticated user,
        provided the order has been fulfilled.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
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
            url="/{contract_id}/tasking/orders/{order_id}/download".format(
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
            return deep_parse_from_annotation(response.json(), OrderItemDownloadUrl)
        if response.status_code == 202:
            return response.json()
        return response.json()

    def get_order_task_details(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> StacFeature:
        """
        Retrieve acquisition details for a tasking order.

        Returns acquisition details for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            StacFeature
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/{order_id}/acquisition/details".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), StacFeature)
        return response.json()

    def get_tasking_feasibility_requests(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> StoredFeasibilityFeatureCollection:
        """
        List all feasibility requests owned by a user.

        Retrieves all tasking feasibility requests owned by a user.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page Default: 25.
            token (Union[None, str]): The pagination token

        Returns:
            StoredFeasibilityFeatureCollection
        """

        params: dict[str, Any] = {}
        params["per_page"] = per_page

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(
                response.json(), StoredFeasibilityFeatureCollection
            )
        return response.json()

    def post_tasking_feasibility(
        self, contract_id: UUID, body: FeasibilityRequest
    ) -> StoredFeasibilityRequest:
        """
        Create feasibility request.

        Searches feasibility options for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            body (FeasibilityRequest): Feature model for incoming feasibility request.

        Returns:
            StoredFeasibilityRequest
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/feasibilities/".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 202:
            return deep_parse_from_annotation(response.json(), StoredFeasibilityRequest)
        return response.json()

    def get_tasking_feasibility_request(
        self,
        contract_id: UUID,
        id: UUID,
    ) -> StoredFeasibilityRequest:
        """
        Retrieve a feasibility request

        Retrieves the tasking feasibility request with a given ID.

        Args:
            contract_id (UUID): Contract ID
            id (UUID): Feasibility Request ID

        Returns:
            StoredFeasibilityRequest
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/{id}".format(
                contract_id=contract_id, id=id
            ),
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), StoredFeasibilityRequest)
        return response.json()

    def get_tasking_feasibility_response(
        self,
        contract_id: UUID,
        id: UUID,
    ) -> FeasibilityResponse:
        """
        Retrieve response for a feasibility request

        Retrieves the tasking feasibility response with a given request ID. Passes are returned
        in ascending order based on the start of the estimated acquisition time.

        Args:
            contract_id (UUID): Contract ID
            id (UUID): Feasibility Request ID

        Returns:
            FeasibilityResponse
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/{id}/response".format(
                contract_id=contract_id, id=id
            ),
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), FeasibilityResponse)
        return response.json()

    def get_price(self, contract_id: UUID, body: PriceRequest) -> OrderPrice:
        """
        Get price for a set of ordering parameters.

        Returns the price for a set of ordering parameters.

        Args:
            contract_id (UUID): Contract ID
            body (PriceRequest): Feature model for incoming price request

        Returns:
            OrderPrice
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/price/".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), OrderPrice)
        return response.json()

    def search(self, contract_id: UUID, body: SearchRequest) -> SearchResponse:
        """
        Search

        Search for feasibility requests/responses and tasking orders owned by the user.

        Args:
            contract_id (UUID): Contract ID
            body (SearchRequest):

        Returns:
            SearchResponse
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/search/".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 200:
            return deep_parse_from_annotation(response.json(), SearchResponse)
        return response.json()
