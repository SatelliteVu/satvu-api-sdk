# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/models_init.py.jinja
"""Contains all the data models used in inputs/outputs"""

from .contracts_addon import ContractsAddon
from .contracts_addon_option import ContractsAddonOption
from .contracts_contract_with_products import ContractsContractWithProducts
from .contracts_geometry import ContractsGeometry
from .contracts_product_summary import ContractsProductSummary
from .list_active_contracts_input import ListActiveContractsInput
from .router_active_contracts_response import RouterActiveContractsResponse
from .router_http_error import RouterHttpError
from .terms_user_terms_accepted import TermsUserTermsAccepted
from .user_acceptance_terms_input import UserAcceptanceTermsInput

__all__ = (
    "ContractsAddon",
    "ContractsAddonOption",
    "ContractsContractWithProducts",
    "ContractsGeometry",
    "ContractsProductSummary",
    "ListActiveContractsInput",
    "RouterActiveContractsResponse",
    "RouterHttpError",
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
