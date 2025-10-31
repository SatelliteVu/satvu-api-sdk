import io
from collections.abc import Callable
from typing import Any, Union
from uuid import UUID

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.services.otm.models.assured_order_request import AssuredOrderRequest
from satvu_api_sdk.services.otm.models.edit_order_payload import EditOrderPayload
from satvu_api_sdk.services.otm.models.feasibility_request import FeasibilityRequest
from satvu_api_sdk.services.otm.models.feasibility_response import FeasibilityResponse
from satvu_api_sdk.services.otm.models.get_order_response_1 import GetOrderResponse1
from satvu_api_sdk.services.otm.models.list_stored_orders_response import (
    ListStoredOrdersResponse,
)
from satvu_api_sdk.services.otm.models.modify_feasibility_request import (
    ModifyFeasibilityRequest,
)
from satvu_api_sdk.services.otm.models.order_item_download_url import (
    OrderItemDownloadUrl,
)
from satvu_api_sdk.services.otm.models.order_price import OrderPrice
from satvu_api_sdk.services.otm.models.outage_1 import Outage1
from satvu_api_sdk.services.otm.models.price_request import PriceRequest
from satvu_api_sdk.services.otm.models.reseller_assured_order_request import (
    ResellerAssuredOrderRequest,
)
from satvu_api_sdk.services.otm.models.reseller_get_order_response_1 import (
    ResellerGetOrderResponse1,
)
from satvu_api_sdk.services.otm.models.reseller_standard_order_request import (
    ResellerStandardOrderRequest,
)
from satvu_api_sdk.services.otm.models.reseller_stored_order_response_1 import (
    ResellerStoredOrderResponse1,
)
from satvu_api_sdk.services.otm.models.search_request import SearchRequest
from satvu_api_sdk.services.otm.models.search_response import SearchResponse
from satvu_api_sdk.services.otm.models.stac_feature import StacFeature
from satvu_api_sdk.services.otm.models.standard_order_request import (
    StandardOrderRequest,
)
from satvu_api_sdk.services.otm.models.stored_feasibility_feature_collection import (
    StoredFeasibilityFeatureCollection,
)
from satvu_api_sdk.services.otm.models.stored_feasibility_request import (
    StoredFeasibilityRequest,
)
from satvu_api_sdk.services.otm.models.stored_order_response_1 import (
    StoredOrderResponse1,
)
from satvu_api_sdk.shared.parsing import parse_response


