from enum import StrEnum


class PrimaryFormat(StrEnum):
    GEOTIFF = "geotiff"
    NITF = "nitf"

    def __str__(self) -> str:
        return str(self.value)
