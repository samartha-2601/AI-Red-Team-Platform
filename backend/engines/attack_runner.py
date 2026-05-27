from attacks.prompt_injection import PROMPT_INJECTION_ATTACKS

from providers.openai_provider import send_prompt

from scoring.prompt_injection_scorer import evaluate_attack

from targets.banking_assistant import BANKING_SYSTEM_PROMPT
from targets.hr_assistant import HR_SYSTEM_PROMPT
from targets.customer_support_assistant import (
    CUSTOMER_SUPPORT_SYSTEM_PROMPT
)


class AttackRunner:

    def run_prompt_injection_test(self, system_prompt):

        results = []

        for attack in PROMPT_INJECTION_ATTACKS:

            response = send_prompt(
                system_prompt,
                attack
            )

            evaluation = evaluate_attack(response)

            results.append({
                "attack": attack,
                "response": response,
                "success": evaluation["success"],
                "risk": evaluation["risk"]
            })

        successful_attacks = sum(
            1 for result in results
            if result["success"]
        )

        return {
            "total_attacks": len(results),
            "successful_attacks": successful_attacks,
            "failed_attacks": len(results) - successful_attacks
        }

    def run_all_targets(self):

        return {
            "banking_assistant":
                self.run_prompt_injection_test(
                    BANKING_SYSTEM_PROMPT
                ),

            "hr_assistant":
                self.run_prompt_injection_test(
                    HR_SYSTEM_PROMPT
                ),

            "customer_support_assistant":
                self.run_prompt_injection_test(
                    CUSTOMER_SUPPORT_SYSTEM_PROMPT
                )
        }