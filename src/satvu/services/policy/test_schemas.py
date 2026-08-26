"""
Schemas for policy service tests.

Generated from OpenAPI spec version v1.
These schemas are used with hypothesis-jsonschema to generate test data.

Stores entire OpenAPI spec as operations with helper functions for access.
"""

from satvu.services.example_cache import get_cached_example_strategy

# Spec hash for example cache invalidation
_SPEC_HASH = "prod-4f453ecf5788a7c7baf4a46f8cbe01fe616cb30a"

# Component schemas for $ref resolution (cleaned for JSON Schema draft-07)
_COMPONENTS = {
    "ContractsAddon": {
        "properties": {
            "name": {
                "description": "Name of the addon option.",
                "example": "Withhold",
                "type": "string",
            },
            "options": {
                "description": "List of options available with this addon.",
                "items": {"$ref": "#/definitions/ContractsAddonOption"},
                "type": "array",
            },
        },
        "required": ["name", "options"],
        "type": "object",
    },
    "ContractsAddonOption": {
        "properties": {
            "default": {"type": "boolean"},
            "eula_type": {
                "description": "The EULA type. Only provided for 'Licence' addons.",
                "example": "Standard",
                "type": "string",
            },
            "label": {
                "description": "Label assigned to addon option.",
                "example": "Withhold - 3 days",
                "type": "string",
            },
            "uplift": {
                "description": "Coefficient "
                "that base "
                "price is "
                "multiplied "
                "by in "
                "percent.",
                "example": 10,
                "format": "int32",
                "type": "integer",
            },
            "value": {
                "description": "Value of the addon option.",
                "example": "3d",
                "type": "string",
            },
        },
        "required": ["label", "uplift", "value"],
        "type": "object",
    },
    "ContractsContractWithProducts": {
        "properties": {
            "active": {
                "description": "Whether the contract is active",
                "example": True,
                "type": "boolean",
            },
            "addons": {
                "description": "Addons associated with this contract",
                "items": {"$ref": "#/definitions/ContractsAddon"},
                "type": "array",
            },
            "allowed_geographical_area": {"$ref": "#/definitions/ContractsGeometry"},
            "contract_id": {
                "description": "Contract ID",
                "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                "type": "string",
            },
            "credit_limit": {"format": "int64", "type": "integer"},
            "end_date": {
                "description": "Contract end date",
                "format": "date",
                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                "type": ["string", "null"],
            },
            "geographical_summary": {
                "description": "Descriptive summary of a contract's geographical area",
                "example": "Northern Europe",
                "type": "string",
            },
            "name": {
                "description": "Contract name",
                "example": "my-contract",
                "type": "string",
            },
            "products": {
                "description": "List of products the contract has access to",
                "items": {"$ref": "#/definitions/ContractsProductSummary"},
                "type": "array",
            },
            "reseller": {
                "description": "Whether the contract is marked for reselling",
                "example": True,
                "type": "boolean",
            },
            "satellite_access": {
                "description": "Satellite access for the contract",
                "items": {"type": "string"},
                "type": "array",
            },
            "start_date": {
                "description": "Contract start date",
                "format": "date",
                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                "type": ["string", "null"],
            },
        },
        "required": [
            "active",
            "addons",
            "allowed_geographical_area",
            "contract_id",
            "end_date",
            "geographical_summary",
            "name",
            "products",
            "reseller",
            "start_date",
        ],
        "type": "object",
    },
    "ContractsGeometry": {
        "description": "Allowed geographical area of the contract",
        "properties": {
            "coordinates": {"description": "Value of any type, including null"},
            "type": {"type": "string"},
        },
        "type": "object",
    },
    "ContractsProductSummary": {
        "properties": {
            "assured_tasking_window_days": {
                "description": "Assured "
                "tasking "
                "window "
                "in "
                "days. "
                "Only "
                "present "
                "for "
                "the "
                "ASSURED_PRIORITY "
                "product.",
                "example": 8,
                "format": "int32",
                "type": ["integer", "null"],
            },
            "code": {
                "description": "Product code",
                "example": "PRODUCT",
                "type": "string",
            },
            "currency": {
                "description": "Product currency",
                "example": "GBP",
                "type": "string",
            },
        },
        "required": ["code", "currency"],
        "type": "object",
    },
    "List-Active-ContractsInput": {
        "properties": {"token": {"description": "User access token", "type": "string"}},
        "required": ["token"],
        "type": "object",
    },
    "RouterActiveContractsResponse": {
        "properties": {
            "result": {
                "description": "Result of the active contracts query",
                "items": {"$ref": "#/definitions/ContractsContractWithProducts"},
                "type": "array",
            },
            "terms_accepted": {
                "description": "User has accepted terms of service",
                "type": "boolean",
            },
        },
        "required": ["result", "terms_accepted"],
        "type": "object",
    },
    "RouterHttpError": {
        "properties": {
            "id": {
                "description": "A unique identifier for the type of error.",
                "type": "string",
            },
            "message": {
                "description": "An error message describing what went wrong.",
                "type": "string",
            },
        },
        "required": ["id", "message"],
        "type": "object",
    },
    "TermsUserTermsAccepted": {
        "properties": {"accepted": {"type": "boolean"}, "user_id": {"type": "string"}},
        "type": "object",
    },
    "User-Acceptance-TermsInput": {
        "properties": {
            "accepted": {
                "description": "Terms and Conditions have been accepted",
                "type": "boolean",
            },
            "token": {"description": "User access token", "type": "string"},
        },
        "required": ["accepted", "token"],
        "type": "object",
    },
}

