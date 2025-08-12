from pydantic import BaseModel, ConfigDict


class LinkBodyType0(BaseModel):
    """ """

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
