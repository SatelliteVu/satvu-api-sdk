from pydantic import BaseModel


class StacMetadataAssets(BaseModel):
    """A dictionary of asset objects that can be downloaded, each with a unique key."""
