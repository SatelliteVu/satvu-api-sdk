from enum import Enum


class AssetBandsDataTypeOfTheBand(str, Enum):
    CFLOAT32 = "cfloat32"
    CFLOAT64 = "cfloat64"
    CINT16 = "cint16"
    CINT32 = "cint32"
    FLOAT16 = "float16"
    FLOAT32 = "float32"
    FLOAT64 = "float64"
    INT16 = "int16"
    INT32 = "int32"
    INT64 = "int64"
    INT8 = "int8"
    OTHER = "other"
    UINT16 = "uint16"
    UINT32 = "uint32"
    UINT64 = "uint64"
    UINT8 = "uint8"

    def __str__(self) -> str:
        return str(self.value)
