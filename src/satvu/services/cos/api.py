# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja
import io
from collections.abc import Callable, Generator
from pathlib import Path
from typing import Any, Union
from uuid import UUID

from satvu.core import SDKClient
from satvu.http import HttpClient
from satvu.http.errors import HttpError
from satvu.result import Err as ResultErr
from satvu.result import Ok as ResultOk
from satvu.result import Result, is_err
from satvu.services.cos.models.collection import Collection
from satvu.services.cos.models.feature_collection_order import FeatureCollectionOrder
from satvu.services.cos.models.order_download_url import OrderDownloadUrl
from satvu.services.cos.models.order_edit_payload import OrderEditPayload
from satvu.services.cos.models.order_item_download_url import OrderItemDownloadUrl
from satvu.services.cos.models.order_page import OrderPage
from satvu.services.cos.models.order_price import OrderPrice
from satvu.services.cos.models.order_submission_payload import OrderSubmissionPayload
from satvu.services.cos.models.price_request import PriceRequest
from satvu.services.cos.models.primary_format import PrimaryFormat
from satvu.services.cos.models.reseller_feature_collection_order import (
    ResellerFeatureCollectionOrder,
)
from satvu.services.cos.models.reseller_order_price import ResellerOrderPrice
from satvu.services.cos.models.reseller_price_request import ResellerPriceRequest
from satvu.services.cos.models.reseller_submission_order_payload import (
    ResellerSubmissionOrderPayload,
)
from satvu.services.cos.models.search_request import SearchRequest
from satvu.shared.parsing import parse_response


