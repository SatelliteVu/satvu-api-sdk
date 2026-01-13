"""Detect endpoints that have pagination support and extract config for test generation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from openapi_python_client.parser.openapi import Endpoint

if TYPE_CHECKING:
    from builder.build import PaginationInfo


@dataclass
class PaginationEndpointConfig:
    """Configuration for a paginated endpoint's test generation."""

    base_method: str
    """Original generated method name (e.g., 'get_search')"""

    iter_method: str
    """Iterator method name (e.g., 'get_search_iter')"""

    http_method: str
    """HTTP method: 'get' or 'post'"""

    url_pattern: str
    """URL path pattern for the endpoint"""

    path_params: list[tuple[str, str]]
    """List of (name, type) tuples for path parameters"""

    query_params: list[tuple[str, str]]
    """List of (name, type) tuples for query parameters (excluding 'token')"""

    has_body: bool
    """True for POST methods with request body"""

    body_type: str | None
    """Body model type if POST method"""

    items_field: str
    """Field containing items array (e.g., 'features', 'orders')"""

    items_type: str | None
    """Type of items in the array"""

    response_type: str
    """Response model type (e.g., 'FeatureCollection')"""


class PaginationEndpointDetector:
    """Detects endpoints with pagination support and extracts test configuration."""

    def __init__(self, api_id: str):
        self.api_id = api_id

    def detect_all(
        self,
        endpoints: list[Endpoint],
        pagination_map: dict[str, PaginationInfo],
    ) -> list[PaginationEndpointConfig]:
        """
        Detect all endpoints with pagination and build test configs.

        Args:
            endpoints: List of parsed endpoints from OpenAPI spec
            pagination_map: Map of endpoint names to their PaginationInfo

        Returns:
            List of pagination endpoint configurations for test generation
        """
        configs = []

        for endpoint in endpoints:
            pagination_info = pagination_map.get(endpoint.name)
            if not pagination_info:
                continue

            config = self._build_config(endpoint, pagination_info)
            if config:
                configs.append(config)

        return configs

    def _build_config(
        self,
        endpoint: Endpoint,
        pagination_info: PaginationInfo,
    ) -> PaginationEndpointConfig | None:
        """Build pagination config from endpoint and pagination info."""
        # Get response type from 200 response
        response_type = None
        for response in endpoint.responses:
            if response.status_code.pattern == "200" and response.prop:
                response_type = response.prop.get_type_string()
                break

        if not response_type:
            return None

        # Extract path parameters
        path_params = [
            (str(param.python_name), param.get_type_string())
            for param in endpoint.path_parameters
        ]

        # Extract query parameters (excluding 'token')
        query_params = [
            (str(param.python_name), param.get_type_string())
            for param in endpoint.query_parameters
            if param.python_name != "token"
        ]

        # Determine if POST with body
        has_body = bool(endpoint.bodies)
        body_type = None
        if has_body and endpoint.bodies:
            body_type_str = endpoint.bodies[0].prop.get_type_string()
            # Extract non-None type from Union[None, ModelType] or Union[ModelType, None]
            body_type = self._extract_model_from_union(body_type_str)

        return PaginationEndpointConfig(
            base_method=endpoint.name,
            iter_method=f"{endpoint.name}_iter",
            http_method=endpoint.method.lower(),
            url_pattern=endpoint.path,
            path_params=path_params,
            query_params=query_params,
            has_body=has_body,
            body_type=body_type,
            items_field=pagination_info.items_field,
            items_type=pagination_info.items_type,
            response_type=response_type,
        )

    @staticmethod
    def _extract_model_from_union(type_str: str) -> str:
        """
        Extract the actual model type from a Union type string.

        Handles patterns like:
        - Union[None, PostSearchInput] -> PostSearchInput
        - Union[PostSearchInput, None] -> PostSearchInput
        - PostSearchInput -> PostSearchInput (passthrough)
        """
        if not type_str.startswith("Union["):
            return type_str

        # Remove Union[ and ] wrapper
        inner = type_str[6:-1]

        # Split by comma and find non-None type
        parts = [p.strip() for p in inner.split(",")]
        for part in parts:
            if part != "None":
                return part

        # Fallback to original if we couldn't parse
        return type_str
