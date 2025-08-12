from pydantic import BaseModel, ConfigDict, Field


class ClientID(BaseModel):
    """
    Attributes:
        client_id (str):
    """

    client_id: str = Field(..., description=None, alias="client_id")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
