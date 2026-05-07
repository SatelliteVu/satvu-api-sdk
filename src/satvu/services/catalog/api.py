# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja

from collections.abc import Callable, Generator
from typing import Any, Union

from satvu.core import SDKClient, _deep_merge
from satvu.http import HttpClient
from satvu.services.catalog.models.acquisition_feature_collection import (
    AcquisitionFeatureCollection,
)
from satvu.services.catalog.models.acquisition_item import AcquisitionItem
from satvu.services.catalog.models.acquisition_queryables import AcquisitionQueryables
from satvu.services.catalog.models.catalog import Catalog
from satvu.services.catalog.models.collection import Collection
from satvu.services.catalog.models.collections import Collections
from satvu.services.catalog.models.conformance import Conformance
from satvu.services.catalog.models.feature import Feature
from satvu.services.catalog.models.feature_collection import FeatureCollection
from satvu.services.catalog.models.get_search_intersects import GetSearchIntersects
from satvu.services.catalog.models.post_collection_search_input import (
    PostCollectionSearchInput,
)
from satvu.services.catalog.models.post_search_input import PostSearchInput
from satvu.services.catalog.models.primary_feature_collection import (
    PrimaryFeatureCollection,
)
from satvu.services.catalog.models.primary_item import PrimaryItem
from satvu.services.catalog.models.primary_queryables import PrimaryQueryables
from satvu.services.catalog.models.queryables import Queryables
from satvu.services.catalog.models.search_response import SearchResponse
from satvu.services.catalog.models.stac_geometry import StacGeometry
from satvu.services.catalog.models.surface_brightness_temperature_feature_collection import (
    SurfaceBrightnessTemperatureFeatureCollection,
)
from satvu.services.catalog.models.surface_brightness_temperature_item import (
    SurfaceBrightnessTemperatureItem,
)
from satvu.services.catalog.models.surface_brightness_temperature_queryables import (
    SurfaceBrightnessTemperatureQueryables,
)
from satvu.services.catalog.models.visual_feature_collection import (
    VisualFeatureCollection,
)
from satvu.services.catalog.models.visual_item import VisualItem
from satvu.services.catalog.models.visual_queryables import VisualQueryables
from satvu.shared.parsing import parse_response


