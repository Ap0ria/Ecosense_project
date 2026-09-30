"""Waste material classification for EcoSense."""

ALLOWED_MATERIALS = (
    "plastic",
    "paper",
    "glass",
    "metal",
    "organic",
    "e-waste",
)

CATEGORY_MAP = {
    "plastic": "Plastic Waste",
    "paper": "Paper Waste",
    "glass": "Glass Waste",
    "metal": "Metal Waste",
    "organic": "Organic Waste",
    "e-waste": "E-Waste",
}


def classify_waste(material: str) -> str:
    """Return the waste category for a supported material."""
    return CATEGORY_MAP.get(material.strip().lower(), "Unknown Waste")


def is_valid_material(material: str) -> bool:
    """Return True when material is one of the supported materials."""
    return material.strip().lower() in ALLOWED_MATERIALS
