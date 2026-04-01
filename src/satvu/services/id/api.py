# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/endpoint_module.py.jinja

from collections.abc import Callable, Generator
from typing import Union
from uuid import UUID

from satvu.core import SDKClient
from satvu.http import HttpClient
from satvu.services.id.models.client_credentials import ClientCredentials
from satvu.services.id.models.client_id import ClientID
from satvu.services.id.models.core_webhook import CoreWebhook
from satvu.services.id.models.create_webhook_response import CreateWebhookResponse
from satvu.services.id.models.edit_webhook_payload import EditWebhookPayload
from satvu.services.id.models.list_webhook_response import ListWebhookResponse
from satvu.services.id.models.notification_description import NotificationDescription
from satvu.services.id.models.post_webhook_response import PostWebhookResponse
from satvu.services.id.models.test_webhook_response import TestWebhookResponse
from satvu.services.id.models.user_info import UserInfo
from satvu.services.id.models.user_settings import UserSettings
from satvu.services.id.models.webhook_response import WebhookResponse
from satvu.shared.parsing import parse_response


class IdService(SDKClient):
    base_path = "/id/v3"

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

    def list_webhooks(
        self,
        per_page: Union[None, int] = 25,
        token: None | str = None,
        timeout: int | None = None,
    ) -> ListWebhookResponse:
        """
        List Webhooks

        List all webhooks.

        Args:
            per_page (Union[None, int]): The number of webhooks to return per page. Default: 25.
            token (None | str): The pagination token
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ListWebhookResponse
        """

        params = {
            "per_page": per_page,
            "token": token,
        }

        result = self.make_request(
            method="get",
            url="/webhooks/",
            params=params,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), ListWebhookResponse)
        return response.json().unwrap()

    def list_webhooks_iter(
        self,
        per_page: Union[None, int] = 25,
        max_pages: int | None = None,
    ) -> Generator[ListWebhookResponse, None, None]:
        """
        List Webhooks (Paginated Iterator)

        Automatically handles pagination by following STAC links.

        Args:
            per_page (Union[None, int]): The number of webhooks to return per page. Default: 25.
            max_pages: Stop after fetching this many pages (default: unlimited)

        Yields:
            Response pages from paginated results

        Example:
            ```python
            for page in sdk.id.list_webhooks_iter(
                max_pages=10
            ):
                for item in page.webhooks:
                    print(item)
            ```
        """
        token = None
        page_count = 0

        while True:
            if max_pages and page_count >= max_pages:
                break

            response = self.list_webhooks(
                per_page=per_page,
                token=token,
            )
            page_count += 1

            yield response

            token = self.extract_next_token(response)
            if not token:
                break

    def create_webhook(
        self,
        body: CoreWebhook,
        timeout: int | None = None,
    ) -> CreateWebhookResponse:
        """
        Create Webhook

        Create a webhook.

        Args:
            body (CoreWebhook):
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            CreateWebhookResponse
        """

        json_body = body.model_dump(by_alias=True, mode="json")

        result = self.make_request(
            method="post",
            url="/webhooks/",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), CreateWebhookResponse)
        return response.json().unwrap()

    def get_webhook(
        self,
        id: UUID,
        timeout: int | None = None,
    ) -> WebhookResponse:
        """
        Get Webhook

        Get information about an existing webhook.

        Args:
            id (UUID): The webhook ID.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            WebhookResponse
        """

        result = self.make_request(
            method="get",
            url=f"/webhooks/{id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), WebhookResponse)
        return response.json().unwrap()

    def delete_webhook(
        self,
        id: UUID,
        timeout: int | None = None,
    ) -> None:
        """
        Delete Webhook

        Delete a webhook.

        Args:
            id (UUID): The webhook ID.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            None
        """

        result = self.make_request(
            method="delete",
            url=f"/webhooks/{id}",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 204:
            return None
        return response.json().unwrap()

    def edit_webhook(
        self,
        body: EditWebhookPayload,
        id: UUID,
        timeout: int | None = None,
    ) -> WebhookResponse:
        """
        Edit Webhook

        Edit a webhook.

        Args:
            id (UUID): The webhook ID.
            body (EditWebhookPayload):
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            WebhookResponse
        """

        json_body = body.model_dump(by_alias=True, mode="json")

        result = self.make_request(
            method="patch",
            url=f"/webhooks/{id}",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), WebhookResponse)
        return response.json().unwrap()

    def get_webhook_events(
        self,
        timeout: int | None = None,
    ) -> list[NotificationDescription]:
        """
        Get Webhook Events

        View all webhook event types.

        Args:
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            list[NotificationDescription]
        """

        result = self.make_request(
            method="get",
            url="/webhooks/events",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(
                response.json().unwrap(), list[NotificationDescription]
            )
        return response.json().unwrap()

    def rotate_webhook_signing_key(
        self,
        id: UUID,
        timeout: int | None = None,
    ) -> PostWebhookResponse:
        """
        Rotate Webhook Signing Key

        Rotate the signing key for a webhook.

        Args:
            id (UUID): The webhook ID.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            PostWebhookResponse
        """

        result = self.make_request(
            method="post",
            url=f"/webhooks/{id}/rotate",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), PostWebhookResponse)
        return response.json().unwrap()

    def test_webhook(
        self,
        id: UUID,
        timeout: int | None = None,
    ) -> TestWebhookResponse:
        """
        Test Webhook

        Test a webhook.

        Args:
            id (UUID): The webhook ID.
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            TestWebhookResponse
        """

        result = self.make_request(
            method="post",
            url=f"/webhooks/{id}/test",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), TestWebhookResponse)
        return response.json().unwrap()

    def get_user_client(
        self,
        timeout: int | None = None,
    ) -> Union[ClientID, None]:
        """
        Get User Client

        Retrieves the Client ID of an API user.

        Args:
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            Union[ClientID, None]
        """

        result = self.make_request(
            method="get",
            url="/client",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), ClientID)
        if response.status_code == 204:
            return None
        return response.json().unwrap()

    def create_user_client(
        self,
        timeout: int | None = None,
    ) -> ClientCredentials:
        """
        Create User Client

        Creates an M2M client to grant API access to a user.

        Args:
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ClientCredentials
        """

        result = self.make_request(
            method="post",
            url="/client",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 201:
            return parse_response(response.json().unwrap(), ClientCredentials)
        return response.json().unwrap()

    def rotate_client_secret(
        self,
        timeout: int | None = None,
    ) -> ClientCredentials:
        """
        Rotate Client Secret

        Generates a new client secret for the M2M client associated with an API user.

        Args:
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            ClientCredentials
        """

        result = self.make_request(
            method="post",
            url="/client/reset",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), ClientCredentials)
        return response.json().unwrap()

    def get_user_details(
        self,
        timeout: int | None = None,
    ) -> UserInfo:
        """
        Get User Details

        Retrieves the details of a user.

        Args:
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            UserInfo
        """

        result = self.make_request(
            method="get",
            url="/user/details",
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), UserInfo)
        return response.json().unwrap()

    def edit_user_settings(
        self,
        body: UserSettings,
        timeout: int | None = None,
    ) -> UserInfo:
        """
        Edit User Settings

        Updates user settings.

        Args:
            body (UserSettings):
            timeout: Optional request timeout in seconds. Overrides the instance timeout if
                provided.

        Returns:
            UserInfo
        """

        json_body = body.model_dump(by_alias=True, mode="json")

        result = self.make_request(
            method="put",
            url="/user/settings",
            json=json_body,
            timeout=timeout,
        )

        # Raise HttpError for failed requests (network errors, 4xx, 5xx, etc.)
        if result.is_err():
            raise result.error()

        response = result.unwrap()

        if response.status_code == 200:
            return parse_response(response.json().unwrap(), UserInfo)
        return response.json().unwrap()
