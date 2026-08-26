"""
Schemas for wallet service tests.

Generated from OpenAPI spec version v1.
These schemas are used with hypothesis-jsonschema to generate test data.

Stores entire OpenAPI spec as operations with helper functions for access.
"""

from satvu.services.example_cache import get_cached_example_strategy

# Spec hash for example cache invalidation
_SPEC_HASH = "prod-86c7c1c166f6d02b9793a5a40b58b572eba03ad6"

# Component schemas for $ref resolution (cleaned for JSON Schema draft-07)
_COMPONENTS = {
    "BatchBalanceResponse": {
        "description": "Response body for batch credit balance queries.",
        "properties": {
            "balances": {
                "additionalProperties": {"$ref": "#/definitions/CreditBalanceResponse"},
                "description": "Mapping of contract IDs to their credit balances.",
                "propertyNames": {"format": "uuid"},
                "title": "Balances",
                "type": "object",
            }
        },
        "required": ["balances"],
        "title": "BatchBalanceResponse",
        "type": "object",
    },
    "CreditBalanceResponse": {
        "description": "Response body for credit balance queries.",
        "properties": {
            "balance": {
                "description": "The "
                "credit "
                "balance "
                "of the "
                "user in "
                "minor "
                "currency "
                "units "
                "(e.g. "
                "pence, "
                "cents).",
                "examples": ["100000"],
                "title": "Balance",
                "type": "integer",
            },
            "billing_cycle": {
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "description": "The "
                "current "
                "billing "
                "cycle, "
                "for "
                "example "
                "the "
                "current "
                "calendar "
                "month "
                "(UTC). "
                "If "
                "the "
                "billing "
                "cycle "
                "is "
                "`null`, "
                "the "
                "billing "
                "period "
                "will "
                "be "
                "from "
                "the "
                "contract "
                "start "
                "date.",
                "examples": [None, "08-2026"],
                "title": "Billing Cycle",
            },
            "currency": {
                "description": "The currency of the credit balance.",
                "examples": ["GBP", "EUR", "USD"],
                "title": "Currency",
                "type": "string",
            },
        },
        "required": ["currency", "balance", "billing_cycle"],
        "title": "CreditBalanceResponse",
        "type": "object",
    },
    "HTTPValidationError": {
        "properties": {
            "detail": {
                "items": {"$ref": "#/definitions/ValidationError"},
                "title": "Detail",
                "type": "array",
            }
        },
        "title": "HTTPValidationError",
        "type": "object",
    },
    "ValidationError": {
        "properties": {
            "ctx": {"title": "Context", "type": "object"},
            "input": {"title": "Input"},
            "loc": {
                "items": {"anyOf": [{"type": "string"}, {"type": "integer"}]},
                "title": "Location",
                "type": "array",
            },
            "msg": {"title": "Message", "type": "string"},
            "type": {"title": "Error Type", "type": "string"},
        },
        "required": ["loc", "msg", "type"],
        "title": "ValidationError",
        "type": "object",
    },
}

