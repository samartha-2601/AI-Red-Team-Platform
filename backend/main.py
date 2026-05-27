from fastapi import FastAPI

from attacks.prompt_injection import PROMPT_INJECTION_ATTACKS
from providers.openai_provider import send_prompt
from targets.banking_assistant import BANKING_SYSTEM_PROMPT

from scoring.prompt_injection_scorer import evaluate_attack

app = FastAPI(
    title="AI Red Team Platform",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "AI Red Team Platform API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/run-prompt-injection-test")
def run_prompt_injection_test():

    results = []

    for attack in PROMPT_INJECTION_ATTACKS:

        response = send_prompt(
            BANKING_SYSTEM_PROMPT,
            attack
        )

        evaluation = evaluate_attack(response)

        results.append({
            "attack": attack,
            "response": response,
            "success": evaluation["success"],
            "risk": evaluation["risk"]
        })

    successful_attacks = sum(1 for result in results if result["success"])

    return {
        "summary": {
            "total_attacks": len(results),
            "successful_attacks": successful_attacks,
            "failed_attacks": len(results) - successful_attacks
        },
        "results": results
    }