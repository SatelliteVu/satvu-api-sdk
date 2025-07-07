from datetime import datetime, date
from typing import Type, List, Union, get_args, get_origin, Any, Literal
from pydantic import BaseModel, ValidationError


def deep_parse_from_annotation(
    data: Any,
    annotation: Any
) -> Any:
    """
    Recursively parses the input data using the provided type annotation.

    This supports:
    - Union[...] and List[Union[...]]
    - Nested BaseModel fields
    - Lists of BaseModel or unions

    Args:
        data: The raw JSON-like object (dict, list, etc.)
        annotation: The type annotation (e.g., List[Union[ModelA, ModelB]])

    Returns:
        The parsed object according to the annotation.
    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    if origin is Union:
        for arg in args:
            try:
                print(f"Trying to parse as {arg}")
                return deep_parse_from_annotation(data, arg)
            except Exception:
                continue
        raise ValueError(f"Could not match data to any Union type: {data}")

    elif origin is list and len(args) == 1:
        return [deep_parse_from_annotation(item, args[0]) for item in data]

    elif origin is Literal:
        if data in args:
            return data
        raise ValueError(f"Value '{data}' does not match any Literal options: {args}")

    elif isinstance(annotation, type) and issubclass(annotation, BaseModel):
        return _recursive_parse_dict(data, annotation)

    elif annotation is datetime:
        return datetime.fromisoformat(data)

    elif annotation is date:
        return date.fromisoformat(data)

    else:
        # Assume primitive type
        return annotation(data)


def _recursive_parse_dict(data: dict, model_cls: Type[BaseModel]) -> BaseModel:
    """
    Parses a dict recursively into a Pydantic model, including support for nested Unions.
    """
    model_fields = model_cls.model_fields
    new_data = {}

    for field_name, field in model_fields.items():
        if field_name not in data:
            continue

        field_value = data[field_name]
        field_type = field.annotation

        try:
            new_data[field_name] = deep_parse_from_annotation(field_value, field_type)
        except Exception as e:
            raise ValueError(f"Failed to parse field '{field_name}' in {model_cls.__name__}: {e}")

    return model_cls(**new_data)


def normalize_keys(obj: Any) -> Any:
    """
    Recursively replaces colons in dictionary keys with underscores
    for a nested JSON-like object (dicts, lists, primitives).
    """
    if isinstance(obj, dict):
        return {
            k.replace(":", "_"): normalize_keys(v)
            for k, v in obj.items()
        }
    elif isinstance(obj, list):
        return [normalize_keys(item) for item in obj]
    else:
        return obj  # Base case: primitive types (str, int, float, etc.)
