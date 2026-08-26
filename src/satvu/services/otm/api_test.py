# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for otm service.

Generated from OpenAPI spec version v2.
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
from satvu.http.errors import ClientError, ServerError
from satvu.services.otm.models.assured_order_request import AssuredOrderRequest
from satvu.services.otm.models.download_pending import DownloadPending
from satvu.services.otm.models.edit_order_payload import EditOrderPayload
from satvu.services.otm.models.edit_series_properties import EditSeriesProperties
from satvu.services.otm.models.feasibility_request import FeasibilityRequest
from satvu.services.otm.models.feasibility_response import FeasibilityResponse
from satvu.services.otm.models.get_order_response import GetOrderResponse
from satvu.services.otm.models.list_order_tasks_response import ListOrderTasksResponse
from satvu.services.otm.models.list_order_tasks_unavailable_response import (
    ListOrderTasksUnavailableResponse,
)
from satvu.services.otm.models.list_series_response import ListSeriesResponse
from satvu.services.otm.models.list_stored_orders_response import (
    ListStoredOrdersResponse,
)
from satvu.services.otm.models.list_stored_orders_response_1 import (
    ListStoredOrdersResponse1,
)
from satvu.services.otm.models.modify_feasibility_request import (
    ModifyFeasibilityRequest,
)
from satvu.services.otm.models.order_item_download_url import OrderItemDownloadUrl
from satvu.services.otm.models.order_modification_price import OrderModificationPrice
from satvu.services.otm.models.order_price import OrderPrice
from satvu.services.otm.models.price_request import PriceRequest
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
from satvu.services.otm.models.series_price_response import SeriesPriceResponse
from satvu.services.otm.models.series_request import SeriesRequest
from satvu.services.otm.models.stac_feature import StacFeature
from satvu.services.otm.models.standard_order_request import StandardOrderRequest
from satvu.services.otm.models.stored_feasibility_feature_collection import (
    StoredFeasibilityFeatureCollection,
)
from satvu.services.otm.models.stored_feasibility_request import (
    StoredFeasibilityRequest,
)
from satvu.services.otm.models.stored_order_response import StoredOrderResponse
from satvu.services.otm.models.stored_series_response import StoredSeriesResponse
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


