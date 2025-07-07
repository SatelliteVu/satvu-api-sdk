from dataclasses import dataclass

from ..models.sort_entities_direction import SortEntitiesDirection
from ..models.sortable_field import SortableField


@dataclass
class SortEntities:
    """
    Attributes:
        field (SortableField):
        direction (SortEntitiesDirection): The directionality of the sort.
    """

    field: SortableField
    direction: SortEntitiesDirection

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {
            "field",
            "direction",
        }

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {
            "field": object,
            "direction": object,
        }

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {}