# Operations: (path, method) -> {responses, requestBody, parameters}
# Each schema has definitions attached for $ref resolution
_OPERATIONS = {
    ("/balances", "get"): {
        "parameters": {},
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "BatchBalanceResponse": {
                            "description": "Response "
                            "body "
                            "for "
                            "batch "
                            "credit "
                            "balance "
                            "queries.",
                            "properties": {
                                "balances": {
                                    "additionalProperties": {
                                        "$ref": "#/definitions/CreditBalanceResponse"
                                    },
                                    "description": "Mapping "
                                    "of "
                                    "contract "
                                    "IDs "
                                    "to "
                                    "their "
                                    "credit "
                                    "balances.",
                                    "propertyNames": {"format": "uuid"},
                                    "title": "Balances",
                                    "type": "object",
                                }
                            },
                            "required": ["balances"],
                            "title": "BatchBalanceResponse",
                            "type": "object",
                        },
                        "CreditBalanceResponse": {
                            "description": "Response body for credit balance queries.",
                            "properties": {
                                "balance": {
                                    "description": "The "
                                    "credit "
                                    "balance "
                                    "of "
                                    "the "
                                    "user "
                                    "in "
                                    "minor "
                                    "currency "
                                    "units "
                                    "(e.g. "
                                    "pence, "
                                    "cents).",
                                    "examples": ["100000"],
                                    "title": "Balance",
                                    "type": "integer",
                                },
                                "billing_cycle": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "current "
                                    "billing "
                                    "cycle, "
                                    "for "
                                    "example "
                                    "the "
                                    "current "
                                    "calendar "
                                    "month "
                                    "(UTC). "
                                    "If "
                                    "the "
                                    "billing "
                                    "cycle "
                                    "is "
                                    "`null`, "
                                    "the "
                                    "billing "
                                    "period "
                                    "will "
                                    "be "
                                    "from "
                                    "the "
                                    "contract "
                                    "start "
                                    "date.",
                                    "examples": [None, "08-2026"],
                                    "title": "Billing Cycle",
                                },
                                "currency": {
                                    "description": "The "
                                    "currency "
                                    "of "
                                    "the "
                                    "credit "
                                    "balance.",
                                    "examples": ["GBP", "EUR", "USD"],
                                    "title": "Currency",
                                    "type": "string",
                                },
                            },
                            "required": ["currency", "balance", "billing_cycle"],
                            "title": "CreditBalanceResponse",
                            "type": "object",
                        },
                        "HTTPValidationError": {
                            "properties": {
                                "detail": {
                                    "items": {"$ref": "#/definitions/ValidationError"},
                                    "title": "Detail",
                                    "type": "array",
                                }
                            },
                            "title": "HTTPValidationError",
                            "type": "object",
                        },
                        "ValidationError": {
                            "properties": {
                                "ctx": {"title": "Context", "type": "object"},
                                "input": {"title": "Input"},
                                "loc": {
                                    "items": {
                                        "anyOf": [
                                            {"type": "string"},
                                            {"type": "integer"},
                                        ]
                                    },
                                    "title": "Location",
                                    "type": "array",
                                },
                                "msg": {"title": "Message", "type": "string"},
                                "type": {"title": "Error Type", "type": "string"},
                            },
                            "required": ["loc", "msg", "type"],
                            "title": "ValidationError",
                            "type": "object",
                        },
                    },
                    "description": "Response body for batch credit balance queries.",
                    "properties": {
                        "balances": {
                            "additionalProperties": {
                                "$ref": "#/definitions/CreditBalanceResponse"
                            },
                            "description": "Mapping "
                            "of "
                            "contract "
                            "IDs "
                            "to "
                            "their "
                            "credit "
                            "balances.",
                            "propertyNames": {"format": "uuid"},
                            "title": "Balances",
                            "type": "object",
                        }
                    },
                    "required": ["balances"],
                    "title": "BatchBalanceResponse",
                    "type": "object",
                },
            }
        },
    },
    ("/{contract_id}/credit", "get"): {
        "parameters": {},
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "BatchBalanceResponse": {
                            "description": "Response "
                            "body "
                            "for "
                            "batch "
                            "credit "
                            "balance "
                            "queries.",
                            "properties": {
                                "balances": {
                                    "additionalProperties": {
                                        "$ref": "#/definitions/CreditBalanceResponse"
                                    },
                                    "description": "Mapping "
                                    "of "
                                    "contract "
                                    "IDs "
                                    "to "
                                    "their "
                                    "credit "
                                    "balances.",
                                    "propertyNames": {"format": "uuid"},
                                    "title": "Balances",
                                    "type": "object",
                                }
                            },
                            "required": ["balances"],
                            "title": "BatchBalanceResponse",
                            "type": "object",
                        },
                        "CreditBalanceResponse": {
                            "description": "Response body for credit balance queries.",
                            "properties": {
                                "balance": {
                                    "description": "The "
                                    "credit "
                                    "balance "
                                    "of "
                                    "the "
                                    "user "
                                    "in "
                                    "minor "
                                    "currency "
                                    "units "
                                    "(e.g. "
                                    "pence, "
                                    "cents).",
                                    "examples": ["100000"],
                                    "title": "Balance",
                                    "type": "integer",
                                },
                                "billing_cycle": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "current "
                                    "billing "
                                    "cycle, "
                                    "for "
                                    "example "
                                    "the "
                                    "current "
                                    "calendar "
                                    "month "
                                    "(UTC). "
                                    "If "
                                    "the "
                                    "billing "
                                    "cycle "
                                    "is "
                                    "`null`, "
                                    "the "
                                    "billing "
                                    "period "
                                    "will "
                                    "be "
                                    "from "
                                    "the "
                                    "contract "
                                    "start "
                                    "date.",
                                    "examples": [None, "08-2026"],
                                    "title": "Billing Cycle",
                                },
                                "currency": {
                                    "description": "The "
                                    "currency "
                                    "of "
                                    "the "
                                    "credit "
                                    "balance.",
                                    "examples": ["GBP", "EUR", "USD"],
                                    "title": "Currency",
                                    "type": "string",
                                },
                            },
                            "required": ["currency", "balance", "billing_cycle"],
                            "title": "CreditBalanceResponse",
                            "type": "object",
                        },
                        "HTTPValidationError": {
                            "properties": {
                                "detail": {
                                    "items": {"$ref": "#/definitions/ValidationError"},
                                    "title": "Detail",
                                    "type": "array",
                                }
                            },
                            "title": "HTTPValidationError",
                            "type": "object",
                        },
                        "ValidationError": {
                            "properties": {
                                "ctx": {"title": "Context", "type": "object"},
                                "input": {"title": "Input"},
                                "loc": {
                                    "items": {
                                        "anyOf": [
                                            {"type": "string"},
                                            {"type": "integer"},
                                        ]
                                    },
                                    "title": "Location",
                                    "type": "array",
                                },
                                "msg": {"title": "Message", "type": "string"},
                                "type": {"title": "Error Type", "type": "string"},
                            },
                            "required": ["loc", "msg", "type"],
                            "title": "ValidationError",
                            "type": "object",
                        },
                    },
                    "description": "Response body for credit balance queries.",
                    "properties": {
                        "balance": {
                            "description": "The "
                            "credit "
                            "balance "
                            "of "
                            "the "
                            "user "
                            "in "
                            "minor "
                            "currency "
                            "units "
                            "(e.g. "
                            "pence, "
                            "cents).",
                            "examples": ["100000"],
                            "title": "Balance",
                            "type": "integer",
                        },
                        "billing_cycle": {
                            "anyOf": [{"type": "string"}, {"type": "null"}],
                            "description": "The "
                            "current "
                            "billing "
                            "cycle, "
                            "for "
                            "example "
                            "the "
                            "current "
                            "calendar "
                            "month "
                            "(UTC). "
                            "If "
                            "the "
                            "billing "
                            "cycle "
                            "is "
                            "`null`, "
                            "the "
                            "billing "
                            "period "
                            "will "
                            "be "
                            "from "
                            "the "
                            "contract "
                            "start "
                            "date.",
                            "examples": [None, "08-2026"],
                            "title": "Billing Cycle",
                        },
                        "currency": {
                            "description": "The currency of the credit balance.",
                            "examples": ["GBP", "EUR", "USD"],
                            "title": "Currency",
                            "type": "string",
                        },
                    },
                    "required": ["currency", "balance", "billing_cycle"],
                    "title": "CreditBalanceResponse",
                    "type": "object",
                },
            },
            "422": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "BatchBalanceResponse": {
                            "description": "Response "
                            "body "
                            "for "
                            "batch "
                            "credit "
                            "balance "
                            "queries.",
                            "properties": {
                                "balances": {
                                    "additionalProperties": {
                                        "$ref": "#/definitions/CreditBalanceResponse"
                                    },
                                    "description": "Mapping "
                                    "of "
                                    "contract "
                                    "IDs "
                                    "to "
                                    "their "
                                    "credit "
                                    "balances.",
                                    "propertyNames": {"format": "uuid"},
                                    "title": "Balances",
                                    "type": "object",
                                }
                            },
                            "required": ["balances"],
                            "title": "BatchBalanceResponse",
                            "type": "object",
                        },
                        "CreditBalanceResponse": {
                            "description": "Response body for credit balance queries.",
                            "properties": {
                                "balance": {
                                    "description": "The "
                                    "credit "
                                    "balance "
                                    "of "
                                    "the "
                                    "user "
                                    "in "
                                    "minor "
                                    "currency "
                                    "units "
                                    "(e.g. "
                                    "pence, "
                                    "cents).",
                                    "examples": ["100000"],
                                    "title": "Balance",
                                    "type": "integer",
                                },
                                "billing_cycle": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "current "
                                    "billing "
                                    "cycle, "
                                    "for "
                                    "example "
                                    "the "
                                    "current "
                                    "calendar "
                                    "month "
                                    "(UTC). "
                                    "If "
                                    "the "
                                    "billing "
                                    "cycle "
                                    "is "
                                    "`null`, "
                                    "the "
                                    "billing "
                                    "period "
                                    "will "
                                    "be "
                                    "from "
                                    "the "
                                    "contract "
                                    "start "
                                    "date.",
                                    "examples": [None, "08-2026"],
                                    "title": "Billing Cycle",
                                },
                                "currency": {
                                    "description": "The "
                                    "currency "
                                    "of "
                                    "the "
                                    "credit "
                                    "balance.",
                                    "examples": ["GBP", "EUR", "USD"],
                                    "title": "Currency",
                                    "type": "string",
                                },
                            },
                            "required": ["currency", "balance", "billing_cycle"],
                            "title": "CreditBalanceResponse",
                            "type": "object",
                        },
                        "HTTPValidationError": {
                            "properties": {
                                "detail": {
                                    "items": {"$ref": "#/definitions/ValidationError"},
                                    "title": "Detail",
                                    "type": "array",
                                }
                            },
                            "title": "HTTPValidationError",
                            "type": "object",
                        },
                        "ValidationError": {
                            "properties": {
                                "ctx": {"title": "Context", "type": "object"},
                                "input": {"title": "Input"},
                                "loc": {
                                    "items": {
                                        "anyOf": [
                                            {"type": "string"},
                                            {"type": "integer"},
                                        ]
                                    },
                                    "title": "Location",
                                    "type": "array",
                                },
                                "msg": {"title": "Message", "type": "string"},
                                "type": {"title": "Error Type", "type": "string"},
                            },
                            "required": ["loc", "msg", "type"],
                            "title": "ValidationError",
                            "type": "object",
                        },
                    },
                    "properties": {
                        "detail": {
                            "items": {"$ref": "#/definitions/ValidationError"},
                            "title": "Detail",
                            "type": "array",
                        }
                    },
                    "title": "HTTPValidationError",
                    "type": "object",
                },
            },
        },
    },
}


