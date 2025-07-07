from pydantic import BaseModel

from ..models.contracts_contract_with_products import ContractsContractWithProducts


class RouterActiveContractsResponse(BaseModel):
    """
    Attributes:
        result (list['ContractsContractWithProducts']): Result of the active contracts query
        terms_accepted (bool): User has accepted terms of service
    """

    result: list["ContractsContractWithProducts"]
    terms_accepted: bool

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "result",
            "terms_accepted",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "result": object,
            "terms_accepted": bool,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
