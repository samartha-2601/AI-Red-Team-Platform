class ComparisonEngine:

    def compare(
        self,
        openai_result,
        ollama_result
    ):

        openai_score = (
            openai_result["overall_score"]
        )

        ollama_score = (
            ollama_result["overall_score"]
        )

        if openai_score < ollama_score:

            more_secure = "openai"

        elif ollama_score < openai_score:

            more_secure = "ollama"

        else:

            more_secure = "tie"

        return {

            "openai": {
                "overall_score":
                    openai_score,

                "overall_rating":
                    openai_result[
                        "overall_rating"
                    ]
            },

            "ollama": {
                "overall_score":
                    ollama_score,

                "overall_rating":
                    ollama_result[
                        "overall_rating"
                    ]
            },

            "comparison": {

                "more_secure_model":
                    more_secure,

                "score_difference":
                    abs(
                        openai_score -
                        ollama_score
                    )
            }
        }