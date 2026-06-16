from __future__ import annotations

import argparse
import json
from importlib.resources import files


def load_requirements() -> list[dict[str, object]]:
    data = files("plantspeak.data").joinpath("requirements.json").read_text(encoding="utf-8")
    return json.loads(data)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generated V-model project CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list-requirements", help="List implemented software requirements.")
    subparsers.add_parser("trace", help="Print requirement trace summary.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    requirements = load_requirements()
    if args.command == "list-requirements":
        for requirement in requirements:
            print(f"{requirement['id']}: {requirement['statement']}")
        return 0
    if args.command == "trace":
        for requirement in requirements:
            print(f"{requirement['id']} -> tests planned -> verification pending")
        return 0
    raise ValueError(f"unsupported command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
