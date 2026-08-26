"""
Schemas for reseller service tests.

Generated from OpenAPI spec version v1.
These schemas are used with hypothesis-jsonschema to generate test data.

Stores entire OpenAPI spec as operations with helper functions for access.
"""

from satvu.services.example_cache import get_cached_example_strategy

# Spec hash for example cache invalidation
_SPEC_HASH = "prod-9e136c84ec890d6df78e475d98c9d1b71c9da17d"

# Component schemas for $ref resolution (cleaned for JSON Schema draft-07)
_COMPONENTS = {
    "CompanyAddress": {
        "properties": {
            "country_code": {
                "description": "2-digit country code of company.",
                "enum": [
                    "AD",
                    "AE",
                    "AF",
                    "AG",
                    "AI",
                    "AL",
                    "AM",
                    "AO",
                    "AQ",
                    "AR",
                    "AT",
                    "AU",
                    "AW",
                    "AX",
                    "AZ",
                    "BA",
                    "BB",
                    "BD",
                    "BE",
                    "BF",
                    "BG",
                    "BH",
                    "BI",
                    "BJ",
                    "BL",
                    "BM",
                    "BN",
                    "BO",
                    "BQ",
                    "BR",
                    "BS",
                    "BT",
                    "BV",
                    "BW",
                    "BY",
                    "BZ",
                    "CA",
                    "CC",
                    "CD",
                    "CF",
                    "CG",
                    "CH",
                    "CI",
                    "CK",
                    "CL",
                    "CM",
                    "CN",
                    "CO",
                    "CR",
                    "CV",
                    "CW",
                    "CX",
                    "CY",
                    "CZ",
                    "DE",
                    "DJ",
                    "DK",
                    "DM",
                    "DO",
                    "DZ",
                    "EC",
                    "EE",
                    "EG",
                    "EH",
                    "ER",
                    "ES",
                    "ET",
                    "FI",
                    "FJ",
                    "FK",
                    "FO",
                    "FR",
                    "GA",
                    "GB",
                    "GD",
                    "GE",
                    "GF",
                    "GG",
                    "GH",
                    "GI",
                    "GL",
                    "GM",
                    "GN",
                    "GP",
                    "GQ",
                    "GR",
                    "GS",
                    "GT",
                    "GW",
                    "GY",
                    "HM",
                    "HN",
                    "HR",
                    "HT",
                    "HU",
                    "ID",
                    "IE",
                    "IL",
                    "IM",
                    "IN",
                    "IO",
                    "IQ",
                    "IS",
                    "IT",
                    "JE",
                    "JM",
                    "JO",
                    "JP",
                    "KE",
                    "KG",
                    "KH",
                    "KI",
                    "KM",
                    "KN",
                    "KR",
                    "KW",
                    "KY",
                    "KZ",
                    "LA",
                    "LB",
                    "LC",
                    "LI",
                    "LK",
                    "LR",
                    "LS",
                    "LT",
                    "LU",
                    "LV",
                    "LY",
                    "MA",
                    "MC",
                    "MD",
                    "ME",
                    "MF",
                    "MG",
                    "MK",
                    "ML",
                    "MM",
                    "MN",
                    "MO",
                    "MQ",
                    "MR",
                    "MS",
                    "MT",
                    "MU",
                    "MV",
                    "MW",
                    "MX",
                    "MY",
                    "MZ",
                    "NA",
                    "NC",
                    "NE",
                    "NF",
                    "NG",
                    "NI",
                    "NL",
                    "NO",
                    "NP",
                    "NR",
                    "NU",
                    "NZ",
                    "OM",
                    "PA",
                    "PE",
                    "PF",
                    "PG",
                    "PH",
                    "PK",
                    "PL",
                    "PM",
                    "PN",
                    "PS",
                    "PT",
                    "PY",
                    "QA",
                    "RE",
                    "RO",
                    "RS",
                    "RU",
                    "RW",
                    "SA",
                    "SB",
                    "SC",
                    "SE",
                    "SG",
                    "SH",
                    "SI",
                    "SJ",
                    "SK",
                    "SL",
                    "SM",
                    "SN",
                    "SO",
                    "SR",
                    "SS",
                    "ST",
                    "SV",
                    "SX",
                    "SZ",
                    "TC",
                    "TD",
                    "TF",
                    "TG",
                    "TH",
                    "TJ",
                    "TK",
                    "TL",
                    "TM",
                    "TN",
                    "TO",
                    "TR",
                    "TT",
                    "TV",
                    "TW",
                    "TZ",
                    "UA",
                    "UG",
                    "US",
                    "UY",
                    "UZ",
                    "VA",
                    "VC",
                    "VE",
                    "VG",
                    "VN",
                    "VU",
                    "WF",
                    "WS",
                    "XK",
                    "YE",
                    "YT",
                    "ZA",
                    "ZM",
                    "ZW",
                ],
                "examples": ["GB"],
                "title": "Country Code",
                "type": "string",
            },
            "postcode": {
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "description": "The postcode/zip code of the company.",
                "examples": ["J1 ABC"],
                "title": "Postcode",
            },
            "street": {
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "description": "The street of the company.",
                "examples": ["1 John Lane"],
                "title": "Street",
            },
        },
        "required": ["country_code"],
        "title": "CompanyAddress",
        "type": "object",
    },
    "CompanySearch": {
        "properties": {
            "fields": {
                "anyOf": [
                    {
                        "items": {"$ref": "#/definitions/CompanySearchFields"},
                        "type": "array",
                    },
                    {"const": "all", "type": "string"},
                ],
                "default": "all",
                "description": "Fields to search "
                "against. Either a "
                "list of fields or "
                "`all`. Defaults "
                "to `all`.",
                "examples": ["all"],
                "title": "Fields",
            },
            "string": {
                "description": "Search string.",
                "title": "String",
                "type": "string",
            },
            "type": {
                "$ref": "#/definitions/MatchType",
                "default": "partial",
                "description": "Type of search.",
            },
        },
        "required": ["string"],
        "title": "CompanySearch",
        "type": "object",
    },
    "CompanySearchFields": {
        "enum": ["name", "id"],
        "title": "CompanySearchFields",
        "type": "string",
    },
    "CreateUser": {
        "description": "Represents payload to create a user",
        "properties": {
            "company_address": {
                "$ref": "#/definitions/CompanyAddress",
                "description": "The address of the company.",
            },
            "company_name": {
                "description": "The name of the company.",
                "examples": ["John Smith's Company"],
                "title": "Company Name",
                "type": "string",
            },
            "user_email": {
                "description": "The email address of the user.",
                "examples": ["john@smith.com"],
                "title": "User Email",
                "type": "string",
            },
            "user_name": {
                "description": "The full name of the user.",
                "examples": ["John Smith"],
                "title": "User Name",
                "type": "string",
            },
        },
        "required": ["user_email", "user_name", "company_name", "company_address"],
        "title": "CreateUser",
        "type": "object",
    },
    "CreateUserResponse": {
        "description": "Represents response when creating user",
        "properties": {
            "company_address": {
                "$ref": "#/definitions/CompanyAddress",
                "description": "The address of the company.",
            },
            "company_id": {
                "description": "The unique identifier for the company.",
                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                "format": "uuid",
                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                "title": "Company Id",
                "type": "string",
            },
            "company_kyc_completed_on": {
                "anyOf": [
                    {
                        "format": "date",
                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                        "type": "string",
                    },
                    {"type": "null"},
                ],
                "description": "The "
                "date "
                "when "
                "KYC "
                "was "
                "completed "
                "for "
                "the "
                "company, "
                "if "
                "applicable. "
                "In "
                "YYYY-MM-DD "
                "format.",
                "title": "Company Kyc Completed On",
            },
            "company_kyc_status": {
                "$ref": "#/definitions/KYCStatus",
                "description": "The KYC status of the company.",
            },
            "company_name": {
                "description": "The name of the company.",
                "examples": ["John Smith's Company"],
                "title": "Company Name",
                "type": "string",
            },
            "user_email": {
                "description": "The email address of the user.",
                "examples": ["john@smith.com"],
                "title": "User Email",
                "type": "string",
            },
            "user_id": {
                "description": "The unique identifier for the user.",
                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                "title": "User Id",
                "type": "string",
            },
            "user_kyc_completed_on": {
                "anyOf": [
                    {
                        "format": "date",
                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                        "type": "string",
                    },
                    {"type": "null"},
                ],
                "description": "The "
                "date "
                "when "
                "KYC "
                "was "
                "completed "
                "for "
                "the "
                "user, "
                "if "
                "applicable. "
                "In "
                "YYYY-MM-DD "
                "format.",
                "title": "User Kyc Completed On",
            },
            "user_kyc_status": {
                "$ref": "#/definitions/KYCStatus",
                "description": "The KYC status of the user.",
            },
            "user_name": {
                "description": "The full name of the user.",
                "examples": ["John Smith"],
                "title": "User Name",
                "type": "string",
            },
        },
        "required": [
            "company_kyc_status",
            "company_id",
            "company_name",
            "company_address",
            "user_kyc_status",
            "user_email",
            "user_name",
            "user_id",
        ],
        "title": "CreateUserResponse",
        "type": "object",
    },
    "GetCompanies": {
        "description": "Represents response to GET companies request",
        "properties": {
            "companies": {
                "description": "All end user companies associated with the reseller.",
                "items": {"$ref": "#/definitions/GetCompany"},
                "title": "Companies",
                "type": "array",
            },
            "context": {
                "$ref": "#/definitions/ResponseContext",
                "description": "Context about the response.",
            },
            "links": {
                "description": "Links to previous and/or next page.",
                "items": {"$ref": "#/definitions/Link"},
                "title": "Links",
                "type": "array",
            },
        },
        "required": ["companies", "links", "context"],
        "title": "GetCompanies",
        "type": "object",
    },
    "GetCompany": {
        "properties": {
            "country": {
                "description": "Country of the company.",
                "examples": ["United Kingdom"],
                "title": "Country",
                "type": "string",
            },
            "country_code": {
                "description": "2-digit ISO country code of the company.",
                "enum": [
                    "AD",
                    "AE",
                    "AF",
                    "AG",
                    "AI",
                    "AL",
                    "AM",
                    "AO",
                    "AQ",
                    "AR",
                    "AT",
                    "AU",
                    "AW",
                    "AX",
                    "AZ",
                    "BA",
                    "BB",
                    "BD",
                    "BE",
                    "BF",
                    "BG",
                    "BH",
                    "BI",
                    "BJ",
                    "BL",
                    "BM",
                    "BN",
                    "BO",
                    "BQ",
                    "BR",
                    "BS",
                    "BT",
                    "BV",
                    "BW",
                    "BY",
                    "BZ",
                    "CA",
                    "CC",
                    "CD",
                    "CF",
                    "CG",
                    "CH",
                    "CI",
                    "CK",
                    "CL",
                    "CM",
                    "CN",
                    "CO",
                    "CR",
                    "CV",
                    "CW",
                    "CX",
                    "CY",
                    "CZ",
                    "DE",
                    "DJ",
                    "DK",
                    "DM",
                    "DO",
                    "DZ",
                    "EC",
                    "EE",
                    "EG",
                    "EH",
                    "ER",
                    "ES",
                    "ET",
                    "FI",
                    "FJ",
                    "FK",
                    "FO",
                    "FR",
                    "GA",
                    "GB",
                    "GD",
                    "GE",
                    "GF",
                    "GG",
                    "GH",
                    "GI",
                    "GL",
                    "GM",
                    "GN",
                    "GP",
                    "GQ",
                    "GR",
                    "GS",
                    "GT",
                    "GW",
                    "GY",
                    "HM",
                    "HN",
                    "HR",
                    "HT",
                    "HU",
                    "ID",
                    "IE",
                    "IL",
                    "IM",
                    "IN",
                    "IO",
                    "IQ",
                    "IS",
                    "IT",
                    "JE",
                    "JM",
                    "JO",
                    "JP",
                    "KE",
                    "KG",
                    "KH",
                    "KI",
                    "KM",
                    "KN",
                    "KR",
                    "KW",
                    "KY",
                    "KZ",
                    "LA",
                    "LB",
                    "LC",
                    "LI",
                    "LK",
                    "LR",
                    "LS",
                    "LT",
                    "LU",
                    "LV",
                    "LY",
                    "MA",
                    "MC",
                    "MD",
                    "ME",
                    "MF",
                    "MG",
                    "MK",
                    "ML",
                    "MM",
                    "MN",
                    "MO",
                    "MQ",
                    "MR",
                    "MS",
                    "MT",
                    "MU",
                    "MV",
                    "MW",
                    "MX",
                    "MY",
                    "MZ",
                    "NA",
                    "NC",
                    "NE",
                    "NF",
                    "NG",
                    "NI",
                    "NL",
                    "NO",
                    "NP",
                    "NR",
                    "NU",
                    "NZ",
                    "OM",
                    "PA",
                    "PE",
                    "PF",
                    "PG",
                    "PH",
                    "PK",
                    "PL",
                    "PM",
                    "PN",
                    "PS",
                    "PT",
                    "PY",
                    "QA",
                    "RE",
                    "RO",
                    "RS",
                    "RU",
                    "RW",
                    "SA",
                    "SB",
                    "SC",
                    "SE",
                    "SG",
                    "SH",
                    "SI",
                    "SJ",
                    "SK",
                    "SL",
                    "SM",
                    "SN",
                    "SO",
                    "SR",
                    "SS",
                    "ST",
                    "SV",
                    "SX",
                    "SZ",
                    "TC",
                    "TD",
                    "TF",
                    "TG",
                    "TH",
                    "TJ",
                    "TK",
                    "TL",
                    "TM",
                    "TN",
                    "TO",
                    "TR",
                    "TT",
                    "TV",
                    "TW",
                    "TZ",
                    "UA",
                    "UG",
                    "US",
                    "UY",
                    "UZ",
                    "VA",
                    "VC",
                    "VE",
                    "VG",
                    "VN",
                    "VU",
                    "WF",
                    "WS",
                    "XK",
                    "YE",
                    "YT",
                    "ZA",
                    "ZM",
                    "ZW",
                ],
                "examples": ["GB"],
                "title": "Country Code",
                "type": "string",
            },
            "created_date": {
                "description": "The date when the user was created.",
                "format": "date",
                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                "title": "Created Date",
                "type": "string",
            },
            "id": {
                "description": "Unique identifier of the company.",
                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                "format": "uuid",
                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                "title": "Id",
                "type": "string",
            },
            "kyc_completed_on": {
                "anyOf": [
                    {
                        "format": "date",
                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                        "type": "string",
                    },
                    {"type": "null"},
                ],
                "description": "The date "
                "when KYC "
                "was "
                "completed "
                "for the "
                "company, "
                "if "
                "applicable. "
                "In "
                "YYYY-MM-DD "
                "format.",
                "title": "Kyc Completed On",
            },
            "kyc_status": {
                "$ref": "#/definitions/KYCStatus",
                "description": "KYC status of the company.",
            },
            "name": {
                "description": "The name of the company.",
                "examples": ["John Smith's Company"],
                "title": "Name",
                "type": "string",
            },
            "updated_date": {
                "description": "The date when the user was last updated.",
                "format": "date",
                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                "title": "Updated Date",
                "type": "string",
            },
        },
        "required": [
            "name",
            "country",
            "country_code",
            "id",
            "kyc_status",
            "created_date",
            "updated_date",
        ],
        "title": "GetCompany",
        "type": "object",
    },
    "GetUser": {
        "description": "Represents response to user",
        "properties": {
            "company_id": {
                "description": "The unique identifier for the company.",
                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                "format": "uuid",
                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                "title": "Company Id",
                "type": "string",
            },
            "company_kyc_completed_on": {
                "anyOf": [
                    {
                        "format": "date",
                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                        "type": "string",
                    },
                    {"type": "null"},
                ],
                "description": "The "
                "date "
                "when "
                "KYC "
                "was "
                "completed "
                "for "
                "the "
                "company, "
                "if "
                "applicable. "
                "In "
                "YYYY-MM-DD "
                "format.",
                "title": "Company Kyc Completed On",
            },
            "company_kyc_status": {
                "$ref": "#/definitions/KYCStatus",
                "description": "The KYC status of the company.",
            },
            "company_name": {
                "description": "The name of the company.",
                "examples": ["John Smith's Company"],
                "title": "Company Name",
                "type": "string",
            },
            "user_created_date": {
                "description": "The date when the user was created.",
                "format": "date",
                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                "title": "User Created Date",
                "type": "string",
            },
            "user_email": {
                "description": "The email address of the user.",
                "examples": ["john@smith.com"],
                "title": "User Email",
                "type": "string",
            },
            "user_id": {
                "description": "The unique identifier for the user.",
                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                "title": "User Id",
                "type": "string",
            },
            "user_kyc_completed_on": {
                "anyOf": [
                    {
                        "format": "date",
                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                        "type": "string",
                    },
                    {"type": "null"},
                ],
                "description": "The date "
                "when KYC "
                "was "
                "completed "
                "for the "
                "user, if "
                "applicable. "
                "In "
                "YYYY-MM-DD "
                "format.",
                "title": "User Kyc Completed On",
            },
            "user_kyc_status": {
                "$ref": "#/definitions/KYCStatus",
                "description": "The KYC status of the user.",
            },
            "user_name": {
                "description": "The full name of the user.",
                "examples": ["John Smith"],
                "title": "User Name",
                "type": "string",
            },
            "user_updated_date": {
                "description": "The date when the user was last updated.",
                "format": "date",
                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                "title": "User Updated Date",
                "type": "string",
            },
        },
        "required": [
            "company_kyc_status",
            "company_id",
            "company_name",
            "user_kyc_status",
            "user_email",
            "user_name",
            "user_id",
            "user_created_date",
            "user_updated_date",
        ],
        "title": "GetUser",
        "type": "object",
    },
    "GetUsers": {
        "description": "Represents response to GET users request",
        "properties": {
            "context": {
                "$ref": "#/definitions/ResponseContext",
                "description": "Context about the response.",
            },
            "links": {
                "description": "Links to previous and/or next page.",
                "items": {"$ref": "#/definitions/Link"},
                "title": "Links",
                "type": "array",
            },
            "users": {
                "description": "All end users associated with the reseller.",
                "items": {"$ref": "#/definitions/GetUser"},
                "title": "Users",
                "type": "array",
            },
        },
        "required": ["users", "links", "context"],
        "title": "GetUsers",
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
    "KYCStatus": {
        "enum": ["Passed", "Not completed", "Failed"],
        "title": "KYCStatus",
        "type": "string",
    },
    "Link": {
        "properties": {
            "body": {
                "anyOf": [
                    {"additionalProperties": True, "type": "object"},
                    {"type": "null"},
                ],
                "description": "A JSON object containing "
                "fields/values that must be "
                "included in the body of the "
                "next request.",
                "title": "Body",
            },
            "href": {
                "description": "The link in the format of a URL.",
                "format": "uri",
                "minLength": 1,
                "title": "Href",
                "type": "string",
            },
            "merge": {
                "default": False,
                "description": "If `true`, the headers/body "
                "fields in the `next` link "
                "must be merged into the "
                "original request and be "
                "sent combined in the next "
                "request.",
                "title": "Merge",
                "type": "boolean",
            },
            "method": {
                "$ref": "#/definitions/RequestMethod",
                "default": "GET",
                "description": "The HTTP method of the request.",
            },
            "rel": {
                "description": "The relationship between the "
                "current document and the "
                "linked document.",
                "title": "Rel",
                "type": "string",
            },
            "title": {
                "description": "The title of the link.",
                "title": "Title",
                "type": "string",
            },
            "type": {
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "description": "The media type of the referenced entity.",
                "title": "Type",
            },
        },
        "required": ["href", "rel", "title"],
        "title": "Link",
        "type": "object",
    },
    "MatchType": {"enum": ["exact", "partial"], "title": "MatchType", "type": "string"},
    "RequestMethod": {"enum": ["GET"], "title": "RequestMethod", "type": "string"},
    "ResponseContext": {
        "description": "Contextual information for pagination responses",
        "properties": {
            "limit": {
                "description": "Applied per page results limit.",
                "examples": [25],
                "title": "Limit",
                "type": "integer",
            },
            "matched": {
                "description": "Total number of results.",
                "examples": [10],
                "title": "Matched",
                "type": "integer",
            },
            "returned": {
                "description": "Number of returned users in page.",
                "examples": [10],
                "title": "Returned",
                "type": "integer",
            },
        },
        "required": ["limit", "matched", "returned"],
        "title": "ResponseContext",
        "type": "object",
    },
    "SearchCompanies": {
        "additionalProperties": False,
        "properties": {
            "kyc_status": {
                "anyOf": [
                    {"items": {"$ref": "#/definitions/KYCStatus"}, "type": "array"},
                    {"$ref": "#/definitions/KYCStatus"},
                    {"type": "null"},
                ],
                "description": "The KYC status of the company.",
                "title": "Kyc Status",
            },
            "limit": {
                "default": 100,
                "description": "The number of results to return per page.",
                "maximum": 1000.0,
                "minimum": 1.0,
                "title": "Limit",
                "type": "integer",
            },
            "search": {
                "anyOf": [
                    {"items": {"$ref": "#/definitions/CompanySearch"}, "type": "array"},
                    {"$ref": "#/definitions/CompanySearch"},
                    {"type": "null"},
                ],
                "description": "Search criteria.",
                "title": "Search",
            },
            "token": {
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "description": "The pagination token.",
                "title": "Token",
            },
        },
        "title": "SearchCompanies",
        "type": "object",
    },
    "SearchUsers": {
        "additionalProperties": False,
        "properties": {
            "kyc_status": {
                "anyOf": [
                    {"items": {"$ref": "#/definitions/KYCStatus"}, "type": "array"},
                    {"$ref": "#/definitions/KYCStatus"},
                    {"type": "null"},
                ],
                "description": "The KYC status of the user.",
                "title": "Kyc Status",
            },
            "limit": {
                "default": 100,
                "description": "The number of results to return per page.",
                "maximum": 1000.0,
                "minimum": 1.0,
                "title": "Limit",
                "type": "integer",
            },
            "search": {
                "anyOf": [
                    {"items": {"$ref": "#/definitions/UserSearch"}, "type": "array"},
                    {"$ref": "#/definitions/UserSearch"},
                    {"type": "null"},
                ],
                "description": "Search criteria.",
                "title": "Search",
            },
            "token": {
                "anyOf": [{"type": "string"}, {"type": "null"}],
                "description": "The pagination token.",
                "title": "Token",
            },
        },
        "title": "SearchUsers",
        "type": "object",
    },
    "UserSearch": {
        "properties": {
            "fields": {
                "anyOf": [
                    {
                        "items": {"$ref": "#/definitions/UserSearchFields"},
                        "type": "array",
                    },
                    {"const": "all", "type": "string"},
                ],
                "default": "all",
                "description": "Fields to search "
                "against. Either a "
                "list of fields or "
                "`all`. Defaults to "
                "`all`.",
                "examples": ["all"],
                "title": "Fields",
            },
            "string": {
                "description": "Search string.",
                "title": "String",
                "type": "string",
            },
            "type": {
                "$ref": "#/definitions/MatchType",
                "default": "partial",
                "description": "Type of search.",
            },
        },
        "required": ["string"],
        "title": "UserSearch",
        "type": "object",
    },
    "UserSearchFields": {
        "enum": ["user_email", "user_name", "user_id", "company_name"],
        "title": "UserSearchFields",
        "type": "string",
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
    ("/companies", "get"): {
        "parameters": {},
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
                    "description": "Represents response to GET companies request",
                    "properties": {
                        "companies": {
                            "description": "All "
                            "end "
                            "user "
                            "companies "
                            "associated "
                            "with "
                            "the "
                            "reseller.",
                            "items": {"$ref": "#/definitions/GetCompany"},
                            "title": "Companies",
                            "type": "array",
                        },
                        "context": {
                            "$ref": "#/definitions/ResponseContext",
                            "description": "Context about the response.",
                        },
                        "links": {
                            "description": "Links to previous and/or next page.",
                            "items": {"$ref": "#/definitions/Link"},
                            "title": "Links",
                            "type": "array",
                        },
                    },
                    "required": ["companies", "links", "context"],
                    "title": "GetCompanies",
                    "type": "object",
                },
            },
            "422": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
    ("/search/companies", "post"): {
        "parameters": {},
        "requestBody": {
            "schema": {
                "additionalProperties": False,
                "definitions": {
                    "CompanyAddress": {
                        "properties": {
                            "country_code": {
                                "description": "2-digit country code of company.",
                                "enum": [
                                    "AD",
                                    "AE",
                                    "AF",
                                    "AG",
                                    "AI",
                                    "AL",
                                    "AM",
                                    "AO",
                                    "AQ",
                                    "AR",
                                    "AT",
                                    "AU",
                                    "AW",
                                    "AX",
                                    "AZ",
                                    "BA",
                                    "BB",
                                    "BD",
                                    "BE",
                                    "BF",
                                    "BG",
                                    "BH",
                                    "BI",
                                    "BJ",
                                    "BL",
                                    "BM",
                                    "BN",
                                    "BO",
                                    "BQ",
                                    "BR",
                                    "BS",
                                    "BT",
                                    "BV",
                                    "BW",
                                    "BY",
                                    "BZ",
                                    "CA",
                                    "CC",
                                    "CD",
                                    "CF",
                                    "CG",
                                    "CH",
                                    "CI",
                                    "CK",
                                    "CL",
                                    "CM",
                                    "CN",
                                    "CO",
                                    "CR",
                                    "CV",
                                    "CW",
                                    "CX",
                                    "CY",
                                    "CZ",
                                    "DE",
                                    "DJ",
                                    "DK",
                                    "DM",
                                    "DO",
                                    "DZ",
                                    "EC",
                                    "EE",
                                    "EG",
                                    "EH",
                                    "ER",
                                    "ES",
                                    "ET",
                                    "FI",
                                    "FJ",
                                    "FK",
                                    "FO",
                                    "FR",
                                    "GA",
                                    "GB",
                                    "GD",
                                    "GE",
                                    "GF",
                                    "GG",
                                    "GH",
                                    "GI",
                                    "GL",
                                    "GM",
                                    "GN",
                                    "GP",
                                    "GQ",
                                    "GR",
                                    "GS",
                                    "GT",
                                    "GW",
                                    "GY",
                                    "HM",
                                    "HN",
                                    "HR",
                                    "HT",
                                    "HU",
                                    "ID",
                                    "IE",
                                    "IL",
                                    "IM",
                                    "IN",
                                    "IO",
                                    "IQ",
                                    "IS",
                                    "IT",
                                    "JE",
                                    "JM",
                                    "JO",
                                    "JP",
                                    "KE",
                                    "KG",
                                    "KH",
                                    "KI",
                                    "KM",
                                    "KN",
                                    "KR",
                                    "KW",
                                    "KY",
                                    "KZ",
                                    "LA",
                                    "LB",
                                    "LC",
                                    "LI",
                                    "LK",
                                    "LR",
                                    "LS",
                                    "LT",
                                    "LU",
                                    "LV",
                                    "LY",
                                    "MA",
                                    "MC",
                                    "MD",
                                    "ME",
                                    "MF",
                                    "MG",
                                    "MK",
                                    "ML",
                                    "MM",
                                    "MN",
                                    "MO",
                                    "MQ",
                                    "MR",
                                    "MS",
                                    "MT",
                                    "MU",
                                    "MV",
                                    "MW",
                                    "MX",
                                    "MY",
                                    "MZ",
                                    "NA",
                                    "NC",
                                    "NE",
                                    "NF",
                                    "NG",
                                    "NI",
                                    "NL",
                                    "NO",
                                    "NP",
                                    "NR",
                                    "NU",
                                    "NZ",
                                    "OM",
                                    "PA",
                                    "PE",
                                    "PF",
                                    "PG",
                                    "PH",
                                    "PK",
                                    "PL",
                                    "PM",
                                    "PN",
                                    "PS",
                                    "PT",
                                    "PY",
                                    "QA",
                                    "RE",
                                    "RO",
                                    "RS",
                                    "RU",
                                    "RW",
                                    "SA",
                                    "SB",
                                    "SC",
                                    "SE",
                                    "SG",
                                    "SH",
                                    "SI",
                                    "SJ",
                                    "SK",
                                    "SL",
                                    "SM",
                                    "SN",
                                    "SO",
                                    "SR",
                                    "SS",
                                    "ST",
                                    "SV",
                                    "SX",
                                    "SZ",
                                    "TC",
                                    "TD",
                                    "TF",
                                    "TG",
                                    "TH",
                                    "TJ",
                                    "TK",
                                    "TL",
                                    "TM",
                                    "TN",
                                    "TO",
                                    "TR",
                                    "TT",
                                    "TV",
                                    "TW",
                                    "TZ",
                                    "UA",
                                    "UG",
                                    "US",
                                    "UY",
                                    "UZ",
                                    "VA",
                                    "VC",
                                    "VE",
                                    "VG",
                                    "VN",
                                    "VU",
                                    "WF",
                                    "WS",
                                    "XK",
                                    "YE",
                                    "YT",
                                    "ZA",
                                    "ZM",
                                    "ZW",
                                ],
                                "examples": ["GB"],
                                "title": "Country Code",
                                "type": "string",
                            },
                            "postcode": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The postcode/zip code of the company.",
                                "examples": ["J1 ABC"],
                                "title": "Postcode",
                            },
                            "street": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The street of the company.",
                                "examples": ["1 John Lane"],
                                "title": "Street",
                            },
                        },
                        "required": ["country_code"],
                        "title": "CompanyAddress",
                        "type": "object",
                    },
                    "CompanySearch": {
                        "properties": {
                            "fields": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/CompanySearchFields"
                                        },
                                        "type": "array",
                                    },
                                    {"const": "all", "type": "string"},
                                ],
                                "default": "all",
                                "description": "Fields "
                                "to "
                                "search "
                                "against. "
                                "Either "
                                "a "
                                "list "
                                "of "
                                "fields "
                                "or "
                                "`all`. "
                                "Defaults "
                                "to "
                                "`all`.",
                                "examples": ["all"],
                                "title": "Fields",
                            },
                            "string": {
                                "description": "Search string.",
                                "title": "String",
                                "type": "string",
                            },
                            "type": {
                                "$ref": "#/definitions/MatchType",
                                "default": "partial",
                                "description": "Type of search.",
                            },
                        },
                        "required": ["string"],
                        "title": "CompanySearch",
                        "type": "object",
                    },
                    "CompanySearchFields": {
                        "enum": ["name", "id"],
                        "title": "CompanySearchFields",
                        "type": "string",
                    },
                    "CreateUser": {
                        "description": "Represents payload to create a user",
                        "properties": {
                            "company_address": {
                                "$ref": "#/definitions/CompanyAddress",
                                "description": "The address of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                        },
                        "required": [
                            "user_email",
                            "user_name",
                            "company_name",
                            "company_address",
                        ],
                        "title": "CreateUser",
                        "type": "object",
                    },
                    "CreateUserResponse": {
                        "description": "Represents response when creating user",
                        "properties": {
                            "company_address": {
                                "$ref": "#/definitions/CompanyAddress",
                                "description": "The address of the company.",
                            },
                            "company_id": {
                                "description": "The unique identifier for the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Company Id",
                                "type": "string",
                            },
                            "company_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Company Kyc Completed On",
                            },
                            "company_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_id": {
                                "description": "The unique identifier for the user.",
                                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                                "title": "User Id",
                                "type": "string",
                            },
                            "user_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "user, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "User Kyc Completed On",
                            },
                            "user_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the user.",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                        },
                        "required": [
                            "company_kyc_status",
                            "company_id",
                            "company_name",
                            "company_address",
                            "user_kyc_status",
                            "user_email",
                            "user_name",
                            "user_id",
                        ],
                        "title": "CreateUserResponse",
                        "type": "object",
                    },
                    "GetCompanies": {
                        "description": "Represents response to GET companies request",
                        "properties": {
                            "companies": {
                                "description": "All "
                                "end "
                                "user "
                                "companies "
                                "associated "
                                "with "
                                "the "
                                "reseller.",
                                "items": {"$ref": "#/definitions/GetCompany"},
                                "title": "Companies",
                                "type": "array",
                            },
                            "context": {
                                "$ref": "#/definitions/ResponseContext",
                                "description": "Context about the response.",
                            },
                            "links": {
                                "description": "Links to previous and/or next page.",
                                "items": {"$ref": "#/definitions/Link"},
                                "title": "Links",
                                "type": "array",
                            },
                        },
                        "required": ["companies", "links", "context"],
                        "title": "GetCompanies",
                        "type": "object",
                    },
                    "GetCompany": {
                        "properties": {
                            "country": {
                                "description": "Country of the company.",
                                "examples": ["United Kingdom"],
                                "title": "Country",
                                "type": "string",
                            },
                            "country_code": {
                                "description": "2-digit "
                                "ISO "
                                "country "
                                "code "
                                "of "
                                "the "
                                "company.",
                                "enum": [
                                    "AD",
                                    "AE",
                                    "AF",
                                    "AG",
                                    "AI",
                                    "AL",
                                    "AM",
                                    "AO",
                                    "AQ",
                                    "AR",
                                    "AT",
                                    "AU",
                                    "AW",
                                    "AX",
                                    "AZ",
                                    "BA",
                                    "BB",
                                    "BD",
                                    "BE",
                                    "BF",
                                    "BG",
                                    "BH",
                                    "BI",
                                    "BJ",
                                    "BL",
                                    "BM",
                                    "BN",
                                    "BO",
                                    "BQ",
                                    "BR",
                                    "BS",
                                    "BT",
                                    "BV",
                                    "BW",
                                    "BY",
                                    "BZ",
                                    "CA",
                                    "CC",
                                    "CD",
                                    "CF",
                                    "CG",
                                    "CH",
                                    "CI",
                                    "CK",
                                    "CL",
                                    "CM",
                                    "CN",
                                    "CO",
                                    "CR",
                                    "CV",
                                    "CW",
                                    "CX",
                                    "CY",
                                    "CZ",
                                    "DE",
                                    "DJ",
                                    "DK",
                                    "DM",
                                    "DO",
                                    "DZ",
                                    "EC",
                                    "EE",
                                    "EG",
                                    "EH",
                                    "ER",
                                    "ES",
                                    "ET",
                                    "FI",
                                    "FJ",
                                    "FK",
                                    "FO",
                                    "FR",
                                    "GA",
                                    "GB",
                                    "GD",
                                    "GE",
                                    "GF",
                                    "GG",
                                    "GH",
                                    "GI",
                                    "GL",
                                    "GM",
                                    "GN",
                                    "GP",
                                    "GQ",
                                    "GR",
                                    "GS",
                                    "GT",
                                    "GW",
                                    "GY",
                                    "HM",
                                    "HN",
                                    "HR",
                                    "HT",
                                    "HU",
                                    "ID",
                                    "IE",
                                    "IL",
                                    "IM",
                                    "IN",
                                    "IO",
                                    "IQ",
                                    "IS",
                                    "IT",
                                    "JE",
                                    "JM",
                                    "JO",
                                    "JP",
                                    "KE",
                                    "KG",
                                    "KH",
                                    "KI",
                                    "KM",
                                    "KN",
                                    "KR",
                                    "KW",
                                    "KY",
                                    "KZ",
                                    "LA",
                                    "LB",
                                    "LC",
                                    "LI",
                                    "LK",
                                    "LR",
                                    "LS",
                                    "LT",
                                    "LU",
                                    "LV",
                                    "LY",
                                    "MA",
                                    "MC",
                                    "MD",
                                    "ME",
                                    "MF",
                                    "MG",
                                    "MK",
                                    "ML",
                                    "MM",
                                    "MN",
                                    "MO",
                                    "MQ",
                                    "MR",
                                    "MS",
                                    "MT",
                                    "MU",
                                    "MV",
                                    "MW",
                                    "MX",
                                    "MY",
                                    "MZ",
                                    "NA",
                                    "NC",
                                    "NE",
                                    "NF",
                                    "NG",
                                    "NI",
                                    "NL",
                                    "NO",
                                    "NP",
                                    "NR",
                                    "NU",
                                    "NZ",
                                    "OM",
                                    "PA",
                                    "PE",
                                    "PF",
                                    "PG",
                                    "PH",
                                    "PK",
                                    "PL",
                                    "PM",
                                    "PN",
                                    "PS",
                                    "PT",
                                    "PY",
                                    "QA",
                                    "RE",
                                    "RO",
                                    "RS",
                                    "RU",
                                    "RW",
                                    "SA",
                                    "SB",
                                    "SC",
                                    "SE",
                                    "SG",
                                    "SH",
                                    "SI",
                                    "SJ",
                                    "SK",
                                    "SL",
                                    "SM",
                                    "SN",
                                    "SO",
                                    "SR",
                                    "SS",
                                    "ST",
                                    "SV",
                                    "SX",
                                    "SZ",
                                    "TC",
                                    "TD",
                                    "TF",
                                    "TG",
                                    "TH",
                                    "TJ",
                                    "TK",
                                    "TL",
                                    "TM",
                                    "TN",
                                    "TO",
                                    "TR",
                                    "TT",
                                    "TV",
                                    "TW",
                                    "TZ",
                                    "UA",
                                    "UG",
                                    "US",
                                    "UY",
                                    "UZ",
                                    "VA",
                                    "VC",
                                    "VE",
                                    "VG",
                                    "VN",
                                    "VU",
                                    "WF",
                                    "WS",
                                    "XK",
                                    "YE",
                                    "YT",
                                    "ZA",
                                    "ZM",
                                    "ZW",
                                ],
                                "examples": ["GB"],
                                "title": "Country Code",
                                "type": "string",
                            },
                            "created_date": {
                                "description": "The date when the user was created.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "Created Date",
                                "type": "string",
                            },
                            "id": {
                                "description": "Unique identifier of the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Id",
                                "type": "string",
                            },
                            "kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Kyc Completed On",
                            },
                            "kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "KYC status of the company.",
                            },
                            "name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Name",
                                "type": "string",
                            },
                            "updated_date": {
                                "description": "The "
                                "date "
                                "when "
                                "the "
                                "user "
                                "was "
                                "last "
                                "updated.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "Updated Date",
                                "type": "string",
                            },
                        },
                        "required": [
                            "name",
                            "country",
                            "country_code",
                            "id",
                            "kyc_status",
                            "created_date",
                            "updated_date",
                        ],
                        "title": "GetCompany",
                        "type": "object",
                    },
                    "GetUser": {
                        "description": "Represents response to user",
                        "properties": {
                            "company_id": {
                                "description": "The unique identifier for the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Company Id",
                                "type": "string",
                            },
                            "company_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Company Kyc Completed On",
                            },
                            "company_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_created_date": {
                                "description": "The date when the user was created.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "User Created Date",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_id": {
                                "description": "The unique identifier for the user.",
                                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                                "title": "User Id",
                                "type": "string",
                            },
                            "user_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "user, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "User Kyc Completed On",
                            },
                            "user_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the user.",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                            "user_updated_date": {
                                "description": "The "
                                "date "
                                "when "
                                "the "
                                "user "
                                "was "
                                "last "
                                "updated.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "User Updated Date",
                                "type": "string",
                            },
                        },
                        "required": [
                            "company_kyc_status",
                            "company_id",
                            "company_name",
                            "user_kyc_status",
                            "user_email",
                            "user_name",
                            "user_id",
                            "user_created_date",
                            "user_updated_date",
                        ],
                        "title": "GetUser",
                        "type": "object",
                    },
                    "GetUsers": {
                        "description": "Represents response to GET users request",
                        "properties": {
                            "context": {
                                "$ref": "#/definitions/ResponseContext",
                                "description": "Context about the response.",
                            },
                            "links": {
                                "description": "Links to previous and/or next page.",
                                "items": {"$ref": "#/definitions/Link"},
                                "title": "Links",
                                "type": "array",
                            },
                            "users": {
                                "description": "All "
                                "end "
                                "users "
                                "associated "
                                "with "
                                "the "
                                "reseller.",
                                "items": {"$ref": "#/definitions/GetUser"},
                                "title": "Users",
                                "type": "array",
                            },
                        },
                        "required": ["users", "links", "context"],
                        "title": "GetUsers",
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
                    "KYCStatus": {
                        "enum": ["Passed", "Not completed", "Failed"],
                        "title": "KYCStatus",
                        "type": "string",
                    },
                    "Link": {
                        "properties": {
                            "body": {
                                "anyOf": [
                                    {"additionalProperties": True, "type": "object"},
                                    {"type": "null"},
                                ],
                                "description": "A "
                                "JSON "
                                "object "
                                "containing "
                                "fields/values "
                                "that "
                                "must "
                                "be "
                                "included "
                                "in "
                                "the "
                                "body "
                                "of "
                                "the "
                                "next "
                                "request.",
                                "title": "Body",
                            },
                            "href": {
                                "description": "The link in the format of a URL.",
                                "format": "uri",
                                "minLength": 1,
                                "title": "Href",
                                "type": "string",
                            },
                            "merge": {
                                "default": False,
                                "description": "If "
                                "`true`, "
                                "the "
                                "headers/body "
                                "fields "
                                "in "
                                "the "
                                "`next` "
                                "link "
                                "must "
                                "be "
                                "merged "
                                "into "
                                "the "
                                "original "
                                "request "
                                "and "
                                "be "
                                "sent "
                                "combined "
                                "in "
                                "the "
                                "next "
                                "request.",
                                "title": "Merge",
                                "type": "boolean",
                            },
                            "method": {
                                "$ref": "#/definitions/RequestMethod",
                                "default": "GET",
                                "description": "The HTTP method of the request.",
                            },
                            "rel": {
                                "description": "The "
                                "relationship "
                                "between "
                                "the "
                                "current "
                                "document "
                                "and "
                                "the "
                                "linked "
                                "document.",
                                "title": "Rel",
                                "type": "string",
                            },
                            "title": {
                                "description": "The title of the link.",
                                "title": "Title",
                                "type": "string",
                            },
                            "type": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The "
                                "media "
                                "type "
                                "of "
                                "the "
                                "referenced "
                                "entity.",
                                "title": "Type",
                            },
                        },
                        "required": ["href", "rel", "title"],
                        "title": "Link",
                        "type": "object",
                    },
                    "MatchType": {
                        "enum": ["exact", "partial"],
                        "title": "MatchType",
                        "type": "string",
                    },
                    "RequestMethod": {
                        "enum": ["GET"],
                        "title": "RequestMethod",
                        "type": "string",
                    },
                    "ResponseContext": {
                        "description": "Contextual "
                        "information "
                        "for "
                        "pagination "
                        "responses",
                        "properties": {
                            "limit": {
                                "description": "Applied per page results limit.",
                                "examples": [25],
                                "title": "Limit",
                                "type": "integer",
                            },
                            "matched": {
                                "description": "Total number of results.",
                                "examples": [10],
                                "title": "Matched",
                                "type": "integer",
                            },
                            "returned": {
                                "description": "Number of returned users in page.",
                                "examples": [10],
                                "title": "Returned",
                                "type": "integer",
                            },
                        },
                        "required": ["limit", "matched", "returned"],
                        "title": "ResponseContext",
                        "type": "object",
                    },
                    "SearchCompanies": {
                        "additionalProperties": False,
                        "properties": {
                            "kyc_status": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/KYCStatus"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/KYCStatus"},
                                    {"type": "null"},
                                ],
                                "description": "The KYC status of the company.",
                                "title": "Kyc Status",
                            },
                            "limit": {
                                "default": 100,
                                "description": "The "
                                "number "
                                "of "
                                "results "
                                "to "
                                "return "
                                "per "
                                "page.",
                                "maximum": 1000.0,
                                "minimum": 1.0,
                                "title": "Limit",
                                "type": "integer",
                            },
                            "search": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/CompanySearch"
                                        },
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/CompanySearch"},
                                    {"type": "null"},
                                ],
                                "description": "Search criteria.",
                                "title": "Search",
                            },
                            "token": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The pagination token.",
                                "title": "Token",
                            },
                        },
                        "title": "SearchCompanies",
                        "type": "object",
                    },
                    "SearchUsers": {
                        "additionalProperties": False,
                        "properties": {
                            "kyc_status": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/KYCStatus"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/KYCStatus"},
                                    {"type": "null"},
                                ],
                                "description": "The KYC status of the user.",
                                "title": "Kyc Status",
                            },
                            "limit": {
                                "default": 100,
                                "description": "The "
                                "number "
                                "of "
                                "results "
                                "to "
                                "return "
                                "per "
                                "page.",
                                "maximum": 1000.0,
                                "minimum": 1.0,
                                "title": "Limit",
                                "type": "integer",
                            },
                            "search": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/UserSearch"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/UserSearch"},
                                    {"type": "null"},
                                ],
                                "description": "Search criteria.",
                                "title": "Search",
                            },
                            "token": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The pagination token.",
                                "title": "Token",
                            },
                        },
                        "title": "SearchUsers",
                        "type": "object",
                    },
                    "UserSearch": {
                        "properties": {
                            "fields": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/UserSearchFields"
                                        },
                                        "type": "array",
                                    },
                                    {"const": "all", "type": "string"},
                                ],
                                "default": "all",
                                "description": "Fields "
                                "to "
                                "search "
                                "against. "
                                "Either "
                                "a "
                                "list "
                                "of "
                                "fields "
                                "or "
                                "`all`. "
                                "Defaults "
                                "to "
                                "`all`.",
                                "examples": ["all"],
                                "title": "Fields",
                            },
                            "string": {
                                "description": "Search string.",
                                "title": "String",
                                "type": "string",
                            },
                            "type": {
                                "$ref": "#/definitions/MatchType",
                                "default": "partial",
                                "description": "Type of search.",
                            },
                        },
                        "required": ["string"],
                        "title": "UserSearch",
                        "type": "object",
                    },
                    "UserSearchFields": {
                        "enum": ["user_email", "user_name", "user_id", "company_name"],
                        "title": "UserSearchFields",
                        "type": "string",
                    },
                    "ValidationError": {
                        "properties": {
                            "ctx": {"title": "Context", "type": "object"},
                            "input": {"title": "Input"},
                            "loc": {
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
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
                    "kyc_status": {
                        "anyOf": [
                            {
                                "items": {"$ref": "#/definitions/KYCStatus"},
                                "type": "array",
                            },
                            {"$ref": "#/definitions/KYCStatus"},
                            {"type": "null"},
                        ],
                        "description": "The KYC status of the company.",
                        "title": "Kyc Status",
                    },
                    "limit": {
                        "default": 100,
                        "description": "The number of results to return per page.",
                        "maximum": 1000.0,
                        "minimum": 1.0,
                        "title": "Limit",
                        "type": "integer",
                    },
                    "search": {
                        "anyOf": [
                            {
                                "items": {"$ref": "#/definitions/CompanySearch"},
                                "type": "array",
                            },
                            {"$ref": "#/definitions/CompanySearch"},
                            {"type": "null"},
                        ],
                        "description": "Search criteria.",
                        "title": "Search",
                    },
                    "token": {
                        "anyOf": [{"type": "string"}, {"type": "null"}],
                        "description": "The pagination token.",
                        "title": "Token",
                    },
                },
                "title": "SearchCompanies",
                "type": "object",
            }
        },
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
                    "description": "Represents response to GET companies request",
                    "properties": {
                        "companies": {
                            "description": "All "
                            "end "
                            "user "
                            "companies "
                            "associated "
                            "with "
                            "the "
                            "reseller.",
                            "items": {"$ref": "#/definitions/GetCompany"},
                            "title": "Companies",
                            "type": "array",
                        },
                        "context": {
                            "$ref": "#/definitions/ResponseContext",
                            "description": "Context about the response.",
                        },
                        "links": {
                            "description": "Links to previous and/or next page.",
                            "items": {"$ref": "#/definitions/Link"},
                            "title": "Links",
                            "type": "array",
                        },
                    },
                    "required": ["companies", "links", "context"],
                    "title": "GetCompanies",
                    "type": "object",
                },
            },
            "422": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
    ("/search/users", "post"): {
        "parameters": {},
        "requestBody": {
            "schema": {
                "additionalProperties": False,
                "definitions": {
                    "CompanyAddress": {
                        "properties": {
                            "country_code": {
                                "description": "2-digit country code of company.",
                                "enum": [
                                    "AD",
                                    "AE",
                                    "AF",
                                    "AG",
                                    "AI",
                                    "AL",
                                    "AM",
                                    "AO",
                                    "AQ",
                                    "AR",
                                    "AT",
                                    "AU",
                                    "AW",
                                    "AX",
                                    "AZ",
                                    "BA",
                                    "BB",
                                    "BD",
                                    "BE",
                                    "BF",
                                    "BG",
                                    "BH",
                                    "BI",
                                    "BJ",
                                    "BL",
                                    "BM",
                                    "BN",
                                    "BO",
                                    "BQ",
                                    "BR",
                                    "BS",
                                    "BT",
                                    "BV",
                                    "BW",
                                    "BY",
                                    "BZ",
                                    "CA",
                                    "CC",
                                    "CD",
                                    "CF",
                                    "CG",
                                    "CH",
                                    "CI",
                                    "CK",
                                    "CL",
                                    "CM",
                                    "CN",
                                    "CO",
                                    "CR",
                                    "CV",
                                    "CW",
                                    "CX",
                                    "CY",
                                    "CZ",
                                    "DE",
                                    "DJ",
                                    "DK",
                                    "DM",
                                    "DO",
                                    "DZ",
                                    "EC",
                                    "EE",
                                    "EG",
                                    "EH",
                                    "ER",
                                    "ES",
                                    "ET",
                                    "FI",
                                    "FJ",
                                    "FK",
                                    "FO",
                                    "FR",
                                    "GA",
                                    "GB",
                                    "GD",
                                    "GE",
                                    "GF",
                                    "GG",
                                    "GH",
                                    "GI",
                                    "GL",
                                    "GM",
                                    "GN",
                                    "GP",
                                    "GQ",
                                    "GR",
                                    "GS",
                                    "GT",
                                    "GW",
                                    "GY",
                                    "HM",
                                    "HN",
                                    "HR",
                                    "HT",
                                    "HU",
                                    "ID",
                                    "IE",
                                    "IL",
                                    "IM",
                                    "IN",
                                    "IO",
                                    "IQ",
                                    "IS",
                                    "IT",
                                    "JE",
                                    "JM",
                                    "JO",
                                    "JP",
                                    "KE",
                                    "KG",
                                    "KH",
                                    "KI",
                                    "KM",
                                    "KN",
                                    "KR",
                                    "KW",
                                    "KY",
                                    "KZ",
                                    "LA",
                                    "LB",
                                    "LC",
                                    "LI",
                                    "LK",
                                    "LR",
                                    "LS",
                                    "LT",
                                    "LU",
                                    "LV",
                                    "LY",
                                    "MA",
                                    "MC",
                                    "MD",
                                    "ME",
                                    "MF",
                                    "MG",
                                    "MK",
                                    "ML",
                                    "MM",
                                    "MN",
                                    "MO",
                                    "MQ",
                                    "MR",
                                    "MS",
                                    "MT",
                                    "MU",
                                    "MV",
                                    "MW",
                                    "MX",
                                    "MY",
                                    "MZ",
                                    "NA",
                                    "NC",
                                    "NE",
                                    "NF",
                                    "NG",
                                    "NI",
                                    "NL",
                                    "NO",
                                    "NP",
                                    "NR",
                                    "NU",
                                    "NZ",
                                    "OM",
                                    "PA",
                                    "PE",
                                    "PF",
                                    "PG",
                                    "PH",
                                    "PK",
                                    "PL",
                                    "PM",
                                    "PN",
                                    "PS",
                                    "PT",
                                    "PY",
                                    "QA",
                                    "RE",
                                    "RO",
                                    "RS",
                                    "RU",
                                    "RW",
                                    "SA",
                                    "SB",
                                    "SC",
                                    "SE",
                                    "SG",
                                    "SH",
                                    "SI",
                                    "SJ",
                                    "SK",
                                    "SL",
                                    "SM",
                                    "SN",
                                    "SO",
                                    "SR",
                                    "SS",
                                    "ST",
                                    "SV",
                                    "SX",
                                    "SZ",
                                    "TC",
                                    "TD",
                                    "TF",
                                    "TG",
                                    "TH",
                                    "TJ",
                                    "TK",
                                    "TL",
                                    "TM",
                                    "TN",
                                    "TO",
                                    "TR",
                                    "TT",
                                    "TV",
                                    "TW",
                                    "TZ",
                                    "UA",
                                    "UG",
                                    "US",
                                    "UY",
                                    "UZ",
                                    "VA",
                                    "VC",
                                    "VE",
                                    "VG",
                                    "VN",
                                    "VU",
                                    "WF",
                                    "WS",
                                    "XK",
                                    "YE",
                                    "YT",
                                    "ZA",
                                    "ZM",
                                    "ZW",
                                ],
                                "examples": ["GB"],
                                "title": "Country Code",
                                "type": "string",
                            },
                            "postcode": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The postcode/zip code of the company.",
                                "examples": ["J1 ABC"],
                                "title": "Postcode",
                            },
                            "street": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The street of the company.",
                                "examples": ["1 John Lane"],
                                "title": "Street",
                            },
                        },
                        "required": ["country_code"],
                        "title": "CompanyAddress",
                        "type": "object",
                    },
                    "CompanySearch": {
                        "properties": {
                            "fields": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/CompanySearchFields"
                                        },
                                        "type": "array",
                                    },
                                    {"const": "all", "type": "string"},
                                ],
                                "default": "all",
                                "description": "Fields "
                                "to "
                                "search "
                                "against. "
                                "Either "
                                "a "
                                "list "
                                "of "
                                "fields "
                                "or "
                                "`all`. "
                                "Defaults "
                                "to "
                                "`all`.",
                                "examples": ["all"],
                                "title": "Fields",
                            },
                            "string": {
                                "description": "Search string.",
                                "title": "String",
                                "type": "string",
                            },
                            "type": {
                                "$ref": "#/definitions/MatchType",
                                "default": "partial",
                                "description": "Type of search.",
                            },
                        },
                        "required": ["string"],
                        "title": "CompanySearch",
                        "type": "object",
                    },
                    "CompanySearchFields": {
                        "enum": ["name", "id"],
                        "title": "CompanySearchFields",
                        "type": "string",
                    },
                    "CreateUser": {
                        "description": "Represents payload to create a user",
                        "properties": {
                            "company_address": {
                                "$ref": "#/definitions/CompanyAddress",
                                "description": "The address of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                        },
                        "required": [
                            "user_email",
                            "user_name",
                            "company_name",
                            "company_address",
                        ],
                        "title": "CreateUser",
                        "type": "object",
                    },
                    "CreateUserResponse": {
                        "description": "Represents response when creating user",
                        "properties": {
                            "company_address": {
                                "$ref": "#/definitions/CompanyAddress",
                                "description": "The address of the company.",
                            },
                            "company_id": {
                                "description": "The unique identifier for the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Company Id",
                                "type": "string",
                            },
                            "company_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Company Kyc Completed On",
                            },
                            "company_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_id": {
                                "description": "The unique identifier for the user.",
                                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                                "title": "User Id",
                                "type": "string",
                            },
                            "user_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "user, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "User Kyc Completed On",
                            },
                            "user_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the user.",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                        },
                        "required": [
                            "company_kyc_status",
                            "company_id",
                            "company_name",
                            "company_address",
                            "user_kyc_status",
                            "user_email",
                            "user_name",
                            "user_id",
                        ],
                        "title": "CreateUserResponse",
                        "type": "object",
                    },
                    "GetCompanies": {
                        "description": "Represents response to GET companies request",
                        "properties": {
                            "companies": {
                                "description": "All "
                                "end "
                                "user "
                                "companies "
                                "associated "
                                "with "
                                "the "
                                "reseller.",
                                "items": {"$ref": "#/definitions/GetCompany"},
                                "title": "Companies",
                                "type": "array",
                            },
                            "context": {
                                "$ref": "#/definitions/ResponseContext",
                                "description": "Context about the response.",
                            },
                            "links": {
                                "description": "Links to previous and/or next page.",
                                "items": {"$ref": "#/definitions/Link"},
                                "title": "Links",
                                "type": "array",
                            },
                        },
                        "required": ["companies", "links", "context"],
                        "title": "GetCompanies",
                        "type": "object",
                    },
                    "GetCompany": {
                        "properties": {
                            "country": {
                                "description": "Country of the company.",
                                "examples": ["United Kingdom"],
                                "title": "Country",
                                "type": "string",
                            },
                            "country_code": {
                                "description": "2-digit "
                                "ISO "
                                "country "
                                "code "
                                "of "
                                "the "
                                "company.",
                                "enum": [
                                    "AD",
                                    "AE",
                                    "AF",
                                    "AG",
                                    "AI",
                                    "AL",
                                    "AM",
                                    "AO",
                                    "AQ",
                                    "AR",
                                    "AT",
                                    "AU",
                                    "AW",
                                    "AX",
                                    "AZ",
                                    "BA",
                                    "BB",
                                    "BD",
                                    "BE",
                                    "BF",
                                    "BG",
                                    "BH",
                                    "BI",
                                    "BJ",
                                    "BL",
                                    "BM",
                                    "BN",
                                    "BO",
                                    "BQ",
                                    "BR",
                                    "BS",
                                    "BT",
                                    "BV",
                                    "BW",
                                    "BY",
                                    "BZ",
                                    "CA",
                                    "CC",
                                    "CD",
                                    "CF",
                                    "CG",
                                    "CH",
                                    "CI",
                                    "CK",
                                    "CL",
                                    "CM",
                                    "CN",
                                    "CO",
                                    "CR",
                                    "CV",
                                    "CW",
                                    "CX",
                                    "CY",
                                    "CZ",
                                    "DE",
                                    "DJ",
                                    "DK",
                                    "DM",
                                    "DO",
                                    "DZ",
                                    "EC",
                                    "EE",
                                    "EG",
                                    "EH",
                                    "ER",
                                    "ES",
                                    "ET",
                                    "FI",
                                    "FJ",
                                    "FK",
                                    "FO",
                                    "FR",
                                    "GA",
                                    "GB",
                                    "GD",
                                    "GE",
                                    "GF",
                                    "GG",
                                    "GH",
                                    "GI",
                                    "GL",
                                    "GM",
                                    "GN",
                                    "GP",
                                    "GQ",
                                    "GR",
                                    "GS",
                                    "GT",
                                    "GW",
                                    "GY",
                                    "HM",
                                    "HN",
                                    "HR",
                                    "HT",
                                    "HU",
                                    "ID",
                                    "IE",
                                    "IL",
                                    "IM",
                                    "IN",
                                    "IO",
                                    "IQ",
                                    "IS",
                                    "IT",
                                    "JE",
                                    "JM",
                                    "JO",
                                    "JP",
                                    "KE",
                                    "KG",
                                    "KH",
                                    "KI",
                                    "KM",
                                    "KN",
                                    "KR",
                                    "KW",
                                    "KY",
                                    "KZ",
                                    "LA",
                                    "LB",
                                    "LC",
                                    "LI",
                                    "LK",
                                    "LR",
                                    "LS",
                                    "LT",
                                    "LU",
                                    "LV",
                                    "LY",
                                    "MA",
                                    "MC",
                                    "MD",
                                    "ME",
                                    "MF",
                                    "MG",
                                    "MK",
                                    "ML",
                                    "MM",
                                    "MN",
                                    "MO",
                                    "MQ",
                                    "MR",
                                    "MS",
                                    "MT",
                                    "MU",
                                    "MV",
                                    "MW",
                                    "MX",
                                    "MY",
                                    "MZ",
                                    "NA",
                                    "NC",
                                    "NE",
                                    "NF",
                                    "NG",
                                    "NI",
                                    "NL",
                                    "NO",
                                    "NP",
                                    "NR",
                                    "NU",
                                    "NZ",
                                    "OM",
                                    "PA",
                                    "PE",
                                    "PF",
                                    "PG",
                                    "PH",
                                    "PK",
                                    "PL",
                                    "PM",
                                    "PN",
                                    "PS",
                                    "PT",
                                    "PY",
                                    "QA",
                                    "RE",
                                    "RO",
                                    "RS",
                                    "RU",
                                    "RW",
                                    "SA",
                                    "SB",
                                    "SC",
                                    "SE",
                                    "SG",
                                    "SH",
                                    "SI",
                                    "SJ",
                                    "SK",
                                    "SL",
                                    "SM",
                                    "SN",
                                    "SO",
                                    "SR",
                                    "SS",
                                    "ST",
                                    "SV",
                                    "SX",
                                    "SZ",
                                    "TC",
                                    "TD",
                                    "TF",
                                    "TG",
                                    "TH",
                                    "TJ",
                                    "TK",
                                    "TL",
                                    "TM",
                                    "TN",
                                    "TO",
                                    "TR",
                                    "TT",
                                    "TV",
                                    "TW",
                                    "TZ",
                                    "UA",
                                    "UG",
                                    "US",
                                    "UY",
                                    "UZ",
                                    "VA",
                                    "VC",
                                    "VE",
                                    "VG",
                                    "VN",
                                    "VU",
                                    "WF",
                                    "WS",
                                    "XK",
                                    "YE",
                                    "YT",
                                    "ZA",
                                    "ZM",
                                    "ZW",
                                ],
                                "examples": ["GB"],
                                "title": "Country Code",
                                "type": "string",
                            },
                            "created_date": {
                                "description": "The date when the user was created.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "Created Date",
                                "type": "string",
                            },
                            "id": {
                                "description": "Unique identifier of the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Id",
                                "type": "string",
                            },
                            "kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Kyc Completed On",
                            },
                            "kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "KYC status of the company.",
                            },
                            "name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Name",
                                "type": "string",
                            },
                            "updated_date": {
                                "description": "The "
                                "date "
                                "when "
                                "the "
                                "user "
                                "was "
                                "last "
                                "updated.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "Updated Date",
                                "type": "string",
                            },
                        },
                        "required": [
                            "name",
                            "country",
                            "country_code",
                            "id",
                            "kyc_status",
                            "created_date",
                            "updated_date",
                        ],
                        "title": "GetCompany",
                        "type": "object",
                    },
                    "GetUser": {
                        "description": "Represents response to user",
                        "properties": {
                            "company_id": {
                                "description": "The unique identifier for the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Company Id",
                                "type": "string",
                            },
                            "company_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Company Kyc Completed On",
                            },
                            "company_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_created_date": {
                                "description": "The date when the user was created.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "User Created Date",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_id": {
                                "description": "The unique identifier for the user.",
                                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                                "title": "User Id",
                                "type": "string",
                            },
                            "user_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "user, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "User Kyc Completed On",
                            },
                            "user_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the user.",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                            "user_updated_date": {
                                "description": "The "
                                "date "
                                "when "
                                "the "
                                "user "
                                "was "
                                "last "
                                "updated.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "User Updated Date",
                                "type": "string",
                            },
                        },
                        "required": [
                            "company_kyc_status",
                            "company_id",
                            "company_name",
                            "user_kyc_status",
                            "user_email",
                            "user_name",
                            "user_id",
                            "user_created_date",
                            "user_updated_date",
                        ],
                        "title": "GetUser",
                        "type": "object",
                    },
                    "GetUsers": {
                        "description": "Represents response to GET users request",
                        "properties": {
                            "context": {
                                "$ref": "#/definitions/ResponseContext",
                                "description": "Context about the response.",
                            },
                            "links": {
                                "description": "Links to previous and/or next page.",
                                "items": {"$ref": "#/definitions/Link"},
                                "title": "Links",
                                "type": "array",
                            },
                            "users": {
                                "description": "All "
                                "end "
                                "users "
                                "associated "
                                "with "
                                "the "
                                "reseller.",
                                "items": {"$ref": "#/definitions/GetUser"},
                                "title": "Users",
                                "type": "array",
                            },
                        },
                        "required": ["users", "links", "context"],
                        "title": "GetUsers",
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
                    "KYCStatus": {
                        "enum": ["Passed", "Not completed", "Failed"],
                        "title": "KYCStatus",
                        "type": "string",
                    },
                    "Link": {
                        "properties": {
                            "body": {
                                "anyOf": [
                                    {"additionalProperties": True, "type": "object"},
                                    {"type": "null"},
                                ],
                                "description": "A "
                                "JSON "
                                "object "
                                "containing "
                                "fields/values "
                                "that "
                                "must "
                                "be "
                                "included "
                                "in "
                                "the "
                                "body "
                                "of "
                                "the "
                                "next "
                                "request.",
                                "title": "Body",
                            },
                            "href": {
                                "description": "The link in the format of a URL.",
                                "format": "uri",
                                "minLength": 1,
                                "title": "Href",
                                "type": "string",
                            },
                            "merge": {
                                "default": False,
                                "description": "If "
                                "`true`, "
                                "the "
                                "headers/body "
                                "fields "
                                "in "
                                "the "
                                "`next` "
                                "link "
                                "must "
                                "be "
                                "merged "
                                "into "
                                "the "
                                "original "
                                "request "
                                "and "
                                "be "
                                "sent "
                                "combined "
                                "in "
                                "the "
                                "next "
                                "request.",
                                "title": "Merge",
                                "type": "boolean",
                            },
                            "method": {
                                "$ref": "#/definitions/RequestMethod",
                                "default": "GET",
                                "description": "The HTTP method of the request.",
                            },
                            "rel": {
                                "description": "The "
                                "relationship "
                                "between "
                                "the "
                                "current "
                                "document "
                                "and "
                                "the "
                                "linked "
                                "document.",
                                "title": "Rel",
                                "type": "string",
                            },
                            "title": {
                                "description": "The title of the link.",
                                "title": "Title",
                                "type": "string",
                            },
                            "type": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The "
                                "media "
                                "type "
                                "of "
                                "the "
                                "referenced "
                                "entity.",
                                "title": "Type",
                            },
                        },
                        "required": ["href", "rel", "title"],
                        "title": "Link",
                        "type": "object",
                    },
                    "MatchType": {
                        "enum": ["exact", "partial"],
                        "title": "MatchType",
                        "type": "string",
                    },
                    "RequestMethod": {
                        "enum": ["GET"],
                        "title": "RequestMethod",
                        "type": "string",
                    },
                    "ResponseContext": {
                        "description": "Contextual "
                        "information "
                        "for "
                        "pagination "
                        "responses",
                        "properties": {
                            "limit": {
                                "description": "Applied per page results limit.",
                                "examples": [25],
                                "title": "Limit",
                                "type": "integer",
                            },
                            "matched": {
                                "description": "Total number of results.",
                                "examples": [10],
                                "title": "Matched",
                                "type": "integer",
                            },
                            "returned": {
                                "description": "Number of returned users in page.",
                                "examples": [10],
                                "title": "Returned",
                                "type": "integer",
                            },
                        },
                        "required": ["limit", "matched", "returned"],
                        "title": "ResponseContext",
                        "type": "object",
                    },
                    "SearchCompanies": {
                        "additionalProperties": False,
                        "properties": {
                            "kyc_status": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/KYCStatus"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/KYCStatus"},
                                    {"type": "null"},
                                ],
                                "description": "The KYC status of the company.",
                                "title": "Kyc Status",
                            },
                            "limit": {
                                "default": 100,
                                "description": "The "
                                "number "
                                "of "
                                "results "
                                "to "
                                "return "
                                "per "
                                "page.",
                                "maximum": 1000.0,
                                "minimum": 1.0,
                                "title": "Limit",
                                "type": "integer",
                            },
                            "search": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/CompanySearch"
                                        },
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/CompanySearch"},
                                    {"type": "null"},
                                ],
                                "description": "Search criteria.",
                                "title": "Search",
                            },
                            "token": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The pagination token.",
                                "title": "Token",
                            },
                        },
                        "title": "SearchCompanies",
                        "type": "object",
                    },
                    "SearchUsers": {
                        "additionalProperties": False,
                        "properties": {
                            "kyc_status": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/KYCStatus"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/KYCStatus"},
                                    {"type": "null"},
                                ],
                                "description": "The KYC status of the user.",
                                "title": "Kyc Status",
                            },
                            "limit": {
                                "default": 100,
                                "description": "The "
                                "number "
                                "of "
                                "results "
                                "to "
                                "return "
                                "per "
                                "page.",
                                "maximum": 1000.0,
                                "minimum": 1.0,
                                "title": "Limit",
                                "type": "integer",
                            },
                            "search": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/UserSearch"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/UserSearch"},
                                    {"type": "null"},
                                ],
                                "description": "Search criteria.",
                                "title": "Search",
                            },
                            "token": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The pagination token.",
                                "title": "Token",
                            },
                        },
                        "title": "SearchUsers",
                        "type": "object",
                    },
                    "UserSearch": {
                        "properties": {
                            "fields": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/UserSearchFields"
                                        },
                                        "type": "array",
                                    },
                                    {"const": "all", "type": "string"},
                                ],
                                "default": "all",
                                "description": "Fields "
                                "to "
                                "search "
                                "against. "
                                "Either "
                                "a "
                                "list "
                                "of "
                                "fields "
                                "or "
                                "`all`. "
                                "Defaults "
                                "to "
                                "`all`.",
                                "examples": ["all"],
                                "title": "Fields",
                            },
                            "string": {
                                "description": "Search string.",
                                "title": "String",
                                "type": "string",
                            },
                            "type": {
                                "$ref": "#/definitions/MatchType",
                                "default": "partial",
                                "description": "Type of search.",
                            },
                        },
                        "required": ["string"],
                        "title": "UserSearch",
                        "type": "object",
                    },
                    "UserSearchFields": {
                        "enum": ["user_email", "user_name", "user_id", "company_name"],
                        "title": "UserSearchFields",
                        "type": "string",
                    },
                    "ValidationError": {
                        "properties": {
                            "ctx": {"title": "Context", "type": "object"},
                            "input": {"title": "Input"},
                            "loc": {
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
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
                    "kyc_status": {
                        "anyOf": [
                            {
                                "items": {"$ref": "#/definitions/KYCStatus"},
                                "type": "array",
                            },
                            {"$ref": "#/definitions/KYCStatus"},
                            {"type": "null"},
                        ],
                        "description": "The KYC status of the user.",
                        "title": "Kyc Status",
                    },
                    "limit": {
                        "default": 100,
                        "description": "The number of results to return per page.",
                        "maximum": 1000.0,
                        "minimum": 1.0,
                        "title": "Limit",
                        "type": "integer",
                    },
                    "search": {
                        "anyOf": [
                            {
                                "items": {"$ref": "#/definitions/UserSearch"},
                                "type": "array",
                            },
                            {"$ref": "#/definitions/UserSearch"},
                            {"type": "null"},
                        ],
                        "description": "Search criteria.",
                        "title": "Search",
                    },
                    "token": {
                        "anyOf": [{"type": "string"}, {"type": "null"}],
                        "description": "The pagination token.",
                        "title": "Token",
                    },
                },
                "title": "SearchUsers",
                "type": "object",
            }
        },
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
                    "description": "Represents response to GET users request",
                    "properties": {
                        "context": {
                            "$ref": "#/definitions/ResponseContext",
                            "description": "Context about the response.",
                        },
                        "links": {
                            "description": "Links to previous and/or next page.",
                            "items": {"$ref": "#/definitions/Link"},
                            "title": "Links",
                            "type": "array",
                        },
                        "users": {
                            "description": "All "
                            "end "
                            "users "
                            "associated "
                            "with "
                            "the "
                            "reseller.",
                            "items": {"$ref": "#/definitions/GetUser"},
                            "title": "Users",
                            "type": "array",
                        },
                    },
                    "required": ["users", "links", "context"],
                    "title": "GetUsers",
                    "type": "object",
                },
            },
            "422": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
    ("/user", "post"): {
        "parameters": {},
        "requestBody": {
            "schema": {
                "definitions": {
                    "CompanyAddress": {
                        "properties": {
                            "country_code": {
                                "description": "2-digit country code of company.",
                                "enum": [
                                    "AD",
                                    "AE",
                                    "AF",
                                    "AG",
                                    "AI",
                                    "AL",
                                    "AM",
                                    "AO",
                                    "AQ",
                                    "AR",
                                    "AT",
                                    "AU",
                                    "AW",
                                    "AX",
                                    "AZ",
                                    "BA",
                                    "BB",
                                    "BD",
                                    "BE",
                                    "BF",
                                    "BG",
                                    "BH",
                                    "BI",
                                    "BJ",
                                    "BL",
                                    "BM",
                                    "BN",
                                    "BO",
                                    "BQ",
                                    "BR",
                                    "BS",
                                    "BT",
                                    "BV",
                                    "BW",
                                    "BY",
                                    "BZ",
                                    "CA",
                                    "CC",
                                    "CD",
                                    "CF",
                                    "CG",
                                    "CH",
                                    "CI",
                                    "CK",
                                    "CL",
                                    "CM",
                                    "CN",
                                    "CO",
                                    "CR",
                                    "CV",
                                    "CW",
                                    "CX",
                                    "CY",
                                    "CZ",
                                    "DE",
                                    "DJ",
                                    "DK",
                                    "DM",
                                    "DO",
                                    "DZ",
                                    "EC",
                                    "EE",
                                    "EG",
                                    "EH",
                                    "ER",
                                    "ES",
                                    "ET",
                                    "FI",
                                    "FJ",
                                    "FK",
                                    "FO",
                                    "FR",
                                    "GA",
                                    "GB",
                                    "GD",
                                    "GE",
                                    "GF",
                                    "GG",
                                    "GH",
                                    "GI",
                                    "GL",
                                    "GM",
                                    "GN",
                                    "GP",
                                    "GQ",
                                    "GR",
                                    "GS",
                                    "GT",
                                    "GW",
                                    "GY",
                                    "HM",
                                    "HN",
                                    "HR",
                                    "HT",
                                    "HU",
                                    "ID",
                                    "IE",
                                    "IL",
                                    "IM",
                                    "IN",
                                    "IO",
                                    "IQ",
                                    "IS",
                                    "IT",
                                    "JE",
                                    "JM",
                                    "JO",
                                    "JP",
                                    "KE",
                                    "KG",
                                    "KH",
                                    "KI",
                                    "KM",
                                    "KN",
                                    "KR",
                                    "KW",
                                    "KY",
                                    "KZ",
                                    "LA",
                                    "LB",
                                    "LC",
                                    "LI",
                                    "LK",
                                    "LR",
                                    "LS",
                                    "LT",
                                    "LU",
                                    "LV",
                                    "LY",
                                    "MA",
                                    "MC",
                                    "MD",
                                    "ME",
                                    "MF",
                                    "MG",
                                    "MK",
                                    "ML",
                                    "MM",
                                    "MN",
                                    "MO",
                                    "MQ",
                                    "MR",
                                    "MS",
                                    "MT",
                                    "MU",
                                    "MV",
                                    "MW",
                                    "MX",
                                    "MY",
                                    "MZ",
                                    "NA",
                                    "NC",
                                    "NE",
                                    "NF",
                                    "NG",
                                    "NI",
                                    "NL",
                                    "NO",
                                    "NP",
                                    "NR",
                                    "NU",
                                    "NZ",
                                    "OM",
                                    "PA",
                                    "PE",
                                    "PF",
                                    "PG",
                                    "PH",
                                    "PK",
                                    "PL",
                                    "PM",
                                    "PN",
                                    "PS",
                                    "PT",
                                    "PY",
                                    "QA",
                                    "RE",
                                    "RO",
                                    "RS",
                                    "RU",
                                    "RW",
                                    "SA",
                                    "SB",
                                    "SC",
                                    "SE",
                                    "SG",
                                    "SH",
                                    "SI",
                                    "SJ",
                                    "SK",
                                    "SL",
                                    "SM",
                                    "SN",
                                    "SO",
                                    "SR",
                                    "SS",
                                    "ST",
                                    "SV",
                                    "SX",
                                    "SZ",
                                    "TC",
                                    "TD",
                                    "TF",
                                    "TG",
                                    "TH",
                                    "TJ",
                                    "TK",
                                    "TL",
                                    "TM",
                                    "TN",
                                    "TO",
                                    "TR",
                                    "TT",
                                    "TV",
                                    "TW",
                                    "TZ",
                                    "UA",
                                    "UG",
                                    "US",
                                    "UY",
                                    "UZ",
                                    "VA",
                                    "VC",
                                    "VE",
                                    "VG",
                                    "VN",
                                    "VU",
                                    "WF",
                                    "WS",
                                    "XK",
                                    "YE",
                                    "YT",
                                    "ZA",
                                    "ZM",
                                    "ZW",
                                ],
                                "examples": ["GB"],
                                "title": "Country Code",
                                "type": "string",
                            },
                            "postcode": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The postcode/zip code of the company.",
                                "examples": ["J1 ABC"],
                                "title": "Postcode",
                            },
                            "street": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The street of the company.",
                                "examples": ["1 John Lane"],
                                "title": "Street",
                            },
                        },
                        "required": ["country_code"],
                        "title": "CompanyAddress",
                        "type": "object",
                    },
                    "CompanySearch": {
                        "properties": {
                            "fields": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/CompanySearchFields"
                                        },
                                        "type": "array",
                                    },
                                    {"const": "all", "type": "string"},
                                ],
                                "default": "all",
                                "description": "Fields "
                                "to "
                                "search "
                                "against. "
                                "Either "
                                "a "
                                "list "
                                "of "
                                "fields "
                                "or "
                                "`all`. "
                                "Defaults "
                                "to "
                                "`all`.",
                                "examples": ["all"],
                                "title": "Fields",
                            },
                            "string": {
                                "description": "Search string.",
                                "title": "String",
                                "type": "string",
                            },
                            "type": {
                                "$ref": "#/definitions/MatchType",
                                "default": "partial",
                                "description": "Type of search.",
                            },
                        },
                        "required": ["string"],
                        "title": "CompanySearch",
                        "type": "object",
                    },
                    "CompanySearchFields": {
                        "enum": ["name", "id"],
                        "title": "CompanySearchFields",
                        "type": "string",
                    },
                    "CreateUser": {
                        "description": "Represents payload to create a user",
                        "properties": {
                            "company_address": {
                                "$ref": "#/definitions/CompanyAddress",
                                "description": "The address of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                        },
                        "required": [
                            "user_email",
                            "user_name",
                            "company_name",
                            "company_address",
                        ],
                        "title": "CreateUser",
                        "type": "object",
                    },
                    "CreateUserResponse": {
                        "description": "Represents response when creating user",
                        "properties": {
                            "company_address": {
                                "$ref": "#/definitions/CompanyAddress",
                                "description": "The address of the company.",
                            },
                            "company_id": {
                                "description": "The unique identifier for the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Company Id",
                                "type": "string",
                            },
                            "company_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Company Kyc Completed On",
                            },
                            "company_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_id": {
                                "description": "The unique identifier for the user.",
                                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                                "title": "User Id",
                                "type": "string",
                            },
                            "user_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "user, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "User Kyc Completed On",
                            },
                            "user_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the user.",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                        },
                        "required": [
                            "company_kyc_status",
                            "company_id",
                            "company_name",
                            "company_address",
                            "user_kyc_status",
                            "user_email",
                            "user_name",
                            "user_id",
                        ],
                        "title": "CreateUserResponse",
                        "type": "object",
                    },
                    "GetCompanies": {
                        "description": "Represents response to GET companies request",
                        "properties": {
                            "companies": {
                                "description": "All "
                                "end "
                                "user "
                                "companies "
                                "associated "
                                "with "
                                "the "
                                "reseller.",
                                "items": {"$ref": "#/definitions/GetCompany"},
                                "title": "Companies",
                                "type": "array",
                            },
                            "context": {
                                "$ref": "#/definitions/ResponseContext",
                                "description": "Context about the response.",
                            },
                            "links": {
                                "description": "Links to previous and/or next page.",
                                "items": {"$ref": "#/definitions/Link"},
                                "title": "Links",
                                "type": "array",
                            },
                        },
                        "required": ["companies", "links", "context"],
                        "title": "GetCompanies",
                        "type": "object",
                    },
                    "GetCompany": {
                        "properties": {
                            "country": {
                                "description": "Country of the company.",
                                "examples": ["United Kingdom"],
                                "title": "Country",
                                "type": "string",
                            },
                            "country_code": {
                                "description": "2-digit "
                                "ISO "
                                "country "
                                "code "
                                "of "
                                "the "
                                "company.",
                                "enum": [
                                    "AD",
                                    "AE",
                                    "AF",
                                    "AG",
                                    "AI",
                                    "AL",
                                    "AM",
                                    "AO",
                                    "AQ",
                                    "AR",
                                    "AT",
                                    "AU",
                                    "AW",
                                    "AX",
                                    "AZ",
                                    "BA",
                                    "BB",
                                    "BD",
                                    "BE",
                                    "BF",
                                    "BG",
                                    "BH",
                                    "BI",
                                    "BJ",
                                    "BL",
                                    "BM",
                                    "BN",
                                    "BO",
                                    "BQ",
                                    "BR",
                                    "BS",
                                    "BT",
                                    "BV",
                                    "BW",
                                    "BY",
                                    "BZ",
                                    "CA",
                                    "CC",
                                    "CD",
                                    "CF",
                                    "CG",
                                    "CH",
                                    "CI",
                                    "CK",
                                    "CL",
                                    "CM",
                                    "CN",
                                    "CO",
                                    "CR",
                                    "CV",
                                    "CW",
                                    "CX",
                                    "CY",
                                    "CZ",
                                    "DE",
                                    "DJ",
                                    "DK",
                                    "DM",
                                    "DO",
                                    "DZ",
                                    "EC",
                                    "EE",
                                    "EG",
                                    "EH",
                                    "ER",
                                    "ES",
                                    "ET",
                                    "FI",
                                    "FJ",
                                    "FK",
                                    "FO",
                                    "FR",
                                    "GA",
                                    "GB",
                                    "GD",
                                    "GE",
                                    "GF",
                                    "GG",
                                    "GH",
                                    "GI",
                                    "GL",
                                    "GM",
                                    "GN",
                                    "GP",
                                    "GQ",
                                    "GR",
                                    "GS",
                                    "GT",
                                    "GW",
                                    "GY",
                                    "HM",
                                    "HN",
                                    "HR",
                                    "HT",
                                    "HU",
                                    "ID",
                                    "IE",
                                    "IL",
                                    "IM",
                                    "IN",
                                    "IO",
                                    "IQ",
                                    "IS",
                                    "IT",
                                    "JE",
                                    "JM",
                                    "JO",
                                    "JP",
                                    "KE",
                                    "KG",
                                    "KH",
                                    "KI",
                                    "KM",
                                    "KN",
                                    "KR",
                                    "KW",
                                    "KY",
                                    "KZ",
                                    "LA",
                                    "LB",
                                    "LC",
                                    "LI",
                                    "LK",
                                    "LR",
                                    "LS",
                                    "LT",
                                    "LU",
                                    "LV",
                                    "LY",
                                    "MA",
                                    "MC",
                                    "MD",
                                    "ME",
                                    "MF",
                                    "MG",
                                    "MK",
                                    "ML",
                                    "MM",
                                    "MN",
                                    "MO",
                                    "MQ",
                                    "MR",
                                    "MS",
                                    "MT",
                                    "MU",
                                    "MV",
                                    "MW",
                                    "MX",
                                    "MY",
                                    "MZ",
                                    "NA",
                                    "NC",
                                    "NE",
                                    "NF",
                                    "NG",
                                    "NI",
                                    "NL",
                                    "NO",
                                    "NP",
                                    "NR",
                                    "NU",
                                    "NZ",
                                    "OM",
                                    "PA",
                                    "PE",
                                    "PF",
                                    "PG",
                                    "PH",
                                    "PK",
                                    "PL",
                                    "PM",
                                    "PN",
                                    "PS",
                                    "PT",
                                    "PY",
                                    "QA",
                                    "RE",
                                    "RO",
                                    "RS",
                                    "RU",
                                    "RW",
                                    "SA",
                                    "SB",
                                    "SC",
                                    "SE",
                                    "SG",
                                    "SH",
                                    "SI",
                                    "SJ",
                                    "SK",
                                    "SL",
                                    "SM",
                                    "SN",
                                    "SO",
                                    "SR",
                                    "SS",
                                    "ST",
                                    "SV",
                                    "SX",
                                    "SZ",
                                    "TC",
                                    "TD",
                                    "TF",
                                    "TG",
                                    "TH",
                                    "TJ",
                                    "TK",
                                    "TL",
                                    "TM",
                                    "TN",
                                    "TO",
                                    "TR",
                                    "TT",
                                    "TV",
                                    "TW",
                                    "TZ",
                                    "UA",
                                    "UG",
                                    "US",
                                    "UY",
                                    "UZ",
                                    "VA",
                                    "VC",
                                    "VE",
                                    "VG",
                                    "VN",
                                    "VU",
                                    "WF",
                                    "WS",
                                    "XK",
                                    "YE",
                                    "YT",
                                    "ZA",
                                    "ZM",
                                    "ZW",
                                ],
                                "examples": ["GB"],
                                "title": "Country Code",
                                "type": "string",
                            },
                            "created_date": {
                                "description": "The date when the user was created.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "Created Date",
                                "type": "string",
                            },
                            "id": {
                                "description": "Unique identifier of the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Id",
                                "type": "string",
                            },
                            "kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Kyc Completed On",
                            },
                            "kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "KYC status of the company.",
                            },
                            "name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Name",
                                "type": "string",
                            },
                            "updated_date": {
                                "description": "The "
                                "date "
                                "when "
                                "the "
                                "user "
                                "was "
                                "last "
                                "updated.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "Updated Date",
                                "type": "string",
                            },
                        },
                        "required": [
                            "name",
                            "country",
                            "country_code",
                            "id",
                            "kyc_status",
                            "created_date",
                            "updated_date",
                        ],
                        "title": "GetCompany",
                        "type": "object",
                    },
                    "GetUser": {
                        "description": "Represents response to user",
                        "properties": {
                            "company_id": {
                                "description": "The unique identifier for the company.",
                                "examples": ["666607ef-5c29-42fc-ba1b-90bb451c86c7"],
                                "format": "uuid",
                                "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                "title": "Company Id",
                                "type": "string",
                            },
                            "company_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "company, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "Company Kyc Completed On",
                            },
                            "company_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the company.",
                            },
                            "company_name": {
                                "description": "The name of the company.",
                                "examples": ["John Smith's Company"],
                                "title": "Company Name",
                                "type": "string",
                            },
                            "user_created_date": {
                                "description": "The date when the user was created.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "User Created Date",
                                "type": "string",
                            },
                            "user_email": {
                                "description": "The email address of the user.",
                                "examples": ["john@smith.com"],
                                "title": "User Email",
                                "type": "string",
                            },
                            "user_id": {
                                "description": "The unique identifier for the user.",
                                "examples": ["9814613e-3b32-4cc4-a60b-86c16eac1cd4"],
                                "title": "User Id",
                                "type": "string",
                            },
                            "user_kyc_completed_on": {
                                "anyOf": [
                                    {
                                        "format": "date",
                                        "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                        "type": "string",
                                    },
                                    {"type": "null"},
                                ],
                                "description": "The "
                                "date "
                                "when "
                                "KYC "
                                "was "
                                "completed "
                                "for "
                                "the "
                                "user, "
                                "if "
                                "applicable. "
                                "In "
                                "YYYY-MM-DD "
                                "format.",
                                "title": "User Kyc Completed On",
                            },
                            "user_kyc_status": {
                                "$ref": "#/definitions/KYCStatus",
                                "description": "The KYC status of the user.",
                            },
                            "user_name": {
                                "description": "The full name of the user.",
                                "examples": ["John Smith"],
                                "title": "User Name",
                                "type": "string",
                            },
                            "user_updated_date": {
                                "description": "The "
                                "date "
                                "when "
                                "the "
                                "user "
                                "was "
                                "last "
                                "updated.",
                                "format": "date",
                                "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                "title": "User Updated Date",
                                "type": "string",
                            },
                        },
                        "required": [
                            "company_kyc_status",
                            "company_id",
                            "company_name",
                            "user_kyc_status",
                            "user_email",
                            "user_name",
                            "user_id",
                            "user_created_date",
                            "user_updated_date",
                        ],
                        "title": "GetUser",
                        "type": "object",
                    },
                    "GetUsers": {
                        "description": "Represents response to GET users request",
                        "properties": {
                            "context": {
                                "$ref": "#/definitions/ResponseContext",
                                "description": "Context about the response.",
                            },
                            "links": {
                                "description": "Links to previous and/or next page.",
                                "items": {"$ref": "#/definitions/Link"},
                                "title": "Links",
                                "type": "array",
                            },
                            "users": {
                                "description": "All "
                                "end "
                                "users "
                                "associated "
                                "with "
                                "the "
                                "reseller.",
                                "items": {"$ref": "#/definitions/GetUser"},
                                "title": "Users",
                                "type": "array",
                            },
                        },
                        "required": ["users", "links", "context"],
                        "title": "GetUsers",
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
                    "KYCStatus": {
                        "enum": ["Passed", "Not completed", "Failed"],
                        "title": "KYCStatus",
                        "type": "string",
                    },
                    "Link": {
                        "properties": {
                            "body": {
                                "anyOf": [
                                    {"additionalProperties": True, "type": "object"},
                                    {"type": "null"},
                                ],
                                "description": "A "
                                "JSON "
                                "object "
                                "containing "
                                "fields/values "
                                "that "
                                "must "
                                "be "
                                "included "
                                "in "
                                "the "
                                "body "
                                "of "
                                "the "
                                "next "
                                "request.",
                                "title": "Body",
                            },
                            "href": {
                                "description": "The link in the format of a URL.",
                                "format": "uri",
                                "minLength": 1,
                                "title": "Href",
                                "type": "string",
                            },
                            "merge": {
                                "default": False,
                                "description": "If "
                                "`true`, "
                                "the "
                                "headers/body "
                                "fields "
                                "in "
                                "the "
                                "`next` "
                                "link "
                                "must "
                                "be "
                                "merged "
                                "into "
                                "the "
                                "original "
                                "request "
                                "and "
                                "be "
                                "sent "
                                "combined "
                                "in "
                                "the "
                                "next "
                                "request.",
                                "title": "Merge",
                                "type": "boolean",
                            },
                            "method": {
                                "$ref": "#/definitions/RequestMethod",
                                "default": "GET",
                                "description": "The HTTP method of the request.",
                            },
                            "rel": {
                                "description": "The "
                                "relationship "
                                "between "
                                "the "
                                "current "
                                "document "
                                "and "
                                "the "
                                "linked "
                                "document.",
                                "title": "Rel",
                                "type": "string",
                            },
                            "title": {
                                "description": "The title of the link.",
                                "title": "Title",
                                "type": "string",
                            },
                            "type": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The "
                                "media "
                                "type "
                                "of "
                                "the "
                                "referenced "
                                "entity.",
                                "title": "Type",
                            },
                        },
                        "required": ["href", "rel", "title"],
                        "title": "Link",
                        "type": "object",
                    },
                    "MatchType": {
                        "enum": ["exact", "partial"],
                        "title": "MatchType",
                        "type": "string",
                    },
                    "RequestMethod": {
                        "enum": ["GET"],
                        "title": "RequestMethod",
                        "type": "string",
                    },
                    "ResponseContext": {
                        "description": "Contextual "
                        "information "
                        "for "
                        "pagination "
                        "responses",
                        "properties": {
                            "limit": {
                                "description": "Applied per page results limit.",
                                "examples": [25],
                                "title": "Limit",
                                "type": "integer",
                            },
                            "matched": {
                                "description": "Total number of results.",
                                "examples": [10],
                                "title": "Matched",
                                "type": "integer",
                            },
                            "returned": {
                                "description": "Number of returned users in page.",
                                "examples": [10],
                                "title": "Returned",
                                "type": "integer",
                            },
                        },
                        "required": ["limit", "matched", "returned"],
                        "title": "ResponseContext",
                        "type": "object",
                    },
                    "SearchCompanies": {
                        "additionalProperties": False,
                        "properties": {
                            "kyc_status": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/KYCStatus"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/KYCStatus"},
                                    {"type": "null"},
                                ],
                                "description": "The KYC status of the company.",
                                "title": "Kyc Status",
                            },
                            "limit": {
                                "default": 100,
                                "description": "The "
                                "number "
                                "of "
                                "results "
                                "to "
                                "return "
                                "per "
                                "page.",
                                "maximum": 1000.0,
                                "minimum": 1.0,
                                "title": "Limit",
                                "type": "integer",
                            },
                            "search": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/CompanySearch"
                                        },
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/CompanySearch"},
                                    {"type": "null"},
                                ],
                                "description": "Search criteria.",
                                "title": "Search",
                            },
                            "token": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The pagination token.",
                                "title": "Token",
                            },
                        },
                        "title": "SearchCompanies",
                        "type": "object",
                    },
                    "SearchUsers": {
                        "additionalProperties": False,
                        "properties": {
                            "kyc_status": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/KYCStatus"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/KYCStatus"},
                                    {"type": "null"},
                                ],
                                "description": "The KYC status of the user.",
                                "title": "Kyc Status",
                            },
                            "limit": {
                                "default": 100,
                                "description": "The "
                                "number "
                                "of "
                                "results "
                                "to "
                                "return "
                                "per "
                                "page.",
                                "maximum": 1000.0,
                                "minimum": 1.0,
                                "title": "Limit",
                                "type": "integer",
                            },
                            "search": {
                                "anyOf": [
                                    {
                                        "items": {"$ref": "#/definitions/UserSearch"},
                                        "type": "array",
                                    },
                                    {"$ref": "#/definitions/UserSearch"},
                                    {"type": "null"},
                                ],
                                "description": "Search criteria.",
                                "title": "Search",
                            },
                            "token": {
                                "anyOf": [{"type": "string"}, {"type": "null"}],
                                "description": "The pagination token.",
                                "title": "Token",
                            },
                        },
                        "title": "SearchUsers",
                        "type": "object",
                    },
                    "UserSearch": {
                        "properties": {
                            "fields": {
                                "anyOf": [
                                    {
                                        "items": {
                                            "$ref": "#/definitions/UserSearchFields"
                                        },
                                        "type": "array",
                                    },
                                    {"const": "all", "type": "string"},
                                ],
                                "default": "all",
                                "description": "Fields "
                                "to "
                                "search "
                                "against. "
                                "Either "
                                "a "
                                "list "
                                "of "
                                "fields "
                                "or "
                                "`all`. "
                                "Defaults "
                                "to "
                                "`all`.",
                                "examples": ["all"],
                                "title": "Fields",
                            },
                            "string": {
                                "description": "Search string.",
                                "title": "String",
                                "type": "string",
                            },
                            "type": {
                                "$ref": "#/definitions/MatchType",
                                "default": "partial",
                                "description": "Type of search.",
                            },
                        },
                        "required": ["string"],
                        "title": "UserSearch",
                        "type": "object",
                    },
                    "UserSearchFields": {
                        "enum": ["user_email", "user_name", "user_id", "company_name"],
                        "title": "UserSearchFields",
                        "type": "string",
                    },
                    "ValidationError": {
                        "properties": {
                            "ctx": {"title": "Context", "type": "object"},
                            "input": {"title": "Input"},
                            "loc": {
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
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
                "items": {
                    "description": "Represents payload to create a user",
                    "properties": {
                        "company_address": {
                            "$ref": "#/definitions/CompanyAddress",
                            "description": "The address of the company.",
                        },
                        "company_name": {
                            "description": "The name of the company.",
                            "examples": ["John Smith's Company"],
                            "title": "Company Name",
                            "type": "string",
                        },
                        "user_email": {
                            "description": "The email address of the user.",
                            "examples": ["john@smith.com"],
                            "title": "User Email",
                            "type": "string",
                        },
                        "user_name": {
                            "description": "The full name of the user.",
                            "examples": ["John Smith"],
                            "title": "User Name",
                            "type": "string",
                        },
                    },
                    "required": [
                        "user_email",
                        "user_name",
                        "company_name",
                        "company_address",
                    ],
                    "title": "CreateUser",
                    "type": "object",
                },
                "type": "array",
            }
        },
        "responses": {
            "201": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
                    "items": {"$ref": "#/definitions/CreateUserResponse"},
                    "title": "Response Create-Users",
                    "type": "array",
                },
            },
            "422": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
    ("/users", "get"): {
        "parameters": {},
        "responses": {
            "200": {
                "is_error": False,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
                    "description": "Represents response to GET users request",
                    "properties": {
                        "context": {
                            "$ref": "#/definitions/ResponseContext",
                            "description": "Context about the response.",
                        },
                        "links": {
                            "description": "Links to previous and/or next page.",
                            "items": {"$ref": "#/definitions/Link"},
                            "title": "Links",
                            "type": "array",
                        },
                        "users": {
                            "description": "All "
                            "end "
                            "users "
                            "associated "
                            "with "
                            "the "
                            "reseller.",
                            "items": {"$ref": "#/definitions/GetUser"},
                            "title": "Users",
                            "type": "array",
                        },
                    },
                    "required": ["users", "links", "context"],
                    "title": "GetUsers",
                    "type": "object",
                },
            },
            "422": {
                "is_error": True,
                "schema": {
                    "definitions": {
                        "CompanyAddress": {
                            "properties": {
                                "country_code": {
                                    "description": "2-digit country code of company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "postcode": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "postcode/zip "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "examples": ["J1 ABC"],
                                    "title": "Postcode",
                                },
                                "street": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The street of the company.",
                                    "examples": ["1 John Lane"],
                                    "title": "Street",
                                },
                            },
                            "required": ["country_code"],
                            "title": "CompanyAddress",
                            "type": "object",
                        },
                        "CompanySearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "CompanySearch",
                            "type": "object",
                        },
                        "CompanySearchFields": {
                            "enum": ["name", "id"],
                            "title": "CompanySearchFields",
                            "type": "string",
                        },
                        "CreateUser": {
                            "description": "Represents payload to create a user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "user_email",
                                "user_name",
                                "company_name",
                                "company_address",
                            ],
                            "title": "CreateUser",
                            "type": "object",
                        },
                        "CreateUserResponse": {
                            "description": "Represents response when creating user",
                            "properties": {
                                "company_address": {
                                    "$ref": "#/definitions/CompanyAddress",
                                    "description": "The address of the company.",
                                },
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "company_address",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                            ],
                            "title": "CreateUserResponse",
                            "type": "object",
                        },
                        "GetCompanies": {
                            "description": "Represents "
                            "response "
                            "to "
                            "GET "
                            "companies "
                            "request",
                            "properties": {
                                "companies": {
                                    "description": "All "
                                    "end "
                                    "user "
                                    "companies "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetCompany"},
                                    "title": "Companies",
                                    "type": "array",
                                },
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                            },
                            "required": ["companies", "links", "context"],
                            "title": "GetCompanies",
                            "type": "object",
                        },
                        "GetCompany": {
                            "properties": {
                                "country": {
                                    "description": "Country of the company.",
                                    "examples": ["United Kingdom"],
                                    "title": "Country",
                                    "type": "string",
                                },
                                "country_code": {
                                    "description": "2-digit "
                                    "ISO "
                                    "country "
                                    "code "
                                    "of "
                                    "the "
                                    "company.",
                                    "enum": [
                                        "AD",
                                        "AE",
                                        "AF",
                                        "AG",
                                        "AI",
                                        "AL",
                                        "AM",
                                        "AO",
                                        "AQ",
                                        "AR",
                                        "AT",
                                        "AU",
                                        "AW",
                                        "AX",
                                        "AZ",
                                        "BA",
                                        "BB",
                                        "BD",
                                        "BE",
                                        "BF",
                                        "BG",
                                        "BH",
                                        "BI",
                                        "BJ",
                                        "BL",
                                        "BM",
                                        "BN",
                                        "BO",
                                        "BQ",
                                        "BR",
                                        "BS",
                                        "BT",
                                        "BV",
                                        "BW",
                                        "BY",
                                        "BZ",
                                        "CA",
                                        "CC",
                                        "CD",
                                        "CF",
                                        "CG",
                                        "CH",
                                        "CI",
                                        "CK",
                                        "CL",
                                        "CM",
                                        "CN",
                                        "CO",
                                        "CR",
                                        "CV",
                                        "CW",
                                        "CX",
                                        "CY",
                                        "CZ",
                                        "DE",
                                        "DJ",
                                        "DK",
                                        "DM",
                                        "DO",
                                        "DZ",
                                        "EC",
                                        "EE",
                                        "EG",
                                        "EH",
                                        "ER",
                                        "ES",
                                        "ET",
                                        "FI",
                                        "FJ",
                                        "FK",
                                        "FO",
                                        "FR",
                                        "GA",
                                        "GB",
                                        "GD",
                                        "GE",
                                        "GF",
                                        "GG",
                                        "GH",
                                        "GI",
                                        "GL",
                                        "GM",
                                        "GN",
                                        "GP",
                                        "GQ",
                                        "GR",
                                        "GS",
                                        "GT",
                                        "GW",
                                        "GY",
                                        "HM",
                                        "HN",
                                        "HR",
                                        "HT",
                                        "HU",
                                        "ID",
                                        "IE",
                                        "IL",
                                        "IM",
                                        "IN",
                                        "IO",
                                        "IQ",
                                        "IS",
                                        "IT",
                                        "JE",
                                        "JM",
                                        "JO",
                                        "JP",
                                        "KE",
                                        "KG",
                                        "KH",
                                        "KI",
                                        "KM",
                                        "KN",
                                        "KR",
                                        "KW",
                                        "KY",
                                        "KZ",
                                        "LA",
                                        "LB",
                                        "LC",
                                        "LI",
                                        "LK",
                                        "LR",
                                        "LS",
                                        "LT",
                                        "LU",
                                        "LV",
                                        "LY",
                                        "MA",
                                        "MC",
                                        "MD",
                                        "ME",
                                        "MF",
                                        "MG",
                                        "MK",
                                        "ML",
                                        "MM",
                                        "MN",
                                        "MO",
                                        "MQ",
                                        "MR",
                                        "MS",
                                        "MT",
                                        "MU",
                                        "MV",
                                        "MW",
                                        "MX",
                                        "MY",
                                        "MZ",
                                        "NA",
                                        "NC",
                                        "NE",
                                        "NF",
                                        "NG",
                                        "NI",
                                        "NL",
                                        "NO",
                                        "NP",
                                        "NR",
                                        "NU",
                                        "NZ",
                                        "OM",
                                        "PA",
                                        "PE",
                                        "PF",
                                        "PG",
                                        "PH",
                                        "PK",
                                        "PL",
                                        "PM",
                                        "PN",
                                        "PS",
                                        "PT",
                                        "PY",
                                        "QA",
                                        "RE",
                                        "RO",
                                        "RS",
                                        "RU",
                                        "RW",
                                        "SA",
                                        "SB",
                                        "SC",
                                        "SE",
                                        "SG",
                                        "SH",
                                        "SI",
                                        "SJ",
                                        "SK",
                                        "SL",
                                        "SM",
                                        "SN",
                                        "SO",
                                        "SR",
                                        "SS",
                                        "ST",
                                        "SV",
                                        "SX",
                                        "SZ",
                                        "TC",
                                        "TD",
                                        "TF",
                                        "TG",
                                        "TH",
                                        "TJ",
                                        "TK",
                                        "TL",
                                        "TM",
                                        "TN",
                                        "TO",
                                        "TR",
                                        "TT",
                                        "TV",
                                        "TW",
                                        "TZ",
                                        "UA",
                                        "UG",
                                        "US",
                                        "UY",
                                        "UZ",
                                        "VA",
                                        "VC",
                                        "VE",
                                        "VG",
                                        "VN",
                                        "VU",
                                        "WF",
                                        "WS",
                                        "XK",
                                        "YE",
                                        "YT",
                                        "ZA",
                                        "ZM",
                                        "ZW",
                                    ],
                                    "examples": ["GB"],
                                    "title": "Country Code",
                                    "type": "string",
                                },
                                "created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Created Date",
                                    "type": "string",
                                },
                                "id": {
                                    "description": "Unique identifier of the company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Id",
                                    "type": "string",
                                },
                                "kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Kyc Completed On",
                                },
                                "kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "KYC status of the company.",
                                },
                                "name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Name",
                                    "type": "string",
                                },
                                "updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "name",
                                "country",
                                "country_code",
                                "id",
                                "kyc_status",
                                "created_date",
                                "updated_date",
                            ],
                            "title": "GetCompany",
                            "type": "object",
                        },
                        "GetUser": {
                            "description": "Represents response to user",
                            "properties": {
                                "company_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "company.",
                                    "examples": [
                                        "666607ef-5c29-42fc-ba1b-90bb451c86c7"
                                    ],
                                    "format": "uuid",
                                    "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$",
                                    "title": "Company Id",
                                    "type": "string",
                                },
                                "company_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "company, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "Company Kyc Completed On",
                                },
                                "company_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the company.",
                                },
                                "company_name": {
                                    "description": "The name of the company.",
                                    "examples": ["John Smith's Company"],
                                    "title": "Company Name",
                                    "type": "string",
                                },
                                "user_created_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "created.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Created Date",
                                    "type": "string",
                                },
                                "user_email": {
                                    "description": "The email address of the user.",
                                    "examples": ["john@smith.com"],
                                    "title": "User Email",
                                    "type": "string",
                                },
                                "user_id": {
                                    "description": "The "
                                    "unique "
                                    "identifier "
                                    "for "
                                    "the "
                                    "user.",
                                    "examples": [
                                        "9814613e-3b32-4cc4-a60b-86c16eac1cd4"
                                    ],
                                    "title": "User Id",
                                    "type": "string",
                                },
                                "user_kyc_completed_on": {
                                    "anyOf": [
                                        {
                                            "format": "date",
                                            "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                            "type": "string",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "The "
                                    "date "
                                    "when "
                                    "KYC "
                                    "was "
                                    "completed "
                                    "for "
                                    "the "
                                    "user, "
                                    "if "
                                    "applicable. "
                                    "In "
                                    "YYYY-MM-DD "
                                    "format.",
                                    "title": "User Kyc Completed On",
                                },
                                "user_kyc_status": {
                                    "$ref": "#/definitions/KYCStatus",
                                    "description": "The KYC status of the user.",
                                },
                                "user_name": {
                                    "description": "The full name of the user.",
                                    "examples": ["John Smith"],
                                    "title": "User Name",
                                    "type": "string",
                                },
                                "user_updated_date": {
                                    "description": "The "
                                    "date "
                                    "when "
                                    "the "
                                    "user "
                                    "was "
                                    "last "
                                    "updated.",
                                    "format": "date",
                                    "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}$",
                                    "title": "User Updated Date",
                                    "type": "string",
                                },
                            },
                            "required": [
                                "company_kyc_status",
                                "company_id",
                                "company_name",
                                "user_kyc_status",
                                "user_email",
                                "user_name",
                                "user_id",
                                "user_created_date",
                                "user_updated_date",
                            ],
                            "title": "GetUser",
                            "type": "object",
                        },
                        "GetUsers": {
                            "description": "Represents response to GET users request",
                            "properties": {
                                "context": {
                                    "$ref": "#/definitions/ResponseContext",
                                    "description": "Context about the response.",
                                },
                                "links": {
                                    "description": "Links "
                                    "to "
                                    "previous "
                                    "and/or "
                                    "next "
                                    "page.",
                                    "items": {"$ref": "#/definitions/Link"},
                                    "title": "Links",
                                    "type": "array",
                                },
                                "users": {
                                    "description": "All "
                                    "end "
                                    "users "
                                    "associated "
                                    "with "
                                    "the "
                                    "reseller.",
                                    "items": {"$ref": "#/definitions/GetUser"},
                                    "title": "Users",
                                    "type": "array",
                                },
                            },
                            "required": ["users", "links", "context"],
                            "title": "GetUsers",
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
                        "KYCStatus": {
                            "enum": ["Passed", "Not completed", "Failed"],
                            "title": "KYCStatus",
                            "type": "string",
                        },
                        "Link": {
                            "properties": {
                                "body": {
                                    "anyOf": [
                                        {
                                            "additionalProperties": True,
                                            "type": "object",
                                        },
                                        {"type": "null"},
                                    ],
                                    "description": "A "
                                    "JSON "
                                    "object "
                                    "containing "
                                    "fields/values "
                                    "that "
                                    "must "
                                    "be "
                                    "included "
                                    "in "
                                    "the "
                                    "body "
                                    "of "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Body",
                                },
                                "href": {
                                    "description": "The link in the format of a URL.",
                                    "format": "uri",
                                    "minLength": 1,
                                    "title": "Href",
                                    "type": "string",
                                },
                                "merge": {
                                    "default": False,
                                    "description": "If "
                                    "`true`, "
                                    "the "
                                    "headers/body "
                                    "fields "
                                    "in "
                                    "the "
                                    "`next` "
                                    "link "
                                    "must "
                                    "be "
                                    "merged "
                                    "into "
                                    "the "
                                    "original "
                                    "request "
                                    "and "
                                    "be "
                                    "sent "
                                    "combined "
                                    "in "
                                    "the "
                                    "next "
                                    "request.",
                                    "title": "Merge",
                                    "type": "boolean",
                                },
                                "method": {
                                    "$ref": "#/definitions/RequestMethod",
                                    "default": "GET",
                                    "description": "The HTTP method of the request.",
                                },
                                "rel": {
                                    "description": "The "
                                    "relationship "
                                    "between "
                                    "the "
                                    "current "
                                    "document "
                                    "and "
                                    "the "
                                    "linked "
                                    "document.",
                                    "title": "Rel",
                                    "type": "string",
                                },
                                "title": {
                                    "description": "The title of the link.",
                                    "title": "Title",
                                    "type": "string",
                                },
                                "type": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The "
                                    "media "
                                    "type "
                                    "of "
                                    "the "
                                    "referenced "
                                    "entity.",
                                    "title": "Type",
                                },
                            },
                            "required": ["href", "rel", "title"],
                            "title": "Link",
                            "type": "object",
                        },
                        "MatchType": {
                            "enum": ["exact", "partial"],
                            "title": "MatchType",
                            "type": "string",
                        },
                        "RequestMethod": {
                            "enum": ["GET"],
                            "title": "RequestMethod",
                            "type": "string",
                        },
                        "ResponseContext": {
                            "description": "Contextual "
                            "information "
                            "for "
                            "pagination "
                            "responses",
                            "properties": {
                                "limit": {
                                    "description": "Applied per page results limit.",
                                    "examples": [25],
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "matched": {
                                    "description": "Total number of results.",
                                    "examples": [10],
                                    "title": "Matched",
                                    "type": "integer",
                                },
                                "returned": {
                                    "description": "Number of returned users in page.",
                                    "examples": [10],
                                    "title": "Returned",
                                    "type": "integer",
                                },
                            },
                            "required": ["limit", "matched", "returned"],
                            "title": "ResponseContext",
                            "type": "object",
                        },
                        "SearchCompanies": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the company.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/CompanySearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/CompanySearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchCompanies",
                            "type": "object",
                        },
                        "SearchUsers": {
                            "additionalProperties": False,
                            "properties": {
                                "kyc_status": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/KYCStatus"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/KYCStatus"},
                                        {"type": "null"},
                                    ],
                                    "description": "The KYC status of the user.",
                                    "title": "Kyc Status",
                                },
                                "limit": {
                                    "default": 100,
                                    "description": "The "
                                    "number "
                                    "of "
                                    "results "
                                    "to "
                                    "return "
                                    "per "
                                    "page.",
                                    "maximum": 1000.0,
                                    "minimum": 1.0,
                                    "title": "Limit",
                                    "type": "integer",
                                },
                                "search": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearch"
                                            },
                                            "type": "array",
                                        },
                                        {"$ref": "#/definitions/UserSearch"},
                                        {"type": "null"},
                                    ],
                                    "description": "Search criteria.",
                                    "title": "Search",
                                },
                                "token": {
                                    "anyOf": [{"type": "string"}, {"type": "null"}],
                                    "description": "The pagination token.",
                                    "title": "Token",
                                },
                            },
                            "title": "SearchUsers",
                            "type": "object",
                        },
                        "UserSearch": {
                            "properties": {
                                "fields": {
                                    "anyOf": [
                                        {
                                            "items": {
                                                "$ref": "#/definitions/UserSearchFields"
                                            },
                                            "type": "array",
                                        },
                                        {"const": "all", "type": "string"},
                                    ],
                                    "default": "all",
                                    "description": "Fields "
                                    "to "
                                    "search "
                                    "against. "
                                    "Either "
                                    "a "
                                    "list "
                                    "of "
                                    "fields "
                                    "or "
                                    "`all`. "
                                    "Defaults "
                                    "to "
                                    "`all`.",
                                    "examples": ["all"],
                                    "title": "Fields",
                                },
                                "string": {
                                    "description": "Search string.",
                                    "title": "String",
                                    "type": "string",
                                },
                                "type": {
                                    "$ref": "#/definitions/MatchType",
                                    "default": "partial",
                                    "description": "Type of search.",
                                },
                            },
                            "required": ["string"],
                            "title": "UserSearch",
                            "type": "object",
                        },
                        "UserSearchFields": {
                            "enum": [
                                "user_email",
                                "user_name",
                                "user_id",
                                "company_name",
                            ],
                            "title": "UserSearchFields",
                            "type": "string",
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
        api_name="reseller",
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
        api_name="reseller",
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
        api_name="reseller",
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
