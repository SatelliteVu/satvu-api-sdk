from openapi_python_client.parser.properties.const import ConstProperty
from openapi_python_client.parser.properties.list_property import ListProperty
from openapi_python_client.parser.properties.model_property import ModelProperty
from openapi_python_client.parser.properties.protocol import PropertyProtocol
from openapi_python_client.parser.properties.union import UnionProperty
from openapi_python_client.strings import in_double_quote_literal, safe_for_docstring

from builder.code_strings import unwrap_code
from builder.patches import _UNION_DISCRIMINATORS


def _discriminator_for(
    prop: PropertyProtocol,
) -> tuple[str | None, UnionProperty | None]:
    """Return (property_name, union_prop) if the type is a discriminated Union.

    Handles both bare `Union[...]` fields and `list[Union[...]]` fields.
    """
    if isinstance(prop, UnionProperty):
        return _UNION_DISCRIMINATORS.get(id(prop)), prop
    if isinstance(prop, ListProperty) and isinstance(
        prop.inner_property, UnionProperty
    ):
        return _UNION_DISCRIMINATORS.get(id(prop.inner_property)), prop.inner_property
    return None, None


def to_pydantic_model_field(prop: PropertyProtocol) -> str:
    """
    Returns a string representation of the property as a Pydantic model field.

    Returns:
        A string like: `field_name: FieldType = Field(..., description="...", alias="...")`
    """
    # Append underscore to field names that shadow BaseModel attributes
    # to avoid Pydantic warnings (e.g., "schema" -> "schema_")
    python_name = prop.python_name
    if python_name == "schema":
        python_name = "schema_"

    type_string = unwrap_code(prop.get_type_string())

    if isinstance(prop, ModelProperty):
        # If it's just the class name, quote it for forward reference
        if type_string == prop.class_info.name:
            type_string = f"'{type_string}'"
    else:
        # Wrap discriminated unions so Pydantic dispatches in O(1) instead of
        # scoring every variant. Spec-level `discriminator:` is captured in
        # patches.py and reapplied here because openapi-python-client drops it.
        discriminator_name, union_prop = _discriminator_for(prop)
        if discriminator_name and union_prop is not None:
            union_type_string = unwrap_code(
                union_prop.get_type_string(no_optional=True)
            )
            annotated = f'Annotated[{union_type_string}, Field(discriminator="{discriminator_name}")]'
            if isinstance(prop, ListProperty):
                type_string = f"list[{annotated}]"
            else:
                type_string = annotated

    field_start = f"{python_name}: {type_string}"

    description = (
        f'"""{safe_for_docstring(prop.description)}"""' if prop.description else "None"
    )
    alias = in_double_quote_literal(prop.name)

    # For const (literal) properties, default to the value of the constant
    if isinstance(prop, ConstProperty):
        default = unwrap_code(prop.value.python_code)
        return f'{field_start} = Field(default={default}, description={description}, alias="{alias}")'

    if prop.default is not None:
        default = unwrap_code(prop.default.python_code)
        return f'{field_start} = Field(default={default}, description={description}, alias="{alias}")'

    elif not prop.required:
        return f'{field_start} = Field(default=None, description={description}, alias="{alias}")'

    else:
        return f'{field_start} = Field(..., description={description}, alias="{alias}")'
