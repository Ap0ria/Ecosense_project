"""Statistics calculated from stored waste records."""

import numpy as np
from history import load_records


def get_statistics() -> dict:
    records = load_records()
    quantities = [int(r["quantity"]) for r in records]

    if not quantities:
        return {
            "records": 0, "total": 0, "average": 0,
            "minimum": 0, "maximum": 0, "categories": 0
        }

    values = np.array(quantities)
    categories = {r["category"] for r in records}

    return {
        "records": len(records),
        "total": int(values.sum()),
        "average": float(values.mean()),
        "minimum": int(values.min()),
        "maximum": int(values.max()),
        "categories": len(categories),
    }


def show_statistics() -> None:
    stats = get_statistics()
    print("\nWASTE STATISTICS")
    print("-" * 45)
    print(f"Total records      : {stats['records']}")
    print(f"Total quantity     : {stats['total']}")
    print(f"Average quantity   : {stats['average']:.2f}")
    print(f"Minimum quantity   : {stats['minimum']}")
    print(f"Maximum quantity   : {stats['maximum']}")
    print(f"Categories recorded: {stats['categories']}")
