import os
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
            # Explicitly include .cache for cached OpenAPI specs (excluded by gitignore)
            # If .cache doesn't exist, this mounts an empty directory (safe fallback)
            .with_directory("/src/.cache", source.directory(".cache"))
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
        is_qa: Annotated[bool, dagger.Doc("build for QA environment")] = False,
        version: Annotated[
            str, dagger.Doc("version to build (uses pyproject.toml if not specified)")
        ] = "",
    ) -> dagger.Directory:
        """Returns build artifacts including dist and cached OpenAPI specs.

        The returned directory contains:
        - dist/: Source distribution and wheel
        - .cache/: Cached OpenAPI specs (for GitHub Actions caching)

        Version is determined by the workflow:
        - PR merges: clean semver (e.g., 0.1.3)
        - API triggers: semver.date.time (e.g., 0.1.3.20251219.1553)
        - QA builds: semver.date.timerc0 (e.g., 0.1.3.20251219.1553rc0)
        """
        builder = self.build_container(source).with_env_variable(
            "SATVU_SDK_USE_QA", "1" if is_qa else "0"
        )

        # Forward selective spec fetching env vars from host
        if triggered_api := os.environ.get("SATVU_TRIGGERED_API"):
            builder = builder.with_env_variable("SATVU_TRIGGERED_API", triggered_api)
        if spec_env := os.environ.get("SATVU_SPEC_ENV"):
            builder = builder.with_env_variable("SATVU_SPEC_ENV", spec_env)

        # Note: SATVU_GENERATE_TESTS is intentionally NOT set here.
        # Release builds skip test generation since tests are excluded from the wheel.
        # Test generation is only enabled in test() and test_api() functions.

        # If version provided, update pyproject.toml
        if version:
            pyproject_raw = await source.file("pyproject.toml").contents()
            pyproject_parsed = toml.loads(pyproject_raw)
            pyproject_parsed["project"]["version"] = version
            builder = builder.with_new_file(
                "/src/pyproject.toml", toml.dumps(pyproject_parsed)
            )

        built = builder.with_exec(["uv", "build"])

        # Return composite directory with both dist and cache
        # This allows GitHub Actions to cache the OpenAPI specs for future runs
        return (
            dag.directory()
            .with_directory("dist", built.directory("/src/dist"))
            .with_directory(".cache", built.directory("/src/.cache"))
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

        builder = self.build_container(
            source, python_version=python_version, install_deps=True
        )

        # Forward selective spec fetching env vars from host
        if triggered_api := os.environ.get("SATVU_TRIGGERED_API"):
            builder = builder.with_env_variable("SATVU_TRIGGERED_API", triggered_api)
        if spec_env := os.environ.get("SATVU_SPEC_ENV"):
            builder = builder.with_env_variable("SATVU_SPEC_ENV", spec_env)

        # Enable test generation for test runs (tests are needed to run pytest)
        builder = builder.with_env_variable("SATVU_GENERATE_TESTS", "1")

        run = (
            await builder
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
    async def test_api(
        self,
        source: SOURCE,
        api: Annotated[
            str,
            dagger.Doc(
                "API service to test: catalog, cos, id, otm, policy, reseller, wallet"
            ),
        ],
        python_version: Annotated[
            str, dagger.Doc("Python version to test against")
        ] = DEFAULT_PYTHON_VERSION,
    ) -> dagger.Directory:
        """Runs core tests plus tests for a specific API service.

        This is optimized for workflow_call triggers where only one API changed.
        Core tests (auth, http, streaming, parsing) always run to verify the
        SDK foundation. API-specific tests only run for the specified service.

        For running all tests, use the `test` function instead.
        """
        # Valid API names
        valid_apis = {"catalog", "cos", "id", "otm", "policy", "reseller", "wallet"}

        if not api:
            raise ValueError(
                "API parameter is required. Use `test` function for all tests."
            )

        if api not in valid_apis:
            raise ValueError(
                f"Invalid API '{api}'. Must be one of: {', '.join(sorted(valid_apis))}"
            )

        # Core test paths (always run)
        core_test_paths = [
            "src/satvu/auth_test.py",
            "src/satvu/core_test.py",
            "src/satvu/core_streaming_test.py",
            "src/satvu/core_retry_test.py",
            "src/satvu/http/",
            "src/satvu/shared/",
        ]

        # Core tests + specific API tests
        test_paths = core_test_paths + [f"src/satvu/services/{api}/"]

        pytest_args = [
            "pytest",
            "--junitxml=/tmp/pytest.xml",
            "-n=auto",
            "-v",
        ] + test_paths

        builder = self.build_container(
            source, python_version=python_version, install_deps=True
        )

        # Forward selective spec fetching env vars from host
        if triggered_api := os.environ.get("SATVU_TRIGGERED_API"):
            builder = builder.with_env_variable("SATVU_TRIGGERED_API", triggered_api)
        if spec_env := os.environ.get("SATVU_SPEC_ENV"):
            builder = builder.with_env_variable("SATVU_SPEC_ENV", spec_env)

        # Enable test generation for test runs (tests are needed to run pytest)
        builder = builder.with_env_variable("SATVU_GENERATE_TESTS", "1")

        run = (
            await builder.with_exec(["python", "--version"])
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
