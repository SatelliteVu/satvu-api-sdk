# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for cos service.

Generated from OpenAPI spec version v3.
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
from satvu.services.cos.models.feature_collection_order import FeatureCollectionOrder
from satvu.services.cos.models.order_download_url import OrderDownloadUrl
from satvu.services.cos.models.order_edit_payload import OrderEditPayload
from satvu.services.cos.models.order_item_download_url import OrderItemDownloadUrl
from satvu.services.cos.models.order_page import OrderPage
from satvu.services.cos.models.order_price import OrderPrice
from satvu.services.cos.models.order_submission_payload import OrderSubmissionPayload
from satvu.services.cos.models.price_request import PriceRequest
from satvu.services.cos.models.reseller_feature_collection_order import (
    ResellerFeatureCollectionOrder,
)
from satvu.services.cos.models.reseller_order_price import ResellerOrderPrice
from satvu.services.cos.models.reseller_price_request import ResellerPriceRequest
from satvu.services.cos.models.reseller_submission_order_payload import (
    ResellerSubmissionOrderPayload,
)
from satvu.services.cos.models.search_request import SearchRequest

from .test_schemas import get_request_body_strategy, get_response_strategy


@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestCosService:
    """Property-based tests for CosService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        mock_get_token = Mock(return_value="test_token")
        subdomain = "api"
        env_part = "qa."
        base_path = "/orders/v3"
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
        self.sdk.cos._get_token = mock_get_token

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
        response_data=get_response_strategy("/{contract_id}/{order_id}", "get", "200")
    )
    def test_get_order_200(self, backend, response_data):
        """
        Test get_order with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.cos.get_order(contract_id=contract_id, order_id=order_id)
        assert result is not None
        assert isinstance(
            result, (FeatureCollectionOrder, ResellerFeatureCollectionOrder)
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
        response_data=get_response_strategy("/{contract_id}/{order_id}", "get", "404")
    )
    def test_get_order_404_error(self, backend, response_data):
        """
        Test get_order with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.get_order(contract_id=contract_id, order_id=order_id)
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
        response_data=get_response_strategy("/{contract_id}/{order_id}", "get", "422")
    )
    def test_get_order_422_error(self, backend, response_data):
        """
        Test get_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.get_order(contract_id=contract_id, order_id=order_id)
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
            "/{contract_id}/{order_id}", "patch", "200"
        ),
        body_data=get_request_body_strategy("/{contract_id}/{order_id}", "patch"),
    )
    def test_edit_order_200(self, backend, response_data, body_data):
        """
        Test edit_order with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = OrderEditPayload.model_validate(body_data)
        result = self.sdk.cos.edit_order(
            contract_id=contract_id, order_id=order_id, body=body
        )
        assert result is not None
        assert isinstance(
            result, (FeatureCollectionOrder, ResellerFeatureCollectionOrder)
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
            "/{contract_id}/{order_id}", "patch", "404"
        ),
        body_data=get_request_body_strategy("/{contract_id}/{order_id}", "patch"),
    )
    def test_edit_order_404_error(self, backend, response_data, body_data):
        """
        Test edit_order with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = OrderEditPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.edit_order(
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
            "/{contract_id}/{order_id}", "patch", "422"
        ),
        body_data=get_request_body_strategy("/{contract_id}/{order_id}", "patch"),
    )
    def test_edit_order_422_error(self, backend, response_data, body_data):
        """
        Test edit_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = OrderEditPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.edit_order(
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
    @given(response_data=get_response_strategy("/{contract_id}/", "get", "200"))
    def test_query_orders_200(self, backend, response_data):
        """
        Test query_orders with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.cos.query_orders(contract_id=contract_id)
        assert result is not None
        assert isinstance(result, OrderPage)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/{contract_id}/", "get", "422"))
    def test_query_orders_422_error(self, backend, response_data):
        """
        Test query_orders with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.query_orders(contract_id=contract_id)
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
        response_data=get_response_strategy("/{contract_id}/", "post", "201"),
        body_data=get_request_body_strategy("/{contract_id}/", "post"),
    )
    def test_submit_order_201(self, backend, response_data, body_data):
        """
        Test submit_order with 201 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(201).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[OrderSubmissionPayload, ResellerSubmissionOrderPayload]
        )
        body = body_adapter.validate_python(body_data)
        result = self.sdk.cos.submit_order(contract_id=contract_id, body=body)
        assert result is not None
        assert isinstance(
            result, (FeatureCollectionOrder, ResellerFeatureCollectionOrder)
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
        response_data=get_response_strategy("/{contract_id}/", "post", "400"),
        body_data=get_request_body_strategy("/{contract_id}/", "post"),
    )
    def test_submit_order_400_error(self, backend, response_data, body_data):
        """
        Test submit_order with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[OrderSubmissionPayload, ResellerSubmissionOrderPayload]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.submit_order(contract_id=contract_id, body=body)
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
        response_data=get_response_strategy("/{contract_id}/", "post", "402"),
        body_data=get_request_body_strategy("/{contract_id}/", "post"),
    )
    def test_submit_order_402_error(self, backend, response_data, body_data):
        """
        Test submit_order with 402 error response.

        HTTP 402 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(402).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[OrderSubmissionPayload, ResellerSubmissionOrderPayload]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.submit_order(contract_id=contract_id, body=body)
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
        response_data=get_response_strategy("/{contract_id}/", "post", "403"),
        body_data=get_request_body_strategy("/{contract_id}/", "post"),
    )
    def test_submit_order_403_error(self, backend, response_data, body_data):
        """
        Test submit_order with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[OrderSubmissionPayload, ResellerSubmissionOrderPayload]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.submit_order(contract_id=contract_id, body=body)
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
        response_data=get_response_strategy("/{contract_id}/", "post", "422"),
        body_data=get_request_body_strategy("/{contract_id}/", "post"),
    )
    def test_submit_order_422_error(self, backend, response_data, body_data):
        """
        Test submit_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(
            Union[OrderSubmissionPayload, ResellerSubmissionOrderPayload]
        )
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.submit_order(contract_id=contract_id, body=body)
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
    def test_search_orders_200(self, backend, response_data, body_data):
        """
        Test search_orders with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/search/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchRequest.model_validate(body_data)
        result = self.sdk.cos.search_orders(contract_id=contract_id, body=body)
        assert result is not None
        assert isinstance(result, OrderPage)

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
    def test_search_orders_422_error(self, backend, response_data, body_data):
        """
        Test search_orders with 422 error response.

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
            self.sdk.cos.search_orders(contract_id=contract_id, body=body)
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
            "/{contract_id}/{order_id}/{item_id}/download", "get", "200"
        )
    )
    def test_download_order_item_200(self, backend, response_data):
        """
        Test download_order_item with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/{order_id}/{item_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.cos.download_order_item(
            contract_id=contract_id, order_id=order_id, item_id=item_id
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
            "/{contract_id}/{order_id}/{item_id}/download", "get", "404"
        )
    )
    def test_download_order_item_404_error(self, backend, response_data):
        """
        Test download_order_item with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/{order_id}/{item_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.download_order_item(
                contract_id=contract_id, order_id=order_id, item_id=item_id
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
            "/{contract_id}/{order_id}/{item_id}/download", "get", "422"
        )
    )
    def test_download_order_item_422_error(self, backend, response_data):
        """
        Test download_order_item with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        item_id = uuid4()
        path = f"/{contract_id}/{order_id}/{item_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.download_order_item(
                contract_id=contract_id, order_id=order_id, item_id=item_id
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
            "/{contract_id}/{order_id}/download", "get", "200"
        )
    )
    def test_download_order_200(self, backend, response_data):
        """
        Test download_order with 200 response.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.cos.download_order(contract_id=contract_id, order_id=order_id)
        assert result is not None
        assert isinstance(result, OrderDownloadUrl)

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
            "/{contract_id}/{order_id}/download", "get", "404"
        )
    )
    def test_download_order_404_error(self, backend, response_data):
        """
        Test download_order with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.download_order(contract_id=contract_id, order_id=order_id)
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
            "/{contract_id}/{order_id}/download", "get", "422"
        )
    )
    def test_download_order_422_error(self, backend, response_data):
        """
        Test download_order with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.download_order(contract_id=contract_id, order_id=order_id)
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
        response_data=get_response_strategy("/{contract_id}/price", "post", "200"),
        body_data=get_request_body_strategy("/{contract_id}/price", "post"),
    )
    def test_calculate_price_200(self, backend, response_data, body_data):
        """
        Test calculate_price with 200 response.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/price"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[PriceRequest, ResellerPriceRequest])
        body = body_adapter.validate_python(body_data)
        result = self.sdk.cos.calculate_price(contract_id=contract_id, body=body)
        assert result is not None
        assert isinstance(result, (OrderPrice, ResellerOrderPrice))

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
        response_data=get_response_strategy("/{contract_id}/price", "post", "422"),
        body_data=get_request_body_strategy("/{contract_id}/price", "post"),
    )
    def test_calculate_price_422_error(self, backend, response_data, body_data):
        """
        Test calculate_price with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        contract_id = uuid4()
        path = f"/{contract_id}/price"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(Union[PriceRequest, ResellerPriceRequest])
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.cos.calculate_price(contract_id=contract_id, body=body)
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
        page1_data=get_response_strategy("/{contract_id}/", "get", "200"),
        page2_data=get_response_strategy("/{contract_id}/", "get", "200"),
    )
    def test_query_orders_iter_pagination(self, backend, page1_data, page2_data):
        """Test query_orders_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        contract_id = uuid4()
        path = f"/{contract_id}/"
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
        pages = list(self.sdk.cos.query_orders_iter(contract_id=contract_id))
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
        page1_data=get_response_strategy("/{contract_id}/", "get", "200"),
        page2_data=get_response_strategy("/{contract_id}/", "get", "200"),
        page3_data=get_response_strategy("/{contract_id}/", "get", "200"),
    )
    def test_query_orders_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test query_orders_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        contract_id = uuid4()
        path = f"/{contract_id}/"
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
            self.sdk.cos.query_orders_iter(contract_id=contract_id, max_pages=2)
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
    @given(page_data=get_response_strategy("/{contract_id}/", "get", "200"))
    def test_query_orders_iter_no_next_link(self, backend, page_data):
        """Test query_orders_iter terminates when no next link present."""
        page_data = {**page_data}
        contract_id = uuid4()
        path = f"/{contract_id}/"
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
        pages = list(self.sdk.cos.query_orders_iter(contract_id=contract_id))
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
    def test_search_orders_iter_pagination(self, backend, page1_data, page2_data):
        """Test search_orders_iter follows next links correctly."""
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
        pages = list(
            self.sdk.cos.search_orders_iter(body=body, contract_id=contract_id)
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
        page1_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        page2_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
        page3_data=get_response_strategy("/{contract_id}/search/", "post", "200"),
    )
    def test_search_orders_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test search_orders_iter respects max_pages limit."""
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
            self.sdk.cos.search_orders_iter(
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
    @given(page_data=get_response_strategy("/{contract_id}/search/", "post", "200"))
    def test_search_orders_iter_no_next_link(self, backend, page_data):
        """Test search_orders_iter terminates when no next link present."""
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
        pages = list(
            self.sdk.cos.search_orders_iter(body=body, contract_id=contract_id)
        )
        assert len(pages) == 1

    @pook.on
    def test_download_order_item_to_file_success(self, backend, tmp_path):
        """Test download_order_item_to_file writes file correctly."""
        output_path = tmp_path / "download.zip"
        mock_content = b"fake zip content"
        contract_id = uuid4()
        order_id = uuid4()
        item_id = str(uuid4())
        path = f"/{contract_id}/{order_id}/{item_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).header(
            "x-download-request-id", pook.regex("[0-9a-fA-F-]{36}")
        ).reply(200).body(mock_content).header(
            "Content-Type", "application/zip"
        ).header("Content-Length", str(len(mock_content)))
        result = self.sdk.cos.download_order_item_to_file(
            contract_id=contract_id,
            order_id=order_id,
            item_id=item_id,
            output_path=output_path,
        )
        assert result.is_ok()
        assert output_path.exists()
        assert output_path.read_bytes() == mock_content

    @pook.on
    def test_download_order_item_to_file_progress_callback(self, backend, tmp_path):
        """Test download_order_item_to_file progress callback invocation."""
        output_path = tmp_path / "download.zip"
        mock_content = b"x" * 1024
        progress_calls = []

        def progress_callback(bytes_downloaded: int, total_bytes: int | None):
            progress_calls.append((bytes_downloaded, total_bytes))

        contract_id = uuid4()
        order_id = uuid4()
        item_id = str(uuid4())
        path = f"/{contract_id}/{order_id}/{item_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(200).body(mock_content).header(
            "Content-Type", "application/zip"
        ).header("Content-Length", str(len(mock_content)))
        result = self.sdk.cos.download_order_item_to_file(
            contract_id=contract_id,
            order_id=order_id,
            item_id=item_id,
            output_path=output_path,
            progress_callback=progress_callback,
        )
        assert result.is_ok()
        assert len(progress_calls) > 0
        for bytes_downloaded, total_bytes in progress_calls:
            assert isinstance(bytes_downloaded, int)
            assert isinstance(total_bytes, int) or total_bytes is None

    @pook.on
    def test_download_order_item_to_file_error_404(self, backend, tmp_path):
        """Test download_order_item_to_file error handling (404)."""
        output_path = tmp_path / "download.zip"
        contract_id = uuid4()
        order_id = uuid4()
        item_id = str(uuid4())
        path = f"/{contract_id}/{order_id}/{item_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(404).json({"error": "Not found"}).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.cos.download_order_item_to_file(
            contract_id=contract_id,
            order_id=order_id,
            item_id=item_id,
            output_path=output_path,
        )
        assert result.is_err()
        error = result.error()
        assert isinstance(error, ClientError)
        assert error.status_code == 404

    @pook.on
    def test_download_order_to_file_success(self, backend, tmp_path):
        """Test download_order_to_file writes file correctly."""
        output_path = tmp_path / "download.zip"
        mock_content = b"fake zip content"
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).header(
            "x-download-request-id", pook.regex("[0-9a-fA-F-]{36}")
        ).reply(200).body(mock_content).header(
            "Content-Type", "application/zip"
        ).header("Content-Length", str(len(mock_content)))
        result = self.sdk.cos.download_order_to_file(
            contract_id=contract_id, order_id=order_id, output_path=output_path
        )
        assert result.is_ok()
        assert output_path.exists()
        assert output_path.read_bytes() == mock_content

    @pook.on
    def test_download_order_to_file_progress_callback(self, backend, tmp_path):
        """Test download_order_to_file progress callback invocation."""
        output_path = tmp_path / "download.zip"
        mock_content = b"x" * 1024
        progress_calls = []

        def progress_callback(bytes_downloaded: int, total_bytes: int | None):
            progress_calls.append((bytes_downloaded, total_bytes))

        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(200).body(mock_content).header(
            "Content-Type", "application/zip"
        ).header("Content-Length", str(len(mock_content)))
        result = self.sdk.cos.download_order_to_file(
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
    def test_download_order_to_file_error_404(self, backend, tmp_path):
        """Test download_order_to_file error handling (404)."""
        output_path = tmp_path / "download.zip"
        contract_id = uuid4()
        order_id = uuid4()
        path = f"/{contract_id}/{order_id}/download"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(404).json({"error": "Not found"}).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.cos.download_order_to_file(
            contract_id=contract_id, order_id=order_id, output_path=output_path
        )
        assert result.is_err()
        error = result.error()
        assert isinstance(error, ClientError)
        assert error.status_code == 404
