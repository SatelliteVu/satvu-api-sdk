from enum import Enum


class DownloadOrderCollectionsItem(str, Enum):
    PRIMARY = "primary"
    SURFACE_BRIGHTNESS_TEMPERATURE = "surface-brightness-temperature"

    def __str__(self) -> str:
        return str(self.value)
