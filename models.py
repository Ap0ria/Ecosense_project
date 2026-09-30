"""Data model for one EcoSense waste record."""

from dataclasses import dataclass


@dataclass
class WasteItem:
    item_name: str
    material: str
    condition: str
    quantity: int
    category: str
    status: str
    recommendation: str

    def display(self) -> None:
        print("\nWaste Item")
        print("-" * 45)
        print(f"Item          : {self.item_name}")
        print(f"Material      : {self.material}")
        print(f"Condition     : {self.condition}")
        print(f"Quantity      : {self.quantity}")
        print(f"Category      : {self.category}")
        print(f"Status        : {self.status}")
        print(f"Recommendation: {self.recommendation}")
