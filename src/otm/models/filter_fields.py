from typing import Union

from pydantic import BaseModel


class FilterFields(BaseModel):
    """
    Attributes:
        status (Union[None, list[str], str]):
        min_off_nadir (Union[None, int, list[int]]):
        max_off_nadir (Union[None, int, list[int]]):
    """

    status: Union[None, list[str], str] = None
    min_off_nadir: Union[None, int, list[int]] = None
    max_off_nadir: Union[None, int, list[int]] = None

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}

    @staticmethod
    def get_required_fields_and_types() -> dict:
        """
        Returns a mapping of required fields to their types or nested model classes.
        """
        return {}

    @staticmethod
    def get_optional_fields_and_types() -> dict:
        """
        Returns a mapping of optional fields to their types or nested model classes.
        """
        return {
            "status": object,
            "min_off_nadir": object,
            "max_off_nadir": object,
        }
