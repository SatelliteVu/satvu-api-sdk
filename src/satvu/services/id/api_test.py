# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for id service.

Generated from OpenAPI spec version v3.
Uses property-based testing with hypothesis-jsonschema.
"""

from contextlib import suppress
from unittest.mock import Mock
from uuid import uuid4

import pook
import pytest
from hypothesis import HealthCheck, given, settings

from satvu import SatVuSDK, create_http_client
from satvu.http.errors import ClientError
from satvu.services.id.models.client_credentials import ClientCredentials
from satvu.services.id.models.client_id import ClientID
from satvu.services.id.models.core_webhook import CoreWebhook
from satvu.services.id.models.create_webhook_response import CreateWebhookResponse
from satvu.services.id.models.edit_webhook_payload import EditWebhookPayload
from satvu.services.id.models.list_webhook_response import ListWebhookResponse
from satvu.services.id.models.post_webhook_response import PostWebhookResponse
from satvu.services.id.models.test_webhook_response import TestWebhookResponse
from satvu.services.id.models.user_info import UserInfo
from satvu.services.id.models.user_settings import UserSettings
from satvu.services.id.models.webhook_response import WebhookResponse
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
class TestIdService:
    """Property-based tests for IdService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        mock_get_token = Mock(return_value="test_token")
        subdomain = "api"
        env_part = "qa."
        base_path = "/id/v3"
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
        self.sdk.id._get_token = mock_get_token

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/webhooks/", "get", "200"))
    def test_list_webhooks_200(self, backend, response_data):
        """
        Test list_webhooks with 200 response.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.list_webhooks()
        assert result is not None
        assert isinstance(result, ListWebhookResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/webhooks/", "get", "422"))
    def test_list_webhooks_422_error(self, backend, response_data):
        """
        Test list_webhooks with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.list_webhooks()
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
        response_data=get_response_strategy("/webhooks/", "post", "200"),
        body_data=get_request_body_strategy("/webhooks/", "post"),
    )
    def test_create_webhook_200(self, backend, response_data, body_data):
        """
        Test create_webhook with 200 response.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = CoreWebhook.model_validate(body_data)
        result = self.sdk.id.create_webhook(body=body)
        assert_request_body_matches_input(mock, body_data, "POST /webhooks/")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/webhooks/", "post"),
            "POST /webhooks/",
            body_data,
        )
        assert result is not None
        assert isinstance(result, CreateWebhookResponse)

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
        response_data=get_response_strategy("/webhooks/", "post", "200"),
        body_data=get_request_body_strategy("/webhooks/", "post"),
    )
    def test_create_webhook_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test create_webhook sends no field the caller left unset.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/webhooks/", "post")
        )
        pook.reset()
        pook.on()
        mock = pook.post(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = CoreWebhook.model_validate(body_data)
        with suppress(Exception):
            self.sdk.id.create_webhook(body=body)
        assert_request_body_matches_input(mock, body_data, "POST /webhooks/")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/webhooks/", "post"),
            "POST /webhooks/",
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
        response_data=get_response_strategy("/webhooks/", "post", "400"),
        body_data=get_request_body_strategy("/webhooks/", "post"),
    )
    def test_create_webhook_400_error(self, backend, response_data, body_data):
        """
        Test create_webhook with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = CoreWebhook.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.create_webhook(body=body)
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
        response_data=get_response_strategy("/webhooks/", "post", "403"),
        body_data=get_request_body_strategy("/webhooks/", "post"),
    )
    def test_create_webhook_403_error(self, backend, response_data, body_data):
        """
        Test create_webhook with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = CoreWebhook.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.create_webhook(body=body)
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
        response_data=get_response_strategy("/webhooks/", "post", "422"),
        body_data=get_request_body_strategy("/webhooks/", "post"),
    )
    def test_create_webhook_422_error(self, backend, response_data, body_data):
        """
        Test create_webhook with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/webhooks/"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = CoreWebhook.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.create_webhook(body=body)
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
    @given(response_data=get_response_strategy("/webhooks/{id}", "get", "200"))
    def test_get_webhook_200(self, backend, response_data):
        """
        Test get_webhook with 200 response.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.get_webhook(id=id)
        assert result is not None
        assert isinstance(result, WebhookResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/webhooks/{id}", "get", "404"))
    def test_get_webhook_404_error(self, backend, response_data):
        """
        Test get_webhook with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.get_webhook(id=id)
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
    @given(response_data=get_response_strategy("/webhooks/{id}", "get", "422"))
    def test_get_webhook_422_error(self, backend, response_data):
        """
        Test get_webhook with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.get_webhook(id=id)
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
    @given(response_data=get_response_strategy("/webhooks/{id}", "delete", "404"))
    def test_delete_webhook_404_error(self, backend, response_data):
        """
        Test delete_webhook with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.delete(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.delete_webhook(id=id)
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
    @given(response_data=get_response_strategy("/webhooks/{id}", "delete", "422"))
    def test_delete_webhook_422_error(self, backend, response_data):
        """
        Test delete_webhook with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.delete(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.delete_webhook(id=id)
        assert exc_info.value.status_code == 422

    @pook.on
    def test_delete_webhook_204_no_content(self, backend):
        """
        Test delete_webhook with 204 No Content response.

        204 responses return None (no body).
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.delete(url).reply(204).header("Content-Type", "application/json")
        result = self.sdk.id.delete_webhook(id=id)
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
        response_data=get_response_strategy("/webhooks/{id}", "patch", "200"),
        body_data=get_request_body_strategy("/webhooks/{id}", "patch"),
    )
    def test_edit_webhook_200(self, backend, response_data, body_data):
        """
        Test edit_webhook with 200 response.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.patch(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditWebhookPayload.model_validate(body_data)
        result = self.sdk.id.edit_webhook(id=id, body=body)
        assert_request_body_matches_input(mock, body_data, "PATCH /webhooks/{id}")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/webhooks/{id}", "patch"),
            "PATCH /webhooks/{id}",
            body_data,
        )
        assert result is not None
        assert isinstance(result, WebhookResponse)

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
        response_data=get_response_strategy("/webhooks/{id}", "patch", "200"),
        body_data=get_request_body_strategy("/webhooks/{id}", "patch"),
    )
    def test_edit_webhook_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test edit_webhook sends no field the caller left unset.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/webhooks/{id}", "patch")
        )
        pook.reset()
        pook.on()
        mock = pook.patch(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = EditWebhookPayload.model_validate(body_data)
        with suppress(Exception):
            self.sdk.id.edit_webhook(id=id, body=body)
        assert_request_body_matches_input(mock, body_data, "PATCH /webhooks/{id}")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/webhooks/{id}", "patch"),
            "PATCH /webhooks/{id}",
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
        response_data=get_response_strategy("/webhooks/{id}", "patch", "400"),
        body_data=get_request_body_strategy("/webhooks/{id}", "patch"),
    )
    def test_edit_webhook_400_error(self, backend, response_data, body_data):
        """
        Test edit_webhook with 400 error response.

        HTTP 400 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(400).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditWebhookPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.edit_webhook(id=id, body=body)
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
        response_data=get_response_strategy("/webhooks/{id}", "patch", "403"),
        body_data=get_request_body_strategy("/webhooks/{id}", "patch"),
    )
    def test_edit_webhook_403_error(self, backend, response_data, body_data):
        """
        Test edit_webhook with 403 error response.

        HTTP 403 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(403).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditWebhookPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.edit_webhook(id=id, body=body)
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
        response_data=get_response_strategy("/webhooks/{id}", "patch", "404"),
        body_data=get_request_body_strategy("/webhooks/{id}", "patch"),
    )
    def test_edit_webhook_404_error(self, backend, response_data, body_data):
        """
        Test edit_webhook with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditWebhookPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.edit_webhook(id=id, body=body)
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
        response_data=get_response_strategy("/webhooks/{id}", "patch", "422"),
        body_data=get_request_body_strategy("/webhooks/{id}", "patch"),
    )
    def test_edit_webhook_422_error(self, backend, response_data, body_data):
        """
        Test edit_webhook with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.patch(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = EditWebhookPayload.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.edit_webhook(id=id, body=body)
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
    @given(response_data=get_response_strategy("/webhooks/events", "get", "200"))
    def test_get_webhook_events_200(self, backend, response_data):
        """
        Test get_webhook_events with 200 response.
        """
        path = "/webhooks/events"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.get_webhook_events()
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
    @given(response_data=get_response_strategy("/webhooks/{id}/rotate", "post", "200"))
    def test_rotate_webhook_signing_key_200(self, backend, response_data):
        """
        Test rotate_webhook_signing_key with 200 response.
        """
        id = uuid4()
        path = f"/webhooks/{id}/rotate"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.rotate_webhook_signing_key(id=id)
        assert result is not None
        assert isinstance(result, PostWebhookResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/webhooks/{id}/rotate", "post", "404"))
    def test_rotate_webhook_signing_key_404_error(self, backend, response_data):
        """
        Test rotate_webhook_signing_key with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}/rotate"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.rotate_webhook_signing_key(id=id)
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
    @given(response_data=get_response_strategy("/webhooks/{id}/rotate", "post", "422"))
    def test_rotate_webhook_signing_key_422_error(self, backend, response_data):
        """
        Test rotate_webhook_signing_key with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}/rotate"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.rotate_webhook_signing_key(id=id)
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
    @given(response_data=get_response_strategy("/webhooks/{id}/test", "post", "200"))
    def test_test_webhook_200(self, backend, response_data):
        """
        Test test_webhook with 200 response.
        """
        id = uuid4()
        path = f"/webhooks/{id}/test"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.test_webhook(id=id)
        assert result is not None
        assert isinstance(result, TestWebhookResponse)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/webhooks/{id}/test", "post", "404"))
    def test_test_webhook_404_error(self, backend, response_data):
        """
        Test test_webhook with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}/test"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.test_webhook(id=id)
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
    @given(response_data=get_response_strategy("/webhooks/{id}/test", "post", "422"))
    def test_test_webhook_422_error(self, backend, response_data):
        """
        Test test_webhook with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        id = uuid4()
        path = f"/webhooks/{id}/test"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.test_webhook(id=id)
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
    @given(response_data=get_response_strategy("/client", "get", "200"))
    def test_get_user_client_200(self, backend, response_data):
        """
        Test get_user_client with 200 response.
        """
        path = "/client"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.get_user_client()
        assert result is not None
        assert isinstance(result, ClientID)

    @pook.on
    def test_get_user_client_204_no_content(self, backend):
        """
        Test get_user_client with 204 No Content response.

        204 responses return None (no body).
        """
        path = "/client"
        url = f"{self.base_url}{path}"
        pook.get(url).reply(204).header("Content-Type", "application/json")
        result = self.sdk.id.get_user_client()
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
    @given(response_data=get_response_strategy("/client", "post", "201"))
    def test_create_user_client_201(self, backend, response_data):
        """
        Test create_user_client with 201 response.
        """
        path = "/client"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(201).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.create_user_client()
        assert result is not None
        assert isinstance(result, ClientCredentials)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/client", "post", "409"))
    def test_create_user_client_409_error(self, backend, response_data):
        """
        Test create_user_client with 409 error response.

        HTTP 409 errors raise ClientError.
        """
        path = "/client"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(409).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.create_user_client()
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
    @given(response_data=get_response_strategy("/client/reset", "post", "200"))
    def test_rotate_client_secret_200(self, backend, response_data):
        """
        Test rotate_client_secret with 200 response.
        """
        path = "/client/reset"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.rotate_client_secret()
        assert result is not None
        assert isinstance(result, ClientCredentials)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/client/reset", "post", "404"))
    def test_rotate_client_secret_404_error(self, backend, response_data):
        """
        Test rotate_client_secret with 404 error response.

        HTTP 404 errors raise ClientError.
        """
        path = "/client/reset"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(404).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.rotate_client_secret()
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
    @given(response_data=get_response_strategy("/user/details", "get", "200"))
    def test_get_user_details_200(self, backend, response_data):
        """
        Test get_user_details with 200 response.
        """
        path = "/user/details"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.id.get_user_details()
        assert result is not None
        assert isinstance(result, UserInfo)

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
        response_data=get_response_strategy("/user/settings", "put", "200"),
        body_data=get_request_body_strategy("/user/settings", "put"),
    )
    def test_edit_user_settings_200(self, backend, response_data, body_data):
        """
        Test edit_user_settings with 200 response.
        """
        path = "/user/settings"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        mock = pook.put(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = UserSettings.model_validate(body_data)
        result = self.sdk.id.edit_user_settings(body=body)
        assert_request_body_matches_input(mock, body_data, "PUT /user/settings")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/user/settings", "put"),
            "PUT /user/settings",
            body_data,
        )
        assert result is not None
        assert isinstance(result, UserInfo)

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
        response_data=get_response_strategy("/user/settings", "put", "200"),
        body_data=get_request_body_strategy("/user/settings", "put"),
    )
    def test_edit_user_settings_minimal_body_sends_only_what_was_set(
        self, backend, response_data, body_data
    ):
        """
        Test edit_user_settings sends no field the caller left unset.
        """
        path = "/user/settings"
        url = f"{self.base_url}{path}"
        body_data = drop_optional_properties(
            body_data, get_request_body_schema("/user/settings", "put")
        )
        pook.reset()
        pook.on()
        mock = pook.put(url)
        mock.reply(200).json(response_data).header("Content-Type", "application/json")
        body = UserSettings.model_validate(body_data)
        with suppress(Exception):
            self.sdk.id.edit_user_settings(body=body)
        assert_request_body_matches_input(mock, body_data, "PUT /user/settings")
        assert_request_body_conforms(
            mock,
            get_request_body_schema("/user/settings", "put"),
            "PUT /user/settings",
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
        response_data=get_response_strategy("/user/settings", "put", "422"),
        body_data=get_request_body_strategy("/user/settings", "put"),
    )
    def test_edit_user_settings_422_error(self, backend, response_data, body_data):
        """
        Test edit_user_settings with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/user/settings"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.put(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = UserSettings.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.id.edit_user_settings(body=body)
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
        page1_data=get_response_strategy("/webhooks/", "get", "200"),
        page2_data=get_response_strategy("/webhooks/", "get", "200"),
    )
    def test_list_webhooks_iter_pagination(self, backend, page1_data, page2_data):
        """Test list_webhooks_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        path = "/webhooks/".format()
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
        pages = list(self.sdk.id.list_webhooks_iter())
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
        page1_data=get_response_strategy("/webhooks/", "get", "200"),
        page2_data=get_response_strategy("/webhooks/", "get", "200"),
        page3_data=get_response_strategy("/webhooks/", "get", "200"),
    )
    def test_list_webhooks_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test list_webhooks_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        path = "/webhooks/".format()
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
        pages = list(self.sdk.id.list_webhooks_iter(max_pages=2))
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
    @given(page_data=get_response_strategy("/webhooks/", "get", "200"))
    def test_list_webhooks_iter_no_next_link(self, backend, page_data):
        """Test list_webhooks_iter terminates when no next link present."""
        page_data = {**page_data}
        path = "/webhooks/".format()
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
        pages = list(self.sdk.id.list_webhooks_iter())
        assert len(pages) == 1
