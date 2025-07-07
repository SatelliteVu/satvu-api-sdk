from pydantic import BaseModel

from ..models.company_address import CompanyAddress


class CreateUser(BaseModel):
    """Represents payload to create a user

    Attributes:
        user_email (str): The email address of the user.
        user_name (str): The full name of the user.
        company_name (str): The name of the company.
        company_address (CompanyAddress):
    """

    user_email: str
    user_name: str
    company_name: str
    company_address: "CompanyAddress"

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "user_email",
            "user_name",
            "company_name",
            "company_address",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "user_email": str,
            "user_name": str,
            "company_name": str,
            "company_address": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
