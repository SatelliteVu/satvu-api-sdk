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

    params: list[tuple[str, str]]
    """List of (name, type) tuples for parameters"""

    docstring: str
    """Description for streaming method"""

    example_filename: str
    """Example filename for docs"""

    default_chunk_size: int = 8192
    """Default chunk size in bytes"""


class StreamingEndpointDetector:
    """Detects which endpoints should have streaming download variants."""

    def __init__(self, api_id: str):
        self.api_id = api_id

    def detect_all(self, endpoints: list[Endpoint]) -> list[StreamingEndpointConfig]:
        """
        Detect all endpoints that should have streaming variants.

        Detection strategy (in order of priority):
        1. Pattern: Path contains '/download' and has redirect parameter
        2. Response: Returns binary content types (application/zip, etc.)

        Args:
            endpoints: List of parsed endpoints from OpenAPI spec

        Returns:
            List of streaming endpoint configurations
        """
        streaming_configs = []

        for endpoint in endpoints:
            config = self._detect_endpoint(endpoint)
            if config:
                streaming_configs.append(config)

        return streaming_configs

    def _detect_endpoint(self, endpoint: Endpoint) -> StreamingEndpointConfig | None:
        """Detect if a single endpoint should have streaming variant."""

        # Strategy 1: Pattern-based detection
        # Check for download endpoints with redirect parameter
        if self._is_download_endpoint_by_pattern(endpoint):
            return self._build_config_from_pattern(endpoint)

        # Strategy 2: Response type detection
        # Check for endpoints that return binary content
        if self._has_binary_response(endpoint):
            return self._build_config_from_response(endpoint)

        return None

    def _is_download_endpoint_by_pattern(self, endpoint: Endpoint) -> bool:
        """
        Detect download endpoints by pattern matching.

        Heuristics:
        - Path contains '/download'
        - Has 'redirect' query parameter (common pattern)
        - HTTP method is GET
        """
        is_get = endpoint.method.lower() == "get"
        has_download_path = "/download" in endpoint.path.lower()
        has_redirect_param = any(
            p.python_name == "redirect" for p in endpoint.query_parameters
        )

        return is_get and has_download_path and has_redirect_param

    def _has_binary_response(self, endpoint: Endpoint) -> bool:
        """Check if endpoint returns binary content."""
        # Check for 3xx redirect responses (common for file downloads)
        has_redirect = any(
            r.status_code.pattern.startswith("3") for r in endpoint.responses
        )

        # Could also check response content types if available in parsed data
        return has_redirect

    def _build_config_from_pattern(self, endpoint: Endpoint) -> StreamingEndpointConfig:
        """Build config from pattern detection."""
        return self._build_config(endpoint)

    def _build_config_from_response(
        self, endpoint: Endpoint
    ) -> StreamingEndpointConfig:
        """Build config from response type detection."""
        return self._build_config(endpoint)

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

        # Extract parameters
        params = []
        for param in endpoint.path_parameters:
            params.append((param.python_name, param.get_type_string()))

        # Filter out 'redirect' from query params (we handle this internally)
        # Also filter out 'collections' if it exists (optional parameter)
        for param in endpoint.query_parameters:
            if param.python_name not in ["redirect"]:
                params.append((param.python_name, param.get_type_string()))

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
            params=params,
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
