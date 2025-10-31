from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class Conformance(BaseModel):
    """
    Attributes:
        conforms_to (list[str]): A list of all conformance classes implemented.
    """

    conforms_to: list[str] = Field(
        ...,
        description="A list of all conformance classes implemented.",
        alias="conformsTo",
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
