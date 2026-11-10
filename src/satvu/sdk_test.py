"""Tests for the SatVuSDK main entry point."""

from base64 import urlsafe_b64encode
from functools import partial
from json import dumps

import pook
import pytest
import requests

from satvu.auth import MemoryCache
from satvu.http import create_http_client
from satvu.result import is_ok
from satvu.sdk import SatVuSDK
from satvu.services.otm import models as otm_models


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


class TestVersionedServices:
    """Versioned APIs: the bare accessor is the stable version, pinned ones hang off it."""

    @pytest.fixture
    def sdk(self):
        return SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            timeout=120,
            max_retry_attempts=10,
        )

    def test_bare_accessor_is_stable_version(self, sdk):
        assert type(sdk.otm).__bases__ == (type(sdk.otm.v2),)

    def test_pinned_version_is_cached_and_separate(self, sdk):
        assert sdk.otm.v2 is sdk.otm.v2
        assert sdk.otm.v2 is not sdk.otm

    def test_pinned_stable_version_shares_http_client(self, sdk):
        assert sdk.otm.v2.client is sdk.otm.client

    def test_config_propagated_to_pinned_version(self, sdk):
        assert sdk.otm.v2.timeout == 120
        assert sdk.otm.v2.max_retry_attempts == 10
        assert sdk.otm.v2.base_path == sdk.otm.base_path

    def test_stable_models_reexported(self):
        assert all(
            getattr(otm_models, name).__module__.startswith("satvu.services.otm.v2.")
            for name in otm_models.__all__
        )


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

    def test_token_expiry_margin_propagated_to_auth(self):
        """Token expiry margin is propagated to AuthService."""
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            token_expiry_margin=30,
        )
        assert sdk.auth.token_expiry_margin == 30

    def test_invalid_token_expiry_margin_env_fails_on_init(self, monkeypatch):
        """A bad env value raises at construction, not on the first request."""
        monkeypatch.setenv("SATVU_TOKEN_EXPIRY_MARGIN_SECONDS", "soon")
        with pytest.raises(ValueError, match="SATVU_TOKEN_EXPIRY_MARGIN_SECONDS"):
            SatVuSDK(
                client_id="test_id",
                client_secret="test_secret",  # pragma: allowlist secret
            )

    def test_token_cache_propagated_to_auth(self):
        """Token cache is propagated to AuthService."""
        cache = MemoryCache()
        sdk = SatVuSDK(
            client_id="test_id",
            client_secret="test_secret",  # pragma: allowlist secret
            token_cache=cache,
        )
        assert sdk.auth.cache is cache


def _jwt(exp: int) -> str:
    payload = urlsafe_b64encode(dumps({"exp": exp}).encode()).decode().rstrip("=")
    return f"header.{payload}.signature"


@pytest.fixture(
    params=[partial(create_http_client, backend="stdlib"), requests.Session],
    ids=["adapter", "library-client"],
)
def http_client(request):
    client = request.param()
    yield client
    if isinstance(client, requests.Session):
        client.close()


def test_shared_http_client_built_on_first_use():
    """No HTTP client is built until a service is used (keeps cold starts cheap)."""
    sdk = SatVuSDK("test_id", "test_secret")  # pragma: allowlist secret
    assert sdk._shared_client is None

    _ = sdk.wallet
    assert sdk._shared_client is not None
    assert sdk.wallet.client is sdk._shared_client


@pook.on
def test_custom_http_client_shared_across_services(http_client):
    """One client serves auth and every service, each at its own URL."""
    token = _jwt(exp=4_102_444_800)  # 2100-01-01
    pook.post("https://auth.qa.satellitevu.com/oauth/token").reply(200).json(
        {"access_token": token, "token_type": "Bearer", "expires_in": 3600}
    )
    for path in ("/wallet/v1/balances", "/catalog/v1/collections"):
        pook.get(f"https://api.qa.satellitevu.com{path}").header(
            "Authorization", f"Bearer {token}"
        ).reply(200).json({})
    sdk = SatVuSDK(
        "test_id",
        "test_secret",  # pragma: allowlist secret
        env="qa",
        http_client=http_client,
    )

    assert is_ok(sdk.wallet.make_request("GET", "/balances"))
    assert is_ok(sdk.catalog.make_request("GET", "/collections"))
    assert sdk.wallet.client is sdk.catalog.client is sdk.auth.client
    assert sdk.http_client is http_client
