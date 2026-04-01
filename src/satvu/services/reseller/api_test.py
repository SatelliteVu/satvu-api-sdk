# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/test_module.py.jinja
"""
Tests for reseller service.

Generated from OpenAPI spec version 0.1.0.
Uses property-based testing with hypothesis-jsonschema.
"""

from unittest.mock import Mock

import pook
import pytest
from hypothesis import HealthCheck, given, settings
from pydantic import TypeAdapter

from satvu import SatVuSDK, create_http_client
from satvu.http.errors import ClientError
from satvu.services.reseller.models.create_user import CreateUser
from satvu.services.reseller.models.get_companies import GetCompanies
from satvu.services.reseller.models.get_users import GetUsers
from satvu.services.reseller.models.search_companies import SearchCompanies
from satvu.services.reseller.models.search_users import SearchUsers

from .test_schemas import get_request_body_strategy, get_response_strategy


@pytest.mark.parametrize("backend", ["stdlib", "httpx", "urllib3", "requests"])
class TestResellerService:
    """Property-based tests for ResellerService."""

    @pytest.fixture(autouse=True)
    def setup(self, backend):
        """Set up test fixtures before each test method."""
        mock_get_token = Mock(return_value="test_token")
        subdomain = "api"
        env_part = "qa."
        base_path = "/resellers/v1"
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
        self.sdk.reseller._get_token = mock_get_token

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
        response_data=get_response_strategy("/user", "post", "201"),
        body_data=get_request_body_strategy("/user", "post"),
    )
    def test_create_users_201(self, backend, response_data, body_data):
        """
        Test create_users with 201 response.
        """
        path = "/user"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(201).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(list[CreateUser])
        body = body_adapter.validate_python(body_data)
        result = self.sdk.reseller.create_users(items=body)
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
    @given(
        response_data=get_response_strategy("/user", "post", "422"),
        body_data=get_request_body_strategy("/user", "post"),
    )
    def test_create_users_422_error(self, backend, response_data, body_data):
        """
        Test create_users with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/user"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body_adapter = TypeAdapter(list[CreateUser])
        body = body_adapter.validate_python(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.reseller.create_users(items=body)
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
    @given(response_data=get_response_strategy("/users", "get", "200"))
    def test_get_users_200(self, backend, response_data):
        """
        Test get_users with 200 response.
        """
        path = "/users"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.reseller.get_users()
        assert result is not None
        assert isinstance(result, GetUsers)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/users", "get", "422"))
    def test_get_users_422_error(self, backend, response_data):
        """
        Test get_users with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/users"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.reseller.get_users()
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
    @given(response_data=get_response_strategy("/companies", "get", "200"))
    def test_get_companies_200(self, backend, response_data):
        """
        Test get_companies with 200 response.
        """
        path = "/companies"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        result = self.sdk.reseller.get_companies()
        assert result is not None
        assert isinstance(result, GetCompanies)

    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[
            HealthCheck.filter_too_much,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
        ],
    )
    @given(response_data=get_response_strategy("/companies", "get", "422"))
    def test_get_companies_422_error(self, backend, response_data):
        """
        Test get_companies with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/companies"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.get(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        with pytest.raises(ClientError) as exc_info:
            self.sdk.reseller.get_companies()
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
        response_data=get_response_strategy("/search/users", "post", "200"),
        body_data=get_request_body_strategy("/search/users", "post"),
    )
    def test_search_users_200(self, backend, response_data, body_data):
        """
        Test search_users with 200 response.
        """
        path = "/search/users"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchUsers.model_validate(body_data)
        result = self.sdk.reseller.search_users(body=body)
        assert result is not None
        assert isinstance(result, GetUsers)

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
        response_data=get_response_strategy("/search/users", "post", "422"),
        body_data=get_request_body_strategy("/search/users", "post"),
    )
    def test_search_users_422_error(self, backend, response_data, body_data):
        """
        Test search_users with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/search/users"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchUsers.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.reseller.search_users(body=body)
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
        response_data=get_response_strategy("/search/companies", "post", "200"),
        body_data=get_request_body_strategy("/search/companies", "post"),
    )
    def test_search_companies_200(self, backend, response_data, body_data):
        """
        Test search_companies with 200 response.
        """
        path = "/search/companies"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(200).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchCompanies.model_validate(body_data)
        result = self.sdk.reseller.search_companies(body=body)
        assert result is not None
        assert isinstance(result, GetCompanies)

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
        response_data=get_response_strategy("/search/companies", "post", "422"),
        body_data=get_request_body_strategy("/search/companies", "post"),
    )
    def test_search_companies_422_error(self, backend, response_data, body_data):
        """
        Test search_companies with 422 error response.

        HTTP 422 errors raise ClientError.
        """
        path = "/search/companies"
        url = f"{self.base_url}{path}"
        pook.reset()
        pook.on()
        pook.post(url).reply(422).json(response_data).header(
            "Content-Type", "application/json"
        )
        body = SearchCompanies.model_validate(body_data)
        with pytest.raises(ClientError) as exc_info:
            self.sdk.reseller.search_companies(body=body)
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
        page1_data=get_response_strategy("/users", "get", "200"),
        page2_data=get_response_strategy("/users", "get", "200"),
    )
    def test_get_users_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_users_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        path = "/users".format()
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
        pages = list(self.sdk.reseller.get_users_iter())
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
        page1_data=get_response_strategy("/users", "get", "200"),
        page2_data=get_response_strategy("/users", "get", "200"),
        page3_data=get_response_strategy("/users", "get", "200"),
    )
    def test_get_users_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_users_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        path = "/users".format()
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
        pages = list(self.sdk.reseller.get_users_iter(max_pages=2))
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
    @given(page_data=get_response_strategy("/users", "get", "200"))
    def test_get_users_iter_no_next_link(self, backend, page_data):
        """Test get_users_iter terminates when no next link present."""
        page_data = {**page_data}
        path = "/users".format()
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
        pages = list(self.sdk.reseller.get_users_iter())
        assert len(pages) == 1

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
        page1_data=get_response_strategy("/companies", "get", "200"),
        page2_data=get_response_strategy("/companies", "get", "200"),
    )
    def test_get_companies_iter_pagination(self, backend, page1_data, page2_data):
        """Test get_companies_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        path = "/companies".format()
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
        pages = list(self.sdk.reseller.get_companies_iter())
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
        page1_data=get_response_strategy("/companies", "get", "200"),
        page2_data=get_response_strategy("/companies", "get", "200"),
        page3_data=get_response_strategy("/companies", "get", "200"),
    )
    def test_get_companies_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test get_companies_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        path = "/companies".format()
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
        pages = list(self.sdk.reseller.get_companies_iter(max_pages=2))
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
    @given(page_data=get_response_strategy("/companies", "get", "200"))
    def test_get_companies_iter_no_next_link(self, backend, page_data):
        """Test get_companies_iter terminates when no next link present."""
        page_data = {**page_data}
        path = "/companies".format()
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
        pages = list(self.sdk.reseller.get_companies_iter())
        assert len(pages) == 1

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
        page1_data=get_response_strategy("/search/users", "post", "200"),
        page2_data=get_response_strategy("/search/users", "post", "200"),
    )
    def test_search_users_iter_pagination(self, backend, page1_data, page2_data):
        """Test search_users_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        path = "/search/users".format()
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
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        body = SearchUsers()
        pages = list(self.sdk.reseller.search_users_iter(body=body))
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
        page1_data=get_response_strategy("/search/users", "post", "200"),
        page2_data=get_response_strategy("/search/users", "post", "200"),
        page3_data=get_response_strategy("/search/users", "post", "200"),
    )
    def test_search_users_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test search_users_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        path = "/search/users".format()
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
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        body = SearchUsers()
        pages = list(self.sdk.reseller.search_users_iter(body=body, max_pages=2))
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
    @given(page_data=get_response_strategy("/search/users", "post", "200"))
    def test_search_users_iter_no_next_link(self, backend, page_data):
        """Test search_users_iter terminates when no next link present."""
        page_data = {**page_data}
        path = "/search/users".format()
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
        pook.post(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        body = SearchUsers()
        pages = list(self.sdk.reseller.search_users_iter(body=body))
        assert len(pages) == 1

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
        page1_data=get_response_strategy("/search/companies", "post", "200"),
        page2_data=get_response_strategy("/search/companies", "post", "200"),
    )
    def test_search_companies_iter_pagination(self, backend, page1_data, page2_data):
        """Test search_companies_iter follows next links correctly."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        path = "/search/companies".format()
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
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        body = SearchCompanies()
        pages = list(self.sdk.reseller.search_companies_iter(body=body))
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
        page1_data=get_response_strategy("/search/companies", "post", "200"),
        page2_data=get_response_strategy("/search/companies", "post", "200"),
        page3_data=get_response_strategy("/search/companies", "post", "200"),
    )
    def test_search_companies_iter_max_pages(
        self, backend, page1_data, page2_data, page3_data
    ):
        """Test search_companies_iter respects max_pages limit."""
        page1_data = {**page1_data}
        page2_data = {**page2_data}
        page3_data = {**page3_data}
        path = "/search/companies".format()
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
        pook.post(url).times(1).reply(200).json(page1_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page2_data).header(
            "Content-Type", "application/json"
        )
        pook.post(url).times(1).reply(200).json(page3_data).header(
            "Content-Type", "application/json"
        )
        body = SearchCompanies()
        pages = list(self.sdk.reseller.search_companies_iter(body=body, max_pages=2))
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
    @given(page_data=get_response_strategy("/search/companies", "post", "200"))
    def test_search_companies_iter_no_next_link(self, backend, page_data):
        """Test search_companies_iter terminates when no next link present."""
        page_data = {**page_data}
        path = "/search/companies".format()
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
        pook.post(url).times(1).reply(200).json(page_data).header(
            "Content-Type", "application/json"
        )
        body = SearchCompanies()
        pages = list(self.sdk.reseller.search_companies_iter(body=body))
        assert len(pages) == 1
