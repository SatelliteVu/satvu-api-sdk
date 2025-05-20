from dataclasses import dataclass


@dataclass
class StacMetadataAssets:
    """A dictionary of asset objects that can be downloaded, each with a unique key."""

    @staticmethod
    def get_required_fields() -> set[str]:
        """
        Returns the set of required fields for the model.
        """
        return {}
