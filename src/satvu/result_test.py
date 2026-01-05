"""Tests for the Result type system."""

import pytest

from satvu.result import Err, Ok, Result, is_err, is_ok


class TestOk:
    """Tests for Ok variant."""

    def test_construction(self):
        """Ok can be constructed with any value."""
        assert Ok(42)._value == 42
        assert Ok("hello")._value == "hello"
        assert Ok(None)._value is None
        assert Ok([1, 2, 3])._value == [1, 2, 3]

    def test_is_ok_returns_true(self):
        """is_ok() returns True for Ok."""
        assert Ok(42).is_ok() is True

    def test_is_err_returns_false(self):
        """is_err() returns False for Ok."""
        assert Ok(42).is_err() is False

    def test_unwrap_returns_value(self):
        """unwrap() returns the contained value."""
        assert Ok(42).unwrap() == 42
        assert Ok("hello").unwrap() == "hello"

    def test_unwrap_or_returns_value_not_default(self):
        """unwrap_or() returns the value, ignoring default."""
        assert Ok(42).unwrap_or(0) == 42
        assert Ok("hello").unwrap_or("default") == "hello"

    def test_unwrap_or_else_returns_value_not_computed(self):
        """unwrap_or_else() returns the value, not calling the function."""
        called: list[str] = []
        result = Ok(42).unwrap_or_else(lambda e: called.append(e) or 0)  # type: ignore[arg-type]
        assert result == 42
        assert called == []  # Function was not called

    def test_expect_returns_value(self):
        """expect() returns the value for Ok."""
        assert Ok(42).expect("should not fail") == 42

    def test_map_transforms_value(self):
        """map() transforms the contained value."""
        result = Ok(5).map(lambda x: x * 2)
        assert isinstance(result, Ok)
        assert result.unwrap() == 10

    def test_map_with_type_change(self):
        """map() can change the value type."""
        result = Ok(42).map(str)
        assert result.unwrap() == "42"

    def test_map_err_is_noop(self):
        """map_err() does nothing for Ok."""
        original: Ok[int] = Ok(42)
        result = original.map_err(lambda e: e * 2)  # type: ignore[operator]
        assert result is original

    def test_and_then_chains_success(self):
        """and_then() chains operations."""
        result = Ok(5).and_then(lambda x: Ok(x * 2))
        assert isinstance(result, Ok)
        assert result.unwrap() == 10

    def test_and_then_can_return_err(self):
        """and_then() can turn Ok into Err."""
        result = Ok(5).and_then(lambda x: Err("failed") if x > 3 else Ok(x))
        assert isinstance(result, Err)
        assert result.error() == "failed"

    def test_or_else_is_noop(self):
        """or_else() does nothing for Ok."""
        original = Ok(42)
        result = original.or_else(lambda e: Ok(0))
        assert result is original

    def test_repr(self):
        """Ok has a useful repr."""
        assert repr(Ok(42)) == "Ok(42)"
        assert repr(Ok("hello")) == "Ok('hello')"

    def test_equality(self):
        """Ok values can be compared for equality."""
        assert Ok(42) == Ok(42)
        assert Ok("hello") == Ok("hello")
        assert Ok(42) != Ok(43)
        assert Ok(42) != Err(42)
        assert Ok(42) != 42

    def test_hash(self):
        """Ok values can be hashed."""
        assert hash(Ok(42)) == hash(Ok(42))
        assert hash(Ok(42)) != hash(Ok(43))
        # Can be used in sets
        s = {Ok(1), Ok(2), Ok(1)}
        assert len(s) == 2