def get_response_schema(path: str, method: str, status: str) -> dict:
    """
    Get response schema for given operation and status code.

    Args:
        path: Endpoint path (e.g., "/{contract_id}/")
        method: HTTP method (e.g., "get", "post")
        status: Status code (e.g., "200", "404")

    Returns:
        JSON Schema dict with definitions for $ref resolution
    """
    return _OPERATIONS[(path, method)]["responses"][status]["schema"]


def get_response_strategy(path: str, method: str, status: str):
    """
    Get hypothesis strategy for response examples (cached or generated).

    This function provides transparent access to pre-generated examples
    with automatic fallback to on-demand generation via from_schema().
    """
    return get_cached_example_strategy(
        api_name="wallet",
        spec_hash=_SPEC_HASH,
        path=path,
        method=method,
        example_type="response",
        key=status,
        schema_getter=lambda: get_response_schema(path, method, status),
    )


def get_request_body_schema(path: str, method: str) -> dict:
    """
    Get request body schema for given operation.

    Args:
        path: Endpoint path (e.g., "/{contract_id}/search")
        method: HTTP method (e.g., "post", "put")

    Returns:
        JSON Schema dict with definitions for $ref resolution
    """
    return _OPERATIONS[(path, method)]["requestBody"]["schema"]


def get_request_body_strategy(path: str, method: str):
    """Get hypothesis strategy for request body examples (cached or generated)."""
    return get_cached_example_strategy(
        api_name="wallet",
        spec_hash=_SPEC_HASH,
        path=path,
        method=method,
        example_type="body",
        key="requestBody",
        schema_getter=lambda: get_request_body_schema(path, method),
    )


