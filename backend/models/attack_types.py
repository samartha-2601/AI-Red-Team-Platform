from enum import Enum


class AttackType(str, Enum):
    PROMPT_INJECTION = "prompt_injection"
    ADVANCED_PROMPT_INJECTION = "advanced_prompt_injection"
    JAILBREAK = "jailbreak"
    ROLE_CONFUSION = "role_confusion"