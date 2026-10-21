"""
Request body conformance checks for generated service tests.

On the request side the SDK's whole job is to turn a caller's model back into
the body the OpenAPI spec describes. That round trip is where "optional" can
quietly become "nullable": a field the caller never touched reaches the wire as
an explicit null or as an SDK-invented default, or travels under its python name
instead of its alias, and the API rejects a body the SDK itself built.

The generated tests already feed each endpoint a spec-valid body and post it
through a pook mock, so the missing step is inspecting what came out the other
side. Two checks run against every captured body:

``assert_request_body_conforms``
    It still satisfies the schema the body was generated from. Catches a
    required field going missing, or a value whose type or enum broke in
    transit. Only conformance the input already had can be broken, so a body
    that never conformed is skipped rather than blamed on the round trip.

``assert_request_body_matches_input``
    It introduces no key the caller did not set. Deterministic for any input,
    and the tighter of the two for this bug class - it fires whether or not the
    spec happens to forbid null at that position.

``assert_minimal_dump_conforms``
    The opposite direction: a model built from only the fields a caller must
    pass still dumps every key the spec requires. Constants and defaulted
    required fields are filled in by the SDK, so ``exclude_unset`` must not
    strip them.

Excluded from the wheel alongside example_cache.py; this is test-only support
code and pulls in jsonschema, which is not a runtime dependency.
"""

from collections.abc import Iterator
from typing import Any

import pytest
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError, best_match
from pydantic import BaseModel

# Sentinel for "this request carried no body", distinct from a body of ``null``.
_NO_BODY = object()

# Cap the body echoed back in failure messages; generated bodies can be large.
_MAX_BODY_CHARS = 2000

_LEAK_HINT = (
    "A field the caller never set reached the wire - as null, as an SDK "
    "default, or under its python name instead of its alias."
)


def _captured_bodies(mock: Any, operation: str) -> list[Any]:
    """Decode the JSON body of every request pook recorded for ``mock``."""
    requests = list(getattr(mock, "matches", None) or [])
    if not requests:
        raise AssertionError(
            f"{operation}: no request was captured, so the serialised body could "
            f"not be checked. Did the call reach the mock?"
        )

    bodies = []
    for request in requests:
        raw = getattr(request, "body", None)
        if raw is None or raw == b"" or raw == "":
            bodies.append(_NO_BODY)
            continue
        try:
            bodies.append(request.json)
        except (ValueError, TypeError) as exc:
            raise AssertionError(
                f"{operation}: request body was not valid JSON ({exc}). "
                f"Raw body: {raw!r}"
            ) from exc
    return bodies


def drop_optional_properties(body: Any, schema: dict) -> Any:
    """
    Remove the top-level properties the spec does not require.

    Both checks below only bite when the caller left something unset, and which
    fields a generated example omits is decided by the cached example set. This
    manufactures the omission instead, so the guard cannot quietly stop guarding
    if that cache changes. Removing optional properties from a valid body leaves
    a valid body; anything this cannot reason about is returned untouched.

    :param body: A spec-valid request body.
    :param schema: The spec's requestBody schema for that body.
    :returns: The body with its optional top-level properties removed.
    """
    if not isinstance(body, dict) or "properties" not in schema:
        return body
    required = set(schema.get("required", []))
    return {key: value for key, value in body.items() if key in required}


def _ref_chain(schema: dict, definitions: dict) -> Iterator[dict]:
    """Yield each schema on the way through ``$ref`` and single-member ``allOf``."""
    while True:
        yield schema
        if "$ref" in schema:
            schema = definitions.get(schema["$ref"].rsplit("/", 1)[-1], {})
        elif len(schema.get("allOf", [])) == 1:
            schema = schema["allOf"][0]
        else:
            return


def _resolve(schema: dict, definitions: dict) -> dict:
    """Follow ``$ref`` (and single-member ``allOf`` wrappers) to the target schema."""
    *_, target = _ref_chain(schema, definitions)
    return target


def _object_schema(schema: dict, definitions: dict) -> dict | None:
    """
    Return the ``properties``/``required`` of a resolved object schema.

    Multi-member ``allOf`` is merged, as the generated model merges it. Returns
    None for anything that is not an object made of properties.
    """
    if "properties" in schema:
        return schema
    members = schema.get("allOf") or []
    if len(members) < 2:
        return None
    resolved = [_object_schema(_resolve(m, definitions), definitions) for m in members]
    objects = [obj for obj in resolved if obj is not None]
    if len(objects) != len(members):
        return None
    return {
        "properties": {
            key: value for obj in objects for key, value in obj["properties"].items()
        },
        "required": [key for obj in objects for key in obj.get("required", [])],
    }


