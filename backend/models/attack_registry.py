from attacks.prompt_injection import PROMPT_INJECTION_ATTACKS
from attacks.advanced_prompt_injection import (
    ADVANCED_PROMPT_INJECTION_ATTACKS
)
from attacks.jailbreak import JAILBREAK_ATTACKS

from models.owasp_categories import (
    OWASPLLMCategory
)

from attacks.role_confusion import ROLE_CONFUSION_ATTACKS

ATTACK_REGISTRY = {

    "prompt_injection": {
        "attacks": PROMPT_INJECTION_ATTACKS,
        "owasp": OWASPLLMCategory.LLM01
    },

    "advanced_prompt_injection": {
        "attacks": ADVANCED_PROMPT_INJECTION_ATTACKS,
        "owasp": OWASPLLMCategory.LLM01
    },

    "jailbreak": {
        "attacks": JAILBREAK_ATTACKS,
        "owasp": OWASPLLMCategory.LLM07
    },

    "role_confusion": {
        "attacks": ROLE_CONFUSION_ATTACKS,
        "owasp": OWASPLLMCategory.LLM01
    }
}