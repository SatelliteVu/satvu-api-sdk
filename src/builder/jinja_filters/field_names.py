from openapi_python_client.config import ConfigFile
from openapi_python_client.strings import PythonIdentifier

# build.py generates with a default ConfigFile, so this is the prefix in use
_FIELD_PREFIX = ConfigFile().field_prefix


def field_name(python_name: str) -> str:
    """Return the attribute name a property with ``python_name`` is generated under."""
    # Append underscore to field names that shadow BaseModel attributes
    # to avoid Pydantic warnings (e.g., "schema" -> "schema_")
    return "schema_" if python_name == "schema" else python_name


def field_name_for_alias(alias: str) -> str:
    """Return the attribute name generated for the wire name ``alias``."""
    return field_name(str(PythonIdentifier(value=alias, prefix=_FIELD_PREFIX)))
