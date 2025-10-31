from enum import Enum


class AssetBandsNodataType1(str, Enum):
    INF = "inf"
    NAN = "nan"
    VALUE_2 = "-inf"

    def __str__(self) -> str:
        return str(self.value)