class CatalogService(SDKClient):
    base_path = "/catalog/v1"

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

    def landing_page(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> Catalog:
        """
        Landing Page

        Landing page of the API. Entrypoint to which user can access product specifications, product
        applications and API documentation.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Catalog
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Catalog)
        return response.json().unwrap()

    def get_collections(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> Collections:
        """
        Get Collections

        List STAC Collections available within the catalog.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Collections
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Collections)
        return response.json().unwrap()

    def get_collection(
        self,
        contract_id: str,
        collection_id: str,
        timeout: int | None = None,
    ) -> Collection:
        """
        Get Collection

        Retrieves the generic metadata and attributes associated with a given Collection ID within the
        catalog. To see all available Collections, please refer to GET /collections.

        Args:
            contract_id (str): Contract identifier for scoped access
            collection_id (str): Collection ID. Example: collection.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Collection
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/{collection_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Collection)
        return response.json().unwrap()

    def get_item_collection(
        self,
        contract_id: str,
        collection_id: str,
        timeout: int | None = None,
    ) -> SearchResponse:
        """
        Get Item Collection

        Retrieves the entire dataset, represented as a Feature Collection, corresponding to a specified
        Collection ID.

        Args:
            contract_id (str): Contract identifier for scoped access
            collection_id (str): Collection ID. Example: collection.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SearchResponse
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/{collection_id}/items",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), SearchResponse)
        return response.json().unwrap()

    def get_collection_queryables(
        self,
        contract_id: str,
        collection_id: str,
        timeout: int | None = None,
    ) -> Queryables:
        """
        Get Collection Queryables

        Returns the queryable properties for a specific collection. These properties can be used in CQL2
        filter expressions when searching this collection.

        Args:
            contract_id (str): Contract identifier for scoped access
            collection_id (str): Collection ID. Example: collection.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Queryables
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/{collection_id}/queryables",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Queryables)
        return response.json().unwrap()

    def get_item(
        self,
        contract_id: str,
        collection_id: str,
        item_id: str,
        timeout: int | None = None,
    ) -> Feature:
        """
        Get Item

        Retrieves a specified imagery item from a Collection within the Catalog. The item will be
        represented as a Feature dataset.

        Args:
            contract_id (str): Contract identifier for scoped access
            collection_id (str): Collection ID. Example: collection.
            item_id (str): Item ID. Example: item.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Feature
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/{collection_id}/{item_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Feature)
        return response.json().unwrap()

    def conformance(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> Conformance:
        """
        Conformance

        List of implemented conformance classes

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Conformance
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/conformance",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Conformance)
        return response.json().unwrap()

    def queryables(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> Queryables:
        """
        Queryables

        List of queryables available for CQL2 filtering. Returns global properties for cross-collection
        searches.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Queryables
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/queryables",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), Queryables)
        return response.json().unwrap()

    def get_search(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, GetSearchIntersects] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        token: Union[None, str] = None,
        timeout: int | None = None,
    ) -> FeatureCollection:
        """
        Search

        Perform a search on the Catalog with your desired filters. Results will be returned as a Feature
        Collection. Both GET and POST methods are supported for this request.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
                box. Only features that have a geometry that intersects the bounding box are selected.
                Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
                the search for items. Only Item objects in one of the provided collections will be
                searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
                section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
                item1,item2.
            intersects (Union[None, GetSearchIntersects]):
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
                ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            token (Union[None, str]): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            FeatureCollection
        """

        params = {
            "bbox": bbox,
            "collections": collections,
            "datetime": datetime_,
            "filter": filter_,
            "ids": ids,
            "intersects": intersects,
            "limit": limit,
            "sortby": sortby,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/search",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), FeatureCollection)
        return response.json().unwrap()

    def get_search_iter(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, GetSearchIntersects] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        max_pages: int | None = None,
    ) -> Generator[FeatureCollection, None, None]:
        """
        Search (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
            box. Only features that have a geometry that intersects the bounding box are selected.
            Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
            the search for items. Only Item objects in one of the provided collections will be
            searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
            section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
            item1,item2.
            intersects (Union[None, GetSearchIntersects]):
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
            ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.get_search_iter(
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

            response = self.get_search(
                contract_id=contract_id,
                bbox=bbox,
                collections=collections,
                datetime_=datetime_,
                filter_=filter_,
                ids=ids,
                intersects=intersects,
                limit=limit,
                sortby=sortby,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def post_search(
        self,
        body: Union[None, PostSearchInput],
        contract_id: str,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> FeatureCollection:
        """
        Search

        Perform a search on the Catalog with your desired filters. Results will be returned as a Feature
        Collection. Both GET and POST methods are supported for this request.

        Args:
            contract_id (str): Contract identifier for scoped access
            body (Union[None, PostSearchInput]):
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            FeatureCollection
        """

        json_body = body.model_dump(by_alias=True, mode="json") if body else None
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)

        result = self.make_request(
            method="post",
            url=f"/catalog/v1/{contract_id}/search",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), FeatureCollection)
        return response.json().unwrap()

    def post_search_iter(
        self,
        body: Union[None, PostSearchInput],
        contract_id: str,
        extra_body: dict[str, Any] | None = None,
        max_pages: int | None = None,
    ) -> Generator[FeatureCollection, None, None]:
        """
        Search (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (Union[None, PostSearchInput]):
            contract_id (str): Contract identifier for scoped access
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.post_search_iter(
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

            body_with_token = body.model_copy(update={"token": token}) if body else None
            response = self.post_search(
                body=body_with_token,
                contract_id=contract_id,
                extra_body=extra_body,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def get_acquisition_items(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        token: Union[None, str] = None,
        timeout: int | None = None,
    ) -> AcquisitionFeatureCollection:
        """
        Get acquisition Items

        Returns items from the acquisition collection. Response includes all collection-specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
                box. Only features that have a geometry that intersects the bounding box are selected.
                Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
                the search for items. Only Item objects in one of the provided collections will be
                searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
                section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
                item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
                their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
                ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            token (Union[None, str]): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            AcquisitionFeatureCollection
        """

        params = {
            "bbox": bbox,
            "collections": collections,
            "datetime": datetime_,
            "filter": filter_,
            "ids": ids,
            "intersects": intersects,
            "limit": limit,
            "sortby": sortby,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/acquisition/items",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), AcquisitionFeatureCollection
            )
        return response.json().unwrap()

    def get_acquisition_items_iter(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        max_pages: int | None = None,
    ) -> Generator[AcquisitionFeatureCollection, None, None]:
        """
        Get acquisition Items (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
            box. Only features that have a geometry that intersects the bounding box are selected.
            Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
            the search for items. Only Item objects in one of the provided collections will be
            searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
            section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
            item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
            their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
            ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.get_acquisition_items_iter(
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

            response = self.get_acquisition_items(
                contract_id=contract_id,
                bbox=bbox,
                collections=collections,
                datetime_=datetime_,
                filter_=filter_,
                ids=ids,
                intersects=intersects,
                limit=limit,
                sortby=sortby,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def get_acquisition_item(
        self,
        contract_id: str,
        item_id: str,
        timeout: int | None = None,
    ) -> AcquisitionItem:
        """
        Get acquisition Item

        Returns a specific item from the acquisition collection with all collection-specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            item_id (str): Item ID. Example: item.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            AcquisitionItem
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/acquisition/items/{item_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), AcquisitionItem)
        return response.json().unwrap()

    def get_acquisition_queryables(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> AcquisitionQueryables:
        """
        Get acquisition Queryables

        Returns the queryable properties for the acquisition collection. These properties can be used in
        CQL2 filter expressions.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            AcquisitionQueryables
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/acquisition/queryables",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), AcquisitionQueryables)
        return response.json().unwrap()

    def get_primary_items(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        token: Union[None, str] = None,
        timeout: int | None = None,
    ) -> PrimaryFeatureCollection:
        """
        Get primary Items

        Returns items from the primary collection. Response includes all collection-specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
                box. Only features that have a geometry that intersects the bounding box are selected.
                Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
                the search for items. Only Item objects in one of the provided collections will be
                searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
                section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
                item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
                their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
                ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            token (Union[None, str]): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            PrimaryFeatureCollection
        """

        params = {
            "bbox": bbox,
            "collections": collections,
            "datetime": datetime_,
            "filter": filter_,
            "ids": ids,
            "intersects": intersects,
            "limit": limit,
            "sortby": sortby,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/primary/items",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), PrimaryFeatureCollection)
        return response.json().unwrap()

    def get_primary_items_iter(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        max_pages: int | None = None,
    ) -> Generator[PrimaryFeatureCollection, None, None]:
        """
        Get primary Items (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
            box. Only features that have a geometry that intersects the bounding box are selected.
            Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
            the search for items. Only Item objects in one of the provided collections will be
            searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
            section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
            item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
            their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
            ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.get_primary_items_iter(
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

            response = self.get_primary_items(
                contract_id=contract_id,
                bbox=bbox,
                collections=collections,
                datetime_=datetime_,
                filter_=filter_,
                ids=ids,
                intersects=intersects,
                limit=limit,
                sortby=sortby,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def get_primary_item(
        self,
        contract_id: str,
        item_id: str,
        timeout: int | None = None,
    ) -> PrimaryItem:
        """
        Get primary Item

        Returns a specific item from the primary collection with all collection-specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            item_id (str): Item ID. Example: item.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            PrimaryItem
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/primary/items/{item_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), PrimaryItem)
        return response.json().unwrap()

    def get_primary_queryables(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> PrimaryQueryables:
        """
        Get primary Queryables

        Returns the queryable properties for the primary collection. These properties can be used in CQL2
        filter expressions.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            PrimaryQueryables
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/primary/queryables",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), PrimaryQueryables)
        return response.json().unwrap()

    def get_surface_brightness_temperature_items(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        token: Union[None, str] = None,
        timeout: int | None = None,
    ) -> SurfaceBrightnessTemperatureFeatureCollection:
        """
        Get surface-brightness-temperature Items

        Returns items from the surface-brightness-temperature collection. Response includes all collection-
        specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
                box. Only features that have a geometry that intersects the bounding box are selected.
                Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
                the search for items. Only Item objects in one of the provided collections will be
                searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
                section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
                item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
                their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
                ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            token (Union[None, str]): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SurfaceBrightnessTemperatureFeatureCollection
        """

        params = {
            "bbox": bbox,
            "collections": collections,
            "datetime": datetime_,
            "filter": filter_,
            "ids": ids,
            "intersects": intersects,
            "limit": limit,
            "sortby": sortby,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), SurfaceBrightnessTemperatureFeatureCollection
            )
        return response.json().unwrap()

    def get_surface_brightness_temperature_items_iter(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        max_pages: int | None = None,
    ) -> Generator[SurfaceBrightnessTemperatureFeatureCollection, None, None]:
        """
        Get surface-brightness-temperature Items (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
            box. Only features that have a geometry that intersects the bounding box are selected.
            Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
            the search for items. Only Item objects in one of the provided collections will be
            searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
            section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
            item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
            their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
            ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.get_surface_brightness_temperature_items_iter(
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

            response = self.get_surface_brightness_temperature_items(
                contract_id=contract_id,
                bbox=bbox,
                collections=collections,
                datetime_=datetime_,
                filter_=filter_,
                ids=ids,
                intersects=intersects,
                limit=limit,
                sortby=sortby,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def get_surface_brightness_temperature_item(
        self,
        contract_id: str,
        item_id: str,
        timeout: int | None = None,
    ) -> SurfaceBrightnessTemperatureItem:
        """
        Get surface-brightness-temperature Item

        Returns a specific item from the surface-brightness-temperature collection with all collection-
        specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            item_id (str): Item ID. Example: item.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SurfaceBrightnessTemperatureItem
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items/{item_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), SurfaceBrightnessTemperatureItem
            )
        return response.json().unwrap()

    def get_surface_brightness_temperature_queryables(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> SurfaceBrightnessTemperatureQueryables:
        """
        Get surface-brightness-temperature Queryables

        Returns the queryable properties for the surface-brightness-temperature collection. These properties
        can be used in CQL2 filter expressions.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SurfaceBrightnessTemperatureQueryables
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/queryables",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), SurfaceBrightnessTemperatureQueryables
            )
        return response.json().unwrap()

    def get_visual_items(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        token: Union[None, str] = None,
        timeout: int | None = None,
    ) -> VisualFeatureCollection:
        """
        Get visual Items

        Returns items from the visual collection. Response includes all collection-specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
                box. Only features that have a geometry that intersects the bounding box are selected.
                Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
                the search for items. Only Item objects in one of the provided collections will be
                searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
                section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
                item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
                their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
                ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            token (Union[None, str]): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            VisualFeatureCollection
        """

        params = {
            "bbox": bbox,
            "collections": collections,
            "datetime": datetime_,
            "filter": filter_,
            "ids": ids,
            "intersects": intersects,
            "limit": limit,
            "sortby": sortby,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/visual/items",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), VisualFeatureCollection)
        return response.json().unwrap()

    def get_visual_items_iter(
        self,
        contract_id: str,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, dict] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[None, StacGeometry] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        max_pages: int | None = None,
    ) -> Generator[VisualFeatureCollection, None, None]:
        """
        Get visual Items (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (str): Contract identifier for scoped access
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
            box. Only features that have a geometry that intersects the bounding box are selected.
            Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
            the search for items. Only Item objects in one of the provided collections will be
            searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
            section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
            item1,item2.
            intersects (Union[None, StacGeometry]): Searches items by performing intersection between
            their geometry and provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
            ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.get_visual_items_iter(
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

            response = self.get_visual_items(
                contract_id=contract_id,
                bbox=bbox,
                collections=collections,
                datetime_=datetime_,
                filter_=filter_,
                ids=ids,
                intersects=intersects,
                limit=limit,
                sortby=sortby,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def get_visual_item(
        self,
        contract_id: str,
        item_id: str,
        timeout: int | None = None,
    ) -> VisualItem:
        """
        Get visual Item

        Returns a specific item from the visual collection with all collection-specific properties.

        Args:
            contract_id (str): Contract identifier for scoped access
            item_id (str): Item ID. Example: item.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            VisualItem
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/visual/items/{item_id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), VisualItem)
        return response.json().unwrap()

    def get_visual_queryables(
        self,
        contract_id: str,
        timeout: int | None = None,
    ) -> VisualQueryables:
        """
        Get visual Queryables

        Returns the queryable properties for the visual collection. These properties can be used in CQL2
        filter expressions.

        Args:
            contract_id (str): Contract identifier for scoped access
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            VisualQueryables
        """

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/visual/queryables",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), VisualQueryables)
        return response.json().unwrap()

    def getCollectionSearch(
        self,
        contract_id: str,
        collection_id: str,
        bbox: None | str = None,
        datetime_: None | str = None,
        ids: None | str = None,
        limit: int | None = None,
        token: Union[None, str] = None,
        timeout: int | None = None,
    ) -> SearchResponse:
        """
        Search items in a specific collection

        Search for STAC items within a specific collection using query parameters. The collection is
        determined by the URL path parameter.

        Args:
            contract_id (str): Contract ID for access control
            collection_id (str): Collection ID to search within
            bbox (None | str): Bounding box filter as comma-separated floats: west,south,east,north
                Example: -90,-45,90,45.
            datetime_ (None | str): Single date+time, or a range with '/' separator, formatted to
                RFC3339. Example: 1985-04-12T23:20:50.52Z/...
            ids (None | str): Comma-separated list of Item IDs to return. Example: item1,item2.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            token (Union[None, str]): The pagination token.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SearchResponse
        """

        params = {
            "bbox": bbox,
            "datetime": datetime_,
            "ids": ids,
            "limit": limit,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url=f"/catalog/v1/{contract_id}/collections/{collection_id}/search",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), SearchResponse)
        return response.json().unwrap()

    def getCollectionSearch_iter(
        self,
        contract_id: str,
        collection_id: str,
        bbox: None | str = None,
        datetime_: None | str = None,
        ids: None | str = None,
        limit: int | None = None,
        max_pages: int | None = None,
    ) -> Generator[SearchResponse, None, None]:
        """
        Search items in a specific collection (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            contract_id (str): Contract ID for access control
            collection_id (str): Collection ID to search within
            bbox (None | str): Bounding box filter as comma-separated floats: west,south,east,north
            Example: -90,-45,90,45.
            datetime_ (None | str): Single date+time, or a range with '/' separator, formatted to
            RFC3339. Example: 1985-04-12T23:20:50.52Z/...
            ids (None | str): Comma-separated list of Item IDs to return. Example: item1,item2.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.getCollectionSearch_iter(
                contract_id=...,
                collection_id=...,
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

            response = self.getCollectionSearch(
                contract_id=contract_id,
                collection_id=collection_id,
                bbox=bbox,
                datetime_=datetime_,
                ids=ids,
                limit=limit,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def postCollectionSearch(
        self,
        body: Union[None, PostCollectionSearchInput],
        contract_id: str,
        collection_id: str,
        extra_body: dict[str, Any] | None = None,
        timeout: int | None = None,
    ) -> SearchResponse:
        """
        Search items in a specific collection

        Search for STAC items within a specific collection using a JSON request body. The collection is
        determined by the URL path parameter.

        Args:
            contract_id (str): Contract ID for access control
            collection_id (str): Collection ID to search within
            body (Union[None, PostCollectionSearchInput]):
            extra_body: Optional dict deep-merged into the request body after
                serialisation. Use this to pass fields added to the API after this
                SDK version shipped. Nested dicts merge recursively; lists and
                scalars in extra_body replace the original value.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            SearchResponse
        """

        json_body = body.model_dump(by_alias=True, mode="json") if body else None
        if extra_body:
            json_body = _deep_merge(json_body or {}, extra_body)

        result = self.make_request(
            method="post",
            url=f"/catalog/v1/{contract_id}/collections/{collection_id}/search",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), SearchResponse)
        return response.json().unwrap()

    def postCollectionSearch_iter(
        self,
        body: Union[None, PostCollectionSearchInput],
        contract_id: str,
        collection_id: str,
        extra_body: dict[str, Any] | None = None,
        max_pages: int | None = None,
    ) -> Generator[SearchResponse, None, None]:
        """
        Search items in a specific collection (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            body (Union[None, PostCollectionSearchInput]):
            contract_id (str): Contract ID for access control
            collection_id (str): Collection ID to search within
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.catalog.postCollectionSearch_iter(
                body=...,
                contract_id=...,
                collection_id=...,
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

            body_with_token = body.model_copy(update={"token": token}) if body else None
            response = self.postCollectionSearch(
                body=body_with_token,
                contract_id=contract_id,
                collection_id=collection_id,
                extra_body=extra_body,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break
