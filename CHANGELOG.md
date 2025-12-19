# [0.2.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.1...v0.2.0) (2025-12-19)


### Features

* rename package and module to satvu

Renames the package from satvu-api-sdk to satvu and the module
from satvu_api_sdk to satvu for cleaner imports.

Before: from satvu_api_sdk import SatVuSDK
After:  from satvu import SatVuSDK

Updates all imports, docs, examples, and builder templates.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
* implement timestamp versioning for API-triggered releases

Separates release versioning into two paths:

- Push events (PR merges): semantic-release handles clean semver (e.g., 0.1.3)
  with git tags and GitHub releases
- API triggers: timestamp-based versioning (e.g., 0.1.3.20251219.1553)
  without git tags since generated code isn't committed

QA releases use rc0 suffix (e.g., 0.1.3.20251219.1553rc0)

Changes:
- Update Dagger build_release to accept optional version parameter
- Restructure release workflow with PATH 1 (push) and PATH 2 (workflow_call)
- Add CHANGELOG updates for API-triggered releases without tagging

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

## [0.1.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.0...v0.1.1) (2025-12-19)


### Bug Fixes

* add docstring for SatVuSDK.__init__

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>

# [0.1.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.0.0...v0.1.0) (2025-12-19)


### Features

* add docstring for the SatVuSDK class

# Changelog