def _union_member(body: Any, schema: dict, definitions: dict) -> dict | None:
    """Return the ``oneOf``/``anyOf`` branch ``body`` satisfies, if any."""
    for branch in schema.get("oneOf") or schema.get("anyOf") or []:
        if Draft7Validator({**branch, "definitions": definitions}).is_valid(body):
            return branch
    return None


def _is_union_of_objects(schema: dict, definitions: dict) -> bool:
    """Whether more than one branch is an object, so its constants pick the variant."""
    branches = schema.get("oneOf") or schema.get("anyOf") or []
    objects = [
        branch
        for branch in branches
        if _object_schema(_resolve(branch, definitions), definitions) is not None
    ]
    return len(objects) > 1


def _sdk_supplies(prop_schema: dict, definitions: dict) -> bool:
    """
    Whether the generated field gets a value without the caller passing one.

    A ``const`` anywhere on the ``$ref`` chain becomes a ``Literal`` field, but
    openapi-python-client drops a ``default`` set on a referenced schema, so a
    default only counts up to the first ``$ref``.
    """
    chain = list(_ref_chain(prop_schema, definitions))
    if any("const" in step for step in chain):
        return True
    for step in chain:
        if "default" in step:
            return True
        if "$ref" in step:
            return False
    return False


def _reducible_root(body: Any, schema: dict, definitions: dict) -> dict | None:
    """Return the object schema ``minimal_request_body`` reduces ``body`` against."""
    schema = _resolve(schema, definitions)
    member = _union_member(body, schema, definitions)
    if member is not None:
        schema = _resolve(member, definitions)
    return _object_schema(schema, definitions)


def minimal_request_body(
    body: Any, schema: dict, definitions: dict | None = None, *, is_variant=False
) -> Any:
    """
    Reduce a spec-valid body to the fields a caller has to pass, recursively.

    Optional properties go, and so do required ones the SDK can supply itself
    (``const`` or ``default``) - those are exactly the fields ``exclude_unset``
    is at risk of stripping. Inside a union of objects the constants stay: they
    are what tells the variants apart, so a caller passing a dict must set them.

    :param body: A spec-valid request body.
    :param schema: The schema for ``body``, with ``definitions`` attached at the
        root.
    :returns: The reduced body; anything this cannot reason about is untouched.
    """
    defs = schema.get("definitions", {}) if definitions is None else definitions
    schema = _resolve(schema, defs)

    if isinstance(body, list) and isinstance(schema.get("items"), dict):
        return [minimal_request_body(item, schema["items"], defs) for item in body]

    member = _union_member(body, schema, defs)
    if member is not None:
        return minimal_request_body(
            body, member, defs, is_variant=_is_union_of_objects(schema, defs)
        )

    obj = _object_schema(schema, defs)
    if not isinstance(body, dict) or obj is None:
        return body

    required = set(obj.get("required", []))
    properties = obj["properties"]
    return {
        key: minimal_request_body(value, properties.get(key, {}), defs)
        for key, value in body.items()
        if key in required
        and (is_variant or not _sdk_supplies(properties.get(key, {}), defs))
    }


def assert_minimal_dump_conforms(
    model: type[BaseModel], body: Any, schema: dict
) -> None:
    """
    Assert a model built from a caller's minimum still dumps a spec-valid body.

    ``body`` is reduced with ``minimal_request_body``, validated into ``model``
    and dumped exactly as the SDK dumps request bodies. The dump must satisfy
    ``schema``, so every ``required`` key - at any depth - is on the wire.
    Stands down when ``body`` does not conform to start with, as above, and
    skips when the model's schema is not an object this can reduce - passing
    there would test nothing.

    :param model: The generated request model under test.
    :param body: A spec-valid body for ``model``, in wire names.
    :param schema: The model's schema, with ``definitions`` attached.
    :raises AssertionError: If the dump is missing a required key or otherwise
        stops conforming.
    """
    validator = Draft7Validator(schema)
    if best_match(validator.iter_errors(body)):
        return

    if _reducible_root(body, schema, schema.get("definitions", {})) is None:
        pytest.skip(f"{model.__name__}: schema is not a reducible object")

    minimal = minimal_request_body(body, schema)
    dumped = model.model_validate(minimal).model_dump(
        by_alias=True, mode="json", exclude_unset=True
    )
    error = best_match(validator.iter_errors(dumped))
    if error is not None:
        location = "/".join(str(part) for part in error.absolute_path) or "<root>"
        raise AssertionError(
            f"{model.__name__}: a model built from only the caller-required fields "
            f"dumps a body that does not satisfy its schema.\n"
            f"  at {location}: {error.message}\n"
            f"  body given: {_render(minimal)}\n"
            f"  body dumped: {_render(dumped)}\n"
            f"  A spec-required field the SDK supplies (a constant or default) "
            f"was treated as unset and stripped by exclude_unset."
        )


