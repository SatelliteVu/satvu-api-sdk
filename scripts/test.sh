#!/bin/sh

set -eo pipefail

uv run pytest $@
