#!/usr/bin/env python3
"""Check that every KB article has the required sections and metadata. Read-only."""
import glob
import os
import re
import sys

REQUIRED_SECTIONS = ["Symptom", "Cause", "Resolution", "How to verify", "If this does not work"]
REQUIRED_FIELDS = ["Applies to", "Audience", "Last reviewed"]


def lint(path):
    text = open(path, encoding="utf-8").read()
    problems = []
    if not re.match(r"# KB-\d{4}: .+", text):
        problems.append("title must look like '# KB-0000: Title'")
    for s in REQUIRED_SECTIONS:
        if not re.search(rf"^## {re.escape(s)}\s*$", text, re.M):
            problems.append(f"missing section '{s}'")
    for f in REQUIRED_FIELDS:
        if f"| {f} |" not in text:
            problems.append(f"missing field '{f}'")
    res = re.search(r"## Resolution\n(.*?)(?=\n## )", text, re.S)
    if res and len(re.findall(r"^\d+\. ", res.group(1), re.M)) < 3:
        problems.append("Resolution needs at least 3 numbered steps")
    if re.search(r"(?i)password\s*(is|:|=)\s*\w+", text):
        problems.append("article appears to contain a password")
    return problems


def main(root):
    files = sorted(glob.glob(os.path.join(root, "articles", "kb-*.md")))
    bad = 0
    for f in files:
        for p in lint(f):
            bad += 1
            print(f"{os.path.basename(f)}: {p}")
    print(f"{len(files)} articles checked, {bad} problem(s)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
