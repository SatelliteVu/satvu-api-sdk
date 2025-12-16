# Contributing

Thank you for your interest in contributing to the SatVu API SDK!

## Development Setup

### Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

### Getting Started

1. Clone the repository:

```bash
git clone https://github.com/satellitevu/satvu-api-sdk.git
cd satvu-api-sdk
```

2. Run the bootstrap script to install dependencies and set up pre-commit hooks:

```bash
./scripts/bootstrap.sh
```

### Running Tests

```bash
./scripts/test.sh
```

Pass pytest options directly:

```bash
./scripts/test.sh -v                    # Verbose output
./scripts/test.sh -k test_name          # Run specific tests
./scripts/test.sh --all-backends        # Test all HTTP backends
```

### Running Linters

```bash
./scripts/lint.sh
```

This runs all pre-commit hooks including Ruff, Bandit, and type checking.

## SDK Generation

The SDK is auto-generated from OpenAPI specifications. To regenerate:

```bash
# Regenerate all APIs (canonical method)
uv build

# Regenerate specific API (development only)
uv run python -m builder <API_NAME>

# Use cached specs instead of fetching fresh ones
uv run python -m builder <API_NAME> --cached
```

Available API names: `catalog`, `cos`, `id`, `policy`, `otm`, `reseller`, `wallet`

## Project Structure

```
satvu-api-sdk/
├── src/
│   ├── satvu_api_sdk/          # Main SDK package
│   │   ├── sdk.py              # SatVuSDK entry point
│   │   ├── core.py             # SDKClient base class
│   │   ├── auth.py             # Authentication
│   │   ├── result.py           # Result type
│   │   ├── http/               # HTTP adapters
│   │   ├── shared/             # Shared utilities
│   │   └── services/           # Generated API services
│   │       ├── catalog/
│   │       ├── cos/
│   │       └── ...
│   └── builder/                # SDK generator
├── docs/                       # Documentation
├── examples/                   # Usage examples
└── scripts/                    # Development scripts
```

## CI/CD with Dagger

[Dagger](https://docs.dagger.io) provides portable CI:

```bash
dagger call -v test              # Run pytest suite
dagger call -v lint              # Run linters
dagger call -v test-all          # Test all Python versions
```

## Code Style

- We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting
- Type hints are required for all public APIs
- Tests use pytest with the `*_test.py` naming convention

## Commit Convention

This project uses [Conventional Commits](https://www.conventionalcommits.org/) with strict validation via [Commitizen](https://commitizen-tools.github.io/commitizen/). All commits must follow this format:

```
<type>(<scope>): <subject>
```

### Format Rules

- **type**: Required. The category of change (see below)
- **scope**: Required. The area of the codebase affected (see below)
- **subject**: Required. A short description (max 50 characters)

### Commit Types

| Type       | Description                                           |
| ---------- | ----------------------------------------------------- |
| `feat`     | A new feature                                         |
| `fix`      | A bug fix                                             |
| `docs`     | Documentation only changes                            |
| `style`    | Code style (formatting, whitespace, etc.)             |
| `refactor` | Code change that neither fixes a bug nor adds feature |
| `perf`     | Performance improvement                               |
| `test`     | Adding or updating tests                              |
| `build`    | Build system or external dependencies                 |
| `ci`       | CI/CD configuration changes                           |
| `chore`    | Other changes (maintenance, tooling)                  |
| `revert`   | Revert a previous commit                              |

### Scopes

| Scope     | Description                                      |
| --------- | ------------------------------------------------ |
| `core`    | SDK core (`SDKClient`, base functionality)       |
| `auth`    | Authentication (`AuthService`, tokens)           |
| `http`    | HTTP adapters (httpx, requests, urllib3, stdlib) |
| `builder` | SDK code generator                               |
| `deps`    | Dependencies                                     |
| `docs`    | Documentation                                    |
| `test`    | Test infrastructure                              |
| `misc`    | Miscellaneous changes                            |

**Auto-generated service scopes** (typically reserved for CI/automated commits):

| Scope      | Description          |
| ---------- | -------------------- |
| `catalog`  | Catalog API service  |
| `cos`      | COS API service      |
| `id`       | ID API service       |
| `otm`      | OTM API service      |
| `policy`   | Policy API service   |
| `reseller` | Reseller API service |
| `wallet`   | Wallet API service   |

These service scopes are primarily used by automated processes when regenerating SDK code from updated OpenAPI specifications. Manual commits rarely need these scopes.

### Examples

```bash
# Feature
feat(core): add retry logic for transient errors

# Bug fix
fix(auth): handle token refresh race condition

# Documentation
docs(docs): update API usage examples

# Build/CI
ci(misc): add Python 3.13 to test matrix

# Breaking change (add body)
feat(http): migrate to async-first API

BREAKING CHANGE: All HTTP methods now return coroutines
```

### Using the Interactive Prompt

Run `cz commit` for an interactive commit prompt that guides you through the format:

```bash
uv run cz commit
```

### Validation

Commit messages are validated automatically:

- **Pre-commit hook**: Validates format on every commit
- **Pre-push hook**: Validates all commits on the branch before push

If your commit is rejected, check that:

1. Type is one of the allowed values
2. Scope is one of the allowed values
3. Subject is 50 characters or less
4. Format matches `<type>(<scope>): <subject>`

### Version Bumping

Commits trigger automatic version bumps based on type:

| Type                      | Version Bump |
| ------------------------- | ------------ |
| `feat`                    | Minor        |
| `fix`, `refactor`, `perf` | Patch        |
| `BREAKING CHANGE`         | Major        |

## Pull Requests

1. Create a feature branch from `main`
2. Make your changes
3. Ensure tests pass: `./scripts/test.sh`
4. Ensure linting passes: `./scripts/lint.sh`
5. Submit a pull request

## Testing Guidelines

- Unit tests go alongside the code they test (e.g., `auth_test.py` next to `auth.py`)
- Use `pook` for HTTP mocking
- Use the `is_ok()` / `is_err()` type guards for Result assertions
- Generated service tests are in `services/{api}/api_test.py`

See [docs/testing.md](docs/testing.md) for detailed testing documentation.

## Releases

Releases are automated via [semantic-release](https://github.com/semantic-release/semantic-release). You don't need to manually bump versions or update the changelog.

### How Releases Are Triggered

1. **PR merges to main**: A release is triggered automatically when changes to `src/**/*.py` (excluding test files) are merged. The version bump is determined by conventional commit prefixes in the merged commits.

2. **Upstream API changes**: When an upstream API detects OpenAPI spec changes during deployment, it automatically triggers an SDK release.

### Version Bump Rules

| Commit Prefix                         | Version Bump | Example                                |
| ------------------------------------- | ------------ | -------------------------------------- |
| `fix(scope):`                         | Patch        | `fix(auth): handle token refresh race` |
| `feat(scope):`                        | Minor        | `feat(http): add retry middleware`     |
| `feat(scope)!:` or `BREAKING CHANGE:` | Major        | `feat(core)!: change Result API`       |

### Where Releases Go

| Environment | Published To | Version Format      |
| ----------- | ------------ | ------------------- |
| Production  | PyPI         | `1.2.3`             |
| QA          | CodeArtifact | `1.2.3.dev24121642` |

## Questions?

Open an [issue](https://github.com/satellitevu/satvu-api-sdk/issues) for bugs and feature requests, or start a [discussion](https://github.com/satellitevu/satvu-api-sdk/discussions) for questions.
