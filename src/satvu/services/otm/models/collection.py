from enum import Enum


class Collection(str, Enum):
    PRIMARY = "primary"
    SURFACE_BRIGHTNESS_TEMPERATURE = "surface-brightness-temperature"
    VISUAL = "visual"

    def __str__(self) -> str:
        return str(self.value)
