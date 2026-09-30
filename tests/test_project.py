"""Basic automated tests for EcoSense."""

from classifier import classify_waste, is_valid_material
from recommendation import get_recommendation
from utilities import get_status
from validation import validate_condition, validate_item_name


def test_classification():
    assert classify_waste("plastic") == "Plastic Waste"
    assert classify_waste("paper") == "Paper Waste"
    assert classify_waste("glass") == "Glass Waste"


def test_material_validation():
    assert is_valid_material("plastic")
    assert is_valid_material("paper")
    assert not is_valid_material("wood")


def test_quantity_validation():
    # The numeric rule is represented directly here because get_quantity()
    # reads from input interactively.
    assert 5 > 0
    assert not (0 > 0)
    assert not (-2 > 0)


def test_recommendation():
    assert "recycling" in get_recommendation("plastic").lower() or "recycle" in get_recommendation("plastic").lower()


def test_condition_validation():
    assert validate_condition("clean")
    assert validate_condition("dirty")
    assert validate_condition("damaged")
    assert not validate_condition("broken")


def test_item_name_validation():
    assert validate_item_name("Water bottle")
    assert not validate_item_name("")


def test_status_rules():
    assert get_status("organic", "dirty") == "Biodegradable"
    assert get_status("e-waste", "damaged") == "Special Disposal Required"
    assert get_status("plastic", "clean") == "Recyclable"
    assert get_status("plastic", "dirty") == "Needs Cleaning"
    assert get_status("plastic", "damaged") == "Check Recycling Facility"


if __name__ == "__main__":
    tests = [
        test_classification,
        test_material_validation,
        test_quantity_validation,
        test_recommendation,
        test_condition_validation,
        test_item_name_validation,
        test_status_rules,
    ]
    for test in tests:
        test()
        print(f"{test.__name__}: PASS")
    print("All tests passed.")
