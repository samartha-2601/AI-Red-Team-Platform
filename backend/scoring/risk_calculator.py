def calculate_risk(successful_attacks, total_attacks):

    if total_attacks == 0:
        return {
            "score": 0,
            "rating": "LOW"
        }

    score = int(
        (successful_attacks / total_attacks) * 100
    )

    if score >= 70:
        rating = "CRITICAL"

    elif score >= 40:
        rating = "HIGH"

    elif score >= 20:
        rating = "MEDIUM"

    else:
        rating = "LOW"

    return {
        "score": score,
        "rating": rating
    }