# [0.5.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.4.0...v0.5.0) (2026-01-20)


### Features

* **builder:** add hypothesis example caching for faster tests

# [0.4.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.3.1...v0.4.0) (2026-01-15)


### Features

* **builder:** add conditional test generation via SATVU_GENERATE_TESTS
* **build:** exclude tests and builder from wheel distribution

## [0.3.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.3.0...v0.3.1) (2026-01-14)


### Bug Fixes

* **auth:** handle malformed JWTs in expiration check
* **auth:** make MemoryCache instance-level to prevent token leakage
* **misc:** export OpenAPI spec cache from Dagger container
* **release:** set git identity before creating annotated tag

# [0.3.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.2.0...v0.3.0) (2026-01-07)

## [0.3.0.20260113.1752] - 2026-01-13

### feat(reseller): update API descriptions

#### Description Updates
* 1 description(s) modified


## [0.3.0.20260113.1724] - 2026-01-13

### feat(id): update API descriptions

#### Description Updates
* 4 description(s) modified


## [0.3.0.20260112.1536] - 2026-01-12

### feat(policy): update API descriptions

#### Description Updates
* 6 description(s) modified


## [0.3.0.20260112.1243] - 2026-01-12

### feat(otm): update API descriptions

#### Description Updates
* 2 description(s) modified



### Bug Fixes

* handle pook mock responses in stdlib adapter streaming
* **misc:** include scope in changelog entries
* **release:** anchor version grep to start of line


### Features

* add Jinja2 templates for streaming download tests
* integrate streaming test generation into build

# [0.2.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.1...v0.2.0) (2025-12-19)

### Features

- **core:** rename package and module to satvu
- **release:** implement timestamp versioning for API-triggered releases

## [0.1.1](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.1.0...v0.1.1) (2025-12-19)

### Bug Fixes

- **core:** add docstring for SatVuSDK.__init__

# [0.1.0](https://github.com/SatelliteVu/satvu-api-sdk/compare/v0.0.0...v0.1.0) (2025-12-19)

### Features

- **core:** add docstring for the SatVuSDK class
