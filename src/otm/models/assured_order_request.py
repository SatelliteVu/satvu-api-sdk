from pydantic import BaseModel, ConfigDict, Field

from ..models.assured_order_request_properties import AssuredOrderRequestProperties


class AssuredOrderRequest(BaseModel):
    """
    Attributes:
        properties (AssuredOrderRequestProperties):
    """

    properties: "AssuredOrderRequestProperties" = Field(
        ..., description=None, alias="properties"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
