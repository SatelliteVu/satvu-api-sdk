"""Contains all the data models used in inputs/outputs"""

from .civil_date import CivilDate
from .contracts_addon import ContractsAddon
from .contracts_addon_option import ContractsAddonOption
from .contracts_contract_with_products import ContractsContractWithProducts
from .contracts_geometry import ContractsGeometry
from .contracts_product import ContractsProduct
from .post_active_contracts_input import PostActiveContractsInput
from .router_active_contracts_response import RouterActiveContractsResponse
from .router_http_error import RouterHttpError
from .router_query_result import RouterQueryResult
from .terms_user_terms_accepted import TermsUserTermsAccepted
from .user_acceptance_terms_input import UserAcceptanceTermsInput

__all__ = (
    "CivilDate",
    "ContractsAddon",
    "ContractsAddonOption",
    "ContractsContractWithProducts",
    "ContractsGeometry",
    "ContractsProduct",
    "PostActiveContractsInput",
    "RouterActiveContractsResponse",
    "RouterHttpError",
    "RouterQueryResult",
    "TermsUserTermsAccepted",
    "UserAcceptanceTermsInput",
)

# Ensure all Pydantic models have forward refs rebuilt
import inspect
import sys

from pydantic import BaseModel

_current_module = sys.modules[__name__]

for _obj in list(_current_module.__dict__.values()):
    if inspect.isclass(_obj) and issubclass(_obj, BaseModel) and _obj is not BaseModel:
        _obj.model_rebuild()
