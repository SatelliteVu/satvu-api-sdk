from typing import Literal, Union
from pydantic import BaseModel, AnyUrl, Field, UrlConstraints


class HttpsUrl(AnyUrl):
    _constraints = UrlConstraints(max_length=2083, allowed_schemes=["https"])


class Server(BaseModel):
    url: HttpsUrl


class RefSchema(BaseModel):
    ref: str = Field(alias="$ref")


class StringSchema(BaseModel):
    type: Literal["string"]
    description: str | None = None
    example: str | None = None


class NumberSchema(BaseModel):
    type: Literal["number"]
    format: Literal["double"]


class IntegerSchema(BaseModel):
    type: Literal["integer"]
    description: str | None = None
    example: int | None = None
    format: Literal["int32"]
    nullable: bool = False


class ArraySchema(BaseModel):
    type: Literal["array"]
    items: StringSchema | NumberSchema
    description: str | None = None
    example: str | None = None


class ObjectSchema(BaseModel):
    type: Literal["object"]
    properties: dict[
        str,
        Union[
            StringSchema,
            NumberSchema,
            IntegerSchema,
            ArraySchema,
            RefSchema,
            "ObjectSchema",
        ],
    ]
    required: list[str] = []


class Components(BaseModel):
    schemas: dict[
        str,
        StringSchema
        | NumberSchema
        | IntegerSchema
        | ArraySchema
        | ObjectSchema
        | RefSchema,
    ]


class Parameter(BaseModel):
    name: str
    source: Literal["path", "query"] = Field(alias="in")
    description: str | None = None  # TODO: raise warning
    required: bool = False
    schema_: StringSchema | NumberSchema | IntegerSchema | ArraySchema | RefSchema = (
        Field(alias="schema")
    )


class ResponseModel(BaseModel):
    schema_: StringSchema | NumberSchema | IntegerSchema | ArraySchema | RefSchema = (
        Field(alias="schema")
    )


class Response(BaseModel):
    description: str
    content: dict[str, ResponseModel]


class Path(BaseModel):
    summary: str
    description: str
    operation_id: str = Field(alias="operationId")
    parameters: list[Parameter]
    responses: dict[str, Response]


class Paths(BaseModel):
    get: Path | None = None
    post: Path | None = None
    delete: Path | None = None
    put: Path | None = None
    patch: Path | None = None


class Info(BaseModel):
    title: str
    description: str
    version: str


class OpenApi(BaseModel):
    openapi: str
    info: Info
    servers: list[Server]
    paths: dict[str, Paths]
    components: Components

    def resolve(self):
        pass
