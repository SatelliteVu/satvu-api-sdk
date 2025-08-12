from pydantic import BaseModel, ConfigDict, Field

from ..models.company_address import CompanyAddress


class CreateUser(BaseModel):
    """Represents payload to create a user

    Attributes:
        user_email (str): The email address of the user.
        user_name (str): The full name of the user.
        company_name (str): The name of the company.
        company_address (CompanyAddress):
    """

    user_email: str = Field(
        ..., description="The email address of the user.", alias="user_email"
    )
    user_name: str = Field(
        ..., description="The full name of the user.", alias="user_name"
    )
    company_name: str = Field(
        ..., description="The name of the company.", alias="company_name"
    )
    company_address: "CompanyAddress" = Field(
        ..., description=None, alias="company_address"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
