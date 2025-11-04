from datetime import UTC, datetime
from typing import Annotated
import toml

import dagger
from dagger import dag, function, object_type


@object_type
class SatvuApiSdkCi:
    def build_container(self, src_dir: dagger.Directory) -> dagger.Container:
        """Returns a python+uv build container"""
        uv_image = dag.container().from_("ghcr.io/astral-sh/uv:latest")
        return (
            dag.container()
            .from_("python:3.13-alpine")
            .with_file("/bin/uv", uv_image.file("/uv"))
            .with_file("/bin/uvx", uv_image.file("/uvx"))
            .with_workdir("/src")
            .with_directory("/src", src_dir, gitignore=True)
        )

    @function
    async def build_release(
        self,
        source: Annotated[
            dagger.Directory,
            dagger.DefaultPath("/"),
            dagger.Doc("source directory"),
        ],
        is_qa: Annotated[bool, dagger.Doc("build for QA environment")] = True,
        build_number: Annotated[int, dagger.Doc("release build number")] = 0,
    ) -> dagger.Directory:
        """Returns source distribution and package wheel"""
        # 1. generate pyproject.toml with updated version
        pyproject_raw = await source.file("pyproject.toml").contents()
        pyproject_parsed = toml.loads(pyproject_raw)
        sdk_version: str = pyproject_parsed["project"]["version"]
        now = datetime.now(UTC)
        version = f"{sdk_version}.{now:%y%m%d}.{build_number}"
        if is_qa:
            version += ".rc0"
        pyproject_parsed["project"]["version"] = version

        # 2. use builder to create distributions and export dist dir
        return (
            self.build_container(source)
            .with_env_variable("SATVU_SDK_USE_QA", "1" if is_qa else "0")
            .with_new_file("/src/pyproject.toml", toml.dumps(pyproject_parsed))
            .with_exec(["uv", "build"])
            .directory("/src/dist")
        )
