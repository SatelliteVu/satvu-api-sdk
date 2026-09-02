"""Helpers for openapi-python-client's tainted string wrappers.

Since 0.29.1 the generator wraps generated code in `strings.PythonCode` and raw
OpenAPI document text in `schema.UntrustedString`. Neither is a `str` subclass, so
interpolating one straight into an f-string or a template emits its object repr
(`<openapi_python_client.strings.PythonCode object at 0x...>`) into the SDK instead
of failing loudly.

Rule for every builder patch, filter and template: unwrap on the way in, re-wrap on
the way out. Raw document text must go through `safe_for_docstring` or
`in_double_quote_literal` (both re-exported from `openapi_python_client.strings`)
rather than this module — it needs escaping, not just unwrapping.
"""

from openapi_python_client.strings import PythonCode

__all__ = ["unwrap_code"]


def unwrap_code(value: PythonCode | str) -> str:
    """Unwrap generated Python code so it can be embedded in a larger snippet."""
    if isinstance(value, PythonCode):
        return value.as_unembedded_code()
    return value
