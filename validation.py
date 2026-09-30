"""Input validation helpers for EcoSense."""

from classifier import ALLOWED_MATERIALS


def validate_item_name(name: str) -> bool:
    return bool(name and name.strip())


def validate_material(material: str) -> bool:
    return material.strip().lower() in ALLOWED_MATERIALS


def validate_condition(condition: str) -> bool:
    return condition.strip().lower() in ("clean", "dirty", "damaged")


def get_quantity(prompt: str = "Quantity: ") -> int:
    """Keep asking until a positive whole number is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            quantity = int(raw)
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            return quantity
        except ValueError:
            print("Please enter a valid whole number.")


def get_condition() -> str:
    """Keep asking until clean, dirty or damaged is entered."""
    while True:
        value = input("Condition (clean/dirty/damaged): ").strip().lower()
        if validate_condition(value):
            return value
        print("Invalid condition. Please enter clean, dirty or damaged.")
