"""
Tests for TypeAdapter-based parsing in parsing.py

These tests verify that Pydantic's TypeAdapter correctly handles:
- Union type resolution
- Nested models
- Type coercion
- Validation errors
"""

from typing import Union

import pytest
from pydantic import BaseModel, Field

from satvu_api_sdk.shared.parsing import (
    _type_adapter_cache,
    parse_response,
)

# ============================================================================
# Test Fixtures - Minimal Pydantic Models
# ============================================================================


class SimpleOrder(BaseModel):
    """Basic order without reseller info"""

    id: str = Field(..., alias="id")
    name: str = Field(..., alias="name")
    amount: int = Field(..., alias="amount")


class ResellerOrder(BaseModel):
    """Order with reseller-specific field (discriminator)"""

    reseller_id: str = Field(..., alias="reseller_id")  # Unique field
    id: str = Field(..., alias="id")
    name: str = Field(..., alias="name")
    amount: int = Field(..., alias="amount")


class NestedContainer(BaseModel):
    """Model with nested Union field"""

    orders: list[SimpleOrder | ResellerOrder] = Field(..., alias="orders")
    total: int = Field(..., alias="total")


class DeeplyNestedParent(BaseModel):
    """Model with deeply nested Union fields"""

    container: NestedContainer = Field(..., alias="container")
    metadata: dict = Field(..., alias="metadata")


# ============================================================================
# Test Basic Parsing
# ============================================================================


class TestBasicParsing:
    """Tests for basic TypeAdapter parsing functionality"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_parses_simple_model(self):
        """Should parse a simple Pydantic model"""
        data = {"id": "O123", "name": "Basic Order", "amount": 100}
        result = parse_response(data, SimpleOrder)

        assert isinstance(result, SimpleOrder)
        assert result.id == "O123"
        assert result.name == "Basic Order"
        assert result.amount == 100

    def test_parses_list_of_models(self):
        """Should parse a list of models"""
        data = [
            {"id": "O1", "name": "Order 1", "amount": 100},
            {"id": "O2", "name": "Order 2", "amount": 200},
        ]

        result = parse_response(data, list[SimpleOrder])

        assert len(result) == 2
        assert all(isinstance(order, SimpleOrder) for order in result)

    def test_parses_union_types(self):
        """Should parse Union types correctly"""
        annotation = Union[SimpleOrder, ResellerOrder]

        # Parse SimpleOrder
        data1 = {"id": "O1", "name": "Order 1", "amount": 100}
        result1 = parse_response(data1, annotation)
        assert isinstance(result1, SimpleOrder)

        # Parse ResellerOrder (has extra field)
        data2 = {"id": "O2", "name": "Order 2", "amount": 200, "reseller_id": "R123"}
        result2 = parse_response(data2, annotation)
        assert isinstance(result2, ResellerOrder)

    def test_parses_optional_types(self):
        """Should handle Union[Model, None] correctly"""
        annotation = Union[SimpleOrder, None]

        # Parse None
        result_none = parse_response(None, annotation)
        assert result_none is None

        # Parse valid model
        data = {"id": "O123", "name": "Test", "amount": 100}
        result_model = parse_response(data, annotation)
        assert isinstance(result_model, SimpleOrder)


# ============================================================================
# Test Type Coercion
# ============================================================================


class TestTypeCoercion:
    """Tests for Pydantic's automatic type coercion"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_coerces_string_to_int(self):
        """Should coerce string to int automatically"""
        data = {"id": "O123", "name": "Test", "amount": "100"}  # amount is string
        result = parse_response(data, SimpleOrder)

        assert isinstance(result, SimpleOrder)
        assert result.amount == 100  # Coerced to int
        assert isinstance(result.amount, int)

    def test_handles_extra_fields(self):
        """Should ignore extra fields by default"""
        data = {
            "id": "O123",
            "name": "Test",
            "amount": 100,
            "extra_field": "ignored",  # Extra field
        }
        result = parse_response(data, SimpleOrder)

        assert isinstance(result, SimpleOrder)
        assert not hasattr(result, "extra_field")


# ============================================================================
# Test Nested Models
# ============================================================================


