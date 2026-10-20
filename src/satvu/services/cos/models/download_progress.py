# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

import pydantic


class DownloadProgress(pydantic.BaseModel):
    """Progress information for an in-flight download bundling job.

    Attributes:
        total (int): The total number of files the bundler is packaging.
        done (int): The number of files the bundler has already packaged.
    """

    total: int = pydantic.Field(
        ...,
        description="""The total number of files the bundler is packaging.""",
        alias="total",
    )
    done: int = pydantic.Field(
        ...,
        description="""The number of files the bundler has already packaged.""",
        alias="done",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
