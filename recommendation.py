"""Recycling and disposal recommendations."""

RECOMMENDATIONS = {
    "plastic": "Rinse when appropriate and place clean plastic in the recycling stream.",
    "paper": "Keep paper clean and dry; send it to paper recycling.",
    "glass": "Separate glass from general waste and use a suitable glass collection point.",
    "metal": "Separate metal items and send them to an appropriate metal recycling stream.",
    "organic": "Compost suitable food and garden waste where a composting option is available.",
    "e-waste": "Do not put electronics in ordinary rubbish; use an authorised e-waste collection point.",
}


def get_recommendation(material: str) -> str:
    return RECOMMENDATIONS.get(
        material.strip().lower(),
        "No recommendation is available for this material."
    )


def show_recommendations() -> None:
    print("\nRECYCLING RECOMMENDATIONS")
    print("-" * 72)
    for material, advice in RECOMMENDATIONS.items():
        print(f"{material:10} : {advice}")
