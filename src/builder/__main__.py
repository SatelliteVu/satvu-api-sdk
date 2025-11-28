from argparse import ArgumentParser

from builder.build import build
from builder.config import CMD_ARGS

parser = ArgumentParser(__package__, description="OpenAPI SDK builder")
parser.add_argument("api", choices=CMD_ARGS.keys())
parser.add_argument("--cached", action="store_true", default=False)

args = parser.parse_args()

build(api_id=args.api, use_cached=args.cached)
