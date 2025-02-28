import ast as pyast
from hashlib import sha1
from json import dumps, loads
from pathlib import Path

from httpx import get

from openapi_python_client import Project
from openapi_python_client.config import Config, MetaType, ConfigFile
from openapi_python_client.parser.openapi import GeneratorData
from openapi_python_client.parser.errors import GeneratorError

from builder.config import APIS, BASE_URL

BASE_DIR = (Path(__file__).parent / "..").resolve()
CACHE_DIR = BASE_DIR / ".cache"
TEMPLATE_DIR = Path(__file__).parent / "templates"
SRC_DIR = BASE_DIR / "src"


def _load_openapi(api_id: str, use_cached: bool):
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    openapi_url = f"{BASE_URL.rstrip('/')}/{APIS[api_id]}"
    cache_file = CACHE_DIR / f"{api_id}-{sha1(openapi_url.encode()).hexdigest()}.json"

    if not use_cached:
        response = get(openapi_url)
        response.raise_for_status()
        openapi = response.json()
        cache_file.write_text(dumps(openapi))

    return loads(cache_file.read_text()), cache_file


def build(api_id: str, use_cached: False):
    openapi_dict, openapi_src = _load_openapi(api_id, use_cached)
    config = Config.from_sources(
        config_file=ConfigFile(),
        meta_type=MetaType.NONE,
        document_source=openapi_src,
        file_encoding="utf-8",
        overwrite=True,
        output_path=SRC_DIR / api_id,
    )

    openapi = GeneratorData.from_dict(openapi_dict, config=config)
    if isinstance(openapi, GeneratorError):
        print(GeneratorError)
        exit(1)

    project = Project(
        openapi=openapi,
        custom_template_path=TEMPLATE_DIR,
        config=config,
    )

    errors = project.build()
    if len(errors) > 0:
        for error in errors:
            print("=" * 20)
            print(error)
        exit(1)
