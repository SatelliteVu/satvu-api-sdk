"""Tests for the SatVuSDK main entry point."""

from satvu.auth import MemoryCache
from satvu.sdk import SatVuSDK


class TestSatVuSDKInit:
    """Tests for SatVuSDK initialization."""

    def test_init_minimal(self):
        """SDK can be initialized with just credentials."""
        sdk = SatVuSDK(
            client_id="test_id", client_secret="test_secret"
        )  # pragma: allowlist secret
        assert sdk.client_id == "test_id"
        assert sdk.client_secret == "test_secret"  # pragma: allowlist secret

    def test_init_with_token_cache(self):
        """SDK can be initialized with custom token cache."""
        cache = MemoryCache()
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            token_cache=cache,
        )
        assert sdk.token_cache is cache

    def test_init_with_timeout(self):
        """SDK can be initialized with custom timeout."""
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            timeout=60,
        )
        assert sdk.timeout == 60

    def test_init_with_retry_config(self):
        """SDK can be initialized with custom retry configuration."""
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            max_retry_attempts=10,
            max_retry_after_seconds=600.0,
        )
        assert sdk.max_retry_attempts == 10
        assert sdk.max_retry_after_seconds == 600.0

    def test_init_defaults(self):
        """SDK has sensible defaults."""
        sdk = SatVuSDK(
            client_id="test_id", client_secret="test_secret"
        )  # pragma: allowlist secret
        assert sdk.env is None
        assert sdk.token_cache is None
        assert sdk.http_client is None
        assert sdk.timeout == 30
        assert sdk.max_retry_attempts == 5
        assert sdk.max_retry_after_seconds == 300.0


class TestLazyServiceInitialization:
    """Tests for lazy service initialization."""

    def test_services_not_created_on_init(self):
        """Services are not created during SDK initialization."""
        sdk = SatVuSDK(
            client_id="test_id", client_secret="test_secret"
        )  # pragma: allowlist secret
        assert sdk._auth is None
        assert sdk._catalog is None
        assert sdk._cos is None
        assert sdk._id is None
        assert sdk._otm is None
        assert sdk._policy is None
        assert sdk._reseller is None
        assert sdk._wallet is None

    def test_auth_created_on_access(self):
        """AuthService is created on first access."""
        sdk = SatVuSDK(
            client_id="test_id", client_secret="test_secret"
        )  # pragma: allowlist secret
        assert sdk._auth is None
        _ = sdk.auth
        assert sdk._auth is not None

    def test_catalog_created_on_access(self):
        """CatalogService is created on first access."""
        sdk = SatVuSDK(
            client_id="test_id", client_secret="test_secret"
        )  # pragma: allowlist secret
        assert sdk._catalog is None
        _ = sdk.catalog
        assert sdk._catalog is not None

    def test_services_cached(self):
        """Services are cached after first access."""
        sdk = SatVuSDK(
            client_id="test_id", client_secret="test_secret"
        )  # pragma: allowlist secret
        auth1 = sdk.auth
        auth2 = sdk.auth
        assert auth1 is auth2

        catalog1 = sdk.catalog
        catalog2 = sdk.catalog
        assert catalog1 is catalog2


class TestConfigPropagation:
    """Tests for configuration propagation to services."""

    def test_timeout_propagated_to_services(self):
        """Timeout is propagated to services."""
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            timeout=120,
        )
        assert sdk.auth.timeout == 120
        assert sdk.catalog.timeout == 120

    def test_retry_config_propagated(self):
        """Retry configuration is propagated to services."""
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            max_retry_attempts=10,
            max_retry_after_seconds=600.0,
        )
        assert sdk.catalog.max_retry_attempts == 10
        assert sdk.catalog.max_retry_after_seconds == 600.0

    def test_token_cache_propagated_to_auth(self):
        """Token cache is propagated to AuthService."""
        cache = MemoryCache()
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            token_cache=cache,
        )
        assert sdk.auth.cache is cache
