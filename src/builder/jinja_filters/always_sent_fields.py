from openapi_python_client.parser.properties.const import ConstProperty
from openapi_python_client.parser.properties.protocol import PropertyProtocol

from builder.jinja_filters.field_names import field_name


def always_sent_fields(required_props: list[PropertyProtocol]) -> list[str]:
    """
    Return the names of the required fields the SDK fills in itself.

    Request bodies are dumped with `exclude_unset=True`, so a field whose value
    comes from a generated default (a `Literal` constant or a spec default)
    counts as unset and is stripped - but the spec still requires it on the
    wire. Optional defaulted fields are not passed in: the server applies the
    same default, and omitting them keeps the body to what the caller set.
    """
    return [
        field_name(prop.python_name)
        for prop in required_props
        if isinstance(prop, ConstProperty) or prop.default is not None
    ]
