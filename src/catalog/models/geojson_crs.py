from typing import Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.geojson_crs_properties import GeojsonCRSProperties


class GeojsonCRS(BaseModel):
    """
    Attributes:
        properties (Union[None, GeojsonCRSProperties]):
        type_ (Union[None, str]):
    """

    properties: Union[None, "GeojsonCRSProperties"] = Field(
        None, description=None, alias="properties"
    )
    type_: Union[None, str] = Field(None, description=None, alias="type")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
