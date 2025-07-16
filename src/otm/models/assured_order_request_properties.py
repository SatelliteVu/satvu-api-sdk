from typing import Literal, Union

from pydantic import BaseModel


class AssuredOrderRequestProperties(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        signature (str): Signature token.
        addon_withhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
    """

    product: Literal["assured"] = "assured"
    signature: str
    addon_withhold: Union[None, str] = None
