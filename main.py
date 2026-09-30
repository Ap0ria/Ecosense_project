"""EcoSense main program."""

from classifier import classify_waste, is_valid_material, ALLOWED_MATERIALS
from validation import validate_item_name, get_quantity, get_condition
from recommendation import get_recommendation, show_recommendations
from models import WasteItem
from history import save_record, show_history, search_records
from statistics import show_statistics
from utilities import print_header, print_materials, get_status


def classify_waste_feature() -> None:
    print("\nCLASSIFY WASTE")
    print("-" * 45)

    item_name = input("Item name: ").strip()
    if not validate_item_name(item_name):
        print("Item name cannot be empty.")
        return

    material = input("Material: ").strip().lower()
    if not is_valid_material(material):
        print("Invalid material.")
        print_materials()
        return

    condition = get_condition()
    quantity = get_quantity()

    category = classify_waste(material)
    status = get_status(material, condition)
    recommendation = get_recommendation(material)

    item = WasteItem(
        item_name=item_name,
        material=material,
        condition=condition,
        quantity=quantity,
        category=category,
        status=status,
        recommendation=recommendation,
    )
    save_record(item)
    item.display()
    print("\nRecord saved successfully.")


def menu() -> None:
    while True:
        print_header()
        print("1. Classify Waste")
        print("2. View Waste History")
        print("3. Search Records")
        print("4. View Statistics")
        print("5. View Recycling Recommendations")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            classify_waste_feature()
        elif choice == "2":
            show_history()
        elif choice == "3":
            query = input("Search item name or material: ")
            search_records(query)
        elif choice == "4":
            show_statistics()
        elif choice == "5":
            show_recommendations()
        elif choice == "6":
            print("Thank you for using EcoSense.")
            break
        else:
            print("Invalid choice.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    menu()