def _render(value: Any) -> str:
    rendered = repr(value)
    if len(rendered) > _MAX_BODY_CHARS:
        return f"{rendered[:_MAX_BODY_CHARS]}... (truncated)"
    return rendered


def _invented_keys(sent: Any, given: Any, path: str = "") -> list[str]:
    """
    Collect paths present in ``sent`` but absent from ``given``.

    Both sides use wire names, since the input body came from the spec, so a
    field serialised under its python name shows up here as an invented key.
    """
    if isinstance(sent, dict):
        if not isinstance(given, dict):
            return []
        invented = [f"{path}/{key}" for key in sent if key not in given]
        for key, value in sent.items():
            if key in given:
                invented.extend(_invented_keys(value, given[key], f"{path}/{key}"))
        return invented

    if isinstance(sent, list) and isinstance(given, list):
        invented = []
        # A length mismatch is not an invented key, and strict=True would raise
        # ValueError here instead of letting the caller see an assertion.
        for index, (sent_item, given_item) in enumerate(zip(sent, given, strict=False)):
            invented.extend(_invented_keys(sent_item, given_item, f"{path}/{index}"))
        return invented

    return []


def assert_request_body_conforms(
    mock: Any, schema: dict, operation: str, given_body: Any = None
) -> None:
    """
    Assert every body captured by ``mock`` satisfies the requestBody schema.

    Serialisation can only preserve or destroy the conformance the input
    already had. When ``given_body`` does not satisfy the schema itself there is
    nothing here for the SDK to have broken, so the check stands down - example
    generation is not always able to produce a conforming body for every
    schema, and failing then would blame the round trip for its input.

    :param mock: The pook ``Mock`` that intercepted the call.
    :param schema: The spec's requestBody schema, with ``definitions`` attached.
    :param operation: Human-readable operation label, used in failures.
    :param given_body: The body data the model was built from. Omit to assert
        conformance unconditionally.
    :raises AssertionError: If no request was captured, a body was not JSON, or
        a body that started out conforming stopped conforming.
    """
    validator = Draft7Validator(schema)
    if given_body is not None and best_match(validator.iter_errors(given_body)):
        return

    for body in _captured_bodies(mock, operation):
        if body is _NO_BODY:
            continue
        error = best_match(validator.iter_errors(body))
        if error is not None:
            raise AssertionError(_format_conformance_failure(operation, body, error))


def _format_conformance_failure(
    operation: str, body: Any, error: ValidationError
) -> str:
    location = "/".join(str(part) for part in error.absolute_path) or "<root>"
    return (
        f"{operation}: the serialised request body does not satisfy the spec's "
        f"requestBody schema.\n"
        f"  at {location}: {error.message}\n"
        f"  body sent: {_render(body)}\n"
        f"  {_LEAK_HINT}"
    )


def assert_request_body_matches_input(
    mock: Any, given_body: Any, operation: str
) -> None:
    """
    Assert the serialised body introduces no key the caller did not set.

    Omission has to survive the round trip: if the caller left a field alone,
    nothing about it belongs on the wire. This holds for any input, which makes
    it the deterministic counterpart to schema conformance.

    :param mock: The pook ``Mock`` that intercepted the call.
    :param given_body: The body data the model was built from, in wire names.
    :param operation: Human-readable operation label, used in failures.
    :raises AssertionError: If the serialised body carries invented keys.
    """
    for body in _captured_bodies(mock, operation):
        if body is _NO_BODY:
            continue
        invented = _invented_keys(body, given_body)
        if invented:
            listed = "\n".join(f"    {key}" for key in sorted(invented))
            raise AssertionError(
                f"{operation}: the serialised request body carries "
                f"{len(invented)} key(s) the caller never set:\n"
                f"{listed}\n"
                f"  body sent: {_render(body)}\n"
                f"  body given: {_render(given_body)}\n"
                f"  {_LEAK_HINT}"
            )
