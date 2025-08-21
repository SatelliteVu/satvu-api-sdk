from datetime import datetime, date
from typing import Union, get_args, get_origin, Any, Literal
from pydantic import BaseModel


def deep_parse_from_annotation(data: Any, annotation: Any) -> Any:
    """
    Recursively parses the input data using the provided type annotation.

    This supports:
    - Union[...] and List[Union[...]]
    - Nested BaseModel fields
    - Lists of BaseModel or unions

    :param data: The raw JSON-like object (dict, list, etc.)
    :param annotation: The type annotation (e.g., List[Union[ModelA, ModelB]], ModelC, etc.)
    :return: The parsed object according to the annotation.
    """
    origin = get_origin(annotation)
    args = get_args(annotation)

    # If data is None, return None directly if the annotation allows it
    # otherwise, raise an error
    if data is None:
        if annotation is type(None):
            return None
        if origin is Union and type(None) in args:
            return None
        raise ValueError(f"Received None for non-optional type {annotation}")

    # If annotation is a Union, try each type in the Union
    if origin is Union:
        for arg in args:
            try:
                return deep_parse_from_annotation(data, arg)
            except Exception:
                continue
        raise ValueError(f"Could not match data to any Union type: {data}")

    elif origin is list:
        # If the data is a list, recursively parse each item
        if isinstance(data, list):
            return [deep_parse_from_annotation(item, args[0]) for item in data]
        # If the data is not a list, raise an error
        else:
            raise ValueError(f"Expected a list but got {type(data).__name__}: {data}")

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

    elif annotation is str:
        # If the annotation is str, return the data as is
        return data

    elif annotation == Any:
        # If Any is used, return the data as is
        return data

    else:
        # Assume primitive type
        return annotation(data)


def _recursive_parse_dict(data: dict, model_cls):
    """
    Parses a dict recursively into a Pydantic model, including support for nested Unions.
    """
    model_fields = model_cls.model_fields
    new_data = {}

    for field in model_fields.values():
        if field.alias not in list(data.keys()):
            continue

        field_value = data[field.alias]
        field_type = field.annotation

        try:
            new_data[field.alias] = deep_parse_from_annotation(field_value, field_type)
        except Exception as e:
            raise ValueError(
                f"Failed to parse field '{field.alias}' in {model_cls.__name__}: {e}"
            )

    return model_cls.model_validate(new_data, by_alias=True)


def normalize_keys(obj: Any) -> Any:
    """
    Recursively replaces colons in dictionary keys with underscores
    for a nested JSON-like object (dicts, lists, primitives).
    """
    if isinstance(obj, dict):
        return {k.replace(":", "_"): normalize_keys(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [normalize_keys(item) for item in obj]
    else:
        return obj  # Base case: primitive types (str, int, float, etc.)
