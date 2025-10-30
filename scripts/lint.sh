#!/bin/sh

set -eo pipefail

uv run pre-commit run --all-files
