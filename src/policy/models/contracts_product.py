from pydantic import BaseModel


class ContractsProduct(BaseModel):
    """
    Attributes:
        code (str): Product code Example: PRODUCT.
        currency (str): Product currency Example: GBP.
        priority (int): Product priority Example: 40.
    """

    code: str
    currency: str
    priority: int
