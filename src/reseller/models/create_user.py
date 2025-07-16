from pydantic import BaseModel, Field

from ..models.company_address import CompanyAddress


class CreateUser(BaseModel):
    """Represents payload to create a user

    Attributes:
        user_email (str): The email address of the user.
        user_name (str): The full name of the user.
        company_name (str): The name of the company.
        company_address (CompanyAddress):
    """

    user_email: str = Field(..., description="The email address of the user.")
    user_name: str = Field(..., description="The full name of the user.")
    company_name: str = Field(..., description="The name of the company.")
    company_address: "CompanyAddress" = Field(..., description=None)
