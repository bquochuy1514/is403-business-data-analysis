"""Print a reproducible first profile of the original IS403 dataset.

Run from the repository root with: python src/audit_dataset.py
Only Python's standard library is required. The original CSV is never modified.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from statistics import median


ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "raw" / "online_shoppers_intention.csv"
NUMERIC_COLUMNS = (
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues",
    "SpecialDay",
)
MISSING_MARKERS = {"", "?"}


def main() -> None:
    with DATASET.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        columns = reader.fieldnames or []
        rows = list(reader)

    if not rows or "Revenue" not in columns:
        raise ValueError("Dataset is empty or lacks the Revenue label")

    labels = Counter(row["Revenue"] for row in rows)
    duplicate_count = len(rows) - len(
        {tuple(row[column] for column in columns) for row in rows}
    )

    print(f"File: {DATASET.relative_to(ROOT)}")
    print(f"Sessions: {len(rows):,}; input columns: {len(columns) - 1}; total columns: {len(columns)}")
    print(f"Revenue counts: {dict(labels)}")
    print(f"Exact duplicate rows (including Revenue): {duplicate_count}")
    print("\nColumn profile:")

    for column in columns:
        values = [row[column].strip() for row in rows]
        missing = sum(value in MISSING_MARKERS for value in values)
        unique = len(set(values))

        if column in NUMERIC_COLUMNS:
            numbers = [float(value) for value in values if value not in MISSING_MARKERS]
            print(
                f"- {column}: numeric; missing={missing}; unique={unique}; "
                f"min={min(numbers):.4g}; median={median(numbers):.4g}; "
                f"max={max(numbers):.4g}; zero={sum(number == 0 for number in numbers)}"
            )
        else:
            top = ", ".join(
                f"{value} ({count})" for value, count in Counter(values).most_common(5)
            )
            print(
                f"- {column}: categorical; missing={missing}; "
                f"unique={unique}; most common={top}"
            )

    print("\nSelected descriptive comparisons with Revenue (not causal effects):")
    for column in ("ProductRelated", "ProductRelated_Duration"):
        purchased = [
            float(row[column]) for row in rows if row["Revenue"] == "TRUE"
        ]
        not_purchased = [
            float(row[column]) for row in rows if row["Revenue"] == "FALSE"
        ]
        print(
            f"- {column} median: TRUE={median(purchased):.3f}; "
            f"FALSE={median(not_purchased):.3f}"
        )

    for column in ("PageValues", "VisitorType"):
        groups: dict[str, list[int]] = {}
        for row in rows:
            group = (
                ">0" if float(row[column]) > 0 else "=0"
            ) if column == "PageValues" else row[column]
            counts = groups.setdefault(group, [0, 0])
            counts[0] += 1
            counts[1] += row["Revenue"] == "TRUE"
        for group, (total, purchased) in groups.items():
            print(
                f"- {column} {group}: {purchased}/{total} TRUE "
                f"({100 * purchased / total:.2f}%)"
            )


if __name__ == "__main__":
    main()
