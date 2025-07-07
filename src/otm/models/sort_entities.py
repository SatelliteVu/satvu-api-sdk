from pydantic import BaseModel

from ..models.sort_entities_direction import SortEntitiesDirection
from ..models.sortable_field import SortableField


class SortEntities(BaseModel):
    """
    Attributes:
        field (SortableField):
        direction (SortEntitiesDirection): The directionality of the sort.
    """

    field: SortableField
    direction: SortEntitiesDirection
