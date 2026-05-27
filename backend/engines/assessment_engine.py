from scoring.risk_calculator import calculate_risk


class AssessmentEngine:

    def create_assessment(
        self,
        target_name,
        categories
    ):

        total_successful = sum(
            category["successful_attacks"]
            for category in categories.values()
        )

        total_attacks = sum(
            category["total_attacks"]
            for category in categories.values()
        )

        overall = calculate_risk(
            total_successful,
            total_attacks
        )

        return {
            "target": target_name,
            "categories": categories,
            "overall_score": overall["score"],
            "overall_rating": overall["rating"]
        }