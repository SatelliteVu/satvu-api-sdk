from enum import StrEnum


class DownloadOrderItemPrimaryFormatsItem(StrEnum):
    GEOTIFF = "geotiff"
    NITF = "nitf"

    def __str__(self) -> str:
        return str(self.value)
