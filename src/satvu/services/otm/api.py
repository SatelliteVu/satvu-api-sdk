# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja
import io
from collections.abc import Callable, Generator
from pathlib import Path
from typing import Any, Union
from uuid import UUID

from satvu.core import SDKClient, _deep_merge
from satvu.http import HttpClient
from satvu.http.errors import HttpError
from satvu.result import Err as ResultErr
from satvu.result import Ok as ResultOk
from satvu.result import Result, is_err
from satvu.services.otm.models.assured_order_request import AssuredOrderRequest
from satvu.services.otm.models.collection import Collection
from satvu.services.otm.models.edit_order_payload import EditOrderPayload
from satvu.services.otm.models.feasibility_request import FeasibilityRequest
from satvu.services.otm.models.feasibility_response import FeasibilityResponse
from satvu.services.otm.models.get_order_response import GetOrderResponse
from satvu.services.otm.models.list_order_tasks_response import ListOrderTasksResponse
from satvu.services.otm.models.list_order_tasks_unavailable_response import (
    ListOrderTasksUnavailableResponse,
)
from satvu.services.otm.models.list_stored_orders_response import (
    ListStoredOrdersResponse,
)
from satvu.services.otm.models.modify_feasibility_request import (
    ModifyFeasibilityRequest,
)
from satvu.services.otm.models.order_item_download_url import OrderItemDownloadUrl
from satvu.services.otm.models.order_modification_price import OrderModificationPrice
from satvu.services.otm.models.order_price import OrderPrice
from satvu.services.otm.models.outage import Outage
from satvu.services.otm.models.price_request import PriceRequest
from satvu.services.otm.models.primary_format import PrimaryFormat
from satvu.services.otm.models.reseller_assured_order_request import (
    ResellerAssuredOrderRequest,
)
from satvu.services.otm.models.reseller_get_order_response import (
    ResellerGetOrderResponse,
)
from satvu.services.otm.models.reseller_standard_order_request import (
    ResellerStandardOrderRequest,
)
from satvu.services.otm.models.reseller_stored_order_response import (
    ResellerStoredOrderResponse,
)
from satvu.services.otm.models.search_request import SearchRequest
from satvu.services.otm.models.search_response import SearchResponse
from satvu.services.otm.models.stac_feature import StacFeature
from satvu.services.otm.models.standard_order_request import StandardOrderRequest
from satvu.services.otm.models.stored_feasibility_feature_collection import (
    StoredFeasibilityFeatureCollection,
)
from satvu.services.otm.models.stored_feasibility_request import (
    StoredFeasibilityRequest,
)
from satvu.services.otm.models.stored_order_response import StoredOrderResponse
from satvu.shared.parsing import parse_response


