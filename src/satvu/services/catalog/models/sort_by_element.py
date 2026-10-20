# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class SortByElement(pydantic.BaseModel):
    """
    Attributes:
        direction (str): The direction to sort by, either 'asc' or 'desc'. Example: desc.
        field (str): The name of the field to sort by. Example: datetime.
    """

    direction: str = pydantic.Field(
        ...,
        description="""The direction to sort by, either 'asc' or 'desc'.""",
        alias="direction",
    )
    field: str = pydantic.Field(
        ..., description="""The name of the field to sort by.""", alias="field"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
