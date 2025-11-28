from openapi_python_client.parser.properties import (
    ConstProperty,
    ModelProperty,
)
from openapi_python_client.parser.properties.protocol import PropertyProtocol


def to_pydantic_model_field(prop: PropertyProtocol) -> str:
    """
    Returns a string representation of the property as a Pydantic model field.

    Returns:
        A string like: `field_name: FieldType = Field(..., description="...", alias="...")`
    """
    if isinstance(prop, ModelProperty):
        type_string = prop.get_type_string()
        # If it's just the class name, quote it for forward reference
        if type_string == prop.class_info.name:
            type_string = f"'{type_string}'"
        field_start = f"{prop.python_name}: {type_string}"
    else:
        field_start = f"{prop.python_name}: {prop.get_type_string()}"

    description = f'"""{prop.description}"""' if prop.description else "None"

    # For const (literal) properties, default to the value of the constant
    if isinstance(prop, ConstProperty):
        return f'{field_start} = Field(default={prop.value.python_code}, description={description}, alias="{prop.name}")'

    if prop.default is not None:
        return f'{field_start} = Field(default={prop.default.python_code}, description={description}, alias="{prop.name}")'

    elif not prop.required:
        return f'{field_start} = Field(default=None, description={description}, alias="{prop.name}")'

    else:
        return f'{field_start} = Field(..., description={description}, alias="{prop.name}")'
