from datetime import datetime, timezone
from typing import Annotated, TypeAlias

import dagger
import toml
from dagger import dag, function, object_type

SOURCE: TypeAlias = Annotated[
    dagger.Directory,
    dagger.DefaultPath("/"),
    dagger.Doc("source directory"),
]

SUPPORTED_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]
DEFAULT_PYTHON_VERSION = "3.13"


@object_type
class SatvuApiSdkCi:
    def build_container(
        self,
        source: dagger.Directory,
        python_version: str = DEFAULT_PYTHON_VERSION,
        install_deps: bool = False,
    ) -> dagger.Container:
        """Returns a python+uv build container"""
        uv_image = dag.container().from_("ghcr.io/astral-sh/uv:latest")
        builder = (
            dag.container()
            .from_(f"python:{python_version}-alpine")
            .with_file("/bin/uv", uv_image.file("/uv"))
            .with_file("/bin/uvx", uv_image.file("/uvx"))
            .with_workdir("/src")
            .with_directory("/src", source, gitignore=True, exclude=[".dagger"])
        )

        if install_deps:
            builder = builder.with_exec(
                [
                    "uv",
                    "sync",
                    "--all-extras",
                    "--frozen",
                    "--python=/usr/local/bin/python",
                ]
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
        now = datetime.now(timezone.utc)
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
        paths: list[str] = [".dagger/src", "builder", "src"],  # noqa: B006
        skip_test_ids: list[str] = ["B404", "B603", "B310"],  # noqa: B006
        exclude_paths: list[str] = ["*_test.py", "conftest.py"],  # noqa: B006
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
        paths: list[str] = ["src"],  # noqa: B006
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
    async def test(
        self,
        source: SOURCE,
        python_version: Annotated[
            str, dagger.Doc("Python version to test against")
        ] = DEFAULT_PYTHON_VERSION,
        add_opts: str = "",
        with_coverage: Annotated[
            bool, dagger.Doc("Enable coverage reporting (disable for faster runs)")
        ] = True,
    ) -> dagger.Directory:
        """Runs test suite for a specific Python version"""

        pytest_args = [
            "pytest",
            "--junitxml=/tmp/pytest.xml",
            "-n=auto",
            "-v",
        ]

        # Only add coverage args when requested
        if with_coverage:
            pytest_args.extend(
                [
                    "--cov-report=term-missing:skip-covered",
                    "--cov=src",
                ]
            )

        run = (
            await self.build_container(
                source, python_version=python_version, install_deps=True
            )
            # Verify correct Python version is being used
            .with_exec(["python", "--version"])
            .with_env_variable("PYTEST_ADDOPTS", add_opts)
            .with_exec(["/bin/uv", "build"])
            .with_exec(
                pytest_args,
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

    @function
    async def test_all(self, source: SOURCE) -> str:
        """Runs test suite across all supported Python versions in parallel"""
        import asyncio

        results = await asyncio.gather(
            *[self.test(source, python_version=v) for v in SUPPORTED_PYTHON_VERSIONS],
            return_exceptions=True,
        )

        # Check for failures
        failures = []
        for version, result in zip(SUPPORTED_PYTHON_VERSIONS, results, strict=True):
            if isinstance(result, Exception):
                failures.append(f"Python {version}: {result}")

        if failures:
            raise RuntimeError(
                f"Tests failed for {len(failures)} version(s):\n" + "\n".join(failures)
            )

        return f"All tests passed for Python versions: {', '.join(SUPPORTED_PYTHON_VERSIONS)}"
