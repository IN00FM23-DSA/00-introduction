"""
Scoring script — reads report.xml (produced by `pytest --junitxml=report.xml`)
and points.json, awards partial credit per exercise, and writes a summary
to $GITHUB_STEP_SUMMARY (falls back to stdout when that's unset).

Used by both the Tier-1 (per-push) GitHub Actions workflow and by
04-collect-grades.ps1's authoritative run — same rule, so the two scores
always agree.
"""

import json
import os
import xml.etree.ElementTree as ET

POINTS_FILE = "points.json"
REPORT_FILE = "report.xml"


def main():
    with open(POINTS_FILE, encoding="utf-8") as f:
        points = json.load(f)

    # filename -> [passed, total]
    counts = {name: [0, 0] for name in points}

    try:
        tree = ET.parse(REPORT_FILE)
        for case in tree.getroot().iter("testcase"):
            module = case.get("classname", "").split(".", 1)[0]
            filename = f"{module}.py"
            if filename not in counts:
                continue
            counts[filename][1] += 1
            failed = case.find("failure") is not None or case.find("error") is not None
            skipped = case.find("skipped") is not None
            if not failed and not skipped:
                counts[filename][0] += 1
    except (FileNotFoundError, ET.ParseError):
        pass  # no report (e.g. a collection error) -> every exercise stays 0/0

    total_award = 0
    total_possible = 0
    rows = []
    for filename, max_points in points.items():
        passed, total = counts[filename]
        # round-half-up via integer arithmetic: round(max_points * passed / total)
        awarded = 0 if total == 0 else (max_points * passed * 2 + total) // (total * 2)
        total_award += awarded
        total_possible += max_points
        rows.append((filename, passed, total, awarded, max_points))

    write_summary(rows, total_award, total_possible)


def write_summary(rows, total_award, total_possible):
    lines = [
        f"## Score: {total_award}/{total_possible} points",
        "",
        "| Exercise | Tests passed | Points |",
        "|---|---|---|",
    ]
    for filename, passed, total, awarded, max_points in rows:
        lines.append(f"| `{filename}` | {passed}/{total} | {awarded}/{max_points} |")
    summary = "\n".join(lines) + "\n"

    print(summary)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8") as f:
            f.write(summary)


if __name__ == "__main__":
    main()
