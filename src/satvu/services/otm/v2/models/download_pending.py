# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

import pydantic

if TYPE_CHECKING:
    from ..models.download_progress import DownloadProgress


class DownloadPending(pydantic.BaseModel):
    """Response payload returned while a download is still being prepared.

    Attributes:
        message (str): Human-readable status message. Also see the `Retry-After` header.
        progress (DownloadProgress): Progress information for an in-flight download bundling job.
    """

    message: str = pydantic.Field(
        ...,
        description="""Human-readable status message. Also see the `Retry-After` header.""",
        alias="message",
    )
    progress: DownloadProgress = pydantic.Field(
        ...,
        description="""Progress information for an in-flight download bundling job.""",
        alias="progress",
    )

    model_config = pydantic.ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