@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestOtmService:
    """Property-based tests for OtmService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        mock_get_token = Mock(return_value="test_token")
        subdomain = "api"
        env_part = "qa."
        base_path = "/otm/v2"
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
        self.sdk.otm._get_token = mock_get_token

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
            "/{contract_id}/tasking/orders/", "get", "200"
        )
    )
    def test_get_tasking_orders_200(self, backend, response_data):
        """
        Test get_tasking_orders with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_orders(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, ListStoredOrdersResponse1)

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
            "/{contract_id}/tasking/orders/", "get", "422"
        )
    )
    def test_get_tasking_orders_422_error(self, backend, response_data):
        """
        Test get_tasking_orders with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_orders(contract_id=contract_id)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/", "post", "201"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_201(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 201 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(201).json(response_data).header("Content-Type", "application/json")
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        result = self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/orders/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/orders/", "post"),
            "POST /{contract_id}/tasking/orders/",
            body_data,
        )
        assert result is not None
        assert isinstance(result, (ResellerStoredOrderResponse, StoredOrderResponse))

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
            "/{contract_id}/tasking/orders/", "post", "201"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_orders sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/{contract_id}/tasking/orders/", "post")
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(201).json(response_data).header("Content-Type", "application/json")
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with suppress(Exception):
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/orders/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/orders/", "post"),
            "POST /{contract_id}/tasking/orders/",
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
            "/{contract_id}/tasking/orders/", "post", "400"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_400_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
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
            "/{contract_id}/tasking/orders/", "post", "402"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_402_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 402 error response.

        HTTP 402 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(402).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 402

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
            "/{contract_id}/tasking/orders/", "post", "403"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_403_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 403

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
            "/{contract_id}/tasking/orders/", "post", "409"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_409_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 409

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
            "/{contract_id}/tasking/orders/", "post", "422"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_422_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/", "post", "500"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_500_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 500 error response.

        HTTP 500 errors raise ServerError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(500).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ServerError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 500

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
            "/{contract_id}/tasking/orders/", "post", "503"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/orders/", "post"),
    )
    def test_post_tasking_orders_503_error(self, backend, response_data, body_data):
        """
        Test post_tasking_orders with 503 error response.

        HTTP 503 errors raise ServerError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(503).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[
                AssuredOrderRequest,
                ResellerAssuredOrderRequest,
                ResellerStandardOrderRequest,
                StandardOrderRequest,
            ]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ServerError) as exc_info:
            self.sdk.otm.post_tasking_orders(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 503

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
            "/{contract_id}/tasking/orders/{order_id}", "get", "200"
        )
    )
    def test_get_tasking_order_200(self, backend, response_data):
        """
        Test get_tasking_order with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_order(
            contract_id=contract_id, order_id=order_id
        )
        assert result is not None
        assert isinstance(result, (GetOrderResponse, ResellerGetOrderResponse))

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
            "/{contract_id}/tasking/orders/{order_id}", "get", "404"
        )
    )
    def test_get_tasking_order_404_error(self, backend, response_data):
        """
        Test get_tasking_order with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_order(contract_id=contract_id, order_id=order_id)
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
            "/{contract_id}/tasking/orders/{order_id}", "get", "422"
        )
    )
    def test_get_tasking_order_422_error(self, backend, response_data):
        """
        Test get_tasking_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_order(contract_id=contract_id, order_id=order_id)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/{order_id}", "patch", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/orders/{order_id}", "patch"
        ),
    )
    def test_edit_tasking_order_200(self, backend, response_data, body_data):
        """
        Test edit_tasking_order with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.patch(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditOrderPayload.model_validate(body_data)
        result = self.sdk.otm.edit_tasking_order(
            contract_id=contract_id, order_id=order_id, body=body
        )
        assert_request_body_matches_input(
            mock, body_data, "PATCH /{contract_id}/tasking/orders/{order_id}"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/tasking/orders/{order_id}", "patch"
            ),
            "PATCH /{contract_id}/tasking/orders/{order_id}",
            body_data,
        )
        assert result is not None
        assert isinstance(result, (GetOrderResponse, ResellerGetOrderResponse))

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
            "/{contract_id}/tasking/orders/{order_id}", "patch", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/orders/{order_id}", "patch"
        ),
    )
    def test_edit_tasking_order_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test edit_tasking_order sends no field the caller left unset.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema(
                "/{contract_id}/tasking/orders/{order_id}", "patch"
            ),
        )
        pook.reset()
        pook.on()
        mock = pook.patch(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditOrderPayload.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.edit_tasking_order(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert_request_body_matches_input(
            mock, body_data, "PATCH /{contract_id}/tasking/orders/{order_id}"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/tasking/orders/{order_id}", "patch"
            ),
            "PATCH /{contract_id}/tasking/orders/{order_id}",
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
            "/{contract_id}/tasking/orders/{order_id}", "patch", "404"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/orders/{order_id}", "patch"
        ),
    )
    def test_edit_tasking_order_404_error(self, backend, response_data, body_data):
        """
        Test edit_tasking_order with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditOrderPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.edit_tasking_order(
                contract_id=contract_id, order_id=order_id, body=body
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
            "/{contract_id}/tasking/orders/{order_id}", "patch", "422"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/orders/{order_id}", "patch"
        ),
    )
    def test_edit_tasking_order_422_error(self, backend, response_data, body_data):
        """
        Test edit_tasking_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditOrderPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.edit_tasking_order(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/{order_id}/cancel", "post", "404"
        )
    )
    def test_cancel_tasking_order_404_error(self, backend, response_data):
        """
        Test cancel_tasking_order with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.cancel_tasking_order(
                contract_id=contract_id, order_id=order_id
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
            "/{contract_id}/tasking/orders/{order_id}/cancel", "post", "409"
        )
    )
    def test_cancel_tasking_order_409_error(self, backend, response_data):
        """
        Test cancel_tasking_order with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.cancel_tasking_order(
                contract_id=contract_id, order_id=order_id
            )
        assert exc_info.value.status_code == 409

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
            "/{contract_id}/tasking/orders/{order_id}/cancel", "post", "422"
        )
    )
    def test_cancel_tasking_order_422_error(self, backend, response_data):
        """
        Test cancel_tasking_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.cancel_tasking_order(
                contract_id=contract_id, order_id=order_id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/{order_id}/cancel", "post", "500"
        )
    )
    def test_cancel_tasking_order_500_error(self, backend, response_data):
        """
        Test cancel_tasking_order with 500 error response.

        HTTP 500 errors raise ServerError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(500).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ServerError) as exc_info:
            self.sdk.otm.cancel_tasking_order(
                contract_id=contract_id, order_id=order_id
            )
        assert exc_info.value.status_code == 500

    @pook.on
    def test_cancel_tasking_order_204_no_content(self, backend):
        """
        Test cancel_tasking_order with 204 No Content response.

        204 responses return None (no body).
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.post(url).reply(204).header("Content-Type", "application/json")
        result = self.sdk.otm.cancel_tasking_order(
            contract_id=contract_id, order_id=order_id
        )
        assert result is None

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
            "/{contract_id}/tasking/orders/{order_id}/download", "get", "200"
        )
    )
    def test_download_tasking_order_200(self, backend, response_data):
        """
        Test download_tasking_order with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.download_tasking_order(
            contract_id=contract_id, order_id=order_id
        )
        assert result is not None
        assert isinstance(result, OrderItemDownloadUrl)

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
            "/{contract_id}/tasking/orders/{order_id}/download", "get", "202"
        )
    )
    def test_download_tasking_order_202(self, backend, response_data):
        """
        Test download_tasking_order with 202 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(202).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.download_tasking_order(
            contract_id=contract_id, order_id=order_id
        )
        assert result is not None
        assert isinstance(result, DownloadPending)

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
            "/{contract_id}/tasking/orders/{order_id}/download", "get", "422"
        )
    )
    def test_download_tasking_order_422_error(self, backend, response_data):
        """
        Test download_tasking_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.download_tasking_order(
                contract_id=contract_id, order_id=order_id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/{order_id}/acquisition/details", "get", "200"
        )
    )
    def test_get_order_task_details_200(self, backend, response_data):
        """
        Test get_order_task_details with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/acquisition/details"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_order_task_details(
            contract_id=contract_id, order_id=order_id
        )
        assert result is not None
        assert isinstance(result, StacFeature)

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
            "/{contract_id}/tasking/orders/{order_id}/acquisition/details", "get", "422"
        )
    )
    def test_get_order_task_details_422_error(self, backend, response_data):
        """
        Test get_order_task_details with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/acquisition/details"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_order_task_details(
                contract_id=contract_id, order_id=order_id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/{order_id}/tasks", "get", "200"
        )
    )
    def test_get_tasking_order_tasks_200(self, backend, response_data):
        """
        Test get_tasking_order_tasks with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/tasks"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_order_tasks(
            contract_id=contract_id, order_id=order_id
        )
        assert result is not None
        assert isinstance(
            result, (ListOrderTasksResponse, ListOrderTasksUnavailableResponse)
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
            "/{contract_id}/tasking/orders/{order_id}/tasks", "get", "404"
        )
    )
    def test_get_tasking_order_tasks_404_error(self, backend, response_data):
        """
        Test get_tasking_order_tasks with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/tasks"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_order_tasks(
                contract_id=contract_id, order_id=order_id
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
            "/{contract_id}/tasking/orders/{order_id}/tasks", "get", "422"
        )
    )
    def test_get_tasking_order_tasks_422_error(self, backend, response_data):
        """
        Test get_tasking_order_tasks with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/tasks"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_order_tasks(
                contract_id=contract_id, order_id=order_id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        )
    )
    def test_get_tasking_feasibility_requests_200(self, backend, response_data):
        """
        Test get_tasking_feasibility_requests with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_feasibility_requests(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, StoredFeasibilityFeatureCollection)

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
            "/{contract_id}/tasking/feasibilities/", "get", "422"
        )
    )
    def test_get_tasking_feasibility_requests_422_error(self, backend, response_data):
        """
        Test get_tasking_feasibility_requests with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_feasibility_requests(contract_id=contract_id)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/feasibilities/", "post", "202"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/", "post"
        ),
    )
    def test_post_tasking_feasibility_202(self, backend, response_data, body_data):
        """
        Test post_tasking_feasibility with 202 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(202).json(response_data).header("Content-Type", "application/json")
        body = FeasibilityRequest.model_validate(body_data)
        result = self.sdk.otm.post_tasking_feasibility(
            contract_id=contract_id, body=body
        )
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/feasibilities/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/feasibilities/", "post"),
            "POST /{contract_id}/tasking/feasibilities/",
            body_data,
        )
        assert result is not None
        assert isinstance(result, StoredFeasibilityRequest)

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
            "/{contract_id}/tasking/feasibilities/", "post", "202"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/", "post"
        ),
    )
    def test_post_tasking_feasibility_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_feasibility sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema("/{contract_id}/tasking/feasibilities/", "post"),
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(202).json(response_data).header("Content-Type", "application/json")
        body = FeasibilityRequest.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.post_tasking_feasibility(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/feasibilities/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/feasibilities/", "post"),
            "POST /{contract_id}/tasking/feasibilities/",
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
            "/{contract_id}/tasking/feasibilities/", "post", "403"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/", "post"
        ),
    )
    def test_post_tasking_feasibility_403_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_feasibility with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = FeasibilityRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_feasibility(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 403

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
            "/{contract_id}/tasking/feasibilities/", "post", "422"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/", "post"
        ),
    )
    def test_post_tasking_feasibility_422_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_feasibility with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = FeasibilityRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_feasibility(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/feasibilities/{id}", "get", "200"
        )
    )
    def test_get_tasking_feasibility_request_200(self, backend, response_data):
        """
        Test get_tasking_feasibility_request with 200 response.
        """
        contract_id = uuid4()
        id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_feasibility_request(
            contract_id=contract_id, id=id
        )
        assert result is not None
        assert isinstance(result, StoredFeasibilityRequest)

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
            "/{contract_id}/tasking/feasibilities/{id}", "get", "404"
        )
    )
    def test_get_tasking_feasibility_request_404_error(self, backend, response_data):
        """
        Test get_tasking_feasibility_request with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_feasibility_request(contract_id=contract_id, id=id)
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
            "/{contract_id}/tasking/feasibilities/{id}", "get", "422"
        )
    )
    def test_get_tasking_feasibility_request_422_error(self, backend, response_data):
        """
        Test get_tasking_feasibility_request with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_feasibility_request(contract_id=contract_id, id=id)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/feasibilities/{id}/response", "get", "200"
        )
    )
    def test_get_tasking_feasibility_response_200(self, backend, response_data):
        """
        Test get_tasking_feasibility_response with 200 response.
        """
        contract_id = uuid4()
        id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/{id}/response"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_feasibility_response(
            contract_id=contract_id, id=id
        )
        assert result is not None
        assert isinstance(result, FeasibilityResponse)

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
            "/{contract_id}/tasking/feasibilities/{id}/response", "get", "404"
        )
    )
    def test_get_tasking_feasibility_response_404_error(self, backend, response_data):
        """
        Test get_tasking_feasibility_response with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/{id}/response"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_feasibility_response(
                contract_id=contract_id, id=id
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
            "/{contract_id}/tasking/feasibilities/{id}/response", "get", "422"
        )
    )
    def test_get_tasking_feasibility_response_422_error(self, backend, response_data):
        """
        Test get_tasking_feasibility_response with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/{id}/response"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_feasibility_response(
                contract_id=contract_id, id=id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post", "202"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
        ),
    )
    def test_post_tasking_order_feasibility_202(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_order_feasibility with 202 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(202).json(response_data).header("Content-Type", "application/json")
        body = ModifyFeasibilityRequest.model_validate(body_data)
        result = self.sdk.otm.post_tasking_order_feasibility(
            contract_id=contract_id, order_id=order_id, body=body
        )
        assert_request_body_matches_input(
            mock,
            body_data,
            "POST /{contract_id}/tasking/feasibilities/orders/{order_id}",
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
            ),
            "POST /{contract_id}/tasking/feasibilities/orders/{order_id}",
            body_data,
        )
        assert result is not None
        assert isinstance(result, StoredFeasibilityRequest)

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
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post", "202"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
        ),
    )
    def test_post_tasking_order_feasibility_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_order_feasibility sends no field the caller left unset.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/orders/{order_id}"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema(
                "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
            ),
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(202).json(response_data).header("Content-Type", "application/json")
        body = ModifyFeasibilityRequest.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.post_tasking_order_feasibility(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert_request_body_matches_input(
            mock,
            body_data,
            "POST /{contract_id}/tasking/feasibilities/orders/{order_id}",
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
            ),
            "POST /{contract_id}/tasking/feasibilities/orders/{order_id}",
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
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post", "403"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
        ),
    )
    def test_post_tasking_order_feasibility_403_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_order_feasibility with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = ModifyFeasibilityRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_order_feasibility(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert exc_info.value.status_code == 403

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
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post", "404"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
        ),
    )
    def test_post_tasking_order_feasibility_404_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_order_feasibility with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = ModifyFeasibilityRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_order_feasibility(
                contract_id=contract_id, order_id=order_id, body=body
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
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post", "409"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
        ),
    )
    def test_post_tasking_order_feasibility_409_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_order_feasibility with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = ModifyFeasibilityRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_order_feasibility(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert exc_info.value.status_code == 409

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
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post", "422"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/feasibilities/orders/{order_id}", "post"
        ),
    )
    def test_post_tasking_order_feasibility_422_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_order_feasibility with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/orders/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = ModifyFeasibilityRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_order_feasibility(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/price/", "post", "200"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/price/", "post"),
    )
    def test_get_price_200(self, backend, response_data, body_data):
        """
        Test get_price with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = PriceRequest.model_validate(body_data)
        result = self.sdk.otm.get_price(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/price/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/price/", "post"),
            "POST /{contract_id}/tasking/price/",
            body_data,
        )
        assert result is not None
        assert isinstance(result, OrderPrice)

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
            "/{contract_id}/tasking/price/", "post", "200"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/price/", "post"),
    )
    def test_get_price_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test get_price sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/price/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/{contract_id}/tasking/price/", "post")
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = PriceRequest.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.get_price(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/price/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/price/", "post"),
            "POST /{contract_id}/tasking/price/",
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
            "/{contract_id}/tasking/price/", "post", "400"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/price/", "post"),
    )
    def test_get_price_400_error(self, backend, response_data, body_data):
        """
        Test get_price with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = PriceRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_price(contract_id=contract_id, body=body)
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
            "/{contract_id}/tasking/price/", "post", "403"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/price/", "post"),
    )
    def test_get_price_403_error(self, backend, response_data, body_data):
        """
        Test get_price with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = PriceRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_price(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 403

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
            "/{contract_id}/tasking/price/", "post", "422"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/price/", "post"),
    )
    def test_get_price_422_error(self, backend, response_data, body_data):
        """
        Test get_price with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = PriceRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_price(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/price/{order_id}", "post", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/price/{order_id}", "post"
        ),
    )
    def test_calculate_modified_order_price_200(
        self, backend, response_data, body_data
    ):
        """
        Test calculate_modified_order_price with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/price/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditOrderPayload.model_validate(body_data)
        result = self.sdk.otm.calculate_modified_order_price(
            contract_id=contract_id, order_id=order_id, body=body
        )
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/price/{order_id}"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/price/{order_id}", "post"),
            "POST /{contract_id}/tasking/price/{order_id}",
            body_data,
        )
        assert result is not None
        assert isinstance(result, OrderModificationPrice)

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
            "/{contract_id}/tasking/price/{order_id}", "post", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/price/{order_id}", "post"
        ),
    )
    def test_calculate_modified_order_price_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test calculate_modified_order_price sends no field the caller left unset.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/price/{order_id}"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema("/{contract_id}/tasking/price/{order_id}", "post"),
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditOrderPayload.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.calculate_modified_order_price(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/price/{order_id}"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/price/{order_id}", "post"),
            "POST /{contract_id}/tasking/price/{order_id}",
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
            "/{contract_id}/tasking/price/{order_id}", "post", "400"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/price/{order_id}", "post"
        ),
    )
    def test_calculate_modified_order_price_400_error(
        self, backend, response_data, body_data
    ):
        """
        Test calculate_modified_order_price with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/price/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditOrderPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.calculate_modified_order_price(
                contract_id=contract_id, order_id=order_id, body=body
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
            "/{contract_id}/tasking/price/{order_id}", "post", "404"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/price/{order_id}", "post"
        ),
    )
    def test_calculate_modified_order_price_404_error(
        self, backend, response_data, body_data
    ):
        """
        Test calculate_modified_order_price with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/price/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditOrderPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.calculate_modified_order_price(
                contract_id=contract_id, order_id=order_id, body=body
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
            "/{contract_id}/tasking/price/{order_id}", "post", "409"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/price/{order_id}", "post"
        ),
    )
    def test_calculate_modified_order_price_409_error(
        self, backend, response_data, body_data
    ):
        """
        Test calculate_modified_order_price with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/price/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditOrderPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.calculate_modified_order_price(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert exc_info.value.status_code == 409

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
            "/{contract_id}/tasking/price/{order_id}", "post", "422"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/price/{order_id}", "post"
        ),
    )
    def test_calculate_modified_order_price_422_error(
        self, backend, response_data, body_data
    ):
        """
        Test calculate_modified_order_price with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/price/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditOrderPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.calculate_modified_order_price(
                contract_id=contract_id, order_id=order_id, body=body
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/outages/", "get", "200"
        )
    )
    def test_get_unplanned_outages_200(self, backend, response_data):
        """
        Test get_unplanned_outages with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/outages/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_unplanned_outages(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, list)

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
            "/{contract_id}/tasking/outages/", "get", "422"
        )
    )
    def test_get_unplanned_outages_422_error(self, backend, response_data):
        """
        Test get_unplanned_outages with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/outages/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_unplanned_outages(contract_id=contract_id)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/", "get", "200"
        )
    )
    def test_get_tasking_series_200(self, backend, response_data):
        """
        Test get_tasking_series with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_series(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, ListSeriesResponse)

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
            "/{contract_id}/tasking/series/", "get", "422"
        )
    )
    def test_get_tasking_series_422_error(self, backend, response_data):
        """
        Test get_tasking_series with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_series(contract_id=contract_id)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/", "post", "201"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_201(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 201 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(201).json(response_data).header("Content-Type", "application/json")
        body = SeriesRequest.model_validate(body_data)
        result = self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/series/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/series/", "post"),
            "POST /{contract_id}/tasking/series/",
            body_data,
        )
        assert result is not None
        assert isinstance(result, StoredSeriesResponse)

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
            "/{contract_id}/tasking/series/", "post", "201"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_series sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/{contract_id}/tasking/series/", "post")
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(201).json(response_data).header("Content-Type", "application/json")
        body = SeriesRequest.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/series/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/series/", "post"),
            "POST /{contract_id}/tasking/series/",
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
            "/{contract_id}/tasking/series/", "post", "400"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_400_error(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
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
            "/{contract_id}/tasking/series/", "post", "402"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_402_error(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 402 error response.

        HTTP 402 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(402).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 402

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
            "/{contract_id}/tasking/series/", "post", "403"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_403_error(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 403

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
            "/{contract_id}/tasking/series/", "post", "422"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_422_error(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/", "post", "500"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_500_error(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 500 error response.

        HTTP 500 errors raise ServerError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(500).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ServerError) as exc_info:
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 500

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
            "/{contract_id}/tasking/series/", "post", "503"
        ),
        body_data=get_request_body_strategy("/{contract_id}/tasking/series/", "post"),
    )
    def test_post_tasking_series_503_error(self, backend, response_data, body_data):
        """
        Test post_tasking_series with 503 error response.

        HTTP 503 errors raise ServerError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(503).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ServerError) as exc_info:
            self.sdk.otm.post_tasking_series(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 503

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
            "/{contract_id}/tasking/series/{series_id}", "get", "200"
        )
    )
    def test_get_tasking_series_by_id_200(self, backend, response_data):
        """
        Test get_tasking_series_by_id with 200 response.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_series_by_id(
            contract_id=contract_id, series_id=series_id
        )
        assert result is not None
        assert isinstance(result, StoredSeriesResponse)

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
            "/{contract_id}/tasking/series/{series_id}", "get", "404"
        )
    )
    def test_get_tasking_series_by_id_404_error(self, backend, response_data):
        """
        Test get_tasking_series_by_id with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_series_by_id(
                contract_id=contract_id, series_id=series_id
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
            "/{contract_id}/tasking/series/{series_id}", "get", "422"
        )
    )
    def test_get_tasking_series_by_id_422_error(self, backend, response_data):
        """
        Test get_tasking_series_by_id with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_series_by_id(
                contract_id=contract_id, series_id=series_id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/{series_id}", "patch", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/{series_id}", "patch"
        ),
    )
    def test_edit_tasking_series_200(self, backend, response_data, body_data):
        """
        Test edit_tasking_series with 200 response.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.patch(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditSeriesProperties.model_validate(body_data)
        result = self.sdk.otm.edit_tasking_series(
            contract_id=contract_id, series_id=series_id, body=body
        )
        assert_request_body_matches_input(
            mock, body_data, "PATCH /{contract_id}/tasking/series/{series_id}"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/tasking/series/{series_id}", "patch"
            ),
            "PATCH /{contract_id}/tasking/series/{series_id}",
            body_data,
        )
        assert result is not None
        assert isinstance(result, StoredSeriesResponse)

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
            "/{contract_id}/tasking/series/{series_id}", "patch", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/{series_id}", "patch"
        ),
    )
    def test_edit_tasking_series_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test edit_tasking_series sends no field the caller left unset.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema(
                "/{contract_id}/tasking/series/{series_id}", "patch"
            ),
        )
        pook.reset()
        pook.on()
        mock = pook.patch(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditSeriesProperties.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.edit_tasking_series(
                contract_id=contract_id, series_id=series_id, body=body
            )
        assert_request_body_matches_input(
            mock, body_data, "PATCH /{contract_id}/tasking/series/{series_id}"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema(
                "/{contract_id}/tasking/series/{series_id}", "patch"
            ),
            "PATCH /{contract_id}/tasking/series/{series_id}",
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
            "/{contract_id}/tasking/series/{series_id}", "patch", "400"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/{series_id}", "patch"
        ),
    )
    def test_edit_tasking_series_400_error(self, backend, response_data, body_data):
        """
        Test edit_tasking_series with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditSeriesProperties.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.edit_tasking_series(
                contract_id=contract_id, series_id=series_id, body=body
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
            "/{contract_id}/tasking/series/{series_id}", "patch", "404"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/{series_id}", "patch"
        ),
    )
    def test_edit_tasking_series_404_error(self, backend, response_data, body_data):
        """
        Test edit_tasking_series with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditSeriesProperties.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.edit_tasking_series(
                contract_id=contract_id, series_id=series_id, body=body
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
            "/{contract_id}/tasking/series/{series_id}", "patch", "409"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/{series_id}", "patch"
        ),
    )
    def test_edit_tasking_series_409_error(self, backend, response_data, body_data):
        """
        Test edit_tasking_series with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditSeriesProperties.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.edit_tasking_series(
                contract_id=contract_id, series_id=series_id, body=body
            )
        assert exc_info.value.status_code == 409

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
            "/{contract_id}/tasking/series/{series_id}", "patch", "422"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/{series_id}", "patch"
        ),
    )
    def test_edit_tasking_series_422_error(self, backend, response_data, body_data):
        """
        Test edit_tasking_series with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditSeriesProperties.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.edit_tasking_series(
                contract_id=contract_id, series_id=series_id, body=body
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        )
    )
    def test_get_tasking_series_orders_200(self, backend, response_data):
        """
        Test get_tasking_series_orders with 200 response.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.get_tasking_series_orders(
            contract_id=contract_id, series_id=series_id
        )
        assert result is not None
        assert isinstance(result, ListStoredOrdersResponse)

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
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "404"
        )
    )
    def test_get_tasking_series_orders_404_error(self, backend, response_data):
        """
        Test get_tasking_series_orders with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_series_orders(
                contract_id=contract_id, series_id=series_id
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
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "422"
        )
    )
    def test_get_tasking_series_orders_422_error(self, backend, response_data):
        """
        Test get_tasking_series_orders with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/orders/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.get_tasking_series_orders(
                contract_id=contract_id, series_id=series_id
            )
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/price/", "post", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/price/", "post"
        ),
    )
    def test_post_tasking_series_price_200(self, backend, response_data, body_data):
        """
        Test post_tasking_series_price with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = SeriesRequest.model_validate(body_data)
        result = self.sdk.otm.post_tasking_series_price(
            contract_id=contract_id, body=body
        )
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/series/price/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/series/price/", "post"),
            "POST /{contract_id}/tasking/series/price/",
            body_data,
        )
        assert result is not None
        assert isinstance(result, SeriesPriceResponse)

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
            "/{contract_id}/tasking/series/price/", "post", "200"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/price/", "post"
        ),
    )
    def test_post_tasking_series_price_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_series_price sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/price/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data,
            get_request_body_schema("/{contract_id}/tasking/series/price/", "post"),
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = SeriesRequest.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.post_tasking_series_price(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/tasking/series/price/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/tasking/series/price/", "post"),
            "POST /{contract_id}/tasking/series/price/",
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
            "/{contract_id}/tasking/series/price/", "post", "400"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/price/", "post"
        ),
    )
    def test_post_tasking_series_price_400_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_series_price with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series_price(contract_id=contract_id, body=body)
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
            "/{contract_id}/tasking/series/price/", "post", "403"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/price/", "post"
        ),
    )
    def test_post_tasking_series_price_403_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_series_price with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series_price(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 403

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
            "/{contract_id}/tasking/series/price/", "post", "422"
        ),
        body_data=get_request_body_strategy(
            "/{contract_id}/tasking/series/price/", "post"
        ),
    )
    def test_post_tasking_series_price_422_error(
        self, backend, response_data, body_data
    ):
        """
        Test post_tasking_series_price with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/price/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SeriesRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.post_tasking_series_price(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/series/{series_id}/cancel", "post", "404"
        )
    )
    def test_cancel_tasking_series_404_error(self, backend, response_data):
        """
        Test cancel_tasking_series with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.cancel_tasking_series(
                contract_id=contract_id, series_id=series_id
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
            "/{contract_id}/tasking/series/{series_id}/cancel", "post", "409"
        )
    )
    def test_cancel_tasking_series_409_error(self, backend, response_data):
        """
        Test cancel_tasking_series with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.cancel_tasking_series(
                contract_id=contract_id, series_id=series_id
            )
        assert exc_info.value.status_code == 409

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
            "/{contract_id}/tasking/series/{series_id}/cancel", "post", "422"
        )
    )
    def test_cancel_tasking_series_422_error(self, backend, response_data):
        """
        Test cancel_tasking_series with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.cancel_tasking_series(
                contract_id=contract_id, series_id=series_id
            )
        assert exc_info.value.status_code == 422

    @pook.on
    def test_cancel_tasking_series_204_no_content(self, backend):
        """
        Test cancel_tasking_series with 204 No Content response.

        204 responses return None (no body).
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/cancel"
        url = f"{self.base_url}{path}"
        pook.post(url).reply(204).header("Content-Type", "application/json")
        result = self.sdk.otm.cancel_tasking_series(
            contract_id=contract_id, series_id=series_id
        )
        assert result is None

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
            "/{contract_id}/tasking/series/{series_id}/download", "get", "200"
        )
    )
    def test_download_tasking_series_200(self, backend, response_data):
        """
        Test download_tasking_series with 200 response.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.download_tasking_series(
            contract_id=contract_id, series_id=series_id
        )
        assert result is not None
        assert isinstance(result, OrderItemDownloadUrl)

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
            "/{contract_id}/tasking/series/{series_id}/download", "get", "202"
        )
    )
    def test_download_tasking_series_202(self, backend, response_data):
        """
        Test download_tasking_series with 202 response.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(202).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.download_tasking_series(
            contract_id=contract_id, series_id=series_id
        )
        assert result is not None
        assert isinstance(result, DownloadPending)

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
            "/{contract_id}/tasking/series/{series_id}/download", "get", "422"
        )
    )
    def test_download_tasking_series_422_error(self, backend, response_data):
        """
        Test download_tasking_series with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.download_tasking_series(
                contract_id=contract_id, series_id=series_id
            )
        assert exc_info.value.status_code == 422

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
        response_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        body_data=get_request_body_strategy("/{contract_id}/search/", "post"),
    )
    def test_search_200(self, backend, response_data, body_data):
        """
        Test search with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = SearchRequest.model_validate(body_data)
        result = self.sdk.otm.search(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/search/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/search/", "post"),
            "POST /{contract_id}/search/",
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
        response_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        body_data=get_request_body_strategy("/{contract_id}/search/", "post"),
    )
    def test_search_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test search sends no field the caller left unset.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/{contract_id}/search/", "post")
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = SearchRequest.model_validate(body_data)
        with suppress(Exception):
            self.sdk.otm.search(contract_id=contract_id, body=body)
        assert_request_body_matches_input(
            mock, body_data, "POST /{contract_id}/search/"
        )
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/{contract_id}/search/", "post"),
            "POST /{contract_id}/search/",
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
        response_data=get_response_strategy("/{contract_id}/search/", "post", "400"),
        body_data=get_request_body_strategy("/{contract_id}/search/", "post"),
    )
    def test_search_400_error(self, backend, response_data, body_data):
        """
        Test search with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.search(contract_id=contract_id, body=body)
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
        response_data=get_response_strategy("/{contract_id}/search/", "post", "422"),
        body_data=get_request_body_strategy("/{contract_id}/search/", "post"),
    )
    def test_search_422_error(self, backend, response_data, body_data):
        """
        Test search with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchRequest.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.otm.search(contract_id=contract_id, body=body)
        assert exc_info.value.status_code == 422

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
            "/{contract_id}/tasking/orders/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/orders/", "get", "200"
        ),
    )
    def test_get_tasking_orders_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_tasking_orders_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
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
        pages = list(self.sdk.otm.get_tasking_orders_iter(contract_id=contract_id))
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
            "/{contract_id}/tasking/orders/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/orders/", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/tasking/orders/", "get", "200"
        ),
    )
    def test_get_tasking_orders_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_tasking_orders_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
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
            self.sdk.otm.get_tasking_orders_iter(contract_id=contract_id, max_pages=2)
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
        page_data=get_response_strategy("/{contract_id}/tasking/orders/", "get", "200")
    )
    def test_get_tasking_orders_iter_no_next_link(self, backend, page_data):
        """Test get_tasking_orders_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/orders/"
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
        pages = list(self.sdk.otm.get_tasking_orders_iter(contract_id=contract_id))
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
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        ),
    )
    def test_get_tasking_feasibility_requests_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test get_tasking_feasibility_requests_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
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
            self.sdk.otm.get_tasking_feasibility_requests_iter(contract_id=contract_id)
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
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        ),
    )
    def test_get_tasking_feasibility_requests_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_tasking_feasibility_requests_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
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
            self.sdk.otm.get_tasking_feasibility_requests_iter(
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
            "/{contract_id}/tasking/feasibilities/", "get", "200"
        )
    )
    def test_get_tasking_feasibility_requests_iter_no_next_link(
        self, backend, page_data
    ):
        """Test get_tasking_feasibility_requests_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/feasibilities/"
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
            self.sdk.otm.get_tasking_feasibility_requests_iter(contract_id=contract_id)
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
            "/{contract_id}/tasking/series/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/series/", "get", "200"
        ),
    )
    def test_get_tasking_series_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_tasking_series_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
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
        pages = list(self.sdk.otm.get_tasking_series_iter(contract_id=contract_id))
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
            "/{contract_id}/tasking/series/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/series/", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/tasking/series/", "get", "200"
        ),
    )
    def test_get_tasking_series_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_tasking_series_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
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
            self.sdk.otm.get_tasking_series_iter(contract_id=contract_id, max_pages=2)
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
        page_data=get_response_strategy("/{contract_id}/tasking/series/", "get", "200")
    )
    def test_get_tasking_series_iter_no_next_link(self, backend, page_data):
        """Test get_tasking_series_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = uuid4()
        path = f"/{contract_id}/tasking/series/"
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
        pages = list(self.sdk.otm.get_tasking_series_iter(contract_id=contract_id))
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
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        ),
    )
    def test_get_tasking_series_orders_iter_pagination(
        self, backend, page1_data, page2_data
    ):
        """Test get_tasking_series_orders_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/orders/"
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
            self.sdk.otm.get_tasking_series_orders_iter(
                contract_id=contract_id, series_id=series_id
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
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        ),
        page2_data=get_response_strategy(
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        ),
        page3_data=get_response_strategy(
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        ),
    )
    def test_get_tasking_series_orders_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_tasking_series_orders_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/orders/"
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
            self.sdk.otm.get_tasking_series_orders_iter(
                contract_id=contract_id, series_id=series_id, max_pages=2
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
            "/{contract_id}/tasking/series/{series_id}/orders/", "get", "200"
        )
    )
    def test_get_tasking_series_orders_iter_no_next_link(self, backend, page_data):
        """Test get_tasking_series_orders_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = uuid4()
        series_id = uuid4()
        path = f"/{contract_id}/tasking/series/{series_id}/orders/"
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
            self.sdk.otm.get_tasking_series_orders_iter(
                contract_id=contract_id, series_id=series_id
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
        page1_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        page2_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
    )
    def test_search_iter_pagination(self, backend, page1_data, page2_data):
        """Test search_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
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
        body = SearchRequest()
        pages = list(self.sdk.otm.search_iter(body=body, contract_id=contract_id))
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
        page1_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        page2_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        page3_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
    )
    def test_search_iter_max_pages(self, backend, page1_data, page2_data, page3_data):
        """Test search_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
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
        body = SearchRequest()
        pages = list(
            self.sdk.otm.search_iter(body=body, contract_id=contract_id, max_pages=2)
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
    @given(page_data=get_response_strategy("/{contract_id}/search/", "post", "200"))
    def test_search_iter_no_next_link(self, backend, page_data):
        """Test search_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
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
        body = SearchRequest()
        pages = list(self.sdk.otm.search_iter(body=body, contract_id=contract_id))
        assert len(pages) == 1

    @pook.on
    def test_download_tasking_order_to_file_success(self, backend, tmp_path):
        """Test download_tasking_order_to_file writes file correctly."""
        output_path = tmp_path / "download.zip"
        mock_content = b"fake zip content"
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).header(
            "x-download-request-id", pook.regex("[0-9a-fA-F-]{36}")
        ).reply(200).body(mock_content).header(
            "Content-Type", "application/zip"
        ).header("Content-Length", str(len(mock_content)))
        result = self.sdk.otm.download_tasking_order_to_file(
            contract_id=contract_id, order_id=order_id, output_path=output_path
        )
        assert result.is_ok()
        assert output_path.exists()
        assert output_path.read_bytes() == mock_content

    @pook.on
    def test_download_tasking_order_to_file_progress_callback(self, backend, tmp_path):
        """Test download_tasking_order_to_file progress callback invocation."""
        output_path = tmp_path / "download.zip"
        mock_content = b"x" * 1024
        progress_calls = []

        def progress_callback(bytes_downloaded: int, total_bytes: int | None):
            progress_calls.append((bytes_downloaded, total_bytes))

        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(200).body(mock_content).header(
            "Content-Type", "application/zip"
        ).header("Content-Length", str(len(mock_content)))
        result = self.sdk.otm.download_tasking_order_to_file(
            contract_id=contract_id,
            order_id=order_id,
            output_path=output_path,
            progress_callback=progress_callback,
        )
        assert result.is_ok()
        assert len(progress_calls) > 0
        for bytes_downloaded, total_bytes in progress_calls:
            assert isinstance(bytes_downloaded, int)
            assert isinstance(total_bytes, int) or total_bytes is None

    @pook.on
    def test_download_tasking_order_to_file_error_404(self, backend, tmp_path):
        """Test download_tasking_order_to_file error handling (404)."""
        output_path = tmp_path / "download.zip"
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/tasking/orders/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(404).json({"error": "Not found"}).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.otm.download_tasking_order_to_file(
            contract_id=contract_id, order_id=order_id, output_path=output_path
        )
        assert result.is_err()
        error = result.error()
        assert isinstance(error, ClientError)
        assert error.status_code == 404
