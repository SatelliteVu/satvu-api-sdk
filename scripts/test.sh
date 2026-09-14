#!/bin/bash

set -eo pipefail

uv run pytest $@
