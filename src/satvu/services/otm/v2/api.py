# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja
import io
from collections.abc import Callable, Generator
from pathlib import Path
from typing import Any, Union
from uuid import UUID, uuid4

from satvu.core import SDKClient, _deep_merge
from satvu.http import HttpClient
from satvu.http.errors import HttpError
from satvu.result import Err as ResultErr
from satvu.result import Ok as ResultOk
from satvu.result import Result, is_err
from satvu.services.otm.v2.models.assured_order_request import AssuredOrderRequest
from satvu.services.otm.v2.models.collection import Collection
from satvu.services.otm.v2.models.download_pending import DownloadPending
from satvu.services.otm.v2.models.edit_order_payload import EditOrderPayload
from satvu.services.otm.v2.models.edit_series_properties import EditSeriesProperties
from satvu.services.otm.v2.models.feasibility_request import FeasibilityRequest
from satvu.services.otm.v2.models.feasibility_response import FeasibilityResponse
from satvu.services.otm.v2.models.get_order_response import GetOrderResponse
from satvu.services.otm.v2.models.list_order_tasks_response import (
    ListOrderTasksResponse,
)
from satvu.services.otm.v2.models.list_order_tasks_unavailable_response import (
    ListOrderTasksUnavailableResponse,
)
from satvu.services.otm.v2.models.list_series_response import ListSeriesResponse
from satvu.services.otm.v2.models.list_stored_orders_response import (
    ListStoredOrdersResponse,
)
from satvu.services.otm.v2.models.list_stored_orders_response_1 import (
    ListStoredOrdersResponse1,
)
from satvu.services.otm.v2.models.modify_feasibility_request import (
    ModifyFeasibilityRequest,
)
from satvu.services.otm.v2.models.order_item_download_url import OrderItemDownloadUrl
from satvu.services.otm.v2.models.order_modification_price import OrderModificationPrice
from satvu.services.otm.v2.models.order_price import OrderPrice
from satvu.services.otm.v2.models.outage import Outage
from satvu.services.otm.v2.models.price_request import PriceRequest
from satvu.services.otm.v2.models.primary_format import PrimaryFormat
from satvu.services.otm.v2.models.reseller_assured_order_request import (
    ResellerAssuredOrderRequest,
)
from satvu.services.otm.v2.models.reseller_get_order_response import (
    ResellerGetOrderResponse,
)
from satvu.services.otm.v2.models.reseller_standard_order_request import (
    ResellerStandardOrderRequest,
)
from satvu.services.otm.v2.models.reseller_stored_order_response import (
    ResellerStoredOrderResponse,
)
from satvu.services.otm.v2.models.search_request import SearchRequest
from satvu.services.otm.v2.models.search_response import SearchResponse
from satvu.services.otm.v2.models.series_price_response import SeriesPriceResponse
from satvu.services.otm.v2.models.series_request import SeriesRequest
from satvu.services.otm.v2.models.stac_feature import StacFeature
from satvu.services.otm.v2.models.standard_order_request import StandardOrderRequest
from satvu.services.otm.v2.models.stored_feasibility_feature_collection import (
    StoredFeasibilityFeatureCollection,
)
from satvu.services.otm.v2.models.stored_feasibility_request import (
    StoredFeasibilityRequest,
)
from satvu.services.otm.v2.models.stored_order_response import StoredOrderResponse
from satvu.services.otm.v2.models.stored_series_response import StoredSeriesResponse
from satvu.shared.parsing import parse_response


