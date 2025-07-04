import io
from collections.abc import Callable
from typing import Any, Dict, List, Union, Unpack
from uuid import UUID

from satvu_api_sdk.core import SDKClient

from cos.models.download_order_collections_type_0_item import (
    DownloadOrderCollectionsType0Item,
)
from cos.models.feature_collection_order import FeatureCollectionOrder
from cos.models.order_download_url import OrderDownloadUrl
from cos.models.order_item_download_url import OrderItemDownloadUrl
from cos.models.order_page import OrderPage
from cos.models.order_payload import OrderPayload
from cos.models.reseller_feature_collection_order import ResellerFeatureCollectionOrder
from cos.models.reseller_order_payload import ResellerOrderPayload


def disambiguate_union_response(response_data: dict, response_disambiguation: dict):
    """
    Select the best-matching model class to instantiate from the union.

    Args:
        response_data (dict): The response data to disambiguate.
        response_disambiguation (dict): Configuration for disambiguation.

    Returns:
        Any: The instantiated model or the original response data.
    """
    discriminator = response_disambiguation.get("discriminator")
    mapping = response_disambiguation.get("discriminator_mapping")
    fallback_models = response_disambiguation.get("fallback_models")

    print(fallback_models)

    if discriminator and mapping and discriminator in response_data:
        disc_value = response_data[discriminator]
        model_cls = mapping.get(disc_value)
        if model_cls:
            try:
                return model_cls(**response_data)
            except Exception:
                pass

    def _type_matches(value, expected_type):
        if expected_type == UUID:
            return isinstance(value, str)
        origin = getattr(expected_type, "__origin__", None)
        if origin is not None:
            if origin is Union:
                return any(_type_matches(value, t) for t in expected_type.__args__)
            elif origin in {list, List}:
                return isinstance(value, list) and all(
                    _type_matches(v, expected_type.__args__[0]) for v in value
                )
            elif origin in {dict, Dict}:
                return isinstance(value, dict) and all(
                    _type_matches(v, expected_type.__args__[1]) for v in value.values()
                )

        if hasattr(expected_type, "get_required_fields_and_types"):
            return _required_fields_and_types_match(value, expected_type)
        return isinstance(value, expected_type)

    def _required_fields_and_types_match(data, model_cls):
        if not isinstance(data, dict):
            return False
        required = model_cls.get_required_fields_and_types()
        print(f"Required fields and types: {required}")
        return all(
            field in data and _type_matches(data[field], typ)
            for field, typ in required.items()
        )

    def _count_optional_matches(data, model_cls):
        if not isinstance(data, dict):
            return 0
        optional = model_cls.get_optional_fields_and_types()
        return sum(
            1
            for field, typ in optional.items()
            if field in data and _type_matches(data[field], typ)
        )

    response_fields = set(response_data.keys())
    candidates = []
    for model_cls in fallback_models:
        model_cls = eval(model_cls)
        if model_cls.get_required_fields().issubset(response_fields):
            print("X")
            if _required_fields_and_types_match(response_data, model_cls):
                print("Y")
                matching_optional = _count_optional_matches(response_data, model_cls)
                candidates.append((model_cls, matching_optional))

    if candidates:
        candidates.sort(
            key=lambda x: (x[1], len(x[0].get_required_fields())), reverse=True
        )
        for model_cls, _ in candidates:
            try:
                return model_cls(**response_data)
            except Exception:
                continue

    return response_data