class CosService(SDKClient):
    base_path = "/orders/v3"

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

    def get_order(
        self, contract_id: UUID, order_id: UUID, timeout: int | None = None
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Order details

        Retrieve order details for a specified Order ID owned by the authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """
        result = self.make_request(
            method="get", url=f"/{contract_id}/{order_id}", timeout=timeout
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(),
                FeatureCollectionOrder | ResellerFeatureCollectionOrder,
            )
        return response.json().unwrap()

    def edit_order(
        self,
        body: OrderEditPayload,
        contract_id: UUID,
        order_id: UUID,
        timeout: int | None = None,
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Edit Order

        Edit the name of an order owned by the authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.
            body (OrderEditPayload): Request payload for editing an order.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        result = self.make_request(
            method="patch",
            url=f"/{contract_id}/{order_id}",
            json=json_body,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(),
                FeatureCollectionOrder | ResellerFeatureCollectionOrder,
            )
        return response.json().unwrap()

    def query_orders(
        self,
        contract_id: UUID,
        limit: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> OrderPage:
        """
        Query orders

        Retrieve all existing orders owned by the authenticated user.

        Args:
            contract_id (UUID): The contract ID.
            limit (Union[None, int]): The number of orders to return per page. Default: 25.
            token (None | str): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            OrderPage
        """
        params = {"limit": limit, "token": token}
        result = self.make_request(
            method="get", url=f"/{contract_id}/", params=params, timeout=timeout
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(response.json().unwrap(), OrderPage)
        return response.json().unwrap()

    def query_orders_iter(
        self,
        contract_id: UUID,
        limit: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[OrderPage, None, None]:
        """
        Query orders (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (UUID): The contract ID.
            limit (Union[None, int]): The number of orders to return per page. Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.cos.query_orders_iter(
                contract_id=...,
                max_pages=10
            ):
                for item in page.orders:
                    print(item)
            ```
        """
        token = None
        page_count = 0
        while True:
            if max_pages and page_count >= max_pages:
                break
            response = self.query_orders(
                contract_id=contract_id, limit=limit, token=token
            )
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def submit_order(
        self,
        body: Union["OrderSubmissionPayload", "ResellerSubmissionOrderPayload"],
        contract_id: UUID,
        timeout: int | None = None,
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
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        result = self.make_request(
            method="post", url=f"/{contract_id}/", json=json_body, timeout=timeout
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 201:
            return parse_response(
                response.json().unwrap(),
                FeatureCollectionOrder | ResellerFeatureCollectionOrder,
            )
        return response.json().unwrap()

    def search_orders(
        self, body: SearchRequest, contract_id: UUID, timeout: int | None = None
    ) -> OrderPage:
        """
        Search orders

        Args:
            contract_id (UUID): The contract ID.
            body (SearchRequest):
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            OrderPage
        """
        json_body = body.model_dump(by_alias=True, mode="json")
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
            return parse_response(response.json().unwrap(), OrderPage)
        return response.json().unwrap()

    def search_orders_iter(
        self, body: SearchRequest, contract_id: UUID, max_pages: int | None = None
    ) -> Generator[OrderPage, None, None]:
        """
        Search orders (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (SearchRequest):
            contract_id (UUID): The contract ID.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.cos.search_orders_iter(
                body=...,
                contract_id=...,
                max_pages=10
            ):
                for item in page.orders:
                    print(item)
            ```
        """
        token = None
        page_count = 0
        while True:
            if max_pages and page_count >= max_pages:
                break
            body_with_token = body.model_copy(update={"token": token})
            response = self.search_orders(body=body_with_token, contract_id=contract_id)
            page_count += 1
            yield response
            token = self.extract_next_token(response)
            if not token:
                break

    def download_order_item(
        self,
        contract_id: UUID,
        order_id: UUID,
        item_id: str,
        primary_formats: list["PrimaryFormat"] | None = None,
        redirect: Union[None, bool] = True,
        timeout: int | None = None,
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
            primary_formats (list['PrimaryFormat'] | None): Specify a file format to download.
                            Defaults to geotiff, which will download without nitf.
                            To specify multiple formats, repeat the query parameter.
                            If NITF is specified but not available for an item, GeoTIFF will be provided
                instead.

            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union[OrderItemDownloadUrl, Any, io.BytesIO]
        """
        params = {"primary_formats": primary_formats, "redirect": redirect}
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/{order_id}/{item_id}/download",
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

    def download_order_item_to_file(
        self,
        contract_id: UUID,
        order_id: UUID,
        item_id: str,
        output_path: Path | str,
        *,
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
            item_id (str): The item ID
            output_path (Path | str): Where to save the downloaded file.
            primary_formats (list['PrimaryFormat'] | None): Optional file format(s) to download
            chunk_size (int): Bytes per chunk (default: 8192). Use 64KB+ for faster downloads.
            progress_callback: Optional callback for download progress tracking.
                             Signature: callback(bytes_downloaded: int, total_bytes: int | None)
            timeout: Optional request timeout in seconds. Overrides the instance timeout.

        Returns:
            Result[Path, HttpError]: Ok(Path) on success, Err(HttpError) on failure"""
        params = {"redirect": True, "primary_formats": primary_formats}
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/{order_id}/{item_id}/download",
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

    def download_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        collections: list["Collection"] | None = None,
        primary_formats: list["PrimaryFormat"] | None = None,
        redirect: Union[None, bool] = True,
        timeout: int | None = None,
    ) -> Union[OrderDownloadUrl, Any, io.BytesIO]:
        """
        Order download

        Download all the items for a specified imagery order owned by the authenticated
        user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        If NITF is specified but not available for an item, GeoTIFF will be provided instead.

        Args:
            contract_id (UUID): The contract ID.
            order_id (UUID): The order ID.
            collections (list['Collection'] | None): Specify a subset of collections to download.
                            Defaults to None, which will download only the ordered product.
                            To specify multiple collections, repeat the query parameter.

            primary_formats (list['PrimaryFormat'] | None): Specify a file format to download.
                            Defaults to geotiff, which will download without nitf.
                            To specify multiple formats, repeat the query parameter.
                            If NITF is specified but not available for an item, GeoTIFF will be provided
                instead.

            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union[OrderDownloadUrl, Any, io.BytesIO]
        """
        params = {
            "collections": collections,
            "primary_formats": primary_formats,
            "redirect": redirect,
        }
        result = self.make_request(
            method="get",
            url=f"/{contract_id}/{order_id}/download",
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
            return parse_response(response.json().unwrap(), OrderDownloadUrl)
        if response.status_code == 202:
            return response.json().unwrap()
        return response.json().unwrap()

    def download_order_to_file(
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
            url=f"/{contract_id}/{order_id}/download",
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

    def calculate_price(
        self,
        body: Union["PriceRequest", "ResellerPriceRequest"],
        contract_id: UUID,
        baseprice: Union[None, bool] = False,
        timeout: int | None = None,
    ) -> Union["OrderPrice", "ResellerOrderPrice"]:
        """
        Calculate the price of an order

        Calculate order price based on items and licence level.

        Returns base price (items × unit price) when baseprice=True, or full
        price including licence uplift when baseprice=False. Handles both
        regular and reseller order formats.

        :raises HTTPException: 422 if licence_level missing when required, or
            unknown licence requested, or reseller missing end_user_id.

        Args:
            contract_id (UUID): The contract ID.
            baseprice (Union[None, bool]): Whether to return the base price only, ignoring the licence
                level. Default: False.
            body (Union['PriceRequest', 'ResellerPriceRequest']):
                One of:
                - PriceRequest: Request payload for submitting an order.
                - ResellerPriceRequest: Request payload for calculating order price as a reseller
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union['OrderPrice', 'ResellerOrderPrice']
        """
        json_body = body.model_dump(by_alias=True, mode="json")
        params = {"baseprice": baseprice}
        result = self.make_request(
            method="post",
            url=f"/{contract_id}/price",
            json=json_body,
            params=params,
            timeout=timeout,
        )
        if result.is_err():
            raise result.error()
        response = result.unwrap()
        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), OrderPrice | ResellerOrderPrice
            )
        return response.json().unwrap()
