from enum import StrEnum


class AssetBandsNodataType1(StrEnum):
    INF = "inf"
    NAN = "nan"
    VALUE_2 = "-inf"

    def __str__(self) -> str:
        return str(self.value)
