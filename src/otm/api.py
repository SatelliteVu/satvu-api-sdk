import io
from collections.abc import Callable
from typing import Any, Dict, List, Union, Unpack
from uuid import UUID

from satvu_api_sdk.core import SDKClient

from otm.models.assured_order_request import AssuredOrderRequest
from otm.models.edit_order_payload import EditOrderPayload
from otm.models.feasibility_request import FeasibilityRequest
from otm.models.feasibility_response import FeasibilityResponse
from otm.models.get_order import GetOrder
from otm.models.order_item_download_url import OrderItemDownloadUrl
from otm.models.order_price import OrderPrice
from otm.models.price_request import PriceRequest
from otm.models.reseller_assured_order_request import ResellerAssuredOrderRequest
from otm.models.reseller_get_order import ResellerGetOrder
from otm.models.reseller_standard_order_request import ResellerStandardOrderRequest
from otm.models.reseller_stored_order_request import ResellerStoredOrderRequest
from otm.models.search_request import SearchRequest
from otm.models.search_response import SearchResponse
from otm.models.stac_feature import StacFeature
from otm.models.standard_order_request import StandardOrderRequest
from otm.models.stored_feasibility_feature_collection import (
    StoredFeasibilityFeatureCollection,
)
from otm.models.stored_feasibility_request import StoredFeasibilityRequest
from otm.models.stored_order_request import StoredOrderRequest
from otm.models.stored_order_request_list import StoredOrderRequestList


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


