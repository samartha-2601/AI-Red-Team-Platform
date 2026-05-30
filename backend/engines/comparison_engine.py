class ComparisonEngine:

    def calculate_category_score(
        self,
        category_result
    ):

        total_attacks = (
            category_result["total_attacks"]
        )

        successful_attacks = (
            category_result[
                "successful_attacks"
            ]
        )

        if total_attacks == 0:
            return 0

        return round(
            (
                successful_attacks
                / total_attacks
            ) * 100,
            2
        )

    def compare(
        self,
        result1,
        result2,
        provider1="provider1",
        provider2="provider2"
    ):

        score1 = result1[
            "overall_score"
        ]

        score2 = result2[
            "overall_score"
        ]

        if score1 < score2:

            winner = provider1

        elif score2 < score1:

            winner = provider2

        else:

            winner = "tie"

        category_comparison = {}

        for category_name in (
            result1["categories"]
        ):

            category1 = (
                result1["categories"]
                [category_name]
            )

            category2 = (
                result2["categories"]
                [category_name]
            )

            category_comparison[
                category_name
            ] = {

                provider1:
                    self
                    .calculate_category_score(
                        category1
                    ),

                provider2:
                    self
                    .calculate_category_score(
                        category2
                    ),

                "owasp":
                    category1["owasp"]
            }

        return {

            "target":
                result1["target"],

            "overall_comparison": {

                provider1: {
                    "score":
                        score1,

                    "rating":
                        result1[
                            "overall_rating"
                        ]
                },

                provider2: {
                    "score":
                        score2,

                    "rating":
                        result2[
                            "overall_rating"
                        ]
                },

                "winner":
                    winner,

                "score_difference":
                    abs(
                        score1 - score2
                    )
            },

            "category_comparison":
                category_comparison
        }