class OtmService(SDKClient):
    base_path = "/otm/v2"

    def __init__(
        self,
        env: str | None,
        get_token: Callable[[], str],
        http_client: HttpClient | None = None,
        timeout: int = 30,
        max_retry_attempts: int = 5,
        max_retry_after_seconds: float = 300.0,
    ):
        super().__init__(
            env=env,
            get_token=get_token,
            http_client=http_client,
            timeout=timeout,
            max_retry_attempts=max_retry_attempts,
            max_retry_after_seconds=max_retry_after_seconds,
        )

    def get_tasking_orders(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> ListStoredOrdersResponse:
        """
        List all tasking orders.

        Returns a list of your tasking orders. The orders are returned sorted by creation
        date, with the most recent orders appearing first.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            token (None | str): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ListStoredOrdersResponse
        """
        params = {"per_page": per_page, "token": token}
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/",
            params=params,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), ListStoredOrdersResponse)
        return response.json().unwrap()

    def get_tasking_orders_iter(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[ListStoredOrdersResponse, None, None]:
        """
        List all tasking orders. (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.get_tasking_orders_iter(
                contract_id=...,
                max_pages=10
            ):
                for item in page.features:
                    print(item)
            ```
        """
        token = None
        page_count = 0
        while True:
            if max_pages and page_count >= max_pages:
                break
            response = self.get_tasking_orders(
                contract_id=contract_id, per_page=per_page, token=token
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def post_tasking_orders(
        self,
        body: Union[
            "AssuredOrderRequest",
            "ResellerAssuredOrderRequest",
            "ResellerStandardOrderRequest",
            "StandardOrderRequest",
        ],
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> Union["ResellerStoredOrderResponse", "StoredOrderResponse"]:
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
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['ResellerStoredOrderResponse', 'StoredOrderResponse']
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/orders/",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 201:
            return parse_response(
                response.json().unwrap(),
                ResellerStoredOrderResponse | StoredOrderResponse,
            )
        return response.json().unwrap()

    def get_tasking_order(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> Union["GetOrderResponse", "ResellerGetOrderResponse"]:
        """
        Retrieve a tasking order.

        Retrieves the tasking order with a given ID.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['GetOrderResponse', 'ResellerGetOrderResponse']
        """
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), GetOrderResponse | ResellerGetOrderResponse
            )
        return response.json().unwrap()

    def edit_tasking_order(
        self,
        body: EditOrderPayload,
        contract_id: UUID,
        order_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> Union["GetOrderResponse", "ResellerGetOrderResponse"]:
        """
        Edit a tasking order request.

        Edits a tasking order request.

        Supports modifying:

        **Platform-only parameters (any status):**
        - name: Order name

        **Price-relevant parameters (until fulfillment):**
        - withhold: Withhold option
        - licence_level: Licence level

        **Tasking parameters (Standard orders, Created/Staged only):**
        - geometry: Order location (Point)
        - start_time: Start of tasking window (must be ≥7 days before end_time, cannot be in the past)
        - end_time: End of tasking window (must be ≥7 days after start_time, cannot be in the past)
        - day_night_mode: Day/night/both
        - max_cloud_cover: Maximum cloud coverage (0-100%)
        - min_off_nadir: Minimum off-nadir angle (0-45°)
        - max_off_nadir: Maximum off-nadir angle (0-45°)

        **Status-based restrictions:**
        - Tasking parameters can only be modified for Standard orders before submission
        - Assured orders cannot modify geometry or tasking parameters
        - Price-relevant parameters can be modified until fulfillment

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            body (EditOrderPayload): Payload for editing an order.

                Geometry can be edited for Standard orders in Created/Staged states.
                All property fields are optional - only provided fields will be updated.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['GetOrderResponse', 'ResellerGetOrderResponse']
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="patch",
            url=f"/{contract_id}/tasking/orders/{order_id}",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), GetOrderResponse | ResellerGetOrderResponse
            )
        return response.json().unwrap()

    def cancel_tasking_order(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> None:
        """
        Cancel a tasking order request.

        Cancels a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            None
        """
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/orders/{order_id}/cancel",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 204:
            return None
        return response.json().unwrap()

    def download_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        redirect: Union[None, bool] = True,
        collections: list["Collection"] | None = None,
        primary_formats: list["PrimaryFormat"] | None = None,
        timeout: int | None = None,
    ) -> Union[OrderItemDownloadUrl, Any, io.BytesIO]:
        """
        Download a tasking order.

        Download the item for a specified tasking order owned by the authenticated user,
        provided the order has been fulfilled.

        For acquisition orders, all linked collections (e.g. primary,
        surface-brightness-temperature) are downloaded by default with GeoTIFF
        format for the primary collection. Use the collections parameter to
        download a specific subset.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.
            collections (list['Collection'] | None): Specify a subset of collections to download.
                        For acquisition orders, defaults to all linked collections (e.g. primary,
                        surface-brightness-temperature) with GeoTIFF format for primary.
                        To specify multiple collections, repeat the query parameter.

            primary_formats (list['PrimaryFormat'] | None): Specify a file format to download.
                            Defaults to geotiff, which will download without nitf.
                            To specify multiple formats, repeat the query parameter.
                            If NITF is specified but not available for an item, GeoTIFF will be provided
                instead.

            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union[OrderItemDownloadUrl, Any, io.BytesIO]
        """
        params = {
            "redirect": redirect,
            "collections": collections,
            "primary_formats": primary_formats,
        }
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}/download",
            params=params,
            follow_redirects=redirect if redirect is not None else True,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.headers.get("Content-Type") == "application/zip":
            zip_bytes = io.BytesIO(response.body)
            return zip_bytes
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), OrderItemDownloadUrl)
        if response.status_code == 202:
            return response.json().unwrap()
        return response.json().unwrap()

    def download_tasking_order_to_file(
        self,
        contract_id: UUID,
        order_id: UUID,
        output_path: Path | str,
        *,
        collections: list["Collection"] | None = None,
        primary_formats: list["PrimaryFormat"] | None = None,
        chunk_size: int = 8192,
        progress_callback: Callable[[int, int | None], None] | None = None,
        timeout: int | None = None,
    ) -> Result[Path, HttpError]:
        """Stream high-resolution imagery to disk

        Downloads directly to disk using streaming, avoiding loading
        the entire file into memory. Ideal for large files (1GB+).

        Args:
            contract_id (UUID): The contract ID
            order_id (UUID): The order ID
            output_path (Path | str): Where to save the downloaded file.
            collections (list['Collection'] | None): Optional subset of collections to download
            primary_formats (list['PrimaryFormat'] | None): Optional file format(s) to download
            chunk_size (int): Bytes per chunk (default: 8192). Use 64KB+ for faster downloads.
            progress_callback: Optional callback for download progress tracking.
                             Signature: callback(bytes_downloaded: int, total_bytes: int | None)
            timeout: Optional request timeout in seconds. Overrides the instance timeout.

        Returns:
            Result[Path, HttpError]: Ok(Path) on success, Err(HttpError) on failure"""
        params = {
            "redirect": True,
            "collections": collections,
            "primary_formats": primary_formats,
        }
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}/download",
            params=params,
            follow_redirects=True,
            timeout=timeout,
        )
        if is_err(result):
            return ResultErr(result.error())
        response = result.unwrap()
        downloaded_path = self.stream_to_file(
            response=response,
            output_path=output_path,
            chunk_size=chunk_size,
            progress_callback=progress_callback,
        )
        return ResultOk(downloaded_path)

    def get_order_task_details(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> StacFeature:
        """
        Retrieve acquisition details for a tasking order.

        Returns acquisition details for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StacFeature
        """
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}/acquisition/details",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), StacFeature)
        return response.json().unwrap()

    def get_tasking_order_tasks(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> Union["ListOrderTasksResponse", "ListOrderTasksUnavailableResponse"]:
        """
        List all tasks for a tasking order.

        Returns a list of tasks for an order, sorted by creation date (newest first).

        Includes status history and acquisition metadata for each task.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['ListOrderTasksResponse', 'ListOrderTasksUnavailableResponse']
        """
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}/tasks",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(),
                ListOrderTasksResponse | ListOrderTasksUnavailableResponse,
            )
        return response.json().unwrap()

    def get_tasking_feasibility_requests(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> StoredFeasibilityFeatureCollection:
        """
        List all feasibility requests owned by a user.

        Retrieves all tasking feasibility requests owned by a user.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page Default: 25.
            token (None | str): The pagination token
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredFeasibilityFeatureCollection
        """
        params = {"per_page": per_page, "token": token}
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/feasibilities/",
            params=params,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), StoredFeasibilityFeatureCollection
            )
        return response.json().unwrap()

    def get_tasking_feasibility_requests_iter(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[StoredFeasibilityFeatureCollection, None, None]:
        """
        List all feasibility requests owned by a user. (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.get_tasking_feasibility_requests_iter(
                contract_id=...,
                max_pages=10
            ):
                for item in page.features:
                    print(item)
            ```
        """
        token = None
        page_count = 0
        while True:
            if max_pages and page_count >= max_pages:
                break
            response = self.get_tasking_feasibility_requests(
                contract_id=contract_id, per_page=per_page, token=token
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def post_tasking_feasibility(
        self,
        body: FeasibilityRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> StoredFeasibilityRequest:
        """
        Create feasibility request.

        Searches feasibility options for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            body (FeasibilityRequest): Payload for feasibility request.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredFeasibilityRequest
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/feasibilities/",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 202:
            return parse_response(response.json().unwrap(), StoredFeasibilityRequest)
        return response.json().unwrap()

    def get_tasking_feasibility_request(
        self, contract_id: UUID, id: UUID, timeout: int | None = None
    ) -> StoredFeasibilityRequest:
        """
        Retrieve a feasibility request

        Retrieves the tasking feasibility request with a given ID.

        Args:
            contract_id (UUID): Contract ID
            id (UUID): Feasibility Request ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredFeasibilityRequest
        """
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/feasibilities/{id}",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), StoredFeasibilityRequest)
        return response.json().unwrap()

    def get_tasking_feasibility_response(
        self, contract_id: UUID, id: UUID, timeout: int | None = None
    ) -> FeasibilityResponse:
        """
        Retrieve response for a feasibility request

        Retrieves the tasking feasibility response with a given request ID. Passes are returned
        in ascending order based on the start of the estimated acquisition time.

        Args:
            contract_id (UUID): Contract ID
            id (UUID): Feasibility Request ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            FeasibilityResponse
        """
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/feasibilities/{id}/response",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), FeasibilityResponse)
        return response.json().unwrap()

    def post_tasking_order_feasibility(
        self,
        body: ModifyFeasibilityRequest,
        contract_id: UUID,
        order_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
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
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredFeasibilityRequest
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/feasibilities/orders/{order_id}",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 202:
            return parse_response(response.json().unwrap(), StoredFeasibilityRequest)
        return response.json().unwrap()

    def get_price(
        self,
        body: PriceRequest,
        contract_id: UUID,
        baseprice: Union[None, bool] = False,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> OrderPrice:
        """
        Get price for a set of ordering parameters.

        Returns the price for a set of ordering parameters.

        Args:
            contract_id (UUID): Contract ID
            baseprice (Union[None, bool]): Whether to return the base price only, ignoring any addons
                or the licence level. Default: False.
            body (PriceRequest): Payload for price request.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            OrderPrice
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        params = {"baseprice": baseprice}
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/price/",
            json=json_body,
            params=params,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), OrderPrice)
        return response.json().unwrap()

    def calculate_modified_order_price(
        self,
        body: EditOrderPayload,
        contract_id: UUID,
        order_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> OrderModificationPrice:
        """
        Calculate price for modification of an existing order.

        Returns an updated price for modifying an existing order.

        This endpoint provides a price preview before committing changes via the PATCH /orders/{order_id}
        endpoint.

        The response includes the complete updated order representation showing how the order would look
        after modification, including the original price and the updated price value.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            body (EditOrderPayload): Payload for editing an order.

                Geometry can be edited for Standard orders in Created/Staged states.
                All property fields are optional - only provided fields will be updated.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            OrderModificationPrice
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/price/{order_id}",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), OrderModificationPrice)
        return response.json().unwrap()

    def get_unplanned_outages(
        self, contract_id: UUID, timeout: int | None = None
    ) -> list[Outage]:
        """
        List unplanned satellite outages.

        Args:
            contract_id (UUID): Contract ID
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            list[Outage]
        """
        result = self.make_request(
            method="get", url=f"/{contract_id}/tasking/outages/", timeout=timeout
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), list[Outage])
        return response.json().unwrap()

    def search(
        self,
        body: SearchRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> SearchResponse:
        """
        Search

        Search for feasibility requests/responses and tasking orders owned by the user.

        Args:
            contract_id (UUID): Contract ID
            body (SearchRequest):
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SearchResponse
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/search/",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), SearchResponse)
        return response.json().unwrap()

    def search_iter(
        self,
        body: SearchRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        max_pages: int | None = None,
    ) -> Generator[SearchResponse, None, None]:
        """
        Search (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (SearchRequest):
            contract_id (UUID): Contract ID
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.search_iter(
                body=...,
                contract_id=...,
                max_pages=10
            ):
                for item in page.features:
                    print(item)
            ```
        """
        token = None
        page_count = 0
        while True:
            if max_pages and page_count >= max_pages:
                break
            body_with_token = body.model_copy(update={"token": token})
            response = self.search(
                body=body_with_token, contract_id=contract_id, extra_body=extra_body
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break