class TestErr:
    """Tests for Err variant."""

    def test_construction(self):
        """Err can be constructed with any error value."""
        assert Err("error")._error == "error"
        assert Err(42)._error == 42
        assert Err(None)._error is None

    def test_is_ok_returns_false(self):
        """is_ok() returns False for Err."""
        assert Err("error").is_ok() is False

    def test_is_err_returns_true(self):
        """is_err() returns True for Err."""
        assert Err("error").is_err() is True

    def test_unwrap_raises(self):
        """unwrap() raises ValueError for Err."""
        with pytest.raises(ValueError, match="Called unwrap on Err"):
            Err("error").unwrap()

    def test_unwrap_or_returns_default(self):
        """unwrap_or() returns the default value."""
        assert Err("error").unwrap_or(42) == 42
        assert Err("error").unwrap_or("default") == "default"

    def test_unwrap_or_else_computes_from_error(self):
        """unwrap_or_else() computes value from error."""
        result = Err("hello").unwrap_or_else(lambda e: len(e))
        assert result == 5

    def test_expect_raises_with_message(self):
        """expect() raises with custom message for Err."""
        with pytest.raises(ValueError, match="operation failed"):
            Err("error").expect("operation failed")

    def test_error_returns_error_value(self):
        """error() returns the contained error."""
        assert Err("failed").error() == "failed"
        assert Err(42).error() == 42

    def test_map_is_noop(self):
        """map() does nothing for Err."""
        original: Err[str] = Err("error")
        result = original.map(lambda x: x * 2)  # type: ignore[operator]
        assert result is original

    def test_map_err_transforms_error(self):
        """map_err() transforms the error value."""
        result = Err(5).map_err(lambda e: e * 2)
        assert isinstance(result, Err)
        assert result.error() == 10

    def test_map_err_with_type_change(self):
        """map_err() can change the error type."""
        result = Err(42).map_err(str)
        assert result.error() == "42"

    def test_and_then_is_noop(self):
        """and_then() does nothing for Err."""
        original: Err[str] = Err("error")
        result = original.and_then(lambda x: Ok(x * 2))  # type: ignore[operator]
        assert result is original

    def test_or_else_provides_alternative(self):
        """or_else() provides alternative for Err."""
        result = Err("failed").or_else(lambda e: Ok("recovered"))
        assert isinstance(result, Ok)
        assert result.unwrap() == "recovered"

    def test_or_else_can_return_different_err(self):
        """or_else() can return a different Err."""
        result = Err("first").or_else(lambda e: Err(f"wrapped: {e}"))
        assert isinstance(result, Err)
        assert result.error() == "wrapped: first"

    def test_repr(self):
        """Err has a useful repr."""
        assert repr(Err("error")) == "Err('error')"
        assert repr(Err(42)) == "Err(42)"

    def test_equality(self):
        """Err values can be compared for equality."""
        assert Err("error") == Err("error")
        assert Err(42) == Err(42)
        assert Err("a") != Err("b")
        assert Err(42) != Ok(42)
        assert Err("error") != "error"

    def test_hash(self):
        """Err values can be hashed."""
        assert hash(Err("error")) == hash(Err("error"))
        assert hash(Err("a")) != hash(Err("b"))
        # Can be used in sets
        s = {Err("a"), Err("b"), Err("a")}
        assert len(s) == 2


class TestTypeGuards:
    """Tests for is_ok and is_err type guards."""

    def test_is_ok_with_ok(self):
        """is_ok() returns True for Ok."""
        result: Result[int, str] = Ok(42)
        assert is_ok(result) is True

    def test_is_ok_with_err(self):
        """is_ok() returns False for Err."""
        result: Result[int, str] = Err("error")
        assert is_ok(result) is False

    def test_is_err_with_err(self):
        """is_err() returns True for Err."""
        result: Result[int, str] = Err("error")
        assert is_err(result) is True

    def test_is_err_with_ok(self):
        """is_err() returns False for Ok."""
        result: Result[int, str] = Ok(42)
        assert is_err(result) is False


class TestChaining:
    """Tests for chaining multiple Result operations."""

    def test_railway_oriented_programming(self):
        """Multiple operations can be chained with and_then."""

        def parse_int(s: str) -> Result[int, str]:
            try:
                return Ok(int(s))
            except ValueError:
                return Err(f"not a number: {s}")

        def double(n: int) -> Result[int, str]:
            return Ok(n * 2)

        def check_positive(n: int) -> Result[int, str]:
            return Ok(n) if n > 0 else Err("not positive")

        # Success case
        result = parse_int("5").and_then(double).and_then(check_positive)
        assert is_ok(result)
        assert result.unwrap() == 10

        # Failure early
        result = parse_int("abc").and_then(double).and_then(check_positive)
        assert is_err(result)
        assert result.error() == "not a number: abc"

        # Failure late
        result = parse_int("-5").and_then(double).and_then(check_positive)
        assert is_err(result)
        assert result.error() == "not positive"

    def test_map_and_map_err_chain(self):
        """map and map_err can be chained."""
        ok_result: Result[int, str] = Ok(5)
        err_result: Result[int, str] = Err("error")

        # map only affects Ok
        assert ok_result.map(lambda x: x * 2).map(lambda x: x + 1).unwrap() == 11

        # map_err only affects Err
        final = err_result.map_err(str.upper).map_err(lambda s: f"[{s}]")
        assert final.error() == "[ERROR]"


class TestEdgeCases:
    """Tests for edge cases and special values."""

    def test_ok_with_none(self):
        """Ok can contain None."""
        result = Ok(None)
        assert result.is_ok()
        assert result.unwrap() is None

    def test_err_with_none(self):
        """Err can contain None."""
        result = Err(None)
        assert result.is_err()
        assert result.error() is None

    def test_ok_with_empty_string(self):
        """Ok can contain empty string."""
        result = Ok("")
        assert result.is_ok()
        assert result.unwrap() == ""

    def test_ok_with_zero(self):
        """Ok can contain zero."""
        result = Ok(0)
        assert result.is_ok()
        assert result.unwrap() == 0

    def test_nested_results(self):
        """Results can be nested."""
        nested: Result[Result[int, str], str] = Ok(Ok(42))
        assert is_ok(nested)
        inner = nested.unwrap()
        assert is_ok(inner)
        assert inner.unwrap() == 42
