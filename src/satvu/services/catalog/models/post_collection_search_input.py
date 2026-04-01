# Auto-generated from OpenAPI spec by the SatVu SDK builder — do not edit.
# Source: src/builder/templates/model.py.jinja

from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from ..models.sort_by_element import SortByElement
    from ..models.stac_geometry import StacGeometry


class PostCollectionSearchInput(BaseModel):
    """
    Attributes:
        bbox (Union[None, list[float]]): Array of floats representing a bounding box.
        datetime_ (None | str): Single date+time, or a range with '/' separator. Example: 1985-04-12T23:20:50.52Z/...
        filter_ (Union[None, dict]): Filters using Common Query Language (CQL2).
        ids (Union[None, list[str]]): Array of Item IDs to return.
        intersects (Union[None, StacGeometry]): Searches items by performing intersection between their geometry and
            provided GeoJSON geometry.
        limit (int | None): The maximum number of results to return per page. Example: 10.
        sortby (Union[None, list[SortByElement]]): An array of objects containing a property name and sort direction.
        token (Union[None, str]): The pagination token.
    """

    bbox: Union[None, list[float]] = Field(
        default=None,
        description="""Array of floats representing a bounding box.""",
        alias="bbox",
    )
    datetime_: None | str = Field(
        default=None,
        description="""Single date+time, or a range with '/' separator.""",
        alias="datetime",
    )
    filter_: Union[None, dict] = Field(
        default=None,
        description="""Filters using Common Query Language (CQL2).""",
        alias="filter",
    )
    ids: Union[None, list[str]] = Field(
        default=None, description="""Array of Item IDs to return.""", alias="ids"
    )
    intersects: Union[None, StacGeometry] = Field(
        default=None,
        description="""Searches items by performing intersection between their geometry and provided GeoJSON geometry.""",
        alias="intersects",
    )
    limit: int | None = Field(
        default=None,
        description="""The maximum number of results to return per page.""",
        alias="limit",
    )
    sortby: Union[None, list[SortByElement]] = Field(
        default=None,
        description="""An array of objects containing a property name and sort direction.""",
        alias="sortby",
    )
    token: Union[None, str] = Field(
        default=None, description="""The pagination token.""", alias="token"
    )

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
