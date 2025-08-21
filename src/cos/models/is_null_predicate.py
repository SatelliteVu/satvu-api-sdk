from __future__ import annotations

from typing import TYPE_CHECKING, Union

from pydantic import BaseModel, ConfigDict, Field

from ..models.is_null_predicate_op import IsNullPredicateOp

if TYPE_CHECKING:
    from ..models.and_or_expression import AndOrExpression
    from ..models.arithmetic_expression import ArithmeticExpression
    from ..models.bbox_literal import BboxLiteral
    from ..models.binary_comparison_predicate import BinaryComparisonPredicate
    from ..models.date_instant import DateInstant
    from ..models.geo_json_geometry_collection import GeoJSONGeometryCollection
    from ..models.geo_json_line_string_1 import GeoJSONLineString1
    from ..models.geo_json_multi_line_string_1 import GeoJSONMultiLineString1
    from ..models.geo_json_multi_point_1 import GeoJSONMultiPoint1
    from ..models.geo_json_multi_polygon_1 import GeoJSONMultiPolygon1
    from ..models.geo_json_point_1 import GeoJSONPoint1
    from ..models.geo_json_polygon_1 import GeoJSONPolygon1
    from ..models.is_between_predicate import IsBetweenPredicate
    from ..models.is_in_list_predicate import IsInListPredicate
    from ..models.is_like_predicate import IsLikePredicate
    from ..models.not_expression import NotExpression
    from ..models.property_ref import PropertyRef
    from ..models.timestamp_instant import TimestampInstant


class IsNullPredicate(BaseModel):
    """
    Attributes:
        op ('IsNullPredicateOp'):
        args (list[Union['AndOrExpression', 'ArithmeticExpression', 'BboxLiteral', 'BinaryComparisonPredicate',
            'DateInstant', 'GeoJSONGeometryCollection', 'GeoJSONLineString1', 'GeoJSONMultiLineString1',
            'GeoJSONMultiPoint1', 'GeoJSONMultiPolygon1', 'GeoJSONPoint1', 'GeoJSONPolygon1', 'IsBetweenPredicate',
            'IsInListPredicate', 'IsLikePredicate', 'IsNullPredicate', 'NotExpression', 'PropertyRef', 'TimestampInstant',
            bool, float, str]]):
    """

    op: "IsNullPredicateOp" = Field(..., description=None, alias="op")
    args: list[
        Union[
            "AndOrExpression",
            "ArithmeticExpression",
            "BboxLiteral",
            "BinaryComparisonPredicate",
            "DateInstant",
            "GeoJSONGeometryCollection",
            "GeoJSONLineString1",
            "GeoJSONMultiLineString1",
            "GeoJSONMultiPoint1",
            "GeoJSONMultiPolygon1",
            "GeoJSONPoint1",
            "GeoJSONPolygon1",
            "IsBetweenPredicate",
            "IsInListPredicate",
            "IsLikePredicate",
            "IsNullPredicate",
            "NotExpression",
            "PropertyRef",
            "TimestampInstant",
            bool,
            float,
            str,
        ]
    ] = Field(..., description=None, alias="args")

    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)
