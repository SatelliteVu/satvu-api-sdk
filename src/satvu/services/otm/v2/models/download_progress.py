# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class DownloadProgress(pydantic.BaseModel):
    """The progress of a download being prepared.

    Attributes:
        total (int): The total number of files to package.
        done (int): The number of files packaged so far.
    """

    total: int = pydantic.Field(
        ..., description="""The total number of files to package.""", alias="total"
    )
    done: int = pydantic.Field(
        ..., description="""The number of files packaged so far.""", alias="done"
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
