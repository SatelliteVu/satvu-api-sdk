# Release Process

This document describes how releases are managed for the SatVu API SDK.

## Versioning

The SDK uses [semantic versioning](https://semver.org/) with automated releases via [semantic-release](https://github.com/semantic-release/semantic-release).

| Version Bump              | When             | Example                                |
| ------------------------- | ---------------- | -------------------------------------- |
| **Major** (1.0.0 → 2.0.0) | Breaking changes | Removed methods, changed return types  |
| **Minor** (1.0.0 → 1.1.0) | New features     | New endpoints, new optional parameters |
| **Patch** (1.0.0 → 1.0.1) | Bug fixes        | Fixes, documentation updates           |

## Conventional Commits

Version bumps are determined automatically from commit messages using [conventional commits](https://www.conventionalcommits.org/):

```
fix(auth): handle token refresh edge case     → Patch
feat(catalog): add search endpoint            → Minor
feat(http)!: change adapter interface         → Major (note the !)
```

## Release Flow

1. **PR merged to main** → Tests run → Release created automatically
2. **Version determined** from commit messages since last release
3. **Published to PyPI** via trusted publishing (OIDC)
4. **GitHub Release** created with changelog

## Concurrency

When multiple commits land in quick succession:

- New commits **cancel in-progress** release workflows
- The next workflow **picks up all commits** since the last release tag
- No commits are lost - they're batched into the next release

This ensures releases always reflect the latest state of `main`.

## Changelog

The [CHANGELOG.md](./CHANGELOG.md) is automatically generated from commit messages. Each release includes:

- Grouped changes by type (Features, Bug Fixes, Breaking Changes)
- Links to commits and version comparisons

## Contributing

When contributing, use conventional commit messages so your changes appear correctly in the changelog:

```bash
git commit -m "feat(core): add retry logic for transient failures"
git commit -m "fix(auth): correct token expiration check"
git commit -m "docs: update installation instructions"
```

See [CONTRIBUTING.md](./CONTRIBUTING.md) for full contribution guidelines.
