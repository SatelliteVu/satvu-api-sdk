"""
Result type system for type-safe error handling.

This module provides Rust-style Result types with Ok and Err variants
for handling operations that may fail without using exceptions.
"""

from collections.abc import Callable
from typing import Generic, NoReturn, TypeGuard, TypeVar, Union

T = TypeVar("T")  # Success value type
E = TypeVar("E")  # Error value type
U = TypeVar("U")  # Mapped success value type (for transformations)
F = TypeVar("F")  # Mapped error value type (for transformations)


class Ok(Generic[T]):
    """Represents a successful result containing a value."""

    __slots__ = ("_value",)

    def __init__(self, value: T) -> None:
        """
        Initialize an Ok result.

        Args:
            value: The success value
        """
        self._value = value

    def is_ok(self) -> bool:
        """Check if this is an Ok result."""
        return True

    def is_err(self) -> bool:
        """Check if this is an Err result."""
        return False

    def unwrap(self) -> T:
        """
        Get the contained value.

        Returns:
            The success value

        Example:
            >>> result = Ok(42)
            >>> result.unwrap()
            42
        """
        return self._value

    def unwrap_or(self, default: T) -> T:
        """
        Get the contained value or a default.

        Args:
            default: Default value (ignored for Ok)

        Returns:
            The success value
        """
        return self._value

    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        """
        Get the contained value or compute from error.

        Args:
            op: Function to compute default (ignored for Ok)

        Returns:
            The success value
        """
        return self._value

    def expect(self, msg: str) -> T:
        """
        Get the contained value with a custom panic message.

        Args:
            msg: Custom message (ignored for Ok)

        Returns:
            The success value
        """
        return self._value

    def map(self, op: Callable[[T], U]) -> "Ok[U]":
        """
        Map the contained value.

        Args:
            op: Function to transform the value

        Returns:
            Ok with transformed value

        Example:
            >>> Ok(5).map(lambda x: x * 2)
            Ok(10)
        """
        return Ok(op(self._value))

    def map_err(self, op: Callable[[E], F]) -> "Ok[T]":
        """
        Map the error (no-op for Ok).

        Args:
            op: Function to transform error (ignored)

        Returns:
            Self unchanged
        """
        return self

    def and_then(self, op: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
        """
        Chain operations that may fail.

        Args:
            op: Function returning a Result

        Returns:
            Result from op

        Example:
            >>> Ok(5).and_then(lambda x: Ok(x * 2))
            Ok(10)
        """
        return op(self._value)

    def or_else(self, op: Callable[[E], "Result[T, F]"]) -> "Ok[T]":
        """
        Provide alternative on error (no-op for Ok).

        Args:
            op: Function to compute alternative (ignored)

        Returns:
            Self unchanged
        """
        return self

    def __repr__(self) -> str:
        return f"Ok({self._value!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Ok):
            return self._value == other._value
        return False

    def __hash__(self) -> int:
        return hash(("Ok", self._value))


class Err(Generic[E]):
    """Represents a failed result containing an error."""

    __slots__ = ("_error",)

    def __init__(self, error: E) -> None:
        """
        Initialize an Err result.

        Args:
            error: The error value
        """
        self._error = error

    def is_ok(self) -> bool:
        """Check if this is an Ok result."""
        return False

    def is_err(self) -> bool:
        """Check if this is an Err result."""
        return True

    def unwrap(self) -> NoReturn:
        """
        Get the contained value (raises for Err).

        Raises:
            ValueError: Always raised with the error details

        Example:
            >>> result = Err("failed")
            >>> result.unwrap()
            ValueError: Called unwrap on Err: 'failed'
        """
        raise ValueError(f"Called unwrap on Err: {self._error!r}")

    def unwrap_or(self, default: T) -> T:
        """
        Get the contained value or a default.

        Args:
            default: Default value to return

        Returns:
            The default value

        Example:
            >>> Err("failed").unwrap_or(42)
            42
        """
        return default

    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        """
        Get the contained value or compute from error.

        Args:
            op: Function to compute default from error

        Returns:
            Result of op(error)

        Example:
            >>> Err("failed").unwrap_or_else(lambda e: len(e))
            6
        """
        return op(self._error)

    def expect(self, msg: str) -> NoReturn:
        """
        Get the contained value with a custom panic message.

        Args:
            msg: Custom error message

        Raises:
            ValueError: Always raised with custom message

        Example:
            >>> Err("failed").expect("operation failed")
            ValueError: operation failed: 'failed'
        """
        raise ValueError(f"{msg}: {self._error!r}")

    def map(self, op: Callable[[T], U]) -> "Err[E]":
        """
        Map the contained value (no-op for Err).

        Args:
            op: Function to transform value (ignored)

        Returns:
            Self unchanged
        """
        return self

    def map_err(self, op: Callable[[E], F]) -> "Err[F]":
        """
        Map the error.

        Args:
            op: Function to transform the error

        Returns:
            Err with transformed error

        Example:
            >>> Err(5).map_err(lambda x: x * 2)
            Err(10)
        """
        return Err(op(self._error))

    def and_then(self, op: Callable[[T], "Result[U, E]"]) -> "Err[E]":
        """
        Chain operations that may fail (no-op for Err).

        Args:
            op: Function returning a Result (ignored)

        Returns:
            Self unchanged
        """
        return self

    def or_else(self, op: Callable[[E], "Result[T, F]"]) -> "Result[T, F]":
        """
        Provide alternative on error.

        Args:
            op: Function to compute alternative

        Returns:
            Result from op

        Example:
            >>> Err("failed").or_else(lambda e: Ok("default"))
            Ok("default")
        """
        return op(self._error)

    def error(self) -> E:
        """
        Get the contained error.

        Returns:
            The error value

        Example:
            >>> Err("failed").error()
            "failed"
        """
        return self._error

    def __repr__(self) -> str:
        return f"Err({self._error!r})"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Err):
            return self._error == other._error
        return False

    def __hash__(self) -> int:
        return hash(("Err", self._error))


# Type alias for Result
Result = Union[Ok[T], Err[E]]


# Type guard functions for better type narrowing
def is_ok(result: Result[T, E]) -> TypeGuard[Ok[T]]:
    """
    Type guard to check if a Result is Ok.

    Example:
        >>> result = some_operation()
        >>> if is_ok(result):
        ...     value = result.unwrap()  # Type checker knows this is Ok[T]
    """
    return isinstance(result, Ok)


def is_err(result: Result[T, E]) -> TypeGuard[Err[E]]:
    """
    Type guard to check if a Result is Err.

    Example:
        >>> result = some_operation()
        >>> if is_err(result):
        ...     error = result.error()  # Type checker knows this is Err[E]
    """
    return isinstance(result, Err)


__all__ = ["Ok", "Err", "Result", "is_ok", "is_err"]
