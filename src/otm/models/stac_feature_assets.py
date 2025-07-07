from pydantic import BaseModel


class StacFeatureAssets(BaseModel):
    """A dictionary of asset objects that can be downloaded, each with a unique key."""
