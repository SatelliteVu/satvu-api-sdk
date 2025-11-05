from datetime import UTC, datetime
from typing import Annotated, TypeAlias
import toml

import dagger
from dagger import dag, function, object_type


SOURCE: TypeAlias = Annotated[
    dagger.Directory,
    dagger.DefaultPath("/"),
    dagger.Doc("source directory"),
]


@object_type
class SatvuApiSdkCi:
    def build_container(
        self, source: dagger.Directory, install_deps=False
    ) -> dagger.Container:
        """Returns a python+uv build container"""
        uv_image = dag.container().from_("ghcr.io/astral-sh/uv:latest")
        builder = (
            dag.container()
            .from_("python:3.13-alpine")
            .with_file("/bin/uv", uv_image.file("/uv"))
            .with_file("/bin/uvx", uv_image.file("/uvx"))
            .with_workdir("/src")
            .with_directory("/src", source, gitignore=True, exclude=[".dagger"])
        )

        if install_deps:
            builder = builder.with_exec(
                ["uv", "sync", "--all-extras", "--frozen"]
            ).with_env_variable("PATH", "${PATH}:/src/.venv/bin")

        return builder

    @function
    async def build_release(
        self,
        source: SOURCE,
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

    @function
    async def lint_ruff(self, source: SOURCE):
        """Run ruff linter"""
        return (
            await dag.container()
            .from_("ghcr.io/astral-sh/ruff:latest")
            .with_directory("/src", source, gitignore=True)
            .with_exec(["/ruff", "check"])
        )

    @function
    async def lint_bandit(
        self,
        source: SOURCE,
        paths: list[str] = [".dagger/src", "builder", "src"],
        skip_test_ids: list[str] = ["B404", "B603", "B310"],
        exclude_paths: list[str] = ["*_test.py", "conftest.py"],
    ):
        """Run bandit linter"""
        command = ["uvx", "bandit"]
        if skip_test_ids:
            command += ["-s", ",".join(skip_test_ids)]
        if exclude_paths:
            command += ["-x", ",".join(exclude_paths)]
        command += ["-r"] + paths
        await self.build_container(source).with_exec(command)

    @function
    async def lint_detect_secrets(
        self,
        source: SOURCE,
        paths: list[str] = ["src"],
    ):
        """Run detect-secrets linter"""
        runner = self.build_container(source)
        command = ["uvx", "--from=detect-secrets", "detect-secrets-hook"]
        for path in paths:
            files = await runner.directory("/src").glob(f"{path.rstrip('/')}/**/*.py")
            command += files
        await runner.with_exec(command)
        return command

    @function
    async def lint_fawltydeps(self, source: SOURCE):
        """Run fawltydeps linter"""
        await self.build_container(source).with_exec(
            ["uvx", "fawltydeps", "--detailed", "--check-undeclared"]
        )
        await self.build_container(source).with_exec(
            ["uvx", "fawltydeps", "--detailed", "--check-unused"]
        )

    @function
    async def lint(self, source: SOURCE):
        """Runs linters"""
        await self.lint_ruff(source)
        await self.lint_bandit(source)
        await self.lint_detect_secrets(source)
        await self.lint_fawltydeps(source)

    @function
    async def test(self, source: SOURCE, add_opts: str = "") -> dagger.Directory:
        """Runs test suite"""

        run = (
            await self.build_container(source, install_deps=True)
            .with_env_variable("PYTEST_ADDOPTS", add_opts)
            .with_exec(
                [
                    "pytest",
                    "--junitxml=/tmp/pytest.xml",
                    "--cov-report=term-missing:skip-covered",
                    "--cov=src",
                ],
                redirect_stdout="/tmp/pytest-coverage.txt",  # nosec: B108
            )
        )

        return dag.directory().with_files(
            ".",
            sources=[
                run.file("/tmp/pytest.xml"),  # nosec: B108
                run.file("/tmp/pytest-coverage.txt"),  # nosec: B108
            ],
        )
