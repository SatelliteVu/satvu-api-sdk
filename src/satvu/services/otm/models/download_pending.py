# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.download_progress import DownloadProgress


class DownloadPending(BaseModel):
    """Response payload returned while a download is still being prepared.

    Attributes:
        message (str): Human-readable status message. Also see the `Retry-After` header.
        progress (DownloadProgress): Progress information for an in-flight download bundling job.
    """

    message: str = Field(
        ...,
        description="""Human-readable status message. Also see the `Retry-After` header.""",
        alias="message",
    )
    progress: DownloadProgress = Field(
        ...,
        description="""Progress information for an in-flight download bundling job.""",
        alias="progress",
    )

    model_config = ConfigDict(
        validate_by_name=True, validate_by_alias=True, extra="allow"
    )
