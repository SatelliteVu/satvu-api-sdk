from collections.abc import Callable
from typing import Any, Union, Unpack
from uuid import UUID

from satvu_api_sdk.core import SDKClient

from id.models.client_credentials import ClientCredentials
from id.models.client_id import ClientID
from id.models.core_webhook import CoreWebhook
from id.models.create_webhook_response import CreateWebhookResponse
from id.models.credit_balance_response import CreditBalanceResponse
from id.models.edit_webhook_payload import EditWebhookPayload
from id.models.list_webhook_response import ListWebhookResponse
from id.models.notification_description import NotificationDescription
from id.models.post_webhook_response import PostWebhookResponse
from id.models.test_webhook_response import TestWebhookResponse
from id.models.user_info import UserInfo
from id.models.user_info_deprecated import UserInfoDeprecated
from id.models.user_settings import UserSettings
from id.models.webhook_response import WebhookResponse
from id.types import UNSET, Unset


class IdService(SDKClient):
    base_path = "/id/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_user_client(
        self,
    ) -> ClientID:
        """
        Get User Client

        Retrieves the Client ID of an API user.

        Args:

        Returns:
            ClientID
        """

        response = self.make_request(
            method="get",
            url="/client",
        )

        if response.status_code == 200:
            return ClientID(**response.json())
        if response.status_code == 204:
            return response.json()
        return response.json()

    def create_user_client(
        self,
    ) -> ClientCredentials:
        """
        Create User Client

        Creates an M2M client to grant API access to a user.

        Args:

        Returns:
            ClientCredentials
        """

        response = self.make_request(
            method="post",
            url="/client",
        )

        if response.status_code == 201:
            return ClientCredentials(**response.json())
        return response.json()

    def rotate_client_secret(
        self,
    ) -> ClientCredentials:
        """
        Rotate Client Secret

        Generates a new client secret for the M2M client associated with an API user.

        Args:

        Returns:
            ClientCredentials
        """

        response = self.make_request(
            method="post",
            url="/client/reset",
        )

        if response.status_code == 200:
            return ClientCredentials(**response.json())
        return response.json()

    def get_user_details(
        self,
    ) -> UserInfo:
        """
        Get User Details

        Retrieves the details of a user.

        Args:

        Returns:
            UserInfo
        """

        response = self.make_request(
            method="get",
            url="/user/details",
        )

        if response.status_code == 200:
            return UserInfo(**response.json())
        return response.json()

    def edit_user_settings(self, **kwargs: Unpack[UserSettings]) -> UserInfo:
        """
        Edit User Settings

        Updates user settings.

        Args:
            notifications (Union[None, list['NotificationUpdate']]): Update user notifications
                settings.A full list of notification preferences can be found with the GET user details
                endpoint. Sending empty or null objects will not modify existing preferences.

        Returns:
            UserInfo
        """

        response = self.make_request(
            method="put",
            url="/user/settings",
            json=kwargs,
        )

        if response.status_code == 200:
            return UserInfo(**response.json())
        return response.json()

    def get_user_client__contract_id__client_get(
        self,
        contract_id: UUID,
    ) -> ClientID:
        """
        Get User Client

        Retrieves the Client ID of an API user.

        Args:
            contract_id (UUID): Contract ID

        Returns:
            ClientID
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/client".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return ClientID(**response.json())
        if response.status_code == 204:
            return response.json()
        return response.json()

    def create_user_client__contract_id__client_post(
        self,
        contract_id: UUID,
    ) -> ClientCredentials:
        """
        Create User Client

        Creates an M2M client to grant API access to a user.

        Args:
            contract_id (UUID): Contract ID

        Returns:
            ClientCredentials
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/client".format(contract_id=contract_id),
        )

        if response.status_code == 201:
            return ClientCredentials(**response.json())
        return response.json()

    def rotate_client_secret__contract_id__client_reset_post(
        self,
        contract_id: UUID,
    ) -> ClientCredentials:
        """
        Rotate Client Secret

        Generates a new client secret for the M2M client associated with an API user.

        Args:
            contract_id (UUID): Contract ID

        Returns:
            ClientCredentials
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/client/reset".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return ClientCredentials(**response.json())
        return response.json()

    def get_user_details__contract_id__user_details_get(
        self,
        contract_id: UUID,
    ) -> UserInfoDeprecated:
        """
        Get User Details

        Retrieves the details of a user.

        Args:
            contract_id (UUID): Contract ID

        Returns:
            UserInfoDeprecated
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/user/details".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return UserInfoDeprecated(**response.json())
        return response.json()

    def credit__contract_id__wallet_credit_get(
        self,
        contract_id: UUID,
    ) -> CreditBalanceResponse:
        """
        Credit

        Returns the credit balance for the current billing cycle (UTC calendar month). This is calculated
        as the monthly credit limit for the contract minus the total credits used this month.

        Note: This endpoint is deprecated and will be removed in a future release. Please use the
        equivalent endpoint in the Wallet API - https://api.satellitevu.com/wallet/v1/docs.

        Args:
            contract_id (UUID): Contract ID.

        Returns:
            CreditBalanceResponse
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/wallet/credit".format(contract_id=contract_id),
        )

        if response.status_code == 200:
            return CreditBalanceResponse(**response.json())
        return response.json()

    def list_webhooks(
        self,
        per_page: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> ListWebhookResponse:
        """
        List Webhooks

        List all webhooks.

        Args:
            per_page (Union[None, int]): The number of webhooks to return per page. Default: 25.
            token (Union[None, str]): The pagination token

        Returns:
            ListWebhookResponse
        """

        params: dict[str, Any] = {}
        params["per_page"] = per_page

        json_token: Union[None, str]
        if isinstance(token, Unset):
            json_token = UNSET
        else:
            json_token = token
        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not UNSET and v is not None}
        response = self.make_request(
            method="get",
            url="/webhooks/",
            params=params,
        )

        if response.status_code == 200:
            return ListWebhookResponse(**response.json())
        return response.json()

    def create_webhook(self, **kwargs: Unpack[CoreWebhook]) -> CreateWebhookResponse:
        """
        Create Webhook

        Create a webhook.

        Args:
            event_types (list[Union[ResellerWebhookEvent, WebhookEvent]]): A list of events to
                subscribe to.
            name (str): The name of the webhook.
            url (str): The URL where you want to receive requests for events you are subscribed to.
                Must be HTTPS.

        Returns:
            CreateWebhookResponse
        """

        response = self.make_request(
            method="post",
            url="/webhooks/",
            json=kwargs,
        )

        if response.status_code == 200:
            return CreateWebhookResponse(**response.json())
        return response.json()

    def get_webhook(
        self,
        id: UUID,
    ) -> WebhookResponse:
        """
        Get Webhook

        Get information about an existing webhook.

        Args:
            id (UUID): The webhook ID.

        Returns:
            WebhookResponse
        """

        response = self.make_request(
            method="get",
            url="/webhooks/{id}".format(id=id),
        )

        if response.status_code == 200:
            return WebhookResponse(**response.json())
        return response.json()

    def delete_webhook(
        self,
        id: UUID,
    ) -> Any:
        """
        Delete Webhook

        Delete a webhook.

        Args:
            id (UUID): The webhook ID.

        Returns:
            Any
        """

        response = self.make_request(
            method="delete",
            url="/webhooks/{id}".format(id=id),
        )

        if response.status_code == 204:
            return response.json()
        return response.json()

    def edit_webhook(
        self, id: UUID, **kwargs: Unpack[EditWebhookPayload]
    ) -> WebhookResponse:
        """
        Edit Webhook

        Edit a webhook.

        Args:
            id (UUID): The webhook ID.
            active (Union[None, bool]): Whether the webhook should be active or not.
            event_types (Union[None, list[Union[ResellerWebhookEvent, WebhookEvent]]]): A list of
                events to subscribe to.
            name (Union[None, str]): The name of the webhook.

        Returns:
            WebhookResponse
        """

        response = self.make_request(
            method="patch",
            url="/webhooks/{id}".format(id=id),
            json=kwargs,
        )

        if response.status_code == 200:
            return WebhookResponse(**response.json())
        return response.json()

    def get_webhook_events(
        self,
    ) -> list["NotificationDescription"]:
        """
        Get Webhook Events

        View all webhook event types.

        Args:

        Returns:
            list['NotificationDescription']
        """

        response = self.make_request(
            method="get",
            url="/webhooks/events",
        )

        if response.status_code == 200:
            return list["NotificationDescription"](**response.json())
        return response.json()

    def rotate_webhook_signing_key(
        self,
        id: UUID,
    ) -> PostWebhookResponse:
        """
        Rotate Webhook Signing Key

        Rotate the signing key for a webhook.

        Args:
            id (UUID): The webhook ID.

        Returns:
            PostWebhookResponse
        """

        response = self.make_request(
            method="post",
            url="/webhooks/{id}/rotate".format(id=id),
        )

        if response.status_code == 200:
            return PostWebhookResponse(**response.json())
        return response.json()

    def test_webhook(
        self,
        id: UUID,
    ) -> TestWebhookResponse:
        """
        Test Webhook

        Test a webhook.

        Args:
            id (UUID): The webhook ID.

        Returns:
            TestWebhookResponse
        """

        response = self.make_request(
            method="post",
            url="/webhooks/{id}/test".format(id=id),
        )

        if response.status_code == 200:
            return TestWebhookResponse(**response.json())
        return response.json()