def get_parameter_schema(path: str, method: str, param_name: str) -> dict:
    """
    Get query parameter schema for given operation.

    Args:
        path: Endpoint path
        method: HTTP method
        param_name: Parameter name (e.g., "limit", "token")

    Returns:
        JSON Schema dict
    """
    return _OPERATIONS[(path, method)]["parameters"][param_name]["schema"]


def get_parameter_strategy(path: str, method: str, param_name: str):
    """Get hypothesis strategy for parameter examples (cached or generated)."""
    return get_cached_example_strategy(
        api_name="wallet",
        spec_hash=_SPEC_HASH,
        path=path,
        method=method,
        example_type="param",
        key=param_name,
        schema_getter=lambda: get_parameter_schema(path, method, param_name),
    )


def has_request_body(path: str, method: str) -> bool:
    """Check if operation has a request body."""
    return "requestBody" in _OPERATIONS.get((path, method), {})


def has_parameter(path: str, method: str, param_name: str) -> bool:
    """Check if operation has a specific parameter."""
    return param_name in _OPERATIONS.get((path, method), {}).get("parameters", {})


def is_error_response(path: str, method: str, status: str) -> bool:
    """Check if response is an error response (4xx/5xx)."""
    response = _OPERATIONS.get((path, method), {}).get("responses", {}).get(status, {})
    return response.get("is_error", False)


def has_response_schema(path: str, method: str, status: str) -> bool:
    """Check if operation has a response schema for given status."""
    return status in _OPERATIONS.get((path, method), {}).get("responses", {})