class OtmV2Service(SDKClient):
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

    def list_orders(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> ListStoredOrdersResponse1:
        """
        List orders

        Lists your orders, sorted by creation date, newest first.

        Args:
            contract_id (UUID): The ID of the contract.
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            token (None | str): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ListStoredOrdersResponse1
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
            return parse_response(response.json().unwrap(), ListStoredOrdersResponse1)
        return response.json().unwrap()

    def list_orders_iter(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[ListStoredOrdersResponse1, None, None]:
        """
        List orders (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): The ID of the contract.
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.v2.list_orders_iter(
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
            response = self.list_orders(
                contract_id=contract_id, per_page=per_page, token=token
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def create_order(
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
        Create an order

        Creates an order and reserves its price against the contract.

        Args:
            contract_id (UUID): The ID of the contract.
            body (Union['AssuredOrderRequest', 'ResellerAssuredOrderRequest',
                'ResellerStandardOrderRequest', 'StandardOrderRequest']):
                One of:
                - StandardOrderRequest: A new standard order.
                - AssuredOrderRequest:
                - ResellerStandardOrderRequest: A new standard order for a reseller end user.
                - ResellerAssuredOrderRequest: A new assured order for a reseller end user.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['ResellerStoredOrderResponse', 'StoredOrderResponse']
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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
        Get an order

        Gets an order, including its status history and price.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
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
        Edit an order

        Edits an order.

        Supports modifying:

        **Platform-only parameters (any status):**
        - name: Order name

        **Price-relevant parameters (while `staged` or `in progress`):**
        - withhold: Withhold option
        - licence_level: Licence level

        **Tasking parameters (standard orders, `staged` only):**
        - geometry: Order location (Point)
        - start_time: Start of tasking window (must be ≥7 days before end_time, cannot be in the past)
        - end_time: End of tasking window (must be ≥7 days after start_time, cannot be in the past)
        - day_night_mode: Day/night/both
        - max_cloud_cover: Maximum cloud coverage (0-100%)
        - min_off_nadir: Minimum off-nadir angle (0-45°)
        - max_off_nadir: Maximum off-nadir angle (0-45°)

        **Status-based restrictions:**
        - Tasking parameters can only be changed for standard orders that are still `staged`
        - The geometry and tasking parameters of assured orders cannot be changed
        - Price-relevant parameters can be changed while the order is `staged` or `in progress`

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
            body (EditOrderPayload): Modifications to an order. Omitted fields keep their current
                values.

                `geometry` can only change for standard orders that are still `staged`.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['GetOrderResponse', 'ResellerGetOrderResponse']
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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
        Cancel an order

        Cancels an order.

        Cancelling an order in a series is final and uses up its place in the series: no
        replacement order is scheduled. If it was the last outstanding order in the
        series, the series completes.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
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
    ) -> Union[OrderItemDownloadUrl, DownloadPending, io.BytesIO]:
        """
        Download an order

        Downloads the imagery of a fulfilled order.

        By default, every collection (for example, `primary` and
        `surface-brightness-temperature`) is downloaded, with the `primary` collection
        as GeoTIFF. Use `collections` to download a subset.

        With `redirect` set to `true`, the default, the response redirects to the
        download. With `redirect` set to `false`, it returns a presigned download URL
        that expires.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
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
            Union[OrderItemDownloadUrl, DownloadPending, io.BytesIO]
        """
        params = {
            "redirect": redirect,
            "collections": collections,
            "primary_formats": primary_formats,
        }
        request_id = str(uuid4())
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}/download",
            params=params,
            follow_redirects=redirect if redirect is not None else True,
            timeout=timeout,
            headers={"x-download-request-id": request_id},
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
            return parse_response(response.json().unwrap(), DownloadPending)
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
        request_id = str(uuid4())
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/orders/{order_id}/download",
            params=params,
            follow_redirects=True,
            timeout=timeout,
            headers={"x-download-request-id": request_id},
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

    def get_order_acquisition(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> StacFeature:
        """
        Get the acquisition details of an order

        Gets the acquisition details of an order: the STAC item that fulfilled it.

        Only available once the order is `fulfilled`.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
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

    def list_order_tasks(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> Union["ListOrderTasksResponse", "ListOrderTasksUnavailableResponse"]:
        """
        List the tasks of an order

        Lists the tasks of an order, newest first, with each task's status history and
        acquisition metadata.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
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

    def list_feasibility_requests(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> StoredFeasibilityFeatureCollection:
        """
        List feasibility requests

        Lists the feasibility requests you own.

        Args:
            contract_id (UUID): The ID of the contract.
            per_page (Union[None, int]): The number of feasibility requests to return per page.
                Default: 25.
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

    def list_feasibility_requests_iter(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[StoredFeasibilityFeatureCollection, None, None]:
        """
        List feasibility requests (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): The ID of the contract.
            per_page (Union[None, int]): The number of feasibility requests to return per page.
            Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.v2.list_feasibility_requests_iter(
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
            response = self.list_feasibility_requests(
                contract_id=contract_id, per_page=per_page, token=token
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def create_feasibility_request(
        self,
        body: FeasibilityRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> StoredFeasibilityRequest:
        """
        Create a feasibility request

        Creates a feasibility request, which searches for passes that can image the
        location.

        Args:
            contract_id (UUID): The ID of the contract.
            body (FeasibilityRequest): A feasibility request.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredFeasibilityRequest
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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

    def get_feasibility_request(
        self, contract_id: UUID, id: UUID, timeout: int | None = None
    ) -> StoredFeasibilityRequest:
        """
        Get a feasibility request

        Gets a feasibility request, including its status.

        Args:
            contract_id (UUID): The ID of the contract.
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

    def get_feasibility_response(
        self, contract_id: UUID, id: UUID, timeout: int | None = None
    ) -> FeasibilityResponse:
        """
        Get a feasibility response

        Gets the response to a feasibility request.

        For assured tasking, it has one feature per pass, sorted by the start of the
        estimated acquisition time, earliest first. For standard tasking, it has a single
        feature covering the tasking window.

        Args:
            contract_id (UUID): The ID of the contract.
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

    def create_order_feasibility_request(
        self,
        body: ModifyFeasibilityRequest,
        contract_id: UUID,
        order_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> StoredFeasibilityRequest:
        """
        Create a feasibility request for an order modification

        Creates a feasibility request for an edit to a standard order, without
        changing the order.

        Omitted fields keep the order's current values. Only orders in `staged` status
        can be edited.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): Order ID to modify
            body (ModifyFeasibilityRequest): A feasibility request for an edit to a standard order.
                Omitted fields keep
                the order's current values.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredFeasibilityRequest
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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

    def calculate_price(
        self,
        body: PriceRequest,
        contract_id: UUID,
        baseprice: Union[None, bool] = False,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> OrderPrice:
        """
        Calculate the price of an order

        Calculates the price of an order without creating it.

        Args:
            contract_id (UUID): The ID of the contract.
            baseprice (Union[None, bool]): Whether to return the base price only, ignoring any addons
                or the licence level. Default: False.
            body (PriceRequest): A request for the price of an order.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            OrderPrice
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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
        Calculate the price of an order modification

        Calculates the price of an order modification without making it.

        Takes the same body as `PATCH /{contract_id}/tasking/orders/{order_id}` and
        applies the same checks. Returns the order before and after the modification, each
        with its price.

        Args:
            contract_id (UUID): The ID of the contract.
            order_id (UUID): The ID of the order.
            body (EditOrderPayload): Modifications to an order. Omitted fields keep their current
                values.

                `geometry` can only change for standard orders that are still `staged`.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            OrderModificationPrice
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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

    def list_unplanned_outages(
        self, contract_id: UUID, timeout: int | None = None
    ) -> list[Outage]:
        """
        List unplanned satellite outages

        Lists the unplanned satellite outages in the next 8 days.

        Args:
            contract_id (UUID): The ID of the contract.
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

    def list_series(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> ListSeriesResponse:
        """
        List series

        Lists the series on the contract, sorted by creation date, newest first.

        Args:
            contract_id (UUID): The ID of the contract.
            per_page (Union[None, int]): Number of series to return per page. Default: 25.
            token (None | str): Pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ListSeriesResponse
        """
        params = {"per_page": per_page, "token": token}
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/series/",
            params=params,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), ListSeriesResponse)
        return response.json().unwrap()

    def list_series_iter(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[ListSeriesResponse, None, None]:
        """
        List series (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): The ID of the contract.
            per_page (Union[None, int]): Number of series to return per page. Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.v2.list_series_iter(
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
            response = self.list_series(
                contract_id=contract_id, per_page=per_page, token=token
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def create_series(
        self,
        body: SeriesRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> StoredSeriesResponse:
        """
        Create a series

        Creates a series, which creates standard orders at a set frequency,
        starting from `start_date`.

        Send either `total_order_count` or `end_date` to set how many orders it creates.
        Each order's price is reserved when the series creates it.

        Args:
            contract_id (UUID): The ID of the contract.
            body (SeriesRequest): Request body for creating a recurring tasking series.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredSeriesResponse
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/series/",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 201:
            return parse_response(response.json().unwrap(), StoredSeriesResponse)
        return response.json().unwrap()

    def get_series(
        self, contract_id: UUID, series_id: UUID, timeout: int | None = None
    ) -> StoredSeriesResponse:
        """
        Get a series

        Gets a series, including how many orders it has created.

        Args:
            contract_id (UUID): The ID of the contract.
            series_id (UUID): The ID of the series.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredSeriesResponse
        """
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/series/{series_id}",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), StoredSeriesResponse)
        return response.json().unwrap()

    def edit_series(
        self,
        body: EditSeriesProperties,
        contract_id: UUID,
        series_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> StoredSeriesResponse:
        """
        Edit a series

        Edits a series.

        Omitted fields keep their current values. `name` can be changed or cleared in
        any status; every other field only while the series is `active`.

        Modifications apply only to orders the series creates from now on. Orders it has
        already created are unchanged.

        Args:
            contract_id (UUID): The ID of the contract.
            series_id (UUID): The ID of the series.
            body (EditSeriesProperties): Editable fields for series updates.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            StoredSeriesResponse
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="patch",
            url=f"/{contract_id}/tasking/series/{series_id}",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), StoredSeriesResponse)
        return response.json().unwrap()

    def list_series_orders(
        self,
        contract_id: UUID,
        series_id: UUID,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> ListStoredOrdersResponse:
        """
        List the orders in a series

        Lists the orders in a series, sorted by creation date, newest first.

        Args:
            contract_id (UUID): The ID of the contract.
            series_id (UUID): The ID of the series.
            per_page (Union[None, int]): Number of orders to return per page. Default: 25.
            token (None | str): Pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ListStoredOrdersResponse
        """
        params = {"per_page": per_page, "token": token}
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/series/{series_id}/orders/",
            params=params,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), ListStoredOrdersResponse)
        return response.json().unwrap()

    def list_series_orders_iter(
        self,
        contract_id: UUID,
        series_id: UUID,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[ListStoredOrdersResponse, None, None]:
        """
        List the orders in a series (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): The ID of the contract.
            series_id (UUID): The ID of the series.
            per_page (Union[None, int]): Number of orders to return per page. Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.v2.list_series_orders_iter(
                contract_id=...,
                series_id=...,
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
            response = self.list_series_orders(
                contract_id=contract_id,
                series_id=series_id,
                per_page=per_page,
                token=token,
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def calculate_series_price_estimate(
        self,
        body: SeriesRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> SeriesPriceResponse:
        """
        Calculate the price of a series

        Calculates the estimated price of a series without creating it.

        The estimate is not a commitment: each order's price is reserved when the series
        creates it.

        Args:
            contract_id (UUID): The ID of the contract.
            body (SeriesRequest): Request body for creating a recurring tasking series.
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SeriesPriceResponse
        """
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/series/price/",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), SeriesPriceResponse)
        return response.json().unwrap()

    def cancel_series(
        self, contract_id: UUID, series_id: UUID, timeout: int | None = None
    ) -> None:
        """
        Cancel a series

        Cancels a series, so it creates no more orders.

        Cancelling an already-cancelled series succeeds. A series that has already
        completed cannot be cancelled.

        Args:
            contract_id (UUID): The ID of the contract.
            series_id (UUID): The ID of the series.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            None
        """
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/tasking/series/{series_id}/cancel",
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 204:
            return None
        return response.json().unwrap()

    def download_series(
        self,
        contract_id: UUID,
        series_id: UUID,
        redirect: Union[None, bool] = True,
        collections: list["Collection"] | None = None,
        primary_formats: list["PrimaryFormat"] | None = None,
        timeout: int | None = None,
    ) -> Union[OrderItemDownloadUrl, DownloadPending, io.BytesIO]:
        """
        Download a series

        Downloads the imagery of every fulfilled order in a series as a single bundle.

        By default, every collection (for example, `primary` and
        `surface-brightness-temperature`) is downloaded, with the `primary` collection
        as GeoTIFF. Use `collections` and `primary_formats` to select a subset across
        the whole series.

        Args:
            contract_id (UUID): The ID of the contract.
            series_id (UUID): The ID of the series.
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.
            collections (list['Collection'] | None): Specify a subset of collections to download.
                        Defaults to all linked collections (e.g. primary,
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
            Union[OrderItemDownloadUrl, DownloadPending, io.BytesIO]
        """
        params = {
            "redirect": redirect,
            "collections": collections,
            "primary_formats": primary_formats,
        }
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/tasking/series/{series_id}/download",
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
            return parse_response(response.json().unwrap(), DownloadPending)
        return response.json().unwrap()

    def search(
        self,
        body: SearchRequest,
        contract_id: UUID,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> SearchResponse:
        """
        Search orders and feasibility requests

        Searches the orders and feasibility requests you own.

        Args:
            contract_id (UUID): The ID of the contract.
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
        json_body = body.model_dump(by_alias=True, mode="json", exclude_unset=True)
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
        Search orders and feasibility requests (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (SearchRequest):
            contract_id (UUID): The ID of the contract.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.otm.v2.search_iter(
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