# Operations: (path, method) -> {responses, requestBody, parameters}
# Each schema has definitions attached for $ref resolution
_OPERATIONS = {
    ("/contracts", "post"): {
        "parameters": {},
        "requestBody": {
            "schema": {
                "definitions": {
                    "ContractsAddon": {
                        "properties": {
                            "name": {
                                "description": "Name of the addon option.",
                                "example": "Withhold",
                                "type": "string",
                            },
                            "options": {
                                "description": "List "
                                "of "
                                "options "
                                "available "
                                "with "
                                "this "
                                "addon.",
                                "items": {"$ref": "#/definitions/ContractsAddonOption"},
                                "type": "array",
                            },
                        },
                        "required": ["name", "options"],
                        "type": "object",
                    },
                    "ContractsAddonOption": {
                        "properties": {
                            "default": {"type": "boolean"},
                            "eula_type": {
                                "description": "The "
                                "EULA "
                                "type. "
                                "Only "
                                "provided "
                                "for "
                                "'Licence' "
                                "addons.",
                                "example": "Standard",
                                "type": "string",
                            },
                            "label": {
                                "description": "Label assigned to addon option.",
                                "example": "Withhold - 3 days",
                                "type": "string",
                            },
                            "uplift": {
                                "description": "Coefficient "
                                "that "
                                "base "
                                "price "
                                "is "
                                "multiplied "
                                "by "
                                "in "
                                "percent.",
                                "example": 10,
                                "format": "int32",
                                "type": "integer",
                            },
                            "value": {
                                "description": "Value of the addon option.",
                                "example": "3d",
                                "type": "string",
                            },
                        },
                        "required": ["label", "uplift", "value"],
                        "type": "object",
                    },
                    "ContractsContractWithProducts": {
                        "properties": {
                            "active": {
                                "description": "Whether the contract is active",
                                "example": True,
                                "type": "boolean",
                            },
                            "addons": {
                                "description": "Addons associated with this contract",
                                "items": {"$ref": "#/definitions/ContractsAddon"},
                                "type": "array",
                            },
                            "allowed_geographical_area": {
                                "$ref": "#/definitions/ContractsGeometry"
                            },
                            "contract_id": {
                                "description": "Contract ID",
                                "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                                "type": "string",
                            },
                            "credit_limit": {"format": "int64", "type": "integer"},
                            "end_date": {
                                "description": "Contract end date",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "type": ["string", "null"],
                            },
                            "geographical_summary": {
                                "description": "Descriptive "
                                "summary "
                                "of "
                                "a "
                                "contract's "
                                "geographical "
                                "area",
                                "example": "Northern Europe",
                                "type": "string",
                            },
                            "name": {
                                "description": "Contract name",
                                "example": "my-contract",
                                "type": "string",
                            },
                            "products": {
                                "description": "List "
                                "of "
                                "products "
                                "the "
                                "contract "
                                "has "
                                "access "
                                "to",
                                "items": {
                                    "$ref": "#/definitions/ContractsProductSummary"
                                },
                                "type": "array",
                            },
                            "reseller": {
                                "description": "Whether "
                                "the "
                                "contract "
                                "is "
                                "marked "
                                "for "
                                "reselling",
                                "example": True,
                                "type": "boolean",
                            },
                            "satellite_access": {
                                "description": "Satellite access for the contract",
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            "start_date": {
                                "description": "Contract start date",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "type": ["string", "null"],
                            },
                        },
                        "required": [
                            "active",
                            "addons",
                            "allowed_geographical_area",
                            "contract_id",
                            "end_date",
                            "geographical_summary",
                            "name",
                            "products",
                            "reseller",
                            "start_date",
                        ],
                        "type": "object",
                    },
                    "ContractsGeometry": {
                        "description": "Allowed geographical area of the contract",
                        "properties": {
                            "coordinates": {
                                "description": "Value of any type, including null"
                            },
                            "type": {"type": "string"},
                        },
                        "type": "object",
                    },
                    "ContractsProductSummary": {
                        "properties": {
                            "assured_tasking_window_days": {
                                "description": "Assured "
                                "tasking "
                                "window "
                                "in "
                                "days. "
                                "Only "
                                "present "
                                "for "
                                "the "
                                "ASSURED_PRIORITY "
                                "product.",
                                "example": 8,
                                "format": "int32",
                                "type": ["integer", "null"],
                            },
                            "code": {
                                "description": "Product code",
                                "example": "PRODUCT",
                                "type": "string",
                            },
                            "currency": {
                                "description": "Product currency",
                                "example": "GBP",
                                "type": "string",
                            },
                        },
                        "required": ["code", "currency"],
                        "type": "object",
                    },
                    "List-Active-ContractsInput": {
                        "properties": {
                            "token": {
                                "description": "User access token",
                                "type": "string",
                            }
                        },
                        "required": ["token"],
                        "type": "object",
                    },
                    "RouterActiveContractsResponse": {
                        "properties": {
                            "result": {
                                "description": "Result of the active contracts query",
                                "items": {
                                    "$ref": "#/definitions/ContractsContractWithProducts"
                                },
                                "type": "array",
                            },
                            "terms_accepted": {
                                "description": "User has accepted terms of service",
                                "type": "boolean",
                            },
                        },
                        "required": ["result", "terms_accepted"],
                        "type": "object",
                    },
                    "RouterHttpError": {
                        "properties": {
                            "id": {
                                "description": "A "
                                "unique "
                                "identifier "
                                "for "
                                "the "
                                "type "
                                "of "
                                "error.",
                                "type": "string",
                            },
                            "message": {
                                "description": "An "
                                "error "
                                "message "
                                "describing "
                                "what "
                                "went "
                                "wrong.",
                                "type": "string",
                            },
                        },
                        "required": ["id", "message"],
                        "type": "object",
                    },
                    "TermsUserTermsAccepted": {
                        "properties": {
                            "accepted": {"type": "boolean"},
                            "user_id": {"type": "string"},
                        },
                        "type": "object",
                    },
                    "User-Acceptance-TermsInput": {
                        "properties": {
                            "accepted": {
                                "description": "Terms "
                                "and "
                                "Conditions "
                                "have "
                                "been "
                                "accepted",
                                "type": "boolean",
                            },
                            "token": {
                                "description": "User access token",
                                "type": "string",
                            },
                        },
                        "required": ["accepted", "token"],
                        "type": "object",
                    },
                },
                "properties": {
                    "token": {"description": "User access token", "type": "string"}
                },
                "required": ["token"],
                "type": "object",
            }
        },
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "ContractsAddon": {
                            "properties": {
                                "name": {
                                    "description": "Name of the addon option.",
                                    "example": "Withhold",
                                    "type": "string",
                                },
                                "options": {
                                    "description": "List "
                                    "of "
                                    "options "
                                    "available "
                                    "with "
                                    "this "
                                    "addon.",
                                    "items": {
                                        "$ref": "#/definitions/ContractsAddonOption"
                                    },
                                    "type": "array",
                                },
                            },
                            "required": ["name", "options"],
                            "type": "object",
                        },
                        "ContractsAddonOption": {
                            "properties": {
                                "default": {"type": "boolean"},
                                "eula_type": {
                                    "description": "The "
                                    "EULA "
                                    "type. "
                                    "Only "
                                    "provided "
                                    "for "
                                    "'Licence' "
                                    "addons.",
                                    "example": "Standard",
                                    "type": "string",
                                },
                                "label": {
                                    "description": "Label assigned to addon option.",
                                    "example": "Withhold - 3 days",
                                    "type": "string",
                                },
                                "uplift": {
                                    "description": "Coefficient "
                                    "that "
                                    "base "
                                    "price "
                                    "is "
                                    "multiplied "
                                    "by "
                                    "in "
                                    "percent.",
                                    "example": 10,
                                    "format": "int32",
                                    "type": "integer",
                                },
                                "value": {
                                    "description": "Value of the addon option.",
                                    "example": "3d",
                                    "type": "string",
                                },
                            },
                            "required": ["label", "uplift", "value"],
                            "type": "object",
                        },
                        "ContractsContractWithProducts": {
                            "properties": {
                                "active": {
                                    "description": "Whether the contract is active",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "addons": {
                                    "description": "Addons "
                                    "associated "
                                    "with "
                                    "this "
                                    "contract",
                                    "items": {"$ref": "#/definitions/ContractsAddon"},
                                    "type": "array",
                                },
                                "allowed_geographical_area": {
                                    "$ref": "#/definitions/ContractsGeometry"
                                },
                                "contract_id": {
                                    "description": "Contract ID",
                                    "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                                    "type": "string",
                                },
                                "credit_limit": {"format": "int64", "type": "integer"},
                                "end_date": {
                                    "description": "Contract end date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                                "geographical_summary": {
                                    "description": "Descriptive "
                                    "summary "
                                    "of "
                                    "a "
                                    "contract's "
                                    "geographical "
                                    "area",
                                    "example": "Northern Europe",
                                    "type": "string",
                                },
                                "name": {
                                    "description": "Contract name",
                                    "example": "my-contract",
                                    "type": "string",
                                },
                                "products": {
                                    "description": "List "
                                    "of "
                                    "products "
                                    "the "
                                    "contract "
                                    "has "
                                    "access "
                                    "to",
                                    "items": {
                                        "$ref": "#/definitions/ContractsProductSummary"
                                    },
                                    "type": "array",
                                },
                                "reseller": {
                                    "description": "Whether "
                                    "the "
                                    "contract "
                                    "is "
                                    "marked "
                                    "for "
                                    "reselling",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "satellite_access": {
                                    "description": "Satellite access for the contract",
                                    "items": {"type": "string"},
                                    "type": "array",
                                },
                                "start_date": {
                                    "description": "Contract start date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                            },
                            "required": [
                                "active",
                                "addons",
                                "allowed_geographical_area",
                                "contract_id",
                                "end_date",
                                "geographical_summary",
                                "name",
                                "products",
                                "reseller",
                                "start_date",
                            ],
                            "type": "object",
                        },
                        "ContractsGeometry": {
                            "description": "Allowed geographical area of the contract",
                            "properties": {
                                "coordinates": {
                                    "description": "Value of any type, including null"
                                },
                                "type": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "ContractsProductSummary": {
                            "properties": {
                                "assured_tasking_window_days": {
                                    "description": "Assured "
                                    "tasking "
                                    "window "
                                    "in "
                                    "days. "
                                    "Only "
                                    "present "
                                    "for "
                                    "the "
                                    "ASSURED_PRIORITY "
                                    "product.",
                                    "example": 8,
                                    "format": "int32",
                                    "type": ["integer", "null"],
                                },
                                "code": {
                                    "description": "Product code",
                                    "example": "PRODUCT",
                                    "type": "string",
                                },
                                "currency": {
                                    "description": "Product currency",
                                    "example": "GBP",
                                    "type": "string",
                                },
                            },
                            "required": ["code", "currency"],
                            "type": "object",
                        },
                        "List-Active-ContractsInput": {
                            "properties": {
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                }
                            },
                            "required": ["token"],
                            "type": "object",
                        },
                        "RouterActiveContractsResponse": {
                            "properties": {
                                "result": {
                                    "description": "Result "
                                    "of "
                                    "the "
                                    "active "
                                    "contracts "
                                    "query",
                                    "items": {
                                        "$ref": "#/definitions/ContractsContractWithProducts"
                                    },
                                    "type": "array",
                                },
                                "terms_accepted": {
                                    "description": "User has accepted terms of service",
                                    "type": "boolean",
                                },
                            },
                            "required": ["result", "terms_accepted"],
                            "type": "object",
                        },
                        "RouterHttpError": {
                            "properties": {
                                "id": {
                                    "description": "A "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "type "
                                    "of "
                                    "error.",
                                    "type": "string",
                                },
                                "message": {
                                    "description": "An "
                                    "error "
                                    "message "
                                    "describing "
                                    "what "
                                    "went "
                                    "wrong.",
                                    "type": "string",
                                },
                            },
                            "required": ["id", "message"],
                            "type": "object",
                        },
                        "TermsUserTermsAccepted": {
                            "properties": {
                                "accepted": {"type": "boolean"},
                                "user_id": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "User-Acceptance-TermsInput": {
                            "properties": {
                                "accepted": {
                                    "description": "Terms "
                                    "and "
                                    "Conditions "
                                    "have "
                                    "been "
                                    "accepted",
                                    "type": "boolean",
                                },
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                },
                            },
                            "required": ["accepted", "token"],
                            "type": "object",
                        },
                    },
                    "properties": {
                        "result": {
                            "description": "Result of the active contracts query",
                            "items": {
                                "$ref": "#/definitions/ContractsContractWithProducts"
                            },
                            "type": "array",
                        },
                        "terms_accepted": {
                            "description": "User has accepted terms of service",
                            "type": "boolean",
                        },
                    },
                    "required": ["result", "terms_accepted"],
                    "type": "object",
                },
            },
            "400": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "ContractsAddon": {
                            "properties": {
                                "name": {
                                    "description": "Name of the addon option.",
                                    "example": "Withhold",
                                    "type": "string",
                                },
                                "options": {
                                    "description": "List "
                                    "of "
                                    "options "
                                    "available "
                                    "with "
                                    "this "
                                    "addon.",
                                    "items": {
                                        "$ref": "#/definitions/ContractsAddonOption"
                                    },
                                    "type": "array",
                                },
                            },
                            "required": ["name", "options"],
                            "type": "object",
                        },
                        "ContractsAddonOption": {
                            "properties": {
                                "default": {"type": "boolean"},
                                "eula_type": {
                                    "description": "The "
                                    "EULA "
                                    "type. "
                                    "Only "
                                    "provided "
                                    "for "
                                    "'Licence' "
                                    "addons.",
                                    "example": "Standard",
                                    "type": "string",
                                },
                                "label": {
                                    "description": "Label assigned to addon option.",
                                    "example": "Withhold - 3 days",
                                    "type": "string",
                                },
                                "uplift": {
                                    "description": "Coefficient "
                                    "that "
                                    "base "
                                    "price "
                                    "is "
                                    "multiplied "
                                    "by "
                                    "in "
                                    "percent.",
                                    "example": 10,
                                    "format": "int32",
                                    "type": "integer",
                                },
                                "value": {
                                    "description": "Value of the addon option.",
                                    "example": "3d",
                                    "type": "string",
                                },
                            },
                            "required": ["label", "uplift", "value"],
                            "type": "object",
                        },
                        "ContractsContractWithProducts": {
                            "properties": {
                                "active": {
                                    "description": "Whether the contract is active",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "addons": {
                                    "description": "Addons "
                                    "associated "
                                    "with "
                                    "this "
                                    "contract",
                                    "items": {"$ref": "#/definitions/ContractsAddon"},
                                    "type": "array",
                                },
                                "allowed_geographical_area": {
                                    "$ref": "#/definitions/ContractsGeometry"
                                },
                                "contract_id": {
                                    "description": "Contract ID",
                                    "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                                    "type": "string",
                                },
                                "credit_limit": {"format": "int64", "type": "integer"},
                                "end_date": {
                                    "description": "Contract end date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                                "geographical_summary": {
                                    "description": "Descriptive "
                                    "summary "
                                    "of "
                                    "a "
                                    "contract's "
                                    "geographical "
                                    "area",
                                    "example": "Northern Europe",
                                    "type": "string",
                                },
                                "name": {
                                    "description": "Contract name",
                                    "example": "my-contract",
                                    "type": "string",
                                },
                                "products": {
                                    "description": "List "
                                    "of "
                                    "products "
                                    "the "
                                    "contract "
                                    "has "
                                    "access "
                                    "to",
                                    "items": {
                                        "$ref": "#/definitions/ContractsProductSummary"
                                    },
                                    "type": "array",
                                },
                                "reseller": {
                                    "description": "Whether "
                                    "the "
                                    "contract "
                                    "is "
                                    "marked "
                                    "for "
                                    "reselling",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "satellite_access": {
                                    "description": "Satellite access for the contract",
                                    "items": {"type": "string"},
                                    "type": "array",
                                },
                                "start_date": {
                                    "description": "Contract start date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                            },
                            "required": [
                                "active",
                                "addons",
                                "allowed_geographical_area",
                                "contract_id",
                                "end_date",
                                "geographical_summary",
                                "name",
                                "products",
                                "reseller",
                                "start_date",
                            ],
                            "type": "object",
                        },
                        "ContractsGeometry": {
                            "description": "Allowed geographical area of the contract",
                            "properties": {
                                "coordinates": {
                                    "description": "Value of any type, including null"
                                },
                                "type": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "ContractsProductSummary": {
                            "properties": {
                                "assured_tasking_window_days": {
                                    "description": "Assured "
                                    "tasking "
                                    "window "
                                    "in "
                                    "days. "
                                    "Only "
                                    "present "
                                    "for "
                                    "the "
                                    "ASSURED_PRIORITY "
                                    "product.",
                                    "example": 8,
                                    "format": "int32",
                                    "type": ["integer", "null"],
                                },
                                "code": {
                                    "description": "Product code",
                                    "example": "PRODUCT",
                                    "type": "string",
                                },
                                "currency": {
                                    "description": "Product currency",
                                    "example": "GBP",
                                    "type": "string",
                                },
                            },
                            "required": ["code", "currency"],
                            "type": "object",
                        },
                        "List-Active-ContractsInput": {
                            "properties": {
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                }
                            },
                            "required": ["token"],
                            "type": "object",
                        },
                        "RouterActiveContractsResponse": {
                            "properties": {
                                "result": {
                                    "description": "Result "
                                    "of "
                                    "the "
                                    "active "
                                    "contracts "
                                    "query",
                                    "items": {
                                        "$ref": "#/definitions/ContractsContractWithProducts"
                                    },
                                    "type": "array",
                                },
                                "terms_accepted": {
                                    "description": "User has accepted terms of service",
                                    "type": "boolean",
                                },
                            },
                            "required": ["result", "terms_accepted"],
                            "type": "object",
                        },
                        "RouterHttpError": {
                            "properties": {
                                "id": {
                                    "description": "A "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "type "
                                    "of "
                                    "error.",
                                    "type": "string",
                                },
                                "message": {
                                    "description": "An "
                                    "error "
                                    "message "
                                    "describing "
                                    "what "
                                    "went "
                                    "wrong.",
                                    "type": "string",
                                },
                            },
                            "required": ["id", "message"],
                            "type": "object",
                        },
                        "TermsUserTermsAccepted": {
                            "properties": {
                                "accepted": {"type": "boolean"},
                                "user_id": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "User-Acceptance-TermsInput": {
                            "properties": {
                                "accepted": {
                                    "description": "Terms "
                                    "and "
                                    "Conditions "
                                    "have "
                                    "been "
                                    "accepted",
                                    "type": "boolean",
                                },
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                },
                            },
                            "required": ["accepted", "token"],
                            "type": "object",
                        },
                    },
                    "properties": {
                        "id": {
                            "description": "A unique identifier for the type of error.",
                            "type": "string",
                        },
                        "message": {
                            "description": "An "
                            "error "
                            "message "
                            "describing "
                            "what "
                            "went "
                            "wrong.",
                            "type": "string",
                        },
                    },
                    "required": ["id", "message"],
                    "type": "object",
                },
            },
        },
    },
    ("/terms", "post"): {
        "parameters": {},
        "requestBody": {
            "schema": {
                "definitions": {
                    "ContractsAddon": {
                        "properties": {
                            "name": {
                                "description": "Name of the addon option.",
                                "example": "Withhold",
                                "type": "string",
                            },
                            "options": {
                                "description": "List "
                                "of "
                                "options "
                                "available "
                                "with "
                                "this "
                                "addon.",
                                "items": {"$ref": "#/definitions/ContractsAddonOption"},
                                "type": "array",
                            },
                        },
                        "required": ["name", "options"],
                        "type": "object",
                    },
                    "ContractsAddonOption": {
                        "properties": {
                            "default": {"type": "boolean"},
                            "eula_type": {
                                "description": "The "
                                "EULA "
                                "type. "
                                "Only "
                                "provided "
                                "for "
                                "'Licence' "
                                "addons.",
                                "example": "Standard",
                                "type": "string",
                            },
                            "label": {
                                "description": "Label assigned to addon option.",
                                "example": "Withhold - 3 days",
                                "type": "string",
                            },
                            "uplift": {
                                "description": "Coefficient "
                                "that "
                                "base "
                                "price "
                                "is "
                                "multiplied "
                                "by "
                                "in "
                                "percent.",
                                "example": 10,
                                "format": "int32",
                                "type": "integer",
                            },
                            "value": {
                                "description": "Value of the addon option.",
                                "example": "3d",
                                "type": "string",
                            },
                        },
                        "required": ["label", "uplift", "value"],
                        "type": "object",
                    },
                    "ContractsContractWithProducts": {
                        "properties": {
                            "active": {
                                "description": "Whether the contract is active",
                                "example": True,
                                "type": "boolean",
                            },
                            "addons": {
                                "description": "Addons associated with this contract",
                                "items": {"$ref": "#/definitions/ContractsAddon"},
                                "type": "array",
                            },
                            "allowed_geographical_area": {
                                "$ref": "#/definitions/ContractsGeometry"
                            },
                            "contract_id": {
                                "description": "Contract ID",
                                "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                                "type": "string",
                            },
                            "credit_limit": {"format": "int64", "type": "integer"},
                            "end_date": {
                                "description": "Contract end date",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "type": ["string", "null"],
                            },
                            "geographical_summary": {
                                "description": "Descriptive "
                                "summary "
                                "of "
                                "a "
                                "contract's "
                                "geographical "
                                "area",
                                "example": "Northern Europe",
                                "type": "string",
                            },
                            "name": {
                                "description": "Contract name",
                                "example": "my-contract",
                                "type": "string",
                            },
                            "products": {
                                "description": "List "
                                "of "
                                "products "
                                "the "
                                "contract "
                                "has "
                                "access "
                                "to",
                                "items": {
                                    "$ref": "#/definitions/ContractsProductSummary"
                                },
                                "type": "array",
                            },
                            "reseller": {
                                "description": "Whether "
                                "the "
                                "contract "
                                "is "
                                "marked "
                                "for "
                                "reselling",
                                "example": True,
                                "type": "boolean",
                            },
                            "satellite_access": {
                                "description": "Satellite access for the contract",
                                "items": {"type": "string"},
                                "type": "array",
                            },
                            "start_date": {
                                "description": "Contract start date",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "type": ["string", "null"],
                            },
                        },
                        "required": [
                            "active",
                            "addons",
                            "allowed_geographical_area",
                            "contract_id",
                            "end_date",
                            "geographical_summary",
                            "name",
                            "products",
                            "reseller",
                            "start_date",
                        ],
                        "type": "object",
                    },
                    "ContractsGeometry": {
                        "description": "Allowed geographical area of the contract",
                        "properties": {
                            "coordinates": {
                                "description": "Value of any type, including null"
                            },
                            "type": {"type": "string"},
                        },
                        "type": "object",
                    },
                    "ContractsProductSummary": {
                        "properties": {
                            "assured_tasking_window_days": {
                                "description": "Assured "
                                "tasking "
                                "window "
                                "in "
                                "days. "
                                "Only "
                                "present "
                                "for "
                                "the "
                                "ASSURED_PRIORITY "
                                "product.",
                                "example": 8,
                                "format": "int32",
                                "type": ["integer", "null"],
                            },
                            "code": {
                                "description": "Product code",
                                "example": "PRODUCT",
                                "type": "string",
                            },
                            "currency": {
                                "description": "Product currency",
                                "example": "GBP",
                                "type": "string",
                            },
                        },
                        "required": ["code", "currency"],
                        "type": "object",
                    },
                    "List-Active-ContractsInput": {
                        "properties": {
                            "token": {
                                "description": "User access token",
                                "type": "string",
                            }
                        },
                        "required": ["token"],
                        "type": "object",
                    },
                    "RouterActiveContractsResponse": {
                        "properties": {
                            "result": {
                                "description": "Result of the active contracts query",
                                "items": {
                                    "$ref": "#/definitions/ContractsContractWithProducts"
                                },
                                "type": "array",
                            },
                            "terms_accepted": {
                                "description": "User has accepted terms of service",
                                "type": "boolean",
                            },
                        },
                        "required": ["result", "terms_accepted"],
                        "type": "object",
                    },
                    "RouterHttpError": {
                        "properties": {
                            "id": {
                                "description": "A "
                                "unique "
                                "identifier "
                                "for "
                                "the "
                                "type "
                                "of "
                                "error.",
                                "type": "string",
                            },
                            "message": {
                                "description": "An "
                                "error "
                                "message "
                                "describing "
                                "what "
                                "went "
                                "wrong.",
                                "type": "string",
                            },
                        },
                        "required": ["id", "message"],
                        "type": "object",
                    },
                    "TermsUserTermsAccepted": {
                        "properties": {
                            "accepted": {"type": "boolean"},
                            "user_id": {"type": "string"},
                        },
                        "type": "object",
                    },
                    "User-Acceptance-TermsInput": {
                        "properties": {
                            "accepted": {
                                "description": "Terms "
                                "and "
                                "Conditions "
                                "have "
                                "been "
                                "accepted",
                                "type": "boolean",
                            },
                            "token": {
                                "description": "User access token",
                                "type": "string",
                            },
                        },
                        "required": ["accepted", "token"],
                        "type": "object",
                    },
                },
                "properties": {
                    "accepted": {
                        "description": "Terms and Conditions have been accepted",
                        "type": "boolean",
                    },
                    "token": {"description": "User access token", "type": "string"},
                },
                "required": ["accepted", "token"],
                "type": "object",
            }
        },
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "ContractsAddon": {
                            "properties": {
                                "name": {
                                    "description": "Name of the addon option.",
                                    "example": "Withhold",
                                    "type": "string",
                                },
                                "options": {
                                    "description": "List "
                                    "of "
                                    "options "
                                    "available "
                                    "with "
                                    "this "
                                    "addon.",
                                    "items": {
                                        "$ref": "#/definitions/ContractsAddonOption"
                                    },
                                    "type": "array",
                                },
                            },
                            "required": ["name", "options"],
                            "type": "object",
                        },
                        "ContractsAddonOption": {
                            "properties": {
                                "default": {"type": "boolean"},
                                "eula_type": {
                                    "description": "The "
                                    "EULA "
                                    "type. "
                                    "Only "
                                    "provided "
                                    "for "
                                    "'Licence' "
                                    "addons.",
                                    "example": "Standard",
                                    "type": "string",
                                },
                                "label": {
                                    "description": "Label assigned to addon option.",
                                    "example": "Withhold - 3 days",
                                    "type": "string",
                                },
                                "uplift": {
                                    "description": "Coefficient "
                                    "that "
                                    "base "
                                    "price "
                                    "is "
                                    "multiplied "
                                    "by "
                                    "in "
                                    "percent.",
                                    "example": 10,
                                    "format": "int32",
                                    "type": "integer",
                                },
                                "value": {
                                    "description": "Value of the addon option.",
                                    "example": "3d",
                                    "type": "string",
                                },
                            },
                            "required": ["label", "uplift", "value"],
                            "type": "object",
                        },
                        "ContractsContractWithProducts": {
                            "properties": {
                                "active": {
                                    "description": "Whether the contract is active",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "addons": {
                                    "description": "Addons "
                                    "associated "
                                    "with "
                                    "this "
                                    "contract",
                                    "items": {"$ref": "#/definitions/ContractsAddon"},
                                    "type": "array",
                                },
                                "allowed_geographical_area": {
                                    "$ref": "#/definitions/ContractsGeometry"
                                },
                                "contract_id": {
                                    "description": "Contract ID",
                                    "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                                    "type": "string",
                                },
                                "credit_limit": {"format": "int64", "type": "integer"},
                                "end_date": {
                                    "description": "Contract end date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                                "geographical_summary": {
                                    "description": "Descriptive "
                                    "summary "
                                    "of "
                                    "a "
                                    "contract's "
                                    "geographical "
                                    "area",
                                    "example": "Northern Europe",
                                    "type": "string",
                                },
                                "name": {
                                    "description": "Contract name",
                                    "example": "my-contract",
                                    "type": "string",
                                },
                                "products": {
                                    "description": "List "
                                    "of "
                                    "products "
                                    "the "
                                    "contract "
                                    "has "
                                    "access "
                                    "to",
                                    "items": {
                                        "$ref": "#/definitions/ContractsProductSummary"
                                    },
                                    "type": "array",
                                },
                                "reseller": {
                                    "description": "Whether "
                                    "the "
                                    "contract "
                                    "is "
                                    "marked "
                                    "for "
                                    "reselling",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "satellite_access": {
                                    "description": "Satellite access for the contract",
                                    "items": {"type": "string"},
                                    "type": "array",
                                },
                                "start_date": {
                                    "description": "Contract start date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                            },
                            "required": [
                                "active",
                                "addons",
                                "allowed_geographical_area",
                                "contract_id",
                                "end_date",
                                "geographical_summary",
                                "name",
                                "products",
                                "reseller",
                                "start_date",
                            ],
                            "type": "object",
                        },
                        "ContractsGeometry": {
                            "description": "Allowed geographical area of the contract",
                            "properties": {
                                "coordinates": {
                                    "description": "Value of any type, including null"
                                },
                                "type": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "ContractsProductSummary": {
                            "properties": {
                                "assured_tasking_window_days": {
                                    "description": "Assured "
                                    "tasking "
                                    "window "
                                    "in "
                                    "days. "
                                    "Only "
                                    "present "
                                    "for "
                                    "the "
                                    "ASSURED_PRIORITY "
                                    "product.",
                                    "example": 8,
                                    "format": "int32",
                                    "type": ["integer", "null"],
                                },
                                "code": {
                                    "description": "Product code",
                                    "example": "PRODUCT",
                                    "type": "string",
                                },
                                "currency": {
                                    "description": "Product currency",
                                    "example": "GBP",
                                    "type": "string",
                                },
                            },
                            "required": ["code", "currency"],
                            "type": "object",
                        },
                        "List-Active-ContractsInput": {
                            "properties": {
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                }
                            },
                            "required": ["token"],
                            "type": "object",
                        },
                        "RouterActiveContractsResponse": {
                            "properties": {
                                "result": {
                                    "description": "Result "
                                    "of "
                                    "the "
                                    "active "
                                    "contracts "
                                    "query",
                                    "items": {
                                        "$ref": "#/definitions/ContractsContractWithProducts"
                                    },
                                    "type": "array",
                                },
                                "terms_accepted": {
                                    "description": "User has accepted terms of service",
                                    "type": "boolean",
                                },
                            },
                            "required": ["result", "terms_accepted"],
                            "type": "object",
                        },
                        "RouterHttpError": {
                            "properties": {
                                "id": {
                                    "description": "A "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "type "
                                    "of "
                                    "error.",
                                    "type": "string",
                                },
                                "message": {
                                    "description": "An "
                                    "error "
                                    "message "
                                    "describing "
                                    "what "
                                    "went "
                                    "wrong.",
                                    "type": "string",
                                },
                            },
                            "required": ["id", "message"],
                            "type": "object",
                        },
                        "TermsUserTermsAccepted": {
                            "properties": {
                                "accepted": {"type": "boolean"},
                                "user_id": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "User-Acceptance-TermsInput": {
                            "properties": {
                                "accepted": {
                                    "description": "Terms "
                                    "and "
                                    "Conditions "
                                    "have "
                                    "been "
                                    "accepted",
                                    "type": "boolean",
                                },
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                },
                            },
                            "required": ["accepted", "token"],
                            "type": "object",
                        },
                    },
                    "properties": {
                        "accepted": {"type": "boolean"},
                        "user_id": {"type": "string"},
                    },
                    "type": "object",
                },
            },
            "400": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "ContractsAddon": {
                            "properties": {
                                "name": {
                                    "description": "Name of the addon option.",
                                    "example": "Withhold",
                                    "type": "string",
                                },
                                "options": {
                                    "description": "List "
                                    "of "
                                    "options "
                                    "available "
                                    "with "
                                    "this "
                                    "addon.",
                                    "items": {
                                        "$ref": "#/definitions/ContractsAddonOption"
                                    },
                                    "type": "array",
                                },
                            },
                            "required": ["name", "options"],
                            "type": "object",
                        },
                        "ContractsAddonOption": {
                            "properties": {
                                "default": {"type": "boolean"},
                                "eula_type": {
                                    "description": "The "
                                    "EULA "
                                    "type. "
                                    "Only "
                                    "provided "
                                    "for "
                                    "'Licence' "
                                    "addons.",
                                    "example": "Standard",
                                    "type": "string",
                                },
                                "label": {
                                    "description": "Label assigned to addon option.",
                                    "example": "Withhold - 3 days",
                                    "type": "string",
                                },
                                "uplift": {
                                    "description": "Coefficient "
                                    "that "
                                    "base "
                                    "price "
                                    "is "
                                    "multiplied "
                                    "by "
                                    "in "
                                    "percent.",
                                    "example": 10,
                                    "format": "int32",
                                    "type": "integer",
                                },
                                "value": {
                                    "description": "Value of the addon option.",
                                    "example": "3d",
                                    "type": "string",
                                },
                            },
                            "required": ["label", "uplift", "value"],
                            "type": "object",
                        },
                        "ContractsContractWithProducts": {
                            "properties": {
                                "active": {
                                    "description": "Whether the contract is active",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "addons": {
                                    "description": "Addons "
                                    "associated "
                                    "with "
                                    "this "
                                    "contract",
                                    "items": {"$ref": "#/definitions/ContractsAddon"},
                                    "type": "array",
                                },
                                "allowed_geographical_area": {
                                    "$ref": "#/definitions/ContractsGeometry"
                                },
                                "contract_id": {
                                    "description": "Contract ID",
                                    "example": "bc5bb4dc-a007-4419-8093-184408cdb2d7",
                                    "type": "string",
                                },
                                "credit_limit": {"format": "int64", "type": "integer"},
                                "end_date": {
                                    "description": "Contract end date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                                "geographical_summary": {
                                    "description": "Descriptive "
                                    "summary "
                                    "of "
                                    "a "
                                    "contract's "
                                    "geographical "
                                    "area",
                                    "example": "Northern Europe",
                                    "type": "string",
                                },
                                "name": {
                                    "description": "Contract name",
                                    "example": "my-contract",
                                    "type": "string",
                                },
                                "products": {
                                    "description": "List "
                                    "of "
                                    "products "
                                    "the "
                                    "contract "
                                    "has "
                                    "access "
                                    "to",
                                    "items": {
                                        "$ref": "#/definitions/ContractsProductSummary"
                                    },
                                    "type": "array",
                                },
                                "reseller": {
                                    "description": "Whether "
                                    "the "
                                    "contract "
                                    "is "
                                    "marked "
                                    "for "
                                    "reselling",
                                    "example": True,
                                    "type": "boolean",
                                },
                                "satellite_access": {
                                    "description": "Satellite access for the contract",
                                    "items": {"type": "string"},
                                    "type": "array",
                                },
                                "start_date": {
                                    "description": "Contract start date",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "type": ["string", "null"],
                                },
                            },
                            "required": [
                                "active",
                                "addons",
                                "allowed_geographical_area",
                                "contract_id",
                                "end_date",
                                "geographical_summary",
                                "name",
                                "products",
                                "reseller",
                                "start_date",
                            ],
                            "type": "object",
                        },
                        "ContractsGeometry": {
                            "description": "Allowed geographical area of the contract",
                            "properties": {
                                "coordinates": {
                                    "description": "Value of any type, including null"
                                },
                                "type": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "ContractsProductSummary": {
                            "properties": {
                                "assured_tasking_window_days": {
                                    "description": "Assured "
                                    "tasking "
                                    "window "
                                    "in "
                                    "days. "
                                    "Only "
                                    "present "
                                    "for "
                                    "the "
                                    "ASSURED_PRIORITY "
                                    "product.",
                                    "example": 8,
                                    "format": "int32",
                                    "type": ["integer", "null"],
                                },
                                "code": {
                                    "description": "Product code",
                                    "example": "PRODUCT",
                                    "type": "string",
                                },
                                "currency": {
                                    "description": "Product currency",
                                    "example": "GBP",
                                    "type": "string",
                                },
                            },
                            "required": ["code", "currency"],
                            "type": "object",
                        },
                        "List-Active-ContractsInput": {
                            "properties": {
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                }
                            },
                            "required": ["token"],
                            "type": "object",
                        },
                        "RouterActiveContractsResponse": {
                            "properties": {
                                "result": {
                                    "description": "Result "
                                    "of "
                                    "the "
                                    "active "
                                    "contracts "
                                    "query",
                                    "items": {
                                        "$ref": "#/definitions/ContractsContractWithProducts"
                                    },
                                    "type": "array",
                                },
                                "terms_accepted": {
                                    "description": "User has accepted terms of service",
                                    "type": "boolean",
                                },
                            },
                            "required": ["result", "terms_accepted"],
                            "type": "object",
                        },
                        "RouterHttpError": {
                            "properties": {
                                "id": {
                                    "description": "A "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "type "
                                    "of "
                                    "error.",
                                    "type": "string",
                                },
                                "message": {
                                    "description": "An "
                                    "error "
                                    "message "
                                    "describing "
                                    "what "
                                    "went "
                                    "wrong.",
                                    "type": "string",
                                },
                            },
                            "required": ["id", "message"],
                            "type": "object",
                        },
                        "TermsUserTermsAccepted": {
                            "properties": {
                                "accepted": {"type": "boolean"},
                                "user_id": {"type": "string"},
                            },
                            "type": "object",
                        },
                        "User-Acceptance-TermsInput": {
                            "properties": {
                                "accepted": {
                                    "description": "Terms "
                                    "and "
                                    "Conditions "
                                    "have "
                                    "been "
                                    "accepted",
                                    "type": "boolean",
                                },
                                "token": {
                                    "description": "User access token",
                                    "type": "string",
                                },
                            },
                            "required": ["accepted", "token"],
                            "type": "object",
                        },
                    },
                    "properties": {
                        "id": {
                            "description": "A unique identifier for the type of error.",
                            "type": "string",
                        },
                        "message": {
                            "description": "An "
                            "error "
                            "message "
                            "describing "
                            "what "
                            "went "
                            "wrong.",
                            "type": "string",
                        },
                    },
                    "required": ["id", "message"],
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
        api_name="policy",
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
        api_name="policy",
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
        api_name="policy",
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
