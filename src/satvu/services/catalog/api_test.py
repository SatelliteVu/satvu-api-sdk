# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for catalog service.

Generated from OpenAPI spec version 1.12.1.
Uses property-based testing with hypothesis-jsonschema.
"""

from typing import Union
from unittest.mock import Mock
from uuid import uuid4

import pook
import pytest
from hypothesis import HealthCheck, given, settings
from pydantic import TypeAdapter

from satvu import SatVuSDK, create_http_client
from satvu.http.errors import ClientError
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

from .test_schemas import get_request_body_strategy, get_response_strategy


@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestCatalogService:
    """Property-based tests for CatalogService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        mock_get_token = Mock(return_value="test_token")
        subdomain = "api"
        env_part = "qa."
        base_path = "/catalog/v1"
        self.base_url = f"https://{subdomain}.{env_part}satellitevu.com{base_path}"
        http_client = create_http_client(
            backend=backend, base_url=self.base_url, get_token=mock_get_token
        )
        self.sdk = SatVuSDK(
            client_id="test_client_id",
            client_secret="test_client_secret",
            http_client=http_client,
            env="qa",
        )
        self.sdk.catalog._get_token = mock_get_token

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy("/catalog/v1/{contract_id}", "get", "200")
    )
    def test_landing_page_200(self, backend, response_data):
        """
        Test landing_page with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.landing_page(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, Catalog)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections", "get", "200"
        )
    )
    def test_get_collections_200(self, backend, response_data):
        """
        Test get_collections with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_collections(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, Collections)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}", "get", "200"
        )
    )
    def test_get_collection_200(self, backend, response_data):
        """
        Test get_collection with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_collection(
            contract_id=contract_id, collection_id=collection_id
        )
        assert result is not None
        assert isinstance(result, Collection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}", "get", "404"
        )
    )
    def test_get_collection_404_error(self, backend, response_data):
        """
        Test get_collection with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_collection(
                contract_id=contract_id, collection_id=collection_id
            )
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/items", "get", "200"
        )
    )
    def test_get_item_collection_200(self, backend, response_data):
        """
        Test get_item_collection with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_item_collection(
            contract_id=contract_id, collection_id=collection_id
        )
        assert result is not None
        assert isinstance(result, SearchResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/queryables",
            "get",
            "200",
        )
    )
    def test_get_collection_queryables_200(self, backend, response_data):
        """
        Test get_collection_queryables with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_collection_queryables(
            contract_id=contract_id, collection_id=collection_id
        )
        assert result is not None
        assert isinstance(result, Queryables)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/queryables",
            "get",
            "404",
        )
    )
    def test_get_collection_queryables_404_error(self, backend, response_data):
        """
        Test get_collection_queryables with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_collection_queryables(
                contract_id=contract_id, collection_id=collection_id
            )
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/{item_id}",
            "get",
            "200",
        )
    )
    def test_get_item_200(self, backend, response_data):
        """
        Test get_item with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_item(
            contract_id=contract_id, collection_id=collection_id, item_id=item_id
        )
        assert result is not None
        assert isinstance(result, Feature)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/{item_id}",
            "get",
            "404",
        )
    )
    def test_get_item_404_error(self, backend, response_data):
        """
        Test get_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_item(
                contract_id=contract_id, collection_id=collection_id, item_id=item_id
            )
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/conformance", "get", "200"
        )
    )
    def test_conformance_200(self, backend, response_data):
        """
        Test conformance with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/conformance"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.conformance(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, Conformance)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/queryables", "get", "200"
        )
    )
    def test_queryables_200(self, backend, response_data):
        """
        Test queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.queryables(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, Queryables)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        )
    )
    def test_get_search_200(self, backend, response_data):
        """
        Test get_search with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_search(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, FeatureCollection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "400"
        )
    )
    def test_get_search_400_error(self, backend, response_data):
        """
        Test get_search with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_search(contract_id=contract_id)
        assert exc_info.value.status_code == 400

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        ),
        body_data=get_request_body_strategy("/catalog/v1/{contract_id}/search", "post"),
    )
    def test_post_search_200(self, backend, response_data, body_data):
        """
        Test post_search with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[None, PostSearchInput])
        body = body_adapter.validate_python(body_data)
        result = self.sdk.catalog.post_search(contract_id=contract_id, body=body)
        assert result is not None
        assert isinstance(result, FeatureCollection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "400"
        ),
        body_data=get_request_body_strategy("/catalog/v1/{contract_id}/search", "post"),
    )
    def test_post_search_400_error(self, backend, response_data, body_data):
        """
        Test post_search with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[None, PostSearchInput])
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.post_search(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 400

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        )
    )
    def test_get_acquisition_items_200(self, backend, response_data):
        """
        Test get_acquisition_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_acquisition_items(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, AcquisitionFeatureCollection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items/{item_id}",
            "get",
            "200",
        )
    )
    def test_get_acquisition_item_200(self, backend, response_data):
        """
        Test get_acquisition_item with 200 response.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/acquisition/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_acquisition_item(
            contract_id=contract_id, item_id=item_id
        )
        assert result is not None
        assert isinstance(result, AcquisitionItem)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items/{item_id}",
            "get",
            "404",
        )
    )
    def test_get_acquisition_item_404_error(self, backend, response_data):
        """
        Test get_acquisition_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/acquisition/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_acquisition_item(
                contract_id=contract_id, item_id=item_id
            )
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/queryables", "get", "200"
        )
    )
    def test_get_acquisition_queryables_200(self, backend, response_data):
        """
        Test get_acquisition_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/acquisition/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_acquisition_queryables(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, AcquisitionQueryables)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        )
    )
    def test_get_primary_items_200(self, backend, response_data):
        """
        Test get_primary_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_primary_items(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, PrimaryFeatureCollection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items/{item_id}",
            "get",
            "200",
        )
    )
    def test_get_primary_item_200(self, backend, response_data):
        """
        Test get_primary_item with 200 response.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/primary/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_primary_item(
            contract_id=contract_id, item_id=item_id
        )
        assert result is not None
        assert isinstance(result, PrimaryItem)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items/{item_id}",
            "get",
            "404",
        )
    )
    def test_get_primary_item_404_error(self, backend, response_data):
        """
        Test get_primary_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/primary/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_primary_item(contract_id=contract_id, item_id=item_id)
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/queryables", "get", "200"
        )
    )
    def test_get_primary_queryables_200(self, backend, response_data):
        """
        Test get_primary_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/primary/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_primary_queryables(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, PrimaryQueryables)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        )
    )
    def test_get_surface_brightness_temperature_items_200(self, backend, response_data):
        """
        Test get_surface_brightness_temperature_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_surface_brightness_temperature_items(
            contract_id=contract_id
        )
        assert result is not None
        assert isinstance(result, SurfaceBrightnessTemperatureFeatureCollection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items/{item_id}",
            "get",
            "200",
        )
    )
    def test_get_surface_brightness_temperature_item_200(self, backend, response_data):
        """
        Test get_surface_brightness_temperature_item with 200 response.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_surface_brightness_temperature_item(
            contract_id=contract_id, item_id=item_id
        )
        assert result is not None
        assert isinstance(result, SurfaceBrightnessTemperatureItem)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items/{item_id}",
            "get",
            "404",
        )
    )
    def test_get_surface_brightness_temperature_item_404_error(
        self, backend, response_data
    ):
        """
        Test get_surface_brightness_temperature_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_surface_brightness_temperature_item(
                contract_id=contract_id, item_id=item_id
            )
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/queryables",
            "get",
            "200",
        )
    )
    def test_get_surface_brightness_temperature_queryables_200(
        self, backend, response_data
    ):
        """
        Test get_surface_brightness_temperature_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_surface_brightness_temperature_queryables(
            contract_id=contract_id
        )
        assert result is not None
        assert isinstance(result, SurfaceBrightnessTemperatureQueryables)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        )
    )
    def test_get_visual_items_200(self, backend, response_data):
        """
        Test get_visual_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/visual/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_visual_items(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, VisualFeatureCollection)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items/{item_id}", "get", "200"
        )
    )
    def test_get_visual_item_200(self, backend, response_data):
        """
        Test get_visual_item with 200 response.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/visual/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_visual_item(
            contract_id=contract_id, item_id=item_id
        )
        assert result is not None
        assert isinstance(result, VisualItem)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items/{item_id}", "get", "404"
        )
    )
    def test_get_visual_item_404_error(self, backend, response_data):
        """
        Test get_visual_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/visual/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_visual_item(contract_id=contract_id, item_id=item_id)
        assert exc_info.value.status_code == 404

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/queryables", "get", "200"
        )
    )
    def test_get_visual_queryables_200(self, backend, response_data):
        """
        Test get_visual_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/visual/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.get_visual_queryables(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, VisualQueryables)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        )
    )
    def test_getCollectionSearch_200(self, backend, response_data):
        """
        Test getCollectionSearch with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.getCollectionSearch(
            contract_id=contract_id, collection_id=collection_id
        )
        assert result is not None
        assert isinstance(result, SearchResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        ),
        body_data=get_request_body_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "post"
        ),
    )
    def test_postCollectionSearch_200(self, backend, response_data, body_data):
        """
        Test postCollectionSearch with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[None, PostCollectionSearchInput])
        body = body_adapter.validate_python(body_data)
        result = self.sdk.catalog.postCollectionSearch(
            contract_id=contract_id, collection_id=collection_id, body=body
        )
        assert result is not None
        assert isinstance(result, SearchResponse)

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        ),
    )
    def test_get_search_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_search_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pages = list(self.sdk.catalog.get_search_iter(contract_id=contract_id))
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        ),
    )
    def test_get_search_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_search_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_search_iter(contract_id=contract_id, max_pages=2)
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "get", "200"
        )
    )
    def test_get_search_iter_no_next_link(self, backend, page_data):
        """Test get_search_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        pages = list(self.sdk.catalog.get_search_iter(contract_id=contract_id))
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        ),
    )
    def test_post_search_iter_pagination(self, backend, page1_data, page2_data):
        """Test post_search_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        body = PostSearchInput()
        pages = list(
            self.sdk.catalog.post_search_iter(body=body, contract_id=contract_id)
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        ),
    )
    def test_post_search_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test post_search_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        body = PostSearchInput()
        pages = list(
            self.sdk.catalog.post_search_iter(
                body=body, contract_id=contract_id, max_pages=2
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/search", "post", "200"
        )
    )
    def test_post_search_iter_no_next_link(self, backend, page_data):
        """Test post_search_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/search"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.post(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        body = PostSearchInput()
        pages = list(
            self.sdk.catalog.post_search_iter(body=body, contract_id=contract_id)
        )
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        ),
    )
    def test_get_acquisition_items_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test get_acquisition_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_acquisition_items_iter(contract_id=contract_id)
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        ),
    )
    def test_get_acquisition_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_acquisition_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_acquisition_items_iter(
                contract_id=contract_id, max_pages=2
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/acquisition/items", "get", "200"
        )
    )
    def test_get_acquisition_items_iter_no_next_link(self, backend, page_data):
        """Test get_acquisition_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_acquisition_items_iter(contract_id=contract_id)
        )
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        ),
    )
    def test_get_primary_items_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_primary_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pages = list(self.sdk.catalog.get_primary_items_iter(contract_id=contract_id))
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        ),
    )
    def test_get_primary_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_primary_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_primary_items_iter(
                contract_id=contract_id, max_pages=2
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/primary/items", "get", "200"
        )
    )
    def test_get_primary_items_iter_no_next_link(self, backend, page_data):
        """Test get_primary_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        pages = list(self.sdk.catalog.get_primary_items_iter(contract_id=contract_id))
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
    )
    def test_get_surface_brightness_temperature_items_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test get_surface_brightness_temperature_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_surface_brightness_temperature_items_iter(
                contract_id=contract_id
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
    )
    def test_get_surface_brightness_temperature_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_surface_brightness_temperature_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_surface_brightness_temperature_items_iter(
                contract_id=contract_id, max_pages=2
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        )
    )
    def test_get_surface_brightness_temperature_items_iter_no_next_link(
        self, backend, page_data
    ):
        """Test get_surface_brightness_temperature_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_surface_brightness_temperature_items_iter(
                contract_id=contract_id
            )
        )
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        ),
    )
    def test_get_visual_items_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_visual_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/visual/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pages = list(self.sdk.catalog.get_visual_items_iter(contract_id=contract_id))
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        ),
    )
    def test_get_visual_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_visual_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/visual/items"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.get_visual_items_iter(contract_id=contract_id, max_pages=2)
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/visual/items", "get", "200"
        )
    )
    def test_get_visual_items_iter_no_next_link(self, backend, page_data):
        """Test get_visual_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/visual/items"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        pages = list(self.sdk.catalog.get_visual_items_iter(contract_id=contract_id))
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
    )
    def test_getCollectionSearch_iter_pagination(self, backend, page1_data, page2_data):
        """Test getCollectionSearch_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.getCollectionSearch_iter(
                contract_id=contract_id, collection_id=collection_id
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
    )
    def test_getCollectionSearch_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test getCollectionSearch_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.get(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.getCollectionSearch_iter(
                contract_id=contract_id, collection_id=collection_id, max_pages=2
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search", "get", "200"
        )
    )
    def test_getCollectionSearch_iter_no_next_link(self, backend, page_data):
        """Test getCollectionSearch_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.get(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        pages = list(
            self.sdk.catalog.getCollectionSearch_iter(
                contract_id=contract_id, collection_id=collection_id
            )
        )
        assert len(pages) == 1

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        ),
    )
    def test_postCollectionSearch_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test postCollectionSearch_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=abc123",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = []
        pook.reset()
        pook.on()
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        body = PostCollectionSearchInput()
        pages = list(
            self.sdk.catalog.postCollectionSearch_iter(
                body=body, contract_id=contract_id, collection_id=collection_id
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page1_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        ),
        page2_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        ),
        page3_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        ),
    )
    def test_postCollectionSearch_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test postCollectionSearch_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        page1_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token1",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page2_data["links"] = [
            {
                "rel": "next",
                "href": f"{url}?token=token2",
                "method": "GET",
                "title": "next",
                "type": "application/json",
            }
        ]
        page3_data["links"] = []
        pook.reset()
        pook.on()
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        body = PostCollectionSearchInput()
        pages = list(
            self.sdk.catalog.postCollectionSearch_iter(
                body=body,
                contract_id=contract_id,
                collection_id=collection_id,
                max_pages=2,
            )
        )
        assert len(pages) == 2

    @settings(
        max_examples=3,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        page_data=get_response_strategy(
            "/catalog/v1/{contract_id}/collections/{collection_id}/search",
            "post",
            "200",
        )
    )
    def test_postCollectionSearch_iter_no_next_link(self, backend, page_data):
        """Test postCollectionSearch_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/catalog/v1/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        page_data["links"] = [
            {
                "rel": "self",
                "href": url,
                "method": "GET",
                "title": "self",
                "type": "application/json",
            }
        ]
        pook.reset()
        pook.on()
        pook.post(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        body = PostCollectionSearchInput()
        pages = list(
            self.sdk.catalog.postCollectionSearch_iter(
                body=body, contract_id=contract_id, collection_id=collection_id
            )
        )
        assert len(pages) == 1
