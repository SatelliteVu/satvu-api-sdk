#!/bin/sh

set -eo pipefail

uv sync
uv run pre-commit install
