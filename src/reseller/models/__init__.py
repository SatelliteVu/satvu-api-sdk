"""Contains all the data models used in inputs/outputs"""

from .company_address import CompanyAddress
from .company_address_country_code import CompanyAddressCountryCode
from .company_search import CompanySearch
from .company_search_fields import CompanySearchFields
from .create_user import CreateUser
from .create_user_response import CreateUserResponse
from .get_companies import GetCompanies
from .get_company import GetCompany
from .get_user import GetUser
from .get_users import GetUsers
from .http_validation_error import HTTPValidationError
from .kyc_status import KYCStatus
from .link import Link
from .link_body_type_0 import LinkBodyType0
from .match_type import MatchType
from .request_method import RequestMethod
from .response_context import ResponseContext
from .search_companies import SearchCompanies
from .search_users import SearchUsers
from .user_search import UserSearch
from .user_search_fields import UserSearchFields
from .validation_error import ValidationError

__all__ = (
    "CompanyAddress",
    "CompanyAddressCountryCode",
    "CompanySearch",
    "CompanySearchFields",
    "CreateUser",
    "CreateUserResponse",
    "GetCompanies",
    "GetCompany",
    "GetUser",
    "GetUsers",
    "HTTPValidationError",
    "KYCStatus",
    "Link",
    "LinkBodyType0",
    "MatchType",
    "RequestMethod",
    "ResponseContext",
    "SearchCompanies",
    "SearchUsers",
    "UserSearch",
    "UserSearchFields",
    "ValidationError",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
