from attacks.prompt_injection import PROMPT_INJECTION_ATTACKS
from attacks.advanced_prompt_injection import (
    ADVANCED_PROMPT_INJECTION_ATTACKS
)
from attacks.jailbreak import JAILBREAK_ATTACKS



from scoring.prompt_injection_scorer import evaluate_attack

from targets.banking_assistant import BANKING_SYSTEM_PROMPT
from targets.hr_assistant import HR_SYSTEM_PROMPT
from targets.customer_support_assistant import (
    CUSTOMER_SUPPORT_SYSTEM_PROMPT
)

from engines.assessment_engine import AssessmentEngine


class AttackRunner:

    def __init__(self, provider):

        self.provider = provider

        self.assessment_engine = (
            AssessmentEngine()
        )

    def run_attack_set(self, attacks, system_prompt):

        results = []

        for attack in attacks:

            response = self.provider.send_prompt(
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

    def run_jailbreak_test(self):

        return self.run_attack_set(
            JAILBREAK_ATTACKS,
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
    
    def assess_target(
    self,
    target_name,
    system_prompt
    ):

        from models.attack_registry import ATTACK_REGISTRY

        categories = {}

        for category_name, category_data in ATTACK_REGISTRY.items():

            assessment = self.run_attack_set(
                category_data["attacks"],
                system_prompt
            )

            assessment["owasp"] = (category_data["owasp"].value)

            categories[category_name] = assessment

        return self.assessment_engine.create_assessment(
            target_name,
            categories
        )

    

    def assess_banking_assistant(self):

        return self.assess_target(
            "banking_assistant",
            BANKING_SYSTEM_PROMPT
        )

    def assess_hr_assistant(self):

        return self.assess_target(
            "hr_assistant",
            HR_SYSTEM_PROMPT
        )

    def assess_customer_support_assistant(self):

        return self.assess_target(
            "customer_support_assistant",
            CUSTOMER_SUPPORT_SYSTEM_PROMPT
        )