from pydantic import BaseModel, Field


class ContractsProduct(BaseModel):
    """
    Attributes:
        code (str): Product code Example: PRODUCT.
        currency (str): Product currency Example: GBP.
        priority (int): Product priority Example: 40.
    """

    code: str = Field(..., description="Product code")
    currency: str = Field(..., description="Product currency")
    priority: int = Field(..., description="Product priority")