class OtmService(SDKClient):
    base_path = "/otm/v2"

    def __init__(self, get_token: Callable[[], str], env: str | None):
        super().__init__(env=env, get_token=get_token)

    def get_tasking_orders(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> StoredOrderRequestList:
        """
        List all tasking orders.

        Returns a list of your tasking orders. The orders are returned sorted by creation
        date, with the most recent orders appearing first.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page. Default: 25.
            token (Union[None, str]): The pagination token

        Returns:
            StoredOrderRequestList
        """

        params: dict[str, Any] = {}
        params["per_page"] = per_page

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return StoredOrderRequestList(**response.json())
        return response.json()

    def post_tasking_orders(
        self,
        contract_id: UUID,
        **kwargs: Unpack[
            Union[
                "AssuredOrderRequest",
                "ResellerAssuredOrderRequest",
                "ResellerStandardOrderRequest",
                "StandardOrderRequest",
            ]
        ],
    ) -> Union["ResellerStoredOrderRequest", "StoredOrderRequest"]:
        """
        Create a tasking order request.

        Creates a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            Either (StandardOrderRequest):
                - type (Literal['Feature']):
                - geometry (Point): Point Model
                - properties (StandardOrderRequestPropertiesWithAddons):
            Or: (AssuredOrderRequest):
                - properties (AssuredOrderRequestProperties):
            Or: (ResellerStandardOrderRequest):
                - type (Literal['Feature']):
                - geometry (Point): Point Model
                - properties (StandardOrderRequestPropertiesWithAddons):
                - reseller_end_user_id (UUID):
            Or: (ResellerAssuredOrderRequest):
                - properties (AssuredOrderRequestProperties):
                - reseller_end_user_id (UUID):

        Returns:
            Union['ResellerStoredOrderRequest', 'StoredOrderRequest']
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/orders/".format(contract_id=contract_id),
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
                        "ResellerStoredOrderRequest",
                        "StoredOrderRequest",
                    ],
                },
            )
        return response.json()

    def get_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Union["GetOrder", "ResellerGetOrder"]:
        """
        Retrieve a tasking order.

        Retrieves the tasking order with a given ID.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            Union['GetOrder', 'ResellerGetOrder']
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/{order_id}".format(
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
                    "fallback_models": ["GetOrder", "ResellerGetOrder"],
                },
            )
        return response.json()

    def edit_tasking_order(
        self, contract_id: UUID, order_id: UUID, **kwargs: Unpack[EditOrderPayload]
    ) -> Union["GetOrder", "ResellerGetOrder"]:
        """
        Edit a tasking order request.

        Edits a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
            properties (OrderName):

        Returns:
            Union['GetOrder', 'ResellerGetOrder']
        """

        response = self.make_request(
            method="patch",
            url="/{contract_id}/tasking/orders/{order_id}".format(
                contract_id=contract_id, order_id=order_id
            ),
            json=kwargs,
        )

        if response.status_code == 200:
            # Use centrally-defined union disambiguation (handles recursive matching and discriminators)
            response_data = response.json()
            return disambiguate_union_response(
                response_data,
                {
                    "uses_discriminator": False,
                    "fallback_models": ["GetOrder", "ResellerGetOrder"],
                },
            )
        return response.json()

    def cancel_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> Any:
        """
        Cancel a tasking order request.

        Cancels a tasking order request.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            Any
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/orders/{order_id}/cancel".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 204:
            return response.json()
        return response.json()

    def download_tasking_order(
        self,
        contract_id: UUID,
        order_id: UUID,
        redirect: Union[None, bool] = True,
    ) -> OrderItemDownloadUrl:
        """
        Download a tasking order.

        Download the item for a specified tasking order owned by the authenticated user,
        provided the order has been fulfilled.

        By default, the redirect parameter is set to True which allows the image
        content to be downloaded locally. If the redirect parameter is False, a
        presigned download URL with an expiry will be returned.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID
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
            url="/{contract_id}/tasking/orders/{order_id}/download".format(
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
            return OrderItemDownloadUrl(**response.json())
        if response.status_code == 202:
            return response.json()
        return response.json()

    def get_order_task_details(
        self,
        contract_id: UUID,
        order_id: UUID,
    ) -> StacFeature:
        """
        Retrieve acquisition details for a tasking order.

        Returns acquisition details for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            order_id (UUID): Order ID

        Returns:
            StacFeature
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/orders/{order_id}/acquisition/details".format(
                contract_id=contract_id, order_id=order_id
            ),
        )

        if response.status_code == 200:
            return StacFeature(**response.json())
        return response.json()

    def get_tasking_feasibility_requests(
        self,
        contract_id: UUID,
        per_page: Union[None, int] = 25,
        token: Union[None, str] = None,
    ) -> StoredFeasibilityFeatureCollection:
        """
        List all feasibility requests owned by a user.

        Retrieves all tasking feasibility requests owned by a user.

        Args:
            contract_id (UUID): Contract ID
            per_page (Union[None, int]): The number of orders to return per page Default: 25.
            token (Union[None, str]): The pagination token

        Returns:
            StoredFeasibilityFeatureCollection
        """

        params: dict[str, Any] = {}
        params["per_page"] = per_page

        json_token: Union[None, str] = token

        params["token"] = json_token

        params = {k: v for k, v in params.items() if v is not None}
        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/".format(contract_id=contract_id),
            params=params,
        )

        if response.status_code == 200:
            return StoredFeasibilityFeatureCollection(**response.json())
        return response.json()

    def post_tasking_feasibility(
        self, contract_id: UUID, **kwargs: Unpack[FeasibilityRequest]
    ) -> StoredFeasibilityRequest:
        """
        Create feasibility request.

        Searches feasibility options for a tasking order.

        Args:
            contract_id (UUID): Contract ID
            type (Literal['Feature']):
            geometry (Point): Point Model
            properties (Union['AssuredFeasibilityFields', 'StandardOrderRequestProperties']): A
                dictionary of additional metadata about the requested image.

        Returns:
            StoredFeasibilityRequest
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/feasibilities/".format(contract_id=contract_id),
            json=kwargs,
        )

        if response.status_code == 202:
            return StoredFeasibilityRequest(**response.json())
        return response.json()

    def get_tasking_feasibility_request(
        self,
        contract_id: UUID,
        id: UUID,
    ) -> StoredFeasibilityRequest:
        """
        Retrieve a feasibility request

        Retrieves the tasking feasibility request with a given ID.

        Args:
            contract_id (UUID): Contract ID
            id (UUID): Feasibility Request ID

        Returns:
            StoredFeasibilityRequest
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/{id}".format(
                contract_id=contract_id, id=id
            ),
        )

        if response.status_code == 200:
            return StoredFeasibilityRequest(**response.json())
        return response.json()

    def get_tasking_feasibility_response(
        self,
        contract_id: UUID,
        id: UUID,
    ) -> FeasibilityResponse:
        """
        Retrieve response for a feasibility request

        Retrieves the tasking feasibility response with a given request ID. Passes are returned
        in ascending order based on the start of the estimated acquisition time.

        Args:
            contract_id (UUID): Contract ID
            id (UUID): Feasibility Request ID

        Returns:
            FeasibilityResponse
        """

        response = self.make_request(
            method="get",
            url="/{contract_id}/tasking/feasibilities/{id}/response".format(
                contract_id=contract_id, id=id
            ),
        )

        if response.status_code == 200:
            return FeasibilityResponse(**response.json())
        return response.json()

    def get_price(
        self, contract_id: UUID, **kwargs: Unpack[PriceRequest]
    ) -> OrderPrice:
        """
        Get price for a set of ordering parameters.

        Returns the price for a set of ordering parameters.

        Args:
            contract_id (UUID): Contract ID
            type (Literal['Feature']):
            geometry (Point): Point Model
            properties (Union['AssuredFeasibilityFieldsWithAddons',
                'StandardOrderRequestPropertiesWithAddons']): A dictionary of additional metadata about
                the requested image.

        Returns:
            OrderPrice
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/tasking/price/".format(contract_id=contract_id),
            json=kwargs,
        )

        if response.status_code == 200:
            return OrderPrice(**response.json())
        return response.json()

    def post_search__contract_id__search__post(
        self, contract_id: UUID, **kwargs: Unpack[SearchRequest]
    ) -> SearchResponse:
        """
        Post Search

        Search for feasibility requests/responses and tasking orders owned by the user.

        Args:
            contract_id (UUID): Contract ID
            token (Union[None, str]): Pagination token.
            limit (Union[None, int]): Number of items to return per page.
            collections (Union[None, list[Collections]]): A list of collection types.
            ids (Union[None, list[UUID]]): A list of IDs.
            datetime_ (Union[None, str]):
            created_at (Union[None, str]): The datetime at which the entity was created.
            updated_at (Union[None, str]): The datetime at which the entity was last updated.
            properties (Union['FilterFields', None]): Allowed properties to filter a search.
                Filterable string fields allow one value or a list of values resulting in an equality or
                'IN' comparison respectively. For numeric fields, one value similarly achieves an equality
                operation. A tuple of 2 values can also be provided to search inclusively between a range.
            intersects (Union['GeometryCollection', 'LineString', 'MultiLineString', 'MultiPoint',
                'MultiPolygon', 'Point', 'Polygon', None]): A GeoJSON geometry to filter for. Items are
                returned if the geometry of theitem intersects with the geometry provided.
            sort_by (Union[None, list['SortEntities']]): Sort the order in which results are returned.

        Returns:
            SearchResponse
        """

        response = self.make_request(
            method="post",
            url="/{contract_id}/search/".format(contract_id=contract_id),
            json=kwargs,
        )

        if response.status_code == 200:
            return SearchResponse(**response.json())
        return response.json()