class TestNestedModels:
    """Tests for nested model parsing"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_parses_nested_unions(self):
        """Should handle Union nested inside model fields"""
        data = {
            "orders": [
                {"id": "O1", "name": "Order 1", "amount": 100},
                {"id": "O2", "name": "Order 2", "amount": 200, "reseller_id": "R1"},
            ],
            "total": 2,
        }

        result = parse_response(data, NestedContainer)

        assert isinstance(result, NestedContainer)
        assert len(result.orders) == 2
        assert isinstance(result.orders[0], SimpleOrder)
        assert isinstance(result.orders[1], ResellerOrder)
        assert result.total == 2

    def test_parses_deeply_nested_unions(self):
        """Should handle multiple levels of nesting"""
        data = {
            "container": {
                "orders": [
                    {"id": "O1", "name": "Order 1", "amount": 100},
                    {"id": "O2", "name": "Order 2", "amount": 200, "reseller_id": "R1"},
                ],
                "total": 2,
            },
            "metadata": {"created_by": "test"},
        }

        result = parse_response(data, DeeplyNestedParent)

        assert isinstance(result, DeeplyNestedParent)
        assert isinstance(result.container, NestedContainer)
        assert len(result.container.orders) == 2
        assert isinstance(result.container.orders[0], SimpleOrder)
        assert isinstance(result.container.orders[1], ResellerOrder)


# ============================================================================
# Test Caching
# ============================================================================


class TestCaching:
    """Tests for TypeAdapter caching behavior"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_type_adapter_cache_is_populated(self):
        """Should populate cache on first parse"""
        assert len(_type_adapter_cache) == 0

        data = {"id": "O123", "name": "Test", "amount": 100}
        parse_response(data, SimpleOrder)

        assert len(_type_adapter_cache) == 1

    def test_type_adapter_cache_is_reused(self):
        """Should reuse cached TypeAdapter"""
        data1 = {"id": "O1", "name": "Test1", "amount": 100}
        data2 = {"id": "O2", "name": "Test2", "amount": 200}

        # First parse - cache miss
        parse_response(data1, SimpleOrder)
        cache_size_after_first = len(_type_adapter_cache)

        # Second parse - cache hit
        parse_response(data2, SimpleOrder)
        cache_size_after_second = len(_type_adapter_cache)

        assert cache_size_after_first == cache_size_after_second == 1

    def test_different_annotations_get_separate_cache_entries(self):
        """Should create separate cache entries for different types"""
        simple_data = {"id": "O1", "name": "Test", "amount": 100}
        reseller_data = {"id": "O2", "name": "Test", "amount": 200, "reseller_id": "R1"}

        parse_response(simple_data, SimpleOrder)
        parse_response(reseller_data, ResellerOrder)

        assert len(_type_adapter_cache) == 2


# ============================================================================
# Test Error Handling
# ============================================================================


class TestErrorHandling:
    """Tests for error handling and error messages"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_raises_error_for_missing_required_fields(self):
        """Should raise ValueError when required fields are missing"""
        data = {"id": "O123"}  # Missing 'name' and 'amount'

        with pytest.raises(ValueError) as exc_info:
            parse_response(data, SimpleOrder)

        error_msg = str(exc_info.value)
        assert "Failed to parse data as" in error_msg
        assert "name" in error_msg.lower() or "amount" in error_msg.lower()

    def test_error_shows_data_keys(self):
        """Should show data keys in error message"""
        data = {"id": "test", "unknown_field": "value"}

        with pytest.raises(ValueError) as exc_info:
            parse_response(data, SimpleOrder)

        error_msg = str(exc_info.value)
        assert "Data keys:" in error_msg
        assert "id" in error_msg

    def test_error_shows_validation_details(self):
        """Should show detailed validation errors"""
        data = {
            "id": "test",
            "name": "Test",
            "amount": "not-a-number",
        }  # Invalid amount

        with pytest.raises(ValueError) as exc_info:
            parse_response(data, SimpleOrder)

        error_msg = str(exc_info.value)
        assert "Validation errors" in error_msg

    def test_error_for_type_mismatch(self):
        """Should raise error when data type doesn't match"""
        data = "not a dict"  # SimpleOrder expects dict

        with pytest.raises(ValueError) as exc_info:
            parse_response(data, SimpleOrder)

        error_msg = str(exc_info.value)
        assert "Data type:" in error_msg
        assert "str" in error_msg


# ============================================================================
# Test Union Resolution
# ============================================================================


class TestUnionResolution:
    """Tests for Pydantic's Union type resolution"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_resolves_union_by_unique_fields(self):
        """Should resolve Union based on unique fields"""
        annotation = Union[SimpleOrder, ResellerOrder]

        # Data without reseller_id -> SimpleOrder
        data1 = {"id": "O1", "name": "Order 1", "amount": 100}
        result1 = parse_response(data1, annotation)
        assert isinstance(result1, SimpleOrder)

        # Data with reseller_id -> ResellerOrder
        data2 = {"id": "O2", "name": "Order 2", "amount": 200, "reseller_id": "R123"}
        result2 = parse_response(data2, annotation)
        assert isinstance(result2, ResellerOrder)

    def test_resolves_union_in_lists(self):
        """Should resolve Union types in lists"""
        annotation = list[SimpleOrder | ResellerOrder]
        data = [
            {"id": "O1", "name": "Order 1", "amount": 100},
            {"id": "O2", "name": "Order 2", "amount": 200, "reseller_id": "R1"},
            {"id": "O3", "name": "Order 3", "amount": 300},
            {"id": "O4", "name": "Order 4", "amount": 400, "reseller_id": "R2"},
        ]

        result = parse_response(data, annotation)

        assert len(result) == 4
        assert isinstance(result[0], SimpleOrder)
        assert isinstance(result[1], ResellerOrder)
        assert isinstance(result[2], SimpleOrder)
        assert isinstance(result[3], ResellerOrder)


# ============================================================================
# Test Mixed Union Types
# ============================================================================


class TestMixedUnionTypes:
    """Tests for unions with primitives and models"""

    def setup_method(self):
        """Clear cache before each test"""
        _type_adapter_cache.clear()

    def test_union_with_primitives(self):
        """Should handle Union[Model, str, int]"""
        annotation = Union[SimpleOrder, str, int]

        # Test string
        result_str = parse_response("test", annotation)
        assert result_str == "test"
        assert isinstance(result_str, str)

        # Test int
        result_int = parse_response(42, annotation)
        assert result_int == 42
        assert isinstance(result_int, int)

        # Test model
        data = {"id": "O123", "name": "Test", "amount": 100}
        result_model = parse_response(data, annotation)
        assert isinstance(result_model, SimpleOrder)
