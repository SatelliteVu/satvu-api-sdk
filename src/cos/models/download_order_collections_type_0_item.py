from enum import Enum


class DownloadOrderCollectionsType0Item(str, Enum):
    PRIMARY = "primary"
    VISUAL = "visual"

    def __str__(self) -> str:
        return str(self.value)