class OtmService(SDKClient):
    base_path = "/otm/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_tasking_orders(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
    ) -> ListStoredOrdersResponse:
        """
        List all tasking orders.

        Returns a list of your tasking orders. The orders are returned sorted by creation
        date, with the most recent orders appearing first.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            token (None | str): The pagination token

        Returns:
            ListStoredOrdersResponse
        """

        params = {
            "per_page": per_page,
            "token": token,
        }

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return parse_response(response.json(), ListStoredOrdersResponse)
        return response.json()

    def post_tasking_orders(
        self,
        body: Union[
            "AssuredOrderRequest",
            "ResellerAssuredOrderRequest",
            "ResellerStandardOrderRequest",
            "StandardOrderRequest",
        ],
        contract_id: UUID,
    ) -> Union["ResellerStoredOrderResponse1", "StoredOrderResponse1"]:
        """
        Create a tasking order request.

        Creates a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            body (Union['AssuredOrderRequest', 'ResellerAssuredOrderRequest',
                'ResellerStandardOrderRequest', 'StandardOrderRequest']):
                One of:
                - StandardOrderRequest: Payload for standard order request.
                - AssuredOrderRequest:
                - ResellerStandardOrderRequest: Payload for reseller standard order request.
                - ResellerAssuredOrderRequest: Payload for reseller assured order request.

        Returns:
            Union['ResellerStoredOrderResponse1', 'StoredOrderResponse1']
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/orders/".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 201:
            return parse_response(
                response.json(), ResellerStoredOrderResponse1 | StoredOrderResponse1
            )
        return response.json()

    def get_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union["GetOrderResponse1", "ResellerGetOrderResponse1"]:
        """
        Retrieve a tasking order.

        Retrieves the tasking order with a given ID.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            Union['GetOrderResponse1', 'ResellerGetOrderResponse1']
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            return parse_response(
                response.json(), GetOrderResponse1 | ResellerGetOrderResponse1
            )
        return response.json()

    def edit_tasking_order(
        self,
        body: EditOrderPayload,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union["GetOrderResponse1", "ResellerGetOrderResponse1"]:
        """
        Edit a tasking order request.

        Edits a tasking order request.

        Supports modifying:
        - name: Order name (can be modified at any time)
        - withhold: Withhold option (can be modified until fulfillment)
        - licence_level: Licence level (can be modified until fulfillment)

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            body (EditOrderPayload): Payload for editing an order.

        Returns:
            Union['GetOrderResponse1', 'ResellerGetOrderResponse1']
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
            return parse_response(
                response.json(), GetOrderResponse1 | ResellerGetOrderResponse1
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
    ) -> Union[OrderItemDownloadUrl, Any, io.BytesIO]:
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
            Union[OrderItemDownloadUrl, Any, io.BytesIO]
        """

        params = {
            "redirect": redirect,
        }

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
            return parse_response(response.json(), OrderItemDownloadUrl)
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
            return parse_response(response.json(), StacFeature)
        return response.json()

    def get_tasking_feasibility_requests(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
    ) -> StoredFeasibilityFeatureCollection:
        """
        List all feasibility requests owned by a user.

        Retrieves all tasking feasibility requests owned by a user.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page Default: 25.
            token (None | str): The pagination token

        Returns:
            StoredFeasibilityFeatureCollection
        """

        params = {
            "per_page": per_page,
            "token": token,
        }

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return parse_response(response.json(), StoredFeasibilityFeatureCollection)
        return response.json()

    def post_tasking_feasibility(
        self,
        body: FeasibilityRequest,
        contract_id: UUID,
    ) -> StoredFeasibilityRequest:
        """
        Create feasibility request.

        Searches feasibility options for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            body (FeasibilityRequest): Payload for feasibility request.

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
            return parse_response(response.json(), StoredFeasibilityRequest)
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
            return parse_response(response.json(), StoredFeasibilityRequest)
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
            return parse_response(response.json(), FeasibilityResponse)
        return response.json()

    def post_tasking_order_feasibility(
        self,
        body: ModifyFeasibilityRequest,
        contract_id: UUID,
        order_id: UUID,
    ) -> StoredFeasibilityRequest:
        """
        Create feasibility request for modifying an existing order.

        Performs a feasibility check for modifying an existing tasking order.
        Only supports Standard orders.
        All fields in the payload are optional - unspecified fields will be sourced from the existing order.

        Orders can only be modified if they are not in a terminal or non-modifiable state.
        Orders in the following states can be modified: `committed`, `staged`.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID to modify
            body (ModifyFeasibilityRequest): Payload for modify feasibility request.
                Only supports Standard orders. Assured orders cannot be modified.
                All fields are optional - unspecified fields will be sourced from the existing order.
                At least one field must be provided.

        Returns:
            StoredFeasibilityRequest
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/feasibilities/orders/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
            json=json_body,
        )

        if response.status_code == 202:
            return parse_response(response.json(), StoredFeasibilityRequest)
        return response.json()

    def get_price(
        self,
        body: PriceRequest,
        contract_id: UUID,
        baseprice: Union[None, bool] = False,
    ) -> OrderPrice:
        """
        Get price for a set of ordering parameters.

        Returns the price for a set of ordering parameters.

        Args:
            contract_id (UUID): Contract ID
            baseprice (Union[None, bool]): Whether to return the base price only, ignoring any addons
                or the licence level. Default: False.
            body (PriceRequest): Payload for price request.

        Returns:
            OrderPrice
        """

        json_body = body.model_dump(by_alias=True)

        params = {
            "baseprice": baseprice,
        }

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/price/".format(contract_id=contract_id),
            json=json_body,
            params=params,
        )

        if response.status_code == 200:
            return parse_response(response.json(), OrderPrice)
        return response.json()

    def get_unplanned_outages(
        self,
        contract_id: UUID,
    ) -> list[Outage1]:
        """
        List unplanned satellite outages.

        Args:
            contract_id (UUID): Contract ID

        Returns:
            list[Outage1]
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/outages/".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return parse_response(response.json(), list[Outage1])
        return response.json()

    def search(
        self,
        body: SearchRequest,
        contract_id: UUID,
    ) -> SearchResponse:
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
            return parse_response(response.json(), SearchResponse)
        return response.json()
