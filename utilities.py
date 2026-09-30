"""General utility and status functions."""

from classifier import ALLOWED_MATERIALS


def print_header() -> None:
    print("\n" + "=" * 72)
    print(" ECO SENSE - SMART WASTE CLASSIFICATION & RECORD SYSTEM")
    print("=" * 72)


def print_materials() -> None:
    print("Supported materials:", ", ".join(ALLOWED_MATERIALS))


def get_status(material: str, condition: str) -> str:
    material = material.strip().lower()
    condition = condition.strip().lower()

    if material == "organic":
        return "Biodegradable"
    if material == "e-waste":
        return "Special Disposal Required"
    if condition == "clean":
        return "Recyclable"
    if condition == "dirty":
        return "Needs Cleaning"
    if condition == "damaged":
        return "Check Recycling Facility"
    return "Unknown"
