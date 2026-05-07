from enum import Enum


class DownloadOrderItemPrimaryFormatsItem(str, Enum):
    GEOTIFF = "geotiff"
    NITF = "nitf"

    def __str__(self) -> str:
        return str(self.value)
