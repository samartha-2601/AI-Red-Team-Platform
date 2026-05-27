from attacks.prompt_injection import PROMPT_INJECTION_ATTACKS
from attacks.advanced_prompt_injection import (
    ADVANCED_PROMPT_INJECTION_ATTACKS
)

from providers.openai_provider import send_prompt

from scoring.prompt_injection_scorer import evaluate_attack

from targets.banking_assistant import BANKING_SYSTEM_PROMPT
from targets.hr_assistant import HR_SYSTEM_PROMPT
from targets.customer_support_assistant import (
    CUSTOMER_SUPPORT_SYSTEM_PROMPT
)

from attacks.jailbreak import JAILBREAK_ATTACKS


class AttackRunner:

    def run_attack_set(self, attacks, system_prompt):

        results = []

        for attack in attacks:

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
            "failed_attacks": len(results) - successful_attacks,
            "results": results
        }

    def run_prompt_injection_test(self):

        return self.run_attack_set(
            PROMPT_INJECTION_ATTACKS,
            BANKING_SYSTEM_PROMPT
        )

    def run_advanced_prompt_injection_test(self):

        return self.run_attack_set(
            ADVANCED_PROMPT_INJECTION_ATTACKS,
            BANKING_SYSTEM_PROMPT
        )

    def run_all_targets(self):

        return {
            "banking_assistant":
                self.run_attack_set(
                    PROMPT_INJECTION_ATTACKS,
                    BANKING_SYSTEM_PROMPT
                ),

            "hr_assistant":
                self.run_attack_set(
                    PROMPT_INJECTION_ATTACKS,
                    HR_SYSTEM_PROMPT
                ),

            "customer_support_assistant":
                self.run_attack_set(
                    PROMPT_INJECTION_ATTACKS,
                    CUSTOMER_SUPPORT_SYSTEM_PROMPT
                )
        }
    
    def run_jailbreak_test(self):

        return self.run_attack_set(
            JAILBREAK_ATTACKS,
            BANKING_SYSTEM_PROMPT
        )
