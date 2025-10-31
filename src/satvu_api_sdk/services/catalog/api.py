from collections.abc import Callable
from typing import Union
from uuid import UUID

from satvu_api_sdk.core import SDKClient
from satvu_api_sdk.services.catalog.models.catalog import Catalog
from satvu_api_sdk.services.catalog.models.collection import Collection
from satvu_api_sdk.services.catalog.models.collections import Collections
from satvu_api_sdk.services.catalog.models.conformance import Conformance
from satvu_api_sdk.services.catalog.models.cql_2_queryables_schema import (
    Cql2QueryablesSchema,
)
from satvu_api_sdk.services.catalog.models.feature import Feature
from satvu_api_sdk.services.catalog.models.feature_collection import FeatureCollection
from satvu_api_sdk.services.catalog.models.filter_ import Filter
from satvu_api_sdk.services.catalog.models.geo_json_geometry_collection_1 import (
    GeoJSONGeometryCollection1,
)
from satvu_api_sdk.services.catalog.models.geo_json_line_string import GeoJSONLineString
from satvu_api_sdk.services.catalog.models.geo_json_multi_line_string import (
    GeoJSONMultiLineString,
)
from satvu_api_sdk.services.catalog.models.geo_json_multi_point import GeoJSONMultiPoint
from satvu_api_sdk.services.catalog.models.geo_json_multi_polygon import (
    GeoJSONMultiPolygon,
)
from satvu_api_sdk.services.catalog.models.geo_json_point import GeoJSONPoint
from satvu_api_sdk.services.catalog.models.geo_json_polygon import GeoJSONPolygon
from satvu_api_sdk.services.catalog.models.post_search_input import PostSearchInput
from satvu_api_sdk.services.catalog.models.search_response import SearchResponse
from satvu_api_sdk.shared.parsing import parse_response


