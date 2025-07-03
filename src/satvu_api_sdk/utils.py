from typing import Any, Union, List, Dict


def disambiguate_union_response(response_data: dict, response_disambiguation: Any):
    """
    Given a dict response_data and a response_disambiguation config object,
    select the best-matching model class to instantiate from the union.

    Handles discriminators if present, otherwise uses recursive required/optional
    field and type matching to select the best fit.
    """
    discriminator = getattr(response_disambiguation, "discriminator", None)
    mapping = getattr(response_disambiguation, "discriminator_mapping", None)
    fallback_models = getattr(response_disambiguation, "fallback_models", [])

    # --- Try discriminator if present ---
    if discriminator and mapping and discriminator in response_data:
        disc_value = response_data[discriminator]
        model_cls = mapping.get(disc_value)
        if model_cls:
            try:
                return model_cls(**response_data)
            except Exception:
                pass

    # --- Recursive field/type matching ---


    def _type_matches(value, expected_type):
        origin = getattr(expected_type, "__origin__", None)
        if origin is not None:
            # Handle Union
            if origin is Union:
                return any(_type_matches(value, t) for t in expected_type.__args__)
            # Handle List
            elif origin in {list, List}:
                if not isinstance(value, list):
                    return False
                elem_type = expected_type.__args__[0]
                return all(_type_matches(v, elem_type) for v in value)
            # Handle Dict
            elif origin in {dict, Dict}:
                if not isinstance(value, dict):
                    return False
                val_type = expected_type.__args__[1]
                return all(_type_matches(v, val_type) for v in value.values())
        # Handle nested model classes
        if hasattr(expected_type, "get_required_fields_and_types"):
            return _required_fields_and_types_match(value, expected_type)
        # Fallback: primitives/enums
        try:
            return isinstance(value, expected_type)
        except Exception:
            return False

    def _required_fields_and_types_match(data, model_cls):
        if not isinstance(data, dict):
            return False
        required = model_cls.get_required_fields_and_types()
        for field, typ in required.items():
            if field not in data:
                return False
            if not _type_matches(data[field], typ):
                return False
        return True

    def _count_optional_matches(data, model_cls):
        if not isinstance(data, dict):
            return 0
        count = 0
        optional = model_cls.get_optional_fields_and_types()
        for field, typ in optional.items():
            if field in data and _type_matches(data[field], typ):
                count += 1
        return count

    response_fields = set(response_data.keys())
    candidates = []
    for model_cls in fallback_models:
        if model_cls.get_required_fields().issubset(response_fields):
            if _required_fields_and_types_match(response_data, model_cls):
                matching_optional = _count_optional_matches(response_data, model_cls)
                candidates.append((model_cls, matching_optional))

    if candidates:
        # Prefer model with most matching optional fields, then most required fields
        candidates.sort(key=lambda x: (x[1], len(x[0].get_required_fields())), reverse=True)
        for model_cls, _ in candidates:
            try:
                return model_cls(**response_data)
            except Exception:
                continue

    # Fallback: return unparsed dict
    return response_data