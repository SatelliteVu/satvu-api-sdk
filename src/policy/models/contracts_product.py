from pydantic import BaseModel, ConfigDict, Field


class ContractsProduct(BaseModel):
    """
    Attributes:
        code (str): Product code Example: PRODUCT.
        currency (str): Product currency Example: GBP.
        priority (int): Product priority Example: 40.
    """

    code: str = Field(..., description="Product code", alias="code")
    currency: str = Field(..., description="Product currency", alias="currency")
    priority: int = Field(..., description="Product priority", alias="priority")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