class CatalogService(SDKClient):
    base_path = "/catalog/v1"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def landing_page(
        self,
        contract_id: UUID,
    ) -> Catalog:
        """
        Landing Page

        Landing page of the API. Entrypoint to which user can access product specifications, product
        applications and API documentation.

        Args:
            contract_id (UUID): SatVu Contract ID

        Returns:
            Catalog
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return parse_response(response.json(), Catalog)
        return response.json()

    def conformance(
        self,
        contract_id: UUID,
    ) -> Conformance:
        """
        Conformance

        List of implemented conformance classes

        Args:
            contract_id (UUID): SatVu Contract ID

        Returns:
            Conformance
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/conformance".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return parse_response(response.json(), Conformance)
        return response.json()

    def queryables(
        self,
        contract_id: UUID,
    ) -> Cql2QueryablesSchema:
        """
        Queryables

        List of queryables available for CQL2 filtering

        Args:
            contract_id (UUID): SatVu Contract ID

        Returns:
            Cql2QueryablesSchema
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/queryables".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return parse_response(response.json(), Cql2QueryablesSchema)
        return response.json()

    def get_search(
        self,
        contract_id: UUID,
        bbox: Union[None, list[float]] = None,
        collections: Union[None, list[str]] = None,
        datetime_: None | str = None,
        filter_: Union[None, Filter] = None,
        ids: Union[None, list[str]] = None,
        intersects: Union[
            None,
            Union[
                "GeoJSONGeometryCollection1",
                "GeoJSONLineString",
                "GeoJSONMultiLineString",
                "GeoJSONMultiPoint",
                "GeoJSONMultiPolygon",
                "GeoJSONPoint",
                "GeoJSONPolygon",
            ],
        ] = None,
        limit: int | None = None,
        sortby: Union[None, list[str]] = None,
        token: Union[None, str] = None,
    ) -> FeatureCollection:
        """
        Search

        Perform a search on the Catalog with your desired filters. Results will be returned as a Feature
        Collection. Both GET and POST methods are supported for this request.

        Args:
            contract_id (UUID): SatVu Contract ID
            bbox (Union[None, list[float]]): Comma separated list of floats representing a bounding
                box. Only features that have a geometry that intersects the bounding box are selected.
                Example: -90,-45,90,45.
            collections (Union[None, list[str]]): Comma separated list of Collection IDs to include in
                the search for items. Only Item objects in one of the provided collections will be
                searched. Example: collection1,collection2.
            datetime_ (None | str): Single date+time, or a range ('/') separator, formatted to RFC3339
                section 5.6. Use double dots for open ranges. Example: 1985-04-12T23:20:50.52Z/...
            filter_ (Union[None, Filter]): Filters using Common Query Language (CQL2).
            ids (Union[None, list[str]]): Comma separated list of Item IDs to return. Example:
                item1,item2.
            intersects (Union[None, Union['GeoJSONGeometryCollection1', 'GeoJSONLineString',
                'GeoJSONMultiLineString', 'GeoJSONMultiPoint', 'GeoJSONMultiPolygon', 'GeoJSONPoint',
                'GeoJSONPolygon']]): Search for items by performing intersection between their geometry
                and a provided GeoJSON geometry.
            limit (int | None): The maximum number of results to return per page. Example: 10.
            sortby (Union[None, list[str]]): An array of property names, prefixed by either '+' for
                ascending or '-' for descending. If no prefix is provided, '-' is assumed.
            token (Union[None, str]): The pagination token.

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

        response = self.make_request(
            method="get",
            url="{contract_id}/search".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return parse_response(response.json(), FeatureCollection)
        return response.json()

    def post_search(
        self,
        body: PostSearchInput,
        contract_id: UUID,
    ) -> FeatureCollection:
        """
        Search

        Perform a search on the Catalog with your desired filters. Results will be returned as a Feature
        Collection. Both GET and POST methods are supported for this request.

        Args:
            contract_id (UUID): SatVu Contract ID
            body (PostSearchInput):

        Returns:
            FeatureCollection
        """

        json_body = body.model_dump(by_alias=True)

        response = self.make_request(
            method="post",
            url="{contract_id}/search".format(contract_id=contract_id),
            json=json_body,
        )

        if response.status_code == 200:
            return parse_response(response.json(), FeatureCollection)
        return response.json()

    def get_collections(
        self,
        contract_id: UUID,
    ) -> Collections:
        """
        Get Collections

        List STAC Collections available within the catalog.

        Args:
            contract_id (UUID): SatVu Contract ID

        Returns:
            Collections
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/collections".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return parse_response(response.json(), Collections)
        return response.json()

    def get_collection(
        self,
        contract_id: UUID,
        collection_id: str,
    ) -> Collection:
        """
        Get Collection

        Retrieves the generic metadata and attributes associated with a given Collection ID within the
        catalog. To see all available Collections, please refer to GET /collections.

        Args:
            contract_id (UUID): SatVu Contract ID
            collection_id (str): Collection ID. Example: collection.

        Returns:
            Collection
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/collections/{collection_id}".format(
                contract_id=contract_id, collection_id=collection_id
            ),
        )

        if response.status_code == 200:
            return parse_response(response.json(), Collection)
        return response.json()

    def get_item_collection(
        self,
        contract_id: UUID,
        collection_id: str,
    ) -> SearchResponse:
        """
        Get Item Collection

        Retrieves the entire dataset, represented as a Feature Collection, corresponding to a specified
        Collection ID.

        Args:
            contract_id (UUID): SatVu Contract ID
            collection_id (str): Collection ID. Example: collection.

        Returns:
            SearchResponse
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/collections/{collection_id}/items".format(
                contract_id=contract_id, collection_id=collection_id
            ),
        )

        if response.status_code == 200:
            return parse_response(response.json(), SearchResponse)
        return response.json()

    def get_item(
        self,
        contract_id: UUID,
        collection_id: str,
        item_id: str,
    ) -> Feature:
        """
        Get Item

        Retrieves a specified imagery item from a Collection within the Catalog. The item will be
        represented as a Feature dataset.

        Args:
            contract_id (UUID): SatVu Contract ID
            collection_id (str): Collection ID. Example: collection.
            item_id (str): Item ID. Example: item.

        Returns:
            Feature
        """

        response = self.make_request(
            method="get",
            url="{contract_id}/collections/{collection_id}/{item_id}".format(
                contract_id=contract_id, collection_id=collection_id, item_id=item_id
            ),
        )

        if response.status_code == 200:
            return parse_response(response.json(), Feature)
        return response.json()
