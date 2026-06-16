from __future__ import annotations

import argparse
import json

from plantspeak.devices import build_capability_map, collect_dev_mode_snapshot, default_dev_board_profile
from plantspeak.icd import build_icd_capabilities, capability_summary
from plantspeak.requirements import load_issue_links, load_requirements


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PlantSpeak dev-mode ICD harness.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("list-requirements", help="List implemented software requirements.")
    subparsers.add_parser("trace", help="Print requirement-to-issue and verification trace.")
    subparsers.add_parser("capabilities", help="Print ICD capability summary as JSON.")
    measure = subparsers.add_parser("measure", help="Collect a sensor snapshot.")
    measure.add_argument("--dev-mode", action="store_true", help="Use canned data for unavailable external I2C devices.")
    self_test = subparsers.add_parser("self-test", help="Run deterministic dev-board checks.")
    self_test.add_argument("--dev-mode", action="store_true", help="Use dev-board profile and canned data.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "list-requirements":
        for requirement in load_requirements():
            print(f"{requirement['id']}: {requirement['statement']}")
        return 0
    if args.command == "trace":
        issues = {issue["requirement_ids"][0]: issue for issue in load_issue_links()}
        for capability in build_icd_capabilities():
            issue = issues.get(capability.requirement_id, {})
            print(
                f"{capability.requirement_id} -> #{issue.get('number', 'local')} -> "
                f"{capability.command} -> {capability.verification_method}"
            )
        return 0
    if args.command == "capabilities":
        print(json.dumps(capability_summary(), indent=2, sort_keys=True))
        return 0
    if args.command == "measure":
        if not args.dev_mode:
            raise SystemExit("hardware mode is not implemented yet; rerun with --dev-mode")
        print(json.dumps(collect_dev_mode_snapshot().to_dict(), indent=2, sort_keys=True))
        return 0
    if args.command == "self-test":
        if not args.dev_mode:
            raise SystemExit("self-test currently requires --dev-mode")
        profile = default_dev_board_profile()
        capability_map = build_capability_map(profile)
        checks = {
            "external_i2c_uses_canned_data": capability_map["SW-013"] == "canned-data",
            "button_wake_deferred": capability_map["SW-014"] == "dev-board-unavailable",
            "icd_capabilities_present": len(build_icd_capabilities()) == len(load_requirements()),
        }
        print(json.dumps(checks, indent=2, sort_keys=True))
        return 0 if all(checks.values()) else 1
    raise ValueError(f"unsupported command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
