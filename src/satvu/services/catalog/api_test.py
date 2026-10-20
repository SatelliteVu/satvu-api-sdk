# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for catalog service.

Generated from OpenAPI spec version v1.
Uses property-based testing with hypothesis-jsonschema.
"""

from contextlib import suppress
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
from satvu.services.catalog.models.collection_search_json_input import (
    CollectionSearchJsonInput,
)
from satvu.services.catalog.models.collections import Collections
from satvu.services.catalog.models.conformance import Conformance
from satvu.services.catalog.models.feature import Feature
from satvu.services.catalog.models.feature_collection import FeatureCollection
from satvu.services.catalog.models.primary_feature_collection import (
    PrimaryFeatureCollection,
)
from satvu.services.catalog.models.primary_item import PrimaryItem
from satvu.services.catalog.models.primary_queryables import PrimaryQueryables
from satvu.services.catalog.models.queryables import Queryables
from satvu.services.catalog.models.search_json_input import SearchJsonInput
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
from satvu.services.schema_conformance import (
    assert_request_body_conforms,
    assert_request_body_matches_input,
    drop_optional_properties,
)

from .test_schemas import (
    get_request_body_schema,
    get_request_body_strategy,
    get_response_strategy,
)


@pytest.mark.parametrize(
    "backend", ["stdlib", "httpx", "httpx2", "urllib3", "requests"]
)
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
    @given(response_data=get_response_strategy("/{contract_id}", "get", "200"))
    def test_landing_page_200(self, backend, response_data):
        """
        Test landing_page with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}"
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
    @given(response_data=get_response_strategy("/{contract_id}", "get", "429"))
    def test_landing_page_429_error(self, backend, response_data):
        """
        Test landing_page with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.landing_page(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
        response_data=get_response_strategy("/{contract_id}/collections", "get", "200")
    )
    def test_list_collections_200(self, backend, response_data):
        """
        Test list_collections with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_collections(contract_id=contract_id)
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
        response_data=get_response_strategy("/{contract_id}/collections", "get", "429")
    )
    def test_list_collections_429_error(self, backend, response_data):
        """
        Test list_collections with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_collections(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}", "get", "200"
        )
    )
    def test_get_collection_200(self, backend, response_data):
        """
        Test get_collection with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}"
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
            "/{contract_id}/collections/{collection_id}", "get", "404"
        )
    )
    def test_get_collection_404_error(self, backend, response_data):
        """
        Test get_collection with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}"
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
            "/{contract_id}/collections/{collection_id}", "get", "429"
        )
    )
    def test_get_collection_429_error(self, backend, response_data):
        """
        Test get_collection with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_collection(
                contract_id=contract_id, collection_id=collection_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        )
    )
    def test_list_collection_items_200(self, backend, response_data):
        """
        Test list_collection_items with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_collection_items(
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
            "/{contract_id}/collections/{collection_id}/items", "get", "400"
        )
    )
    def test_list_collection_items_400_error(self, backend, response_data):
        """
        Test list_collection_items with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_collection_items(
                contract_id=contract_id, collection_id=collection_id
            )
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
            "/{contract_id}/collections/{collection_id}/items", "get", "429"
        )
    )
    def test_list_collection_items_429_error(self, backend, response_data):
        """
        Test list_collection_items with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_collection_items(
                contract_id=contract_id, collection_id=collection_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}/queryables", "get", "200"
        )
    )
    def test_list_collection_queryables_200(self, backend, response_data):
        """
        Test list_collection_queryables with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_collection_queryables(
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
            "/{contract_id}/collections/{collection_id}/queryables", "get", "404"
        )
    )
    def test_list_collection_queryables_404_error(self, backend, response_data):
        """
        Test list_collection_queryables with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_collection_queryables(
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
            "/{contract_id}/collections/{collection_id}/queryables", "get", "429"
        )
    )
    def test_list_collection_queryables_429_error(self, backend, response_data):
        """
        Test list_collection_queryables with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_collection_queryables(
                contract_id=contract_id, collection_id=collection_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}/{item_id}", "get", "200"
        )
    )
    def test_get_item_200(self, backend, response_data):
        """
        Test get_item with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/{item_id}"
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
            "/{contract_id}/collections/{collection_id}/{item_id}", "get", "404"
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
        path = f"/{contract_id}/collections/{collection_id}/{item_id}"
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
            "/{contract_id}/collections/{collection_id}/{item_id}", "get", "429"
        )
    )
    def test_get_item_429_error(self, backend, response_data):
        """
        Test get_item with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_item(
                contract_id=contract_id, collection_id=collection_id, item_id=item_id
            )
        assert exc_info.value.status_code == 429

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
        response_data=get_response_strategy("/{contract_id}/conformance", "get", "200")
    )
    def test_list_conformance_classes_200(self, backend, response_data):
        """
        Test list_conformance_classes with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/conformance"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_conformance_classes(contract_id=contract_id)
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
        response_data=get_response_strategy("/{contract_id}/conformance", "get", "429")
    )
    def test_list_conformance_classes_429_error(self, backend, response_data):
        """
        Test list_conformance_classes with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/conformance"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_conformance_classes(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
        response_data=get_response_strategy("/{contract_id}/queryables", "get", "200")
    )
    def test_list_queryables_200(self, backend, response_data):
        """
        Test list_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_queryables(contract_id=contract_id)
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
        response_data=get_response_strategy("/{contract_id}/queryables", "get", "429")
    )
    def test_list_queryables_429_error(self, backend, response_data):
        """
        Test list_queryables with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_queryables(contract_id=contract_id)
        assert exc_info.value.status_code == 429

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/{contract_id}/search", "get", "200"))
    def test_search_text_200(self, backend, response_data):
        """
        Test search_text with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.search_text(contract_id=contract_id)
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
    @given(response_data=get_response_strategy("/{contract_id}/search", "get", "400"))
    def test_search_text_400_error(self, backend, response_data):
        """
        Test search_text with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.search_text(contract_id=contract_id)
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
    @given(response_data=get_response_strategy("/{contract_id}/search", "get", "429"))
    def test_search_text_429_error(self, backend, response_data):
        """
        Test search_text with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.search_text(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
        response_data=get_response_strategy("/{contract_id}/search", "post", "200"),
        body_data=get_request_body_strategy("/{contract_id}/search", "post"),
    )
    def test_search_json_200(self, backend, response_data, body_data):
        """
        Test search_json with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body_adapter = TypeAdapter(Union[None, SearchJsonInput])
        body = body_adapter.validate_python(body_data)
        result = self.sdk.catalog.search_json(contract_id=contract_id, body=body)
        assert_request_body_matches_input(mock, body_data, "POST /{contract_id}/search")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/search", "post"),
            "POST /{contract_id}/search",
            body_data,
        )
        assert result is not None
        assert isinstance(result, FeatureCollection)

    @settings(
        max_examples=5,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy("/{contract_id}/search", "post", "200"),
        body_data=get_request_body_strategy("/{contract_id}/search", "post"),
    )
    def test_search_json_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test search_json sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/{contract_id}/search", "post")
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body_adapter = TypeAdapter(Union[None, SearchJsonInput])
        body = body_adapter.validate_python(body_data)
        with suppress(Exception):
            self.sdk.catalog.search_json(contract_id=contract_id, body=body)
        assert_request_body_matches_input(mock, body_data, "POST /{contract_id}/search")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/search", "post"),
            "POST /{contract_id}/search",
            body_data,
        )

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
        response_data=get_response_strategy("/{contract_id}/search", "post", "400"),
        body_data=get_request_body_strategy("/{contract_id}/search", "post"),
    )
    def test_search_json_400_error(self, backend, response_data, body_data):
        """
        Test search_json with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[None, SearchJsonInput])
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.search_json(contract_id=contract_id, body=body)
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
        response_data=get_response_strategy("/{contract_id}/search", "post", "429"),
        body_data=get_request_body_strategy("/{contract_id}/search", "post"),
    )
    def test_search_json_429_error(self, backend, response_data, body_data):
        """
        Test search_json with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[None, SearchJsonInput])
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.search_json(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/acquisition/items", "get", "200"
        )
    )
    def test_list_acquisition_items_200(self, backend, response_data):
        """
        Test list_acquisition_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_acquisition_items(contract_id=contract_id)
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
            "/{contract_id}/collections/acquisition/items", "get", "400"
        )
    )
    def test_list_acquisition_items_400_error(self, backend, response_data):
        """
        Test list_acquisition_items with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_acquisition_items(contract_id=contract_id)
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
            "/{contract_id}/collections/acquisition/items", "get", "429"
        )
    )
    def test_list_acquisition_items_429_error(self, backend, response_data):
        """
        Test list_acquisition_items with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_acquisition_items(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/acquisition/items/{item_id}", "get", "200"
        )
    )
    def test_get_acquisition_item_200(self, backend, response_data):
        """
        Test get_acquisition_item with 200 response.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/items/{item_id}"
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
            "/{contract_id}/collections/acquisition/items/{item_id}", "get", "404"
        )
    )
    def test_get_acquisition_item_404_error(self, backend, response_data):
        """
        Test get_acquisition_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/items/{item_id}"
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
            "/{contract_id}/collections/acquisition/items/{item_id}", "get", "429"
        )
    )
    def test_get_acquisition_item_429_error(self, backend, response_data):
        """
        Test get_acquisition_item with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_acquisition_item(
                contract_id=contract_id, item_id=item_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/acquisition/queryables", "get", "200"
        )
    )
    def test_list_acquisition_queryables_200(self, backend, response_data):
        """
        Test list_acquisition_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_acquisition_queryables(contract_id=contract_id)
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
            "/{contract_id}/collections/acquisition/queryables", "get", "429"
        )
    )
    def test_list_acquisition_queryables_429_error(self, backend, response_data):
        """
        Test list_acquisition_queryables with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/acquisition/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_acquisition_queryables(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/primary/items", "get", "200"
        )
    )
    def test_list_primary_items_200(self, backend, response_data):
        """
        Test list_primary_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_primary_items(contract_id=contract_id)
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
            "/{contract_id}/collections/primary/items", "get", "400"
        )
    )
    def test_list_primary_items_400_error(self, backend, response_data):
        """
        Test list_primary_items with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_primary_items(contract_id=contract_id)
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
            "/{contract_id}/collections/primary/items", "get", "429"
        )
    )
    def test_list_primary_items_429_error(self, backend, response_data):
        """
        Test list_primary_items with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/primary/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_primary_items(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/primary/items/{item_id}", "get", "200"
        )
    )
    def test_get_primary_item_200(self, backend, response_data):
        """
        Test get_primary_item with 200 response.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/primary/items/{item_id}"
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
            "/{contract_id}/collections/primary/items/{item_id}", "get", "404"
        )
    )
    def test_get_primary_item_404_error(self, backend, response_data):
        """
        Test get_primary_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/primary/items/{item_id}"
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
            "/{contract_id}/collections/primary/items/{item_id}", "get", "429"
        )
    )
    def test_get_primary_item_429_error(self, backend, response_data):
        """
        Test get_primary_item with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/collections/primary/items/{item_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_primary_item(contract_id=contract_id, item_id=item_id)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/primary/queryables", "get", "200"
        )
    )
    def test_list_primary_queryables_200(self, backend, response_data):
        """
        Test list_primary_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/primary/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_primary_queryables(contract_id=contract_id)
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
            "/{contract_id}/collections/primary/queryables", "get", "429"
        )
    )
    def test_list_primary_queryables_429_error(self, backend, response_data):
        """
        Test list_primary_queryables with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/primary/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_primary_queryables(contract_id=contract_id)
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        )
    )
    def test_list_surface_brightness_temperature_items_200(
        self, backend, response_data
    ):
        """
        Test list_surface_brightness_temperature_items with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_surface_brightness_temperature_items(
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
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "400",
        )
    )
    def test_list_surface_brightness_temperature_items_400_error(
        self, backend, response_data
    ):
        """
        Test list_surface_brightness_temperature_items with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_surface_brightness_temperature_items(
                contract_id=contract_id
            )
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
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "429",
        )
    )
    def test_list_surface_brightness_temperature_items_429_error(
        self, backend, response_data
    ):
        """
        Test list_surface_brightness_temperature_items with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/surface-brightness-temperature/items"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_surface_brightness_temperature_items(
                contract_id=contract_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/surface-brightness-temperature/items/{item_id}",
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
        path = (
            f"/{contract_id}/collections/surface-brightness-temperature/items/{item_id}"
        )
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
            "/{contract_id}/collections/surface-brightness-temperature/items/{item_id}",
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
        path = (
            f"/{contract_id}/collections/surface-brightness-temperature/items/{item_id}"
        )
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
            "/{contract_id}/collections/surface-brightness-temperature/items/{item_id}",
            "get",
            "429",
        )
    )
    def test_get_surface_brightness_temperature_item_429_error(
        self, backend, response_data
    ):
        """
        Test get_surface_brightness_temperature_item with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        item_id = uuid4()
        path = (
            f"/{contract_id}/collections/surface-brightness-temperature/items/{item_id}"
        )
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.get_surface_brightness_temperature_item(
                contract_id=contract_id, item_id=item_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/surface-brightness-temperature/queryables",
            "get",
            "200",
        )
    )
    def test_list_surface_brightness_temperature_queryables_200(
        self, backend, response_data
    ):
        """
        Test list_surface_brightness_temperature_queryables with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/surface-brightness-temperature/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.list_surface_brightness_temperature_queryables(
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
            "/{contract_id}/collections/surface-brightness-temperature/queryables",
            "get",
            "429",
        )
    )
    def test_list_surface_brightness_temperature_queryables_429_error(
        self, backend, response_data
    ):
        """
        Test list_surface_brightness_temperature_queryables with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/collections/surface-brightness-temperature/queryables"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.list_surface_brightness_temperature_queryables(
                contract_id=contract_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        )
    )
    def test_collection_search_text_200(self, backend, response_data):
        """
        Test collection_search_text with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.catalog.collection_search_text(
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
            "/{contract_id}/collections/{collection_id}/search", "get", "429"
        )
    )
    def test_collection_search_text_429_error(self, backend, response_data):
        """
        Test collection_search_text with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.collection_search_text(
                contract_id=contract_id, collection_id=collection_id
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post"
        ),
    )
    def test_collection_search_json_200(self, backend, response_data, body_data):
        """
        Test collection_search_json with 200 response.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body_adapter = TypeAdapter(Union[None, CollectionSearchJsonInput])
        body = body_adapter.validate_python(body_data)
        result = self.sdk.catalog.collection_search_json(
            contract_id=contract_id, collection_id=collection_id, body=body
        )
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/collections/{collection_id}/search"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/collections/{collection_id}/search", "post"
            ),
            "POST /{contract_id}/collections/{collection_id}/search",
            body_data,
        )
        assert result is not None
        assert isinstance(result, SearchResponse)

    @settings(
        max_examples=5,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(
        response_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post"
        ),
    )
    def test_collection_search_json_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test collection_search_json sends no field the caller left unset.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema(
                "/{contract_id}/collections/{collection_id}/search", "post"
            ),
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body_adapter = TypeAdapter(Union[None, CollectionSearchJsonInput])
        body = body_adapter.validate_python(body_data)
        with suppress(Exception):
            self.sdk.catalog.collection_search_json(
                contract_id=contract_id, collection_id=collection_id, body=body
            )
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/collections/{collection_id}/search"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/collections/{collection_id}/search", "post"
            ),
            "POST /{contract_id}/collections/{collection_id}/search",
            body_data,
        )

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
            "/{contract_id}/collections/{collection_id}/search", "post", "429"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post"
        ),
    )
    def test_collection_search_json_429_error(self, backend, response_data, body_data):
        """
        Test collection_search_json with 429 error response.

        HTTP 429 errors raise ClientError.
        """
        contract_id = uuid4()
        collection_id = uuid4()
        path = f"/{contract_id}/collections/{collection_id}/search"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(429).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[None, CollectionSearchJsonInput])
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.catalog.collection_search_json(
                contract_id=contract_id, collection_id=collection_id, body=body
            )
        assert exc_info.value.status_code == 429

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
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        ),
    )
    def test_list_collection_items_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test list_collection_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/items"
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
            self.sdk.catalog.list_collection_items_iter(
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
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        ),
    )
    def test_list_collection_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test list_collection_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/items"
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
            self.sdk.catalog.list_collection_items_iter(
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
            "/{contract_id}/collections/{collection_id}/items", "get", "200"
        )
    )
    def test_list_collection_items_iter_no_next_link(self, backend, page_data):
        """Test list_collection_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/items"
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
            self.sdk.catalog.list_collection_items_iter(
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
        page1_data=get_response_strategy("/{contract_id}/search", "get", "200"),
        page2_data=get_response_strategy("/{contract_id}/search", "get", "200"),
    )
    def test_search_text_iter_pagination(self, backend, page1_data, page2_data):
        """Test search_text_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/search"
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
        pages = list(self.sdk.catalog.search_text_iter(contract_id=contract_id))
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
        page1_data=get_response_strategy("/{contract_id}/search", "get", "200"),
        page2_data=get_response_strategy("/{contract_id}/search", "get", "200"),
        page3_data=get_response_strategy("/{contract_id}/search", "get", "200"),
    )
    def test_search_text_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test search_text_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/search"
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
            self.sdk.catalog.search_text_iter(contract_id=contract_id, max_pages=2)
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
    @given(page_data=get_response_strategy("/{contract_id}/search", "get", "200"))
    def test_search_text_iter_no_next_link(self, backend, page_data):
        """Test search_text_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/search"
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
        pages = list(self.sdk.catalog.search_text_iter(contract_id=contract_id))
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
        page1_data=get_response_strategy("/{contract_id}/search", "post", "200"),
        page2_data=get_response_strategy("/{contract_id}/search", "post", "200"),
    )
    def test_search_json_iter_pagination(self, backend, page1_data, page2_data):
        """Test search_json_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/search"
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
        body = SearchJsonInput()
        pages = list(
            self.sdk.catalog.search_json_iter(body=body, contract_id=contract_id)
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
        page1_data=get_response_strategy("/{contract_id}/search", "post", "200"),
        page2_data=get_response_strategy("/{contract_id}/search", "post", "200"),
        page3_data=get_response_strategy("/{contract_id}/search", "post", "200"),
    )
    def test_search_json_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test search_json_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/search"
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
        body = SearchJsonInput()
        pages = list(
            self.sdk.catalog.search_json_iter(
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
    @given(page_data=get_response_strategy("/{contract_id}/search", "post", "200"))
    def test_search_json_iter_no_next_link(self, backend, page_data):
        """Test search_json_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/search"
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
        body = SearchJsonInput()
        pages = list(
            self.sdk.catalog.search_json_iter(body=body, contract_id=contract_id)
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
            "/{contract_id}/collections/acquisition/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/acquisition/items", "get", "200"
        ),
    )
    def test_list_acquisition_items_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test list_acquisition_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/acquisition/items"
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
            self.sdk.catalog.list_acquisition_items_iter(contract_id=contract_id)
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
            "/{contract_id}/collections/acquisition/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/acquisition/items", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/collections/acquisition/items", "get", "200"
        ),
    )
    def test_list_acquisition_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test list_acquisition_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/acquisition/items"
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
            self.sdk.catalog.list_acquisition_items_iter(
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
            "/{contract_id}/collections/acquisition/items", "get", "200"
        )
    )
    def test_list_acquisition_items_iter_no_next_link(self, backend, page_data):
        """Test list_acquisition_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/acquisition/items"
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
            self.sdk.catalog.list_acquisition_items_iter(contract_id=contract_id)
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
            "/{contract_id}/collections/primary/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/primary/items", "get", "200"
        ),
    )
    def test_list_primary_items_iter_pagination(self, backend, page1_data, page2_data):
        """Test list_primary_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/primary/items"
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
        pages = list(self.sdk.catalog.list_primary_items_iter(contract_id=contract_id))
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
            "/{contract_id}/collections/primary/items", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/primary/items", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/collections/primary/items", "get", "200"
        ),
    )
    def test_list_primary_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test list_primary_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/primary/items"
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
            self.sdk.catalog.list_primary_items_iter(
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
            "/{contract_id}/collections/primary/items", "get", "200"
        )
    )
    def test_list_primary_items_iter_no_next_link(self, backend, page_data):
        """Test list_primary_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/primary/items"
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
        pages = list(self.sdk.catalog.list_primary_items_iter(contract_id=contract_id))
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
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
    )
    def test_list_surface_brightness_temperature_items_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test list_surface_brightness_temperature_items_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/surface-brightness-temperature/items"
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
            self.sdk.catalog.list_surface_brightness_temperature_items_iter(
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
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        ),
    )
    def test_list_surface_brightness_temperature_items_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test list_surface_brightness_temperature_items_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/surface-brightness-temperature/items"
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
            self.sdk.catalog.list_surface_brightness_temperature_items_iter(
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
            "/{contract_id}/collections/surface-brightness-temperature/items",
            "get",
            "200",
        )
    )
    def test_list_surface_brightness_temperature_items_iter_no_next_link(
        self, backend, page_data
    ):
        """Test list_surface_brightness_temperature_items_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        path = f"/{contract_id}/collections/surface-brightness-temperature/items"
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
            self.sdk.catalog.list_surface_brightness_temperature_items_iter(
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
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
    )
    def test_collection_search_text_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test collection_search_text_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/search"
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
            self.sdk.catalog.collection_search_text_iter(
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
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        ),
    )
    def test_collection_search_text_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test collection_search_text_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/search"
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
            self.sdk.catalog.collection_search_text_iter(
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
            "/{contract_id}/collections/{collection_id}/search", "get", "200"
        )
    )
    def test_collection_search_text_iter_no_next_link(self, backend, page_data):
        """Test collection_search_text_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/search"
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
            self.sdk.catalog.collection_search_text_iter(
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
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
    )
    def test_collection_search_json_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test collection_search_json_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/search"
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
        body = CollectionSearchJsonInput()
        pages = list(
            self.sdk.catalog.collection_search_json_iter(
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
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        ),
    )
    def test_collection_search_json_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test collection_search_json_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/search"
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
        body = CollectionSearchJsonInput()
        pages = list(
            self.sdk.catalog.collection_search_json_iter(
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
            "/{contract_id}/collections/{collection_id}/search", "post", "200"
        )
    )
    def test_collection_search_json_iter_no_next_link(self, backend, page_data):
        """Test collection_search_json_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = str(uuid4())
        collection_id = str(uuid4())
        path = f"/{contract_id}/collections/{collection_id}/search"
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
        body = CollectionSearchJsonInput()
        pages = list(
            self.sdk.catalog.collection_search_json_iter(
                body=body, contract_id=contract_id, collection_id=collection_id
            )
        )
        assert len(pages) == 1
