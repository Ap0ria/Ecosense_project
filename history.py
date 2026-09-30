"""CSV storage, display and search functions."""

import csv
from pathlib import Path
from models import WasteItem

DATA_FILE = Path(__file__).resolve().parent / "data" / "waste_records.csv"
FIELDNAMES = [
    "item_name", "material", "condition", "quantity",
    "category", "status", "recommendation"
]


def _ensure_file() -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()


def save_record(item: WasteItem) -> None:
    _ensure_file()
    with DATA_FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writerow({
            "item_name": item.item_name,
            "material": item.material,
            "condition": item.condition,
            "quantity": item.quantity,
            "category": item.category,
            "status": item.status,
            "recommendation": item.recommendation,
        })


def load_records() -> list[dict]:
    _ensure_file()
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def show_history() -> None:
    records = load_records()
    print("\nWASTE HISTORY")
    print("-" * 120)
    if not records:
        print("No records found.")
        return

    for i, record in enumerate(records, start=1):
        print(
            f"{i:>3}. {record['item_name']:<18} "
            f"{record['material']:<10} {record['condition']:<9} "
            f"{record['quantity']:<4} {record['category']:<17} "
            f"{record['status']}"
        )


def search_records(query: str) -> list[dict]:
    query = query.strip().lower()
    records = load_records()
    matches = [
        r for r in records
        if query in r["item_name"].lower() or query in r["material"].lower()
    ]

    print("\nSEARCH RESULTS")
    print("-" * 90)
    if not matches:
        print("No matching record found.")
        return []

    for r in matches:
        print(
            f"{r['item_name']} | {r['material']} | {r['condition']} | "
            f"{r['quantity']} | {r['category']} | {r['status']}"
        )
    return matches
