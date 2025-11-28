"""Detect endpoints that should have streaming download variants."""

from dataclasses import dataclass

from openapi_python_client.parser.openapi import Endpoint


@dataclass
class StreamingEndpointConfig:
    """Configuration for a streaming download endpoint."""

    base_method: str
    """Original generated method name (e.g., 'download_order__get')"""

    stream_method: str
    """Name for streaming variant (e.g., 'download_order_stream')"""

    url_pattern: str
    """URL pattern for the endpoint"""

    path_params: list[tuple[str, str]]
    """List of (name, type) tuples for path parameters (used in URL format)"""

    query_params: list[tuple[str, str]]
    """List of (name, type) tuples for query parameters (added to params dict)"""

    docstring: str
    """Description for streaming method"""

    example_filename: str
    """Example filename for docs"""

    default_chunk_size: int = 8192
    """Default chunk size in bytes"""


class StreamingEndpointDetector:
    """Detects which endpoints should have streaming download variants."""

    def __init__(self, api_id: str, openapi_dict: dict):
        self.api_id = api_id
        self.openapi_dict = openapi_dict

    def detect_all(self, endpoints: list[Endpoint]) -> list[StreamingEndpointConfig]:
        """
        Detect all endpoints that should have streaming variants.

        Detection strategy:
        - Extension-based only: Checks for x-streaming-download extension in OpenAPI spec
        - Streaming methods are only generated when explicitly marked with x-streaming-download: true

        Args:
            endpoints: List of parsed endpoints from OpenAPI spec

        Returns:
            List of streaming endpoint configurations
        """
        return [
            config
            for endpoint in endpoints
            if (config := self._check_streaming_extension(endpoint)) is not None
        ]

    def _check_streaming_extension(
        self, endpoint: Endpoint
    ) -> StreamingEndpointConfig | None:
        """
        Check if endpoint has x-streaming-download extension.

        Looks up the endpoint in openapi_dict['paths'] to find custom extensions.
        OpenAPI paths structure: openapi_dict['paths'][path][method]['x-streaming-download']

        Args:
            endpoint: Parsed endpoint from openapi-python-client

        Returns:
            StreamingEndpointConfig if extension found and enabled, None otherwise
        """
        # Look up path in OpenAPI dict
        paths = self.openapi_dict.get("paths", {})

        # Endpoint.path may have been modified by builder (e.g., version prefix stripped)
        # We need to reconstruct the original path by looking at all OpenAPI paths
        operation = None
        method = endpoint.method.lower()

        # Strategy 1: Try exact match first
        if endpoint.path in paths:
            operation = paths[endpoint.path].get(method)

        # Strategy 2: If not found, search by matching path structure
        # The builder may have stripped version prefixes like /v3
        if not operation:
            # Extract path segments from endpoint (without parameters)
            endpoint_segments = [
                seg
                for seg in endpoint.path.split("/")
                if seg and not seg.startswith("{")
            ]

            for path_pattern, path_item in paths.items():
                # Extract segments from OpenAPI path
                openapi_segments = [
                    seg
                    for seg in path_pattern.split("/")
                    if seg and not seg.startswith("{")
                ]

                # Match if the non-parameter segments align
                # (handles /v3/orders/download → /orders/download transformation)
                # Check if endpoint segments are a suffix of openapi segments
                if (
                    endpoint_segments
                    and openapi_segments
                    and openapi_segments[-len(endpoint_segments) :]
                ):
                    operation = path_item.get(method)
                    if operation:
                        break

        if not operation:
            return None

        # Check for x-streaming-download extension
        has_streaming = operation.get("x-streaming-download", False)

        if not has_streaming:
            return None

        # Get x-streaming-config if present
        streaming_config = operation.get("x-streaming-config", {})

        # Extract configuration values
        default_chunk_size = streaming_config.get("default_chunk_size", 8192)
        example_filename = streaming_config.get("example_filename", "download.zip")
        description_override = streaming_config.get("description_override")

        # Build config using extracted values
        return self._build_config(
            endpoint,
            example_filename=example_filename,
            default_chunk_size=default_chunk_size,
            description_override=description_override,
        )

    def _build_config(
        self,
        endpoint: Endpoint,
        example_filename: str = "download.zip",
        default_chunk_size: int = 8192,
        description_override: str | None = None,
    ) -> StreamingEndpointConfig:
        """Build streaming config from endpoint."""

        # Generate streaming method name
        base_method = endpoint.name
        stream_method = self._generate_stream_method_name(base_method)

        # Extract path parameters (used in URL format)
        path_params = [
            (param.python_name, param.get_type_string())
            for param in endpoint.path_parameters
        ]

        # Extract query parameters (added to params dict)
        # Filter out 'redirect' - we handle this internally
        query_params = []
        for param in endpoint.query_parameters:
            if param.python_name not in ["redirect"]:
                query_params.append((param.python_name, param.get_type_string()))

        # Generate docstring
        docstring = (
            description_override
            if description_override
            else self._generate_docstring(endpoint)
        )

        return StreamingEndpointConfig(
            base_method=base_method,
            stream_method=stream_method,
            url_pattern=endpoint.path,
            path_params=path_params,
            query_params=query_params,
            docstring=docstring,
            example_filename=example_filename,
            default_chunk_size=default_chunk_size,
        )

    def _generate_stream_method_name(self, base_method: str) -> str:
        """
        Generate streaming method name from base method.

        Examples:
            download_order__get → download_order_to_file
            download_item__get → download_item_to_file
            download_tasking_order → download_tasking_order_to_file
        """
        # Remove trailing __get suffix if present
        name = base_method.replace("__get", "")

        # Add _to_file suffix if not present
        if not name.endswith("_to_file"):
            name = f"{name}_to_file"

        return name

    def _generate_docstring(self, endpoint: Endpoint) -> str:
        """Generate docstring for streaming method."""
        if endpoint.summary:
            base = endpoint.summary.rstrip(".")
            return f"{base} - save to disk (memory-efficient for large files)."

        return "Save download to disk (memory-efficient for large files)."
