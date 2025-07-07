from typing import Literal, Union

from pydantic import BaseModel


class AssuredFeasibilityFieldsWithAddons(BaseModel):
    """
    Attributes:
        product (Literal['assured']): Assured Priority.
        datetime (str): The closed date-time interval of the request.
        addon_withhold (Union[None, str]): Optional ISO8601 string describing the duration that an order will be
            withheld from the public catalog. Withhold options are specific to the contract. If not specified, the option
            will be set to the default specified in the relevant contract.
    """

    product: Literal["assured"]
    datetime: str
    addon_withhold: Union[None, str] = None
