from enum import Enum


class DownloadOrderPrimaryFormatsItem(str, Enum):
    GEOTIFF = "geotiff"
    NITF = "nitf"

    def __str__(self) -> str:
        return str(self.value)