class CosService(SDKClient):
    base_path = "/orders/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_order_details(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Order details

        Retrieve order details for a specified Order ID owned by the authenticated user.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            # Use centrally-defined union disambiguation (handles recursive matching and discriminators)
            response_data = response.json()
            return disambiguate_union_response(
                response_data,
                {
                    "uses_discriminator": False,
                    "fallback_models": [
                        "FeatureCollectionOrder",
                        "ResellerFeatureCollectionOrder",
                    ],
                },
            )
        return response.json()

    def query_orders(
        self,
        contract_id: UUID,
        limit: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> OrderPage:
        """
        Query orders

        Retrieve all existing orders owned by the authenticated user.

        Args:
            contract_id (UUID): Contract ID.
            limit (Union[None, int]): The number of orders to return per page. Default: 25.
            token (Union[None, str]): The pagination token.

        Returns:
            OrderPage
        """

        params: dict[str, Any] = {}
        json_limit: Union[None, int] = limit

        params["limit"] = json_limit

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return OrderPage(**response.json())
        return response.json()

    def submit_order(
        self,
        contract_id: UUID,
        **kwargs: Unpack[Union["OrderPayload", "ResellerOrderPayload"]],
    ) -> Union["FeatureCollectionOrder", "ResellerFeatureCollectionOrder"]:
        """
        Submit order

        Create and submit a new imagery order of one or more items (maximum 100)
        from SatVu's imagery catalog. The order will be owned by the
        authenticated user.

        Args:
            contract_id (UUID): Contract ID.
            Either (OrderPayload):
                - item_id (Union[list[str], str]): Item ID.
            Or: (ResellerOrderPayload):
                - item_id (Union[list[str], str]): Item ID.
                - reseller_end_user_id (UUID):

        Returns:
            Union['FeatureCollectionOrder', 'ResellerFeatureCollectionOrder']
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/".format(contract_id=contract_id),
            json=kwargs,
        )

        if response.status_code == 201:
            # Use centrally-defined union disambiguation (handles recursive matching and discriminators)
            response_data = response.json()
            return disambiguate_union_response(
                response_data,
                {
                    "uses_discriminator": False,
                    "fallback_models": [
                        "FeatureCollectionOrder",
                        "ResellerFeatureCollectionOrder",
                    ],
                },
            )
        return response.json()

    def download_item(
        self,
        contract_id: UUID,
        order_id: UUID,
        item_id: str,
        redirect: Union[None, bool] = True,
    ) -> OrderItemDownloadUrl:
        """
        Item download

        Download an item, identified by its STAC ID, for a specified imagery order
        owned by the authenticated user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.
            item_id (str): Item ID.
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.

        Returns:
            OrderItemDownloadUrl
        """

        params: dict[str, Any] = {}
        params["redirect"] = redirect

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}/{item_id}/download".format(
                contract_id=contract_id, order_id=order_id, item_id=item_id
            ),
            params=params,
            follow_redirects=redirect,
            timeout=60 if redirect else 5,
        )

        if response.headers.get("Content-Type") == "application/zip":
            zip_bytes = io.BytesIO(response.content)
            return zip_bytes

        if response.status_code == 200:
            return OrderItemDownloadUrl(**response.json())
        if response.status_code == 202:
            return response.json()
        return response.json()

    def download_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        collections: Union[None, list[DownloadOrderCollectionsType0Item]] = None,
        redirect: Union[None, bool] = True,
    ) -> OrderDownloadUrl:
        """
        Order download

        Download all the items for a specified imagery order owned by the authenticated
        user.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID.
            order_id (UUID): Order ID.
            collections (Union[None, list[DownloadOrderCollectionsType0Item]]): Specify a subset of
                collections to download. Defaults to None, which will download only the visual product.
            redirect (Union[None, bool]): If `true` download the image content locally, otherwise if
                `false` return a presigned download URL with an expiry. Defaults to `true`. Default: True.

        Returns:
            OrderDownloadUrl
        """

        params: dict[str, Any] = {}
        json_collections: Union[None, list[str]] = collections

        if isinstance(collections, list):
            json_collections = []
            for collections_type_0_item_data in collections:
                collections_type_0_item = collections_type_0_item_data.value
                json_collections.append(collections_type_0_item)

        params["collections"] = json_collections

        params["redirect"] = redirect

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/{order_id}/download".format(
                contract_id=contract_id, order_id=order_id
            ),
            params=params,
            follow_redirects=redirect,
            timeout=60 if redirect else 5,
        )

        if response.headers.get("Content-Type") == "application/zip":
            zip_bytes = io.BytesIO(response.content)
            return zip_bytes

        if response.status_code == 200:
            return OrderDownloadUrl(**response.json())
        if response.status_code == 202:
            return response.json()
        return response.json()
