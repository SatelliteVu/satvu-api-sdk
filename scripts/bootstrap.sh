#!/bin/sh

set -eo pipefail

uv sync --all-extras
uv run pre-commit install